import json


def get_database_object():
    database_file = open('databases/id.json')
    file_data = database_file.read()
    return json.loads(file_data)


def generate_user_id():
    database = get_database_object()
    user_id = database['user_id']

    updated_id = str(int(user_id) + 1)
    database['user_id'] = updated_id
    update_database_object(database)
    return user_id


def generate_job_id():
    database = get_database_object()
    job_id = database['job_id']
    updated_id = str(int(job_id) + 1)
    database['job_id'] = updated_id
    update_database_object(database)
    return job_id


def generate_education_id():
    database = get_database_object()
    education_id = database['edu_id']
    updated_id = str(int(education_id) + 1)
    database['edu_id'] = updated_id
    update_database_object(database)
    return education_id


def generate_message_id():
    database = get_database_object()
    message_id = database['message_id']
    updated_id = str(int(message_id) + 1)
    database['message_id'] = updated_id
    update_database_object(database)
    return message_id


def update_database_object(updated_database):
    database_file = open('databases/id.json', 'w')
    json.dump(updated_database, database_file, indent=2)
