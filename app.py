from flask import Flask, render_template, request, redirect, url_for, flash
from appwrite.client import Client, AppwriteException
from appwrite.services.account import  Account
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask(__name__)

# Initialize Appwrite client and database service
client = Client()
client.set_endpoint(os.environ['APPWRITE_ENDPOINT'])
client.set_project(os.environ['APPWRITE_PROJECT'])
client.set_key(os.environ['APPWRITE_API_KEY'])
account_service = Account(client)


# Define your web application's routes and views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get user input from the form
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if email ends with kibo.school
        if not email.endswith('kibo.school'):
            flash('Please use a valid kibo.school email address.', 'error')
            return redirect(url_for('signup'))
        
        # Create a new account in Appwrite
        try:
            response = account_service.create(email=email, password=password, name=name)
            user_id = response["$id"]
            # Redirect to the login page
            return redirect(url_for('login'))  
        except AppwriteException as e:
            # Handle Appwrite errors
            error_message = e.message
            flash(error_message, "error")
        
    # Render the sign-up page
    return render_template('signup.html')



# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         # Retrieve data from form submission
#         name = request.form['name']
#         email = request.form['email']
#         message = request.form['message']
        
#         # Save data to Appwrite database collection
#         database.create_document(
#             collection_id='COLLECTION_ID', # Replace COLLECTION_ID with the ID of your Appwrite database collection
#             data={'name': name, 'email': email, 'message': message}
#         )
        
#         return render_template('thanks.html')
#     else:
#         # Retrieve data from Appwrite database collection
#         result = database.list_documents('COLLECTION_ID')
        
#         return render_template('data.html', result=result['documents'])

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
