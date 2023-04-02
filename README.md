# AppwriteApplication

This is a flask application built with Appwrites BAAS. Each user has to register with a unique email after which they create study groups and update them as required.


## Set Up

To run this application locally, make sure you are in the project folder on your terminal then install the dependencies using 
```powershell-interactive
$ pip install -r requirements.txt
```
Run the application using
```azurepowershell
$ python -m flask run
```
Your app should be running on port 5000 if you have your appwrite variables set correctly

<http://127.0.0.1:5000>

## Table Schema

This App has just two models having a one-to-many relationship and make use of the appwrite database: 
- **Users** :Table for saving users. One user can have 0 or many tasks
- **Studygroups**- Table for saving tasks of users. 


## Hosting 
This app is hosted on render and can be accessed from this link [here](https://activity-log.onrender.com/)
