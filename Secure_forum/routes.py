from Secure_forum import databasemanagement
from jinja2 import Environment, select_autoescape
from Secure_forum.forms import RegistrationForm, LoginForm,CreatePostForm, CreateCommentForm
from Secure_forum import app, user
from flask import Flask, render_template, request, jsonify, make_response, flash, redirect, url_for
from flask_login import LoginManager, login_required, logout_user,login_user
from Secure_forum.user import User
from flask_wtf.csrf import CSRFProtect

login_manager = LoginManager()
login_manager.init_app(app)
csrf = CSRFProtect(app)
csrf.init_app(app)

@login_manager.user_loader
def user_loader(email):
    userexists = databasemanagement.getuserid(email)
    if userexists == 'False':
        return
    user = User(userexists[1])
    return user

@app.route("/")
@app.route("/home")
def home():
    cform = CreatePostForm()
    cnpform = CreateCommentForm()
    qrows = databasemanagement.getposts()
    return render_template('homepage.html', rows = qrows, titel='Hompage', status=True, cpform=cform, ccform=cnpform)

@app.route("/login", methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = request.form['password']
        useremail = request.form['email']
        regreturn = databasemanagement.login(useremail,password)
        if(regreturn[0] == 'Success'):
            userid = regreturn[1]
            user = User(userid)
            login_user(user)
            res = make_response(redirect(url_for('home')))
            res.set_cookie('userID', userid)
            return res
        else:
            flash(regreturn)
            return redirect(url_for('login'))
    return render_template('login.html', form=form,  titel='Loginpage', status=True)

@app.route('/logout', methods=['GET'])
@login_required
@csrf.exempt    
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register',methods=['GET','POST'])   
def register():     
    form = RegistrationForm()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        useremail = request.form['email']
        regreturn = databasemanagement.registration(username,password,useremail)
        if(regreturn == 'This email already exists' or regreturn == 'This username already exists'):
            flash(regreturn)
            return redirect(url_for('register'))    
    return render_template('register.html',titel='Registerpage',form=form)


@app.route('/getcomments',methods=['POST'])
@csrf.exempt
def sendcomments():
    if request.method == 'POST':
        postid = request.get_json()
        postcontent, comments = databasemanagement.getcomments(postid['postid'])
        return jsonify(retpostcontent=postcontent, retcomments=comments)

@app.route('/createpost',methods=['POST'])
@login_required
def create_post():
    if request.method == 'POST':
        posttitel = request.form['posttitel']
        postcontent = request.form['postcontent']
        usercookie = request.cookies.get('userID')
        postret = databasemanagement.insert_post(usercookie,posttitel,postcontent)
        if(postret == 'Post was created'):
            flash(postret)
            return redirect(url_for('home'))
        else:
            flash('Error occured while creating a Post')

@app.route('/createcomment',methods=['POST'])
@login_required
def create_comment():
    if request.method == 'POST':
        usercookie = request.cookies.get('userID')
        commentdata = request.form['commentcontent']
        postid = request.form['ccpostid']
        comret = databasemanagement.insert_comment(usercookie,commentdata,postid)
        if(comret == 'Comment was created'):
            flash(comret, 'info')
        else:
            flash(comret, 'error')
    return redirect(url_for('home'))
