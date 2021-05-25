from Secure_forum import databasemanagement
from jinja2 import Environment, select_autoescape
from Secure_forum import app
from flask import Flask, render_template, request, jsonify, make_response

@app.route("/")
@app.route("/home")
def home():
    qrows = databasemanagement.getposts()
    return render_template('homepage.html', rows = qrows, titel='Hompage', status=True)

@app.route("/register")
def register():
    qrows = databasemanagement.getposts()
    return render_template('register.html', rows = qrows, titel='Registerpage', status=True)

@app.route("/login")
def login():
    qrows = databasemanagement.getposts()
    return render_template('login.html', rows = qrows, titel='Loginpage', status=True)

@app.route("/loggedin")
def loggedin():
    qrows = databasemanagement.getposts()
    return render_template('loggedin.html', rows = qrows, titel='Logged in', status=True)    

@app.route('/register',methods=['POST'])   
def startregistration():     
    if request.method == 'POST':
        userdata = request.get_json()
        regreturn = databasemanagement.registration(userdata['inputemail'],userdata['inputpassword'])
        return jsonify(answer=regreturn)

@app.route('/getcomments',methods=['POST'])
def sendcomments():
    if request.method == 'POST':
        postid = request.get_json()
        postcontent, comments = databasemanagement.getcomments(postid['postid'])
        return jsonify(retpostcontent=postcontent, retcomments=comments)

@app.route('/login',methods=['POST'])
def startlogin():
    if request.method == 'POST':
        logindata = request.get_json()
        logret = databasemanagement.login(logindata['inputemail'],logindata['inputpassword'])
        print (logret)
        if((logret[0]) == "Success"):
            res = make_response()
            res.set_cookie('userID', (logret[1]))
            return res
        else:    
            return jsonify(answer=logret)

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

