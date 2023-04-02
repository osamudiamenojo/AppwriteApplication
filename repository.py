from appwrite.client import Client, AppwriteException
from appwrite.services import   Database


# Initialize Appwrite client and database service
client = Client()
client.set_endpoint('https://localhost/v1') # Replace [HOSTNAME_OR_IP] with your Appwrite server's hostname or IP address
client.set_project('64281b2eed359f3a178c') # Replace PROJECT_ID with your Appwrite project ID
client.set_key('771944225395f718867f7a294c53b37c229a5b9760ad44500faf74a6300f63f3e0364469a9da0c75d97aa54dd24a4b09e0ae53946419fce3776f45e77f62a0dde31b1396fc1949267581dff153bdd4186fe64790dfd1031ee9afa712cc75b8fbc67118e87a9386f3ff7470479fe0b99d61b69d5b2271f37882a6140a3d5642b5')
database = Database(client)


# Create a collection
collection = database.create_collection(
    name='study_groups', # Replace with your collection name
    read=['*'], # Public read access
    write=['user:{}'.format(client.get_user()['$id'])] # Only authenticated users can write
)

# Add fields to the collection
collection.add_field(name='name', type='text', required=True)
collection.add_field(name='description', type='text')
collection.add_field(name='topic', type='text', required=True)
collection.add_field(name='schedule', type='text', required=True)

# Create "users" collection
collection = database.create_collection(
    name='users',
    read=['*'],
    write=['user:*'],
    rules=[{
        'field': '$.name',
        'type': 'string',
        'required': True
    }, {
        'field': '$.email',
        'type': 'string',
        'required': True
    }, {
        'field': '$.password',
        'type': 'string',
        'required': True
    }]
)

# Define the user ID and study group ID
user_id = '[USER_ID]'
study_group_id = '[STUDY_GROUP_ID]'

# Get the user and study group records from the database
user_record = database.get_document('users', user_id)
study_group_record = database.get_document('study_groups', study_group_id)

# Add the user to the study group's "members" array
if 'members' in study_group_record['$collection']:
    members = study_group_record['members']
else:
    members = []
members.append(user_id)
study_group_record['members'] = members

# Update the study group record in the database
database.update_document('study_groups', study_group_id, study_group_record)

# Add the study group to the user's "study_groups" array
if 'study_groups' in user_record['$collection']:
    study_groups = user_record['study_groups']
else:
    study_groups = []
study_groups.append(study_group_id)
user_record['study_groups'] = study_groups

# Update the user record in the database
database.update_document('users', user_id, user_record)
