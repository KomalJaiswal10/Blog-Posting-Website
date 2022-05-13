import pymysql as p

def create_con():
    con=p.connect(host='localhost',user='root',password='dineshkomal@2800',database='flask_web_project')
    return con

def insert_auth_details(t):
    con=create_con()
    cur=con.cursor()
    q="insert into author (uname,password,city) values (%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()

def check_username():
    con=create_con()
    cur=con.cursor()
    q="select uname , password from author"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    name=[]
    for i in data:
        name.append(i[0])
    return name


def check_login_author():
    con=create_con()
    cur=con.cursor()
    q="select uname , password from author"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    return data


def save_blog_author(tsb):
    con=create_con()
    cur=con.cursor()
    q="insert into post (a_r_name,author_name , blog_title , blog) values (%s,%s,%s,%s)"
    cur.execute(q,tsb)
    con.commit()
    con.close()


def update_blog(t):
    con=create_con()
    cur=con.cursor()
    q="update post set author_name = %s , blog_title = %s , blog = %s where a_r_name = %s and blog_title = %s"
    cur.execute(q,t)
    con.commit()
    con.close()

def delete_blog(t):
    con=create_con()
    cur=con.cursor()
    q="delete from post where a_r_name = %s and blog_title = %s"
    cur.execute(q,t)
    con.commit()
    con.close()

    



def view_author(vt):
    con=create_con()
    cur=con.cursor()
    q="select author_name , blog_title from post where a_r_name = %s"
    cur.execute(q,vt)
    data=cur.fetchall()
    con.close()
    return data

def view_full_author(t):
    con=create_con()
    cur=con.cursor()
    q="select author_name , blog_title , blog from post where a_r_name = %s and blog_title = %s"
    cur.execute(q,t)
    data=cur.fetchall()
    con.close()
    return data




# User

def check_username_user():
    con=create_con()
    cur=con.cursor()
    q="select uname , password from user"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    name=[]
    for i in data:
        name.append(i[0])
    return name


def insert_user_details(t):
    con=create_con()
    cur=con.cursor()
    q="insert into user (uname,password,city) values (%s,%s,%s)"
    cur.execute(q,t)
    con.commit()
    con.close()


def check_login_user():
    con=create_con()
    cur=con.cursor()
    q="select uname , password from user"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    return data

def view_user():
    con=create_con()
    cur=con.cursor()
    q="select author_name , blog_title from post"
    cur.execute(q)
    data=cur.fetchall()
    con.close()
    return data

def view_full_user(t):
    con=create_con()
    cur=con.cursor()
    q="select author_name , blog_title , blog from post where author_name = %s and blog_title = %s"
    cur.execute(q,t)
    data=cur.fetchall()
    con.close()
    return data




def all_author_name():
    con=create_con()
    cur=con.cursor()
    q="select author_name from post"
    cur.execute(q)
    dname=cur.fetchall()
    con.close()
    return dname

def selected_author(t):
    con=create_con()
    cur=con.cursor()
    q="select author_name , blog_title from post where author_name = %s"
    cur.execute(q,t)
    data=cur.fetchall()
    con.close()
    return data
    

    





