from Secure_forum import databasemanagement
from jinja2 import Environment, select_autoescape
from Secure_forum.forms import RegistrationForm, LoginForm
from Secure_forum import app 
from flask import Flask, render_template, request, jsonify, make_response, flash, redirect, url_for

@app.route("/")
@app.route("/home")
def home():
    qrows = databasemanagement.getposts()
    return render_template('homepage.html', rows = qrows, titel='Hompage', status=True)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = request.form['password']
        useremail = request.form['email']
        
        regreturn = databasemanagement.registration(username,password,useremail)
        if(regreturn == 'This email already exists' or regreturn == 'This username already exists'):
            flash(regreturn)
            return redirect(url_for('register'))
        else:
            flash('Registration succesful')
            return redirect(url_for('loggedin'))
    return render_template('login.html', form=form,  titel='Loginpage', status=True)

@app.route("/loggedin")
def loggedin():
    qrows = databasemanagement.getposts()
    return render_template('loggedin.html', rows = qrows, titel='Logged in', status=True)    

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
def sendcomments():
    if request.method == 'POST':
        postid = request.get_json()
        postcontent, comments = databasemanagement.getcomments(postid['postid'])
        return jsonify(retpostcontent=postcontent, retcomments=comments)

@app.route('/createpost',methods=['POST'])
def create_post():
    if request.method == 'POST':
        usercookie = request.cookies.get('userID')
        postdata = request.get_json()
        print(postdata)
        postret = databasemanagement.insert_post(usercookie,postdata['posttitel'],postdata['postcontent'])
        return jsonify(answer=postret)

@app.route('/createcomment',methods=['POST'])
def create_comment():
    if request.method == 'POST':
        commentdata = request.get_json()
        usercookie = request.cookies.get('userID')
        print(commentdata)
        print(usercookie)
        comret = databasemanagement.insert_comment(usercookie,commentdata['comment'],commentdata['postid'])
        return jsonify(answer=comret)   

