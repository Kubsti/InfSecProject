from flask import Flask, render_template, request, jsonify, make_response
from databasemanagement import getposts, registration, getcomments, login, insert_post, insert_comment
from jinja2 import Environment, select_autoescape

app = Flask(__name__)
@app.route("/")
def home():
    qrows = getposts()
    return render_template('index.html', rows = qrows, status=True)

@app.route('/register',methods=['POST'])   
def startregistration():     
    if request.method == 'POST':
        userdata = request.get_json()
        regreturn = registration(userdata['inputemail'],userdata['inputpassword'])
        return jsonify(answer=regreturn)

@app.route('/getcomments',methods=['POST'])
def sendcomments():
    if request.method == 'POST':
        postid = request.get_json()
        postcontent, comments = getcomments(postid['postid'])
        return jsonify(retpostcontent=postcontent, retcomments=comments)

@app.route('/login',methods=['POST'])
def startlogin():
    if request.method == 'POST':
        logindata = request.get_json()
        logret = login(logindata['inputemail'],logindata['inputpassword'])
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
        postret = insert_post(usercookie,postdata['posttitel'],postdata['postcontent'])
        return jsonify(answer=postret)

@app.route('/createcomment',methods=['POST'])
def create_comment():
    if request.method == 'POST':
        commentdata = request.get_json()
        usercookie = request.cookies.get('userID')
        comret = insert_comment(usercookie,commentdata['comment'],commentdata['postid'])
        return jsonify(answer=comret)   

