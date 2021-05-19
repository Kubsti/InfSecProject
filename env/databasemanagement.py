import psycopg2, uuid
from argon2 import PasswordHasher

def getposts():
    try:
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT posttitel, username from posts,hasposts,forumuser WHERE forumuser.randuserid = hasposts.userid AND hasposts.postid = posts.postid")
        rows = cur.fetchall()
        conn.close()
    except psycopg2.OperationalError as e:
        print('Unable to connet!\n{0}').format(e)
    
    return rows 

def registration(useremail, password):
    try:
        ph = PasswordHasher()
        conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
        cur = conn.cursor()
        cur.execute("SELECT username from forumuser WHERE forumuser.username =%s", (useremail,))
        rows = cur.fetchall()
        if (len(rows) >= 1):
            return "This email already exists"
        else:
            randuserid = str(uuid.uuid1())
            pwhash = ph.hash(password)
            cur.execute("INSERT into forumuser(randuserid, username, passwordhash) VALUES(%s,%s,%s)", (randuserid, useremail,pwhash))
            conn.commit()
            conn.close()
            return "Registration successful"
    except psycopg2.OperationalError as e:
        return "An Error occured during the registration\n{0}".format(e)

