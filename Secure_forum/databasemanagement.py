import psycopg2, uuid
import argon2
from argon2 import PasswordHasher

def getposts():
    try:
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT posttitel, username, Posts.postid from posts,hasposts,forumuser WHERE forumuser.randuserid = hasposts.userid AND hasposts.postid = posts.postid ORDER BY posts.postid DESC")
        rows = cur.fetchall()
        conn.close()
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)
    
    return rows 

def registration(username, password, useremail):
    try:
        ph = PasswordHasher()
        conn = psycopg2.connect(database="secureforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT useremail from forumuser WHERE forumuser.useremail = %s",(useremail,)) 
        rows = cur.fetchall()
        cur.execute("SELECT username from forumuser WHERE forumuser.username = %s",(username,))
        usernameexists = cur.fetchall()
        if (len(rows) >= 1):
            return "This email already exists"
        elif(len(usernameexists) >= 1):
            return "This username already exists"
        else:
            randuserid = str(uuid.uuid1())
            pwhash = ph.hash(password)
            cur.execute("INSERT into forumuser(randuserid, useremail, username, passwordhash) VALUES(%s,%s,%s,%s)", (randuserid, useremail, username,pwhash))
            conn.commit()
            conn.close()
            return "Registration successful"
    except psycopg2.OperationalError as e:
        return "An Error occured during the registration\n{0}".format(e)

def getcomments(postid):
    try:
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT posttitel,postcontent from posts Where posts.postid = %s", (postid,))
        postcontent = cur.fetchall()
        cur.execute("SELECT username, commentcontent from forumcomments,hascomments,forumuser WHERE hascomments.postid =%s AND hascomments.comentid = forumcomments.commentid", (postid,))
        comments = cur.fetchall()
        conn.close()
    except psycopg2.OperationalError as e:
        print('Unable to connect!\n{0}').format(e)
    
    return postcontent, comments 

def login(useremail, password):
    try:
        ph = PasswordHasher()
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT passwordhash, randuserid from forumuser WHERE forumuser.username = %s",(useremail,))
        rows = cur.fetchall()
        if(len(rows) == 0):
            return "We could not find a User for your Username :("
        else:
            try:
                ph.verify((rows[0])[0], password)
                return "Success", (rows[0])[1]
            except (argon2.exceptions.InvalidHash,argon2.exceptions.VerifyMismatchError) as e:
                return "Failure password not recognized"
    except psycopg2.OperationalError as e:
        return "An Error occured during the login\n{0}".format(e)

def insert_post(userid, posttitel, postcontent):
    try:
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO posts(postcontent, posttitel) VALUES(%s,%s) RETURNING postid",(postcontent,posttitel))
        conn.commit()
        postid = cur.fetchall()
        postid = (postid[0])[0]
        cur.execute("INSERT INTO hasposts(userid, postid) VALUES(%s,%s)",(userid,postid))
        conn.commit()
        return "Post was created"
    except psycopg2.OperationalError as e:
        print (e)
        return "Error occured while creating a Post"

def insert_comment(userid,commentcontent,postid):
    try:
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("INSERT INTO forumcomments(commentcreator, commentcontent) VALUES(%s,%s) RETURNING commentid", (userid, commentcontent))
        conn.commit()
        commentid = cur.fetchall()
        commentid = (commentid[0])[0]
        cur.execute("INSERT INTO hascomments(postid, comentid) VALUES(%s,%s)", (postid,commentid))
        conn.commit()
        return "Comment was created"
    except psycopg2.OperationalError as e:
        print (e)
        return "Error occured while creating a Comment"