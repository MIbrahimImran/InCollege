from unittest import mock
import src.constants.error_messages as error_messages
import src.constants.screen_names as screen_names
import src.constants.student_success_story as student_success_story
import src.constants.success_messages as success_messages
import src.models.job_model as jobModel
import src.models.user_model as user_model
import src.services.job_controller as job_controller
import src.services.user_controller as userController
import src.models.profile_model as profileModel

mock_job = {
    "jobs": [{
        "user": "Naruto",
        "title": "Software Engineer",
        "description": "Software Engineer",
        "employer": "Google",
        "location": "Mountain View, CA",
        "requirements": "CSE",
        "salary": "100000",
    }]
}

mock_user = {
    "users": [{
        "user_id": "1",
        "username": "naruto",
        "password": "Password1@",
        "profile": {
            "title": "",
            "first_name": "Naruto",
            "last_name": "Uzumaki",
            "university": "USF",
            "major": "CSE",
            "about": "",
            "education": [],
            "experience": []
        },
        "active_profile": False,
        "settings": {
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "language": "English"
        },
        "jobPosts": [],
        "appliedJobs": [],
        "savedJobs": [],
        "friends": [],
        "friend_requests": [],
        "notifications": []
    }]
}

# TEST FUNCTION


@mock.patch.object(job_controller, 'get_database_object', return_value=mock_job)
@mock.patch.object(job_controller,
                   'update_database_object',
                   return_value="Success")
def test_add_job(get_database_object, update_database_object):
    job = jobModel.Job("Naruto", "Software Engineer", "Google",
                       "Mountain View, CA", "CSE", "100000")
    job_controller.post_job(job)
    assert len(mock_job["jobs"]) == 2


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_first_name(get_database_object, update_database_object):
    assert userController.get_users_by_first_name(
        "Naruto") == mock_user["users"]

    # TEST FUNCTION


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_first_last_name(get_database_object,
                                     update_database_object):
    assert userController.get_user_by_first_last_name(
        "Naruto", "Uzumaki") == mock_user["users"][0]


# TEST FUNCTION
def test_job_db_limit():

    # Clears the jobs list
    job_controller.clear_jobs_list()

    # Check that more jobs can be added
    assert job_controller.is_database_limit_reached() == False

    # Add 5 jobs to the jobs database
    new_job = jobModel.Job("Amazing user", "GM",
                           "Call the shots", "Big Co. Inc.", "Tokyo", "!!!")

    for x in range(10):
        job_controller.post_job(new_job)

    # Check that more jobs cannot be added
    assert job_controller.is_database_limit_reached() == True

    # TEST FUNCTION


def test_previous_screen_option():
    assert screen_names.PREVIOUS_SCREEN == "Previous Screen"


# TEST FUNCTION
def test_promotional_video():
    assert screen_names.PROMOTIONAL_VIDEO_SCREEN == "Promotional Video"


# TEST FUNCTION
def test_search_for_user():
    assert success_messages.USER_FOUND_SUCCESSFUL == "They are a part of the InCollege system"
    assert error_messages.USER_NOT_PART_OF_INCOLLEGE_MESSAGE == "They are not yet a part of the InCollege system yet!"


# TEST FUNCTION
def test_storage_of_job_info():

    # Clear the jobs list
    job_controller.clear_jobs_list()

    # Add a new job to the database
    new_job = jobModel.Job("The best user", "CEO", "Make big decision",
                           "Amazon", "Seattle, WA", "A YUGE AMOUNT. TREMENDOUS.")
    job_controller.post_job(new_job)

    # Store a reference to the jobs database dictionary
    database = job_controller.get_database_object()

    # Store a reference to the jobs list
    jobs_list = database["jobs"]

    # Store a reference to a job that was read from the database
    stored_job = jobs_list[0]

    # Check that you can read the job title from the reference
    stored_job["title"] == "CEO"

    # Check that you can read the job description from the reference
    stored_job["description"] == "Make big decision"

    # Check that you can read the job employer from the reference
    stored_job["employer"] == "Amazon"

    # Check that you can read the job location from the reference
    stored_job["location"] == "Seattle, WA"

    # Check that you can read the job salary from the reference
    stored_job["salary"] == "A YUGE AMOUNT. TREMENDOUS"


# TEST FUNCTION
def test_storage_of_name_of_user():

    # Clear the user list
    userController.clear_users_list()

    # Add a user to the database
    new_user = user_model.User(
        "1", "user", "password", False, profile=profileModel.Profile(first_name="Naruto", last_name="Uzumaki"))
    userController.add_user(new_user)

    # Read from the user database
    stored_user = userController.get_user_by_username("user")

    # Check that you can access the first name of the user
    assert stored_user['profile']["first_name"] == "Naruto"

    # Check that you can access the last name of the user
    assert stored_user['profile']["last_name"] == "Uzumaki"


# TEST FUNCTION
def test_storage_of_user_who_posted_job():

    # Clear the jobs list
    job_controller.clear_jobs_list()

    # Add a new job to the database
    new_job = jobModel.Job("1", "username", "CTO",
                           "ACCELERATE INNOVATION", "META", "SAN FRANCISCO", "$$$")
    job_controller.post_job(new_job)

    # Store a reference to the jobs database dictionary
    database = job_controller.get_database_object()

    # Store a reference to the jobs list
    jobs_list = database["jobs"]

    # Store a reference to a job that was read from the database
    stored_job = jobs_list[0]

    # Check that you can access the user who posted the job
    assert stored_job["user"] == "username"


# TEST FUNCTION
def test_success_story():
    assert student_success_story.STUDENT_SUCCESS_STORY == (
        '\n\nI found value in the InCollege app, it helped me prepare for job interviews through its skills learning program.\n'
        'Through its extensive resume critique program and professional interview tips I was able to apply for multiple SDE roles this year.\n'
        'This summer I received an internship offer from one of the leading tech companies xylophone, I am happy to share my experience \n'
        '\t\t\t\t\t\t\t\t\t\t\t\t\t\t'
        '- Mark Zuckerberg')
