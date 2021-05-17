import psycopg2

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

