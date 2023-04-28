from flask import Flask, request, render_template, redirect
import re

app = Flask(__name__)
@app.route("/")
def index():
    if request.args.get('error') != "":
        error = request.args.get('error')
        return render_template('index.html',error=error)
    else:
        return render_template('index.html',error="")

@app.route("/do-login",methods=['GET','POST'])
def dologin():
    username = request.form['username']
    password = request.form['password']
    resp = passwordCheck(password)
    error = resp['msg']
    status = resp['status']
    if status != 1:
        return redirect(f"/?error={error}")
    else:
        return resp

def passwordCheck(password): # takes the password as a parameter
    response = {            #has a dictionary
        "password":"",
        "msg":"",
        "status":0
        }
    if (len(password) == 0):
        response['msg'] = "Password cannot be empty"
        response['status'] = 0
    elif (len(password) < 8): 
        response['msg'] = "Password must be atleast 8 characters"
        response['status'] = 0
     
    elif (len(password) > 15):
        response['msg'] = "Password must not exceed 15 characters"
        response['status'] = 0
        
    elif not re.search("[a-z]", password): 
        response['msg'] = "Password must have atleast one small Letter"
        response['status'] = 0
        
    elif not re.search("[A-Z]", password): 
        response['msg'] = "Password must have atleast one capital letter"
        response['status'] = 0
        
    elif not re.search("[0-9]", password): 
        response['msg'] = "Password must have at least one number"
        response['status'] = 0
        
    elif not re.search("[!@#$%^&*()]", password): 
        response['msg'] = "Password must have at least one symbol"
        response['status'] = 0
    else:
        response['password'] = password
        response['msg'] = "This is a strong password."
        response['status'] = 1
    return response




if __name__ == "__main__":
    app.run(debug=True, port=7000)