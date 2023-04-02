import appwrite
from repository import client
from appwrite.services.database import Database


database = Database(client)

# Define function for adding a new student
def add_student(name, email, password):
    try:
        response = client.database.create_document(
            collection_id='students',
            data={
                'name': name,
                'email': email,
                'password': password
            }
        )
        return response['$id'] # Return the ID of the new document
    except Exception as e:
        print('Error adding student:', e)
        return None

# Define function for updating a student
def update_student(student_id, name=None, email=None, password=None):
    try:
        update_data = {}
        if name:
            update_data['name'] = name
        if email:
            update_data['email'] = email
        if password:
            update_data['password'] = password
        response = client.database.update_document(
            collection_id='students',
            document_id=student_id,
            data=update_data
        )
        return response['$id'] # Return the ID of the updated document
    except Exception as e:
        print('Error updating student:', e)
        return None

# Define function for deleting a student
def delete_student(student_id):
    try:
        response = client.database.delete_document(
            collection_id='students',
            document_id=student_id
        )
        return True # Return True if deletion was successful
    except Exception as e:
        print('Error deleting student:', e)
        return False

# Define function for adding a new study group
def add_studygroup(name, members):
    try:
        response = client.database.create_document(
            collection_id='studygroups',
            data={
                'name': name,
                'members': members
            }
        )
        return response['$id'] # Return the ID of the new document
    except Exception as e:
        print('Error adding study group:', e)
        return None

# Define function for updating a study group
def update_studygroup(studygroup_id, name=None, members=None):
    try:
        update_data = {}
        if name:
            update_data['name'] = name
        if members:
            update_data['members'] = members
        response = client.database.update_document(
            collection_id='studygroups',
            document_id=studygroup_id,
            data=update_data
        )
        return response['$id'] # Return the ID of the updated document
    except Exception as e:
        print('Error updating study group:', e)
        return None

# Define function for deleting a study group
def delete_studygroup(studygroup_id):
    try:
        response = client.database.delete_document(
            collection_id='studygroups',
            document_id=studygroup_id
        )
        return True # Return True if deletion was successful
    except Exception as e:
        print('Error deleting study group:', e)
        return False


# Define function for getting student information
def get_student(student_id):
    try:
        response = client.database.get_document(
            collection_id='students',
            document_id=student_id
        )
        return response['data'] # Return the data for the student document
    except Exception as e:
        print('Error getting student:', e)
        return None

# Define function for getting study group information
def get_studygroup(studygroup_id):
    try:
        response = client.database.get_document(
            collection_id='studygroups',
            document_id=studygroup_id
        )
        return response['data'] # Return the data for the study group document
    except Exception as e:
        print('Error getting study group:', e)
        return None
    

def get_all_students():
    try:
        # Get all documents from the 'students' collection
        students = database.list_documents('students').get('documents')

        return students
    except Exception as e:
        print('Error getting students:', e)
