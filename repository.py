from appwrite.client import Client, AppwriteException, app
from appwrite.services.account import Account
import appwrite
import os


# Initialize Appwrite client and database service
client = Client()
client.set_endpoint(os.environ['APPWRITE_ENDPOINT'])
client.set_project(os.environ['APPWRITE_PROJECT'])
client.set_key(os.environ['APPWRITE_API_KEY'])
client.set_self_signed()
account_service = Account(client)


students_collection = appwrite.Collection.create(
    name='students',
    read=['*'],
    write=['user:' + client.get_project_id()],
    rules=[
        {
            'label': 'Name',
            'key': 'name',
            'type': 'text',
            'required': True
        },
        {
            'label': 'Email',
            'key': 'email',
            'type': 'email',
            'required': True
        },
        {
            'label': 'Password',
            'key': 'password',
            'type': 'password',
            'required': True
        }
    ]
)

# Check if the students collection was created successfully
if students_collection["$id"]:
    # Get the ID of the new students collection
    students_collection_id = students_collection["$id"]
    print(f'Students collection created successfully with ID: {students_collection_id}')
else:
    print('Error creating students collection: ', students_collection)

# Set up the studygroups collection object with columns
studygroups_collection = appwrite.Collection.create(
    name='studygroups',
    read=['*'],
    write=['user:' + client.get_project_id()],
    rules=[
        {
            'label': 'Name',
            'key': 'name',
            'type': 'text',
            'required': True
        },
        {
            'label': 'Members',
            'key': 'members',
            'type': 'array',
            'required': True,
            'array':
                {
                    'type': 'document',
                    'rules': [
                        {
                            'label': 'Student ID',
                            'key': 'student_id',
                            'type': 'text',
                            'required': True,
                            'reference': {
                                'collection': students_collection_id,
                                'key': '$uid',
                                'display': 'name'
                            }
                        }
                    ]
                }
        }
    ]
)

# Check if the studygroups collection was created successfully
if studygroups_collection["$id"]:
    # Get the ID of the new studygroups collection
    studygroups_collection_id = studygroups_collection["$id"]
    print(f'Studygroups collection created successfully with ID: {studygroups_collection_id}')
else:
    print('Error creating studygroups collection: ', studygroups_collection)
