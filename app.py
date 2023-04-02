from flask import Flask, render_template, request, redirect, url_for, flash, session
from appwrite.client import Client, AppwriteException
from appwrite.services.account import  Account
from dotenv import load_dotenv
from repository import client
from services import *



load_dotenv()

app = Flask(__name__)



@app.route('/')
def index():

    return render_template("home.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get request data
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        # Add student to the database
        student = add_student(name, email, password)
        return render_template('signup_success.html', student=student)
    else:
        return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get request data
        email = request.form['email']
        password = request.form['password']

        # Check if email and password are valid
        # You can implement your own authentication logic here
        # For example, you can check if the email and password match an existing student document
        # If the email and password are valid, you can return a JWT token for authentication
        # For simplicity, this example just renders a success message
        return render_template('login_success.html')
    else:
        return render_template('login.html')

@app.route('/studygroups', methods=['GET', 'POST'])
def create_studygroup():
    if request.method == 'POST':
        # Get request data
        name = request.form['name']
        description = request.form['description']
        member_ids = request.form.getlist('member_ids')

        # Add study group to the database
        studygroup = add_studygroup(name, description, member_ids)
        return render_template('studygroup_success.html', studygroup=studygroup)
    else:
        students = get_all_students()
        return render_template('create_studygroup.html', students=students)

@app.route('/students/<student_id>', methods=['GET'])
def get_student_info(student_id):
    # Get student information from the database
    student = get_student(student_id)
    if student:
        return render_template('student.html', student=student)
    else:
        return render_template('student_not_found.html')

@app.route('/studygroups/<studygroup_id>', methods=['GET'])
def get_studygroup_info(studygroup_id):
    # Get study group information from the database
    studygroup = get_studygroup(studygroup_id)
    if studygroup:
        return render_template('studygroup.html', studygroup=studygroup)
    else:
        return render_template('studygroup_not_found.html')
    
if __name__ == '__main__':
    app.run(debug=True)
