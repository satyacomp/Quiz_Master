from flask import current_app as app #access current running app
from flask import Flask,render_template,request

app=Flask("__name__")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin_dashboard():
    return render_template("admin_dashboard.html",user="IITM")

@app.route("/user")
def user_dashboard():
    return render_template("user_dashboard.html",user="SSN")


#Other routes
@app.route("/login",methods=["GET","POST"])
def user_login():
    if request.method=="POST":
        email=request.form.get("uname")
        pwd=request.form.get("password")

    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def user_signup():
    if request.method=="POST":
        email=request.form.get("uname")
        pwd=request.form.get("password")
        full_name=request.form.get("full_name")
        address=request.form.get("address")
        phone=request.form.get("phno")
        print(email,", ",pwd,",",full_name,", ",address,", ",phone)
        
    return render_template("signup.html")


@app.route("/add_subject",methods=["GET","POST"])
def new_subject():
    return render_template("add_subject.html")


@app.route("/add_chapter",methods=["GET","POST"])
def new_chapter():
    return render_template("add_chapter.html")