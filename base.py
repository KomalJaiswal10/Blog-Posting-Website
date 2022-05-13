
from flask import*
import module_db as d

app=Flask(__name__)

@app.route("/")
def main_page():
    return render_template("mainpage.html")

@app.route("/author_res_log")
def auth_res_log():
    return render_template("author_res_log.html")

@app.route("/regAuthorlink")
def Author_reg_page():
    return render_template("reg_author.html")


@app.route("/submit", methods=["POST"])
def submit_auth_details():
    uname = request.form["uname"]
    pwd = request.form["pwd"]
    city = request.form["city"]
    t=(uname,pwd,city)

    name=d.check_username()
    msg="Registered Successfully"
    if uname in name:
        error='Username not Available'
        return render_template("reg_author.html",error=error)
             
    else:

        d.insert_auth_details(t)   
        return redirect("/loginAuthorlink" )

    


@app.route("/loginAuthorlink")
def Author_login_page():
    return render_template("login_author.html")

@app.route("/author")
def author(aname):
    return render_template("author_interface.html",aname=aname)


@app.route("/checkAuthor",methods=["POST"])
def check_auth_login():
    unamech=request.form["unamech"]
    pwdch=request.form["pwdch"]

    tch=(unamech,pwdch)
    data=d.check_login_author()
    msg=''
    error=None
    
    if tch in data:
        flash='Successfully Logged-IN'
        return author(aname=unamech)
        
    else:
        error='Invalid Inputs'
        return render_template("login_author.html",error=error)
        



@app.route("/addpost_author/<string:id>")
def add_post_auth(id): 
    return render_template("author_addpost.html",namea=id)



@app.route("/save_blog/<string:name>", methods=["POST"])
def save_blog_(name):
    a_r_name=name
    author_name = request.form["authorname"]
    blog_title = request.form["blogtitle"]
    blog = request.form["blog"]

    tsb=(a_r_name,author_name,blog_title,blog)
    d.save_blog_author(tsb)
    return render_template("update_blog.html",tsb=tsb)



@app.route("/edit_blog/<string:an>/<string:abn>/<string:bt>/<string:b>")
def update_blog(an,abn,bt,b):
    ean=an
    eabn=abn
    ebt=bt
    eb=b

    t=(ean,eabn,ebt,eb)
    return render_template("edit_blog_author.html",t=t)
 

@app.route("/esave_blog/<string:name>/<string:title>", methods=["POST"])
def edit_blog(name,title):
    a_name =name
    etitle=title
    author_name = request.form["authorname"]
    blog_title = request.form["blogtitle"]
    blog = request.form["blog"]

    t=(author_name,blog_title,blog,a_name,etitle)
    d.update_blog(t)
    return view_blog_author(a_name) 


@app.route("/ok/<string:name>/<string:title>")
def ok(name,title):
    oname=name
    otitle=title
    return author(aname=name) 


@app.route("/delete_blog/<string:name>/<string:title>")
def delete_blog(name,title):
    dname=name
    dtitle=title
    t=(dname,dtitle)
    d.delete_blog(t)
    return view_blog_author(dname)



@app.route("/back/<string:name>")
def back(name):
    bname=name
    return author(aname=bname )


@app.route("/viewpost_author/<string:name>")
def view_blog_author(name):
    n=name
    vt=(n,)
    data=d.view_author(vt)
    return render_template("view_blog_auth.html", res=data , m=n)


@app.route("/fullblog/<string:name>/<string:title>")
def view_full_blog_author(name,title):
    vft=(name,title)
    data=d.view_full_author(vft)
    return render_template("view_full_blog_auth.html",res=data,vft=vft)








#User Interface

@app.route("/user_res_log")
def user_res_log():
    return render_template("user_res_log.html")

@app.route("/regUserlink")
def User_reg_page():
    return render_template("reg_user.html")

@app.route("/user_submit", methods=["POST"])
def submit_user_details():
    uname = request.form["u_uname"]
    pwd = request.form["u_pwd"]
    city = request.form["u_city"]
    t=(uname,pwd,city)

    name=d.check_username_user()
    if uname in name:
        error='Username not Available'
        return render_template("reg_user.html",error=error)
             
    else:
        d.insert_user_details(t)
        return redirect("/loginUserlink")


@app.route("/loginUserlink")
def User_login_page():
    return render_template("login_user.html")


@app.route("/user")
def user():
    dname=d.all_author_name()
    La=[]
    for i in dname:
        La.append(i)
    
    sa=set(La)
       
    data=d.view_user()
    return render_template("user_interface.html", res=data , sa=sa )

@app.route("/user_fullblog/<string:name>/<string:title>")
def view_full_blog_user(name,title):
    vft=(name,title)
    data=d.view_full_user(vft)
    return render_template("view_full_blog_user.html",res=data)
    


@app.route("/checkUser",methods=["POST"])
def check_user_login():
    unamech=request.form["unamech"]
    pwdch=request.form["pwdch"]

    tch=(unamech,pwdch)
    data=d.check_login_user()
    msg=''
    error=None
    
    if tch in data:
        flash='Successfully Logged-IN'
        return user()
        
    else:
        error='Invalid Inputs'
        return render_template("login_user.html",error=error)


@app.route("/user_back_log")
def back_log_user():
    return redirect("/")


@app.route("/user_back_interface")
def back_user_interface():
    return redirect("/user")


@app.route("/select_author",methods=['GET','POST'])
def selected_author():
    
    select = request.form.get('comp_select')
    t=(select,)
    data=d.selected_author(t)
    return render_template("user_selected_author.html", res=data)


    




if(__name__=="__main__"):
    app.run(debug=True)