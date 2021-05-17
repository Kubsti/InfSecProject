import psycopg2

conn = psycopg2.connect(database="testforum",user="postgres",password="Kubsti4146",host="127.0.0.1",port="5432")
cur = conn.cursor()

cur.execute("SELECT postid, postcontent, posttitel from posts")
rows = cur.fetchall()

for row in rows:
    print ("POSTID = ", row[0])
    print ("POSTCONTENT = ", row[1])
    print ("POSTTITEL = ", row[2])

conn.close()