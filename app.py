from flask import Flask,render_template

app=None

def setup_app():
    app=Flask("__name__")
    #Other backend settings
    print("Quiz Master app is intiated...")
    return app



app=setup_app()#call here

from backend.controller import *

#main program
if __name__=="__main__":
    app.run(debug=True)