from unittest import mock

import src.authentication.auth as auth
import src.constants.mock_job_applications as mockJobApplications
import src.constants.mock_user_credentials_db as mockUserDatabase
import src.routing.routes as routes
import src.services.job_controller as jobController
import src.services.user_controller as userController


# Format of test cases: Setup --> Call a function --> Assertion

# TEST FUNCTION
# This tests that if the student logs in, they will be notified that they have
# applied for a specific number of jobs based on the database
# Doesn't Update any database
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_job_application_count_notification(get_database_object, update_database_object):

    # Setup
    # Get a reference to the mock user database
    # How many notifications does the user have before the function?  They have 0
    # The user has applied for a job, so after the function, they should have 1 notification
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    # Adds a notification to the user's notifications list
    routes.jobsearchScreen.send_number_of_applied_jobs_notification()

    # Assertion
    # Assert the user has 1 notification
    assert auth.logged_in_user["notifications"][0]["message"] == "You have applied for 1 job(s)"


# TEST FUNCTION
# We do not get a fresh mock database for each function call
# Changes from previous functions are stored in the mock database
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_send_job_application_notification(get_database_object, update_database_object):

    # Setup
    # User has no notifications
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    # Adds a notification to the user
    routes.userhomeScreen.send_job_application_notification()

    # Assertion
    # Assert the user has a notification to apply for a job
    assert auth.logged_in_user["notifications"][1]["message"] == "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!"


# TEST FUNCTION
# To do: Find the function where the user is being notified of new job postings
# send_new_job_notification()
@mock.patch.object(userController,
                   'get_all_users',
                   return_value=mockUserDatabase.db["users"])
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")                   
def test_send_new_job_notification(get_all_users, get_database_object, update_database_object):

    # Setup
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    userController.send_new_job_notification()

    # Assertion
    assert auth.logged_in_user["notifications"][2]["message"] == "A new job has been posted"


# TEST FUNCTION
@mock.patch.object(jobController,
                   'get_job_applications',
                   return_value=mockJobApplications.list)
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_notify_users_of_job_deletion(get_job_applications, get_database_object, update_database_object):

    # Setup
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    # Pass in the ID of the job that was deleted
    routes.jobsearchScreen.notify_users_of_job_deletion(100)

    # Assertion
    assert auth.logged_in_user["notifications"][3]["message"] == "Your application for job id 100 has been deleted. The job is no longer available."

    
# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_send_unread_message_notification(get_database_object, update_database_object):
    
    # Setup
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    routes.userhomeScreen.send_unread_message_notification()

    # Assertion
    assert auth.logged_in_user["notifications"][4]["message"] == "You have messages waiting for you!"


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_all_users',
                   return_value=mockUserDatabase.db["users"])
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_send_user_signup_notification(get_all_users, get_database_object, update_database_object):
    
    # Setup
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    # Assumes that user2 is a newly created user
    userController.send_user_signup_notification(mockUserDatabase.user2)

    # Assertion
    assert auth.logged_in_user["notifications"][5]["message"] == "sasuke has joined InCollege"


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_send_profile_completion_notification(get_database_object, update_database_object):

    # Setup
    routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1

    # Call the function
    routes.userhomeScreen.send_profile_completion_notification()

    # Assertion
    assert auth.logged_in_user["notifications"][6]["message"] == "Don't forget to create a profile"
