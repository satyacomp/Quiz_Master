from flask import Flask,render_template
from backend.models import *

app=None

def setup_app():
    app=Flask("__name__")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///quiz_data.sqlite3"
    app.app_context().push()  # push manually so that direct access to the app
    db.init_app(app)
    print("Quiz Master app is intiated...")
    return app



app=setup_app()#call here

from backend.controller import *

#main program
if __name__=="__main__":
    app.run(debug=True)