from flask import current_app as app #access current running app
from flask import Flask,render_template,request,url_for,redirect
from backend.models import *


@app.route("/")
def home():
    return render_template("index.html")

#Other routes
@app.route("/login",methods=["GET","POST"])
def user_login():
    if request.method=="POST":
        email=request.form.get("uname")
        pwd=request.form.get("password")
        #search record
        user=User.query.filter_by(mailid=email,password=pwd).first()
        if user and user.role==2:
            return redirect(url_for('user_dashboard',user_id=user.id))
        elif user and user.role==1:
            return redirect(url_for('admin_dashboard',user_id=user.id))
        
    return render_template("login.html")

@app.route("/signup",methods=["GET","POST"])
def user_signup():
    if request.method=="POST":
        email=request.form.get("uname")
        pwd=request.form.get("password")
        full_name=request.form.get("full_name")
        address=request.form.get("address")
        phone=request.form.get("phno")
        user=User(mailid=email,password=pwd,full_name=full_name,address=address,phno=phone)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_login'))
        
    return render_template("signup.html")




# User routes
@app.route("/user/<int:user_id>")
def user_dashboard(user_id):
    user=User.query.get_or_404(user_id)
    return render_template("user_dashboard.html",user=user)


# Admin routes
@app.route("/admin/<int:user_id>")
def admin_dashboard(user_id):
    user=User.query.get_or_404(user_id)
    return render_template("admin_dashboard.html",user=user)

@app.route("/subject/add/<int:user_id>",methods=["GET","POST"])
def subject(user_id):
    user=User.query.get_or_404(user_id)
    if request.method=="POST":
        s_name=request.form.get("s_name")
        description=request.form.get("description")
        subject=Subject(name=s_name,description=description)
        db.session.add(subject)
        db.session.commit()
        return redirect(url_for('admin_dashboard',user_id=user.id))

    return render_template("add_subject.html",user=user)


@app.route("/chapter/add",methods=["GET","POST"])
def chapter():
    return render_template("add_chapter.html")


@app.route("/quiz/add",methods=["GET","POST"])
def quiz():
    return render_template("add_quiz.html")