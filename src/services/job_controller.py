import json

import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.constants.success_messages as successMessage
import src.api.jobs_api as jobsApi

# Returns True if all job titles in the database are unique
# Otherwise, returns False


def all_job_titles_are_unique():

    # Gets a reference to the jobs dictionary
    jobs_dictionary = get_database_object()

    # Gets a reference to the jobs list
    jobs_list = jobs_dictionary["jobs"]

    # Declares an empty list to store job titles
    job_titles_list = []

    # iterates through all jobs
    for job in jobs_list:

        # Adds the current job's title to the list
        job_titles_list.append(job["title"])

    # Declares an empty set to store job titles already encountered
    job_titles_already_seen = set()

    # Considers each job title
    for job_title in job_titles_list:

        # If the job title has already been found
        if job_title in job_titles_already_seen:

            # Return False since a duplicate job title was found
            return False

        # Indicate that this job title has been seen
        job_titles_already_seen.add(job_title)

    # Return True if no duplicate job titles are found
    return True


def clear_jobs_list():
    # resets the job id to 1 when clearing list
    db = json.load(open('databases/id.json'))
    with open('databases/id.json', 'w') as id_db:
        db['job_id'] = '1'
        json.dump(db, id_db, indent=2)

    database = get_database_object()
    database["jobs"] = []
    update_database_object(database)


def is_database_limit_reached():
    database = get_database_object()
    return len(database["jobs"]) >= 10


def get_database_object():
    database_file = open('databases/job_post.json')
    file_data = database_file.read()
    return json.loads(file_data)


def update_database_object(updated_database):
    database_file = open('databases/job_post.json', 'w')
    json.dump(updated_database, database_file, indent=2)


def post_job(job):
    if (is_database_limit_reached()):
        notificationHandler.display_notification(
            errorMessages.JOB_DATABASE_LIMIT_MESSAGE)
        return

    database = get_database_object()
    database["jobs"].append(job.__dict__)
    update_database_object(database)
    notificationHandler.display_notification(
        successMessage.SUCCESSFUL_JOB_POSTING)
    jobsApi.update_jobs(job)


def delete_job(job_id):
    database = get_database_object()
    for job in database["jobs"]:
        if job["job_id"] == job_id:
            database["jobs"].remove(job)
            update_database_object(database)
            jobsApi.write_jobs()
            return True
    return False


def get_all_jobs():
    database = get_database_object()
    return database["jobs"]


def get_job_by_id(job_id):
    database = get_database_object()
    for job in database["jobs"]:
        if job["job_id"] == job_id:
            return job
    return None


def job_exists(job_id):
    database = get_database_object()
    for job in database["jobs"]:
        if job["job_id"] == job_id:
            return True
    return False


def add_application_to_job(job_id, application):
    database = get_database_object()
    for job in database["jobs"]:
        if job["job_id"] == job_id:
            job["applications"].append(application.__dict__)
            update_database_object(database)
            jobsApi.applied_jobs()
            return True
    return False


def get_job_applications(job_id):
    database = get_database_object()
    for job in database["jobs"]:
        if job["job_id"] == job_id:
            return job["applications"]
    return None

# Returns True if a job in the database has the given title
# Otherwise, returns False


def job_exists_by_title(title_param):

    database = get_database_object()

    for job in database["jobs"]:

        if job["title"] == title_param:

            return True

    return False
