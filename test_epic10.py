from unittest import mock

import src.api.jobs_api as jobsApi
import src.api.student_account_api as studentAccountApi
import src.constants.mock_jobs as mockJobs
import src.constants.mock_user_credentials_db as mockUserDatabase
import src.services.job_controller as jobController
import src.services.user_controller as userController
import src.models.job_application_model as jobApplicationModel
import src.models.user_model as userModel


# TEST FUNCTION
# The parameters do NOT need to match the function names!
# Output saved jobs
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(jobController,
                    'get_database_object',
                    return_value=mockJobs.db)                  
def test_output_saved_jobs_api(get_user_database_object, get_jobs_database_object):
    # jobController.update_database_object()
    jobsApi.saved_jobs()
    with open("src/api/output/MyCollege_savedJobs.txt", "r") as file:
        file_lines = file.readlines()

        assert file_lines[0] == "naruto\n"
        assert file_lines[1] == "CTO\n"
        assert file_lines[2] == "\n"
        assert file_lines[3] == "=====\n"
        assert file_lines[4] == "sasuke\n"
        assert file_lines[5] == "best job\n"
        assert file_lines[6] == "\n"
        assert file_lines[7] == "=====\n"








# TEST FUNCTION
@mock.patch.object(jobController,
                   'get_database_object',
                   return_value=mockJobs.db)
@mock.patch.object(jobController,
                   'update_database_object',
                   return_value="Mock return value")
def test_input_jobs_api(get_database_object, update_database_object):

    # Setup
    # Mock input jobs api file
    with open('src/api/input/newJobs.txt', 'w') as file:
        file.write('Oscars Host\n')
        file.write('You may get in some hot water with jokes.\n')
        file.write('Expect the unexpected, especially from Will Smith!\n')
        file.write('&&&\n')
        file.write('Chris Rock\n')
        file.write('Academy of Motion Picture Arts and Sciences\n')
        file.write('Hollywood, Los Angeles\n')
        file.write(
            'Can\'t put a price on movie magic, that is, until Will Smith shows up!\n')
        file.write('=====\n')

    # Call the function
    # Perhaps "create_jobs()" as the function name would follow the CRUD format.
    jobsApi.get_jobs()

    # Assertion
    # Assert that any new jobs are in the database
    assert jobController.job_exists_by_title("Oscars Host") == True
    assert jobController.job_exists_by_title("Slapfu master") == False


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_input_student_accounts_api(get_database_object, update_database_object):

    # Setup
    with open('src/api/input/studentAccounts.txt', 'w') as file:
        file.write("TheRock Dwayne Johnson\n")
        file.write("Password1@\n")
        file.write("=====\n")

    # Call the function
    # Perhaps it should be named "create_users()"
    studentAccountApi.get_accounts()

    # Assertion
    # Asserts that a user with username TheRock exists
    assert userController.get_user_by_username("TheRock") != None


# TEST FUNCTION
@mock.patch.object(jobController,
                   'get_database_object',
                   return_value=mockJobs.db)
@mock.patch.object(jobController,
                   'is_database_limit_reached',
                   return_value=True)
@mock.patch.object(jobController,
                   'update_database_object',
                   return_value="Mock return value")
def test_jobs_database_limit(get_database_object, is_database_limit_reached, update_database_object):

    # Setup
    # Mock input jobs api file
    with open('src/api/input/newJobs.txt', 'w') as file:
        file.write('11th job\n')
        file.write('Yet another job to post\n')
        file.write('&&&\n')
        file.write('Ambitious Recruiter\n')
        file.write('We Find Talent Co.\n')
        file.write('Worldwide, baby\n')
        file.write('Very tempting amount\n')
        file.write('=====\n')

    # Finds the number of jobs before the function call
    job_list = jobController.get_all_jobs()
    numJobs_before = len(job_list)

    # Call the function
    jobsApi.get_jobs()

    # Assertion

    # Finds the number of jobs before the function call
    job_list = jobController.get_all_jobs()
    numJobs_after = len(job_list)

    # Asserts that no new jobs were added
    assert numJobs_before == numJobs_after


# TEST FUNCTION
@mock.patch.object(jobController,
                   'get_database_object',
                   return_value=mockJobs.db)
def test_output_jobs_api(get_database_object):

    # Setup (Mocking the database)

    # Call the function
    jobsApi.write_jobs()

    # Assertion
    with open("src/api/output/MyCollege_jobs.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that each line of the file is correct
        assert file_lines[0] == "CTO\n"
        assert file_lines[1] == "ACCELERATE INNOVATION\n"
        assert file_lines[2] == "META\n"
        assert file_lines[3] == "SAN FRANCISCO\n"
        assert file_lines[4] == "$$$\n"
        assert file_lines[5] == "=====\n"

        assert file_lines[6] == "best job\n"
        assert file_lines[7] == "best description\n"
        assert file_lines[8] == "best employer\n"
        assert file_lines[9] == "best location\n"
        assert file_lines[10] == "the best\n"
        assert file_lines[11] == "=====\n"


# TEST FUNCTION
@mock.patch.object(jobController,
                   'get_database_object',
                   return_value=mockJobs.db)
@mock.patch.object(jobController,
                   'update_database_object',
                   return_value="Mock return value")
def test_output_jobs_api_after_delete(get_database_object, update_database_object):

    # Setup (Use the mock database)

    # Call the function
    # Deletes "best job" from the mock database
    jobController.delete_job("25")

    # Assertion
    # Opens the jobs output file to be read
    with open("src/api/output/MyCollege_jobs.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that each line of the file is correct
        assert file_lines[0] == "CTO\n"
        assert file_lines[1] == "ACCELERATE INNOVATION\n"
        assert file_lines[2] == "META\n"
        assert file_lines[3] == "SAN FRANCISCO\n"
        assert file_lines[4] == "$$$\n"
        assert file_lines[5] == "=====\n"

        # Assert that the next job is not "best job"
        assert file_lines[6] != "best job\n"

# TEST FUNCTION


@mock.patch.object(jobController,
                   'get_database_object',
                   return_value=mockJobs.db)
@mock.patch.object(jobController,
                   'update_database_object',
                   return_value="Mock return value")
def test_unique_job_title_condition(get_database_object, update_database_object):

    # Setup

    # Assert that the CTO job already exists
    assert jobController.job_exists_by_title("CTO") == True

    # Specify a job that already exists in the mock database
    with open('src/api/input/newJobs.txt', 'w') as file:
        file.write('CTO\n')
        file.write('ACCELERATE INNOVATION\n')
        file.write('&&&\n')
        file.write('username\n')
        file.write('META\n')
        file.write('SAN FRANCISCO\n')
        file.write('$$$\n')
        file.write('=====\n')

    # Call the function
    # Attempts to add a job that already exists
    jobsApi.get_jobs()

    # Assertion
    assert jobController.all_job_titles_are_unique() == True

# TEST FUNCTION


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'is_database_limit_reached',
                   return_value=True)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_users_database_limit(get_database_object, is_database_limit_reached, update_database_object):

    # Setup
    # Mock input users api file
    with open('src/api/input/studentAccounts.txt', 'w') as file:
        file.write('11th user Dave Chappelle\n')
        file.write('Password1@\n')
        file.write('=====\n')

    # Finds the number of users before the function call
    users_dictionary = userController.get_database_object()
    users_list = users_dictionary["users"]
    numUsers_before = len(users_list)

    # Call the function
    studentAccountApi.get_accounts()

    # Finds the number of users after the function call
    users_dictionary = userController.get_database_object()
    users_list = users_dictionary["users"]
    numUsers_after = len(users_list)

    # Assertion
    # Asserts that no new jobs were added
    assert numUsers_before == numUsers_after


@mock.patch.object(userController,
                   'get_user_by_id',
                   return_value=mockUserDatabase.db["users"][0])
def test_applied_jobs_api(get_user_by_id):
    application = jobApplicationModel.JobApplication(
        "1", "11-20-2021", "11-20-2022", "TestApplication")
    jobController.add_application_to_job("25", application)
    jobsApi.applied_jobs()
    with open("src/api/output/MyCollege_appliedJobs.txt", "r") as file:
        file_lines = file.readlines()
        assert file_lines[24] == "TestApplication\n"




# TEST FUNCTION
# @mock.patch.object(userController,
#                    'get_database_object',
#                    return_value=mockUserDatabase.db)                   
# def test_output_saved_jobs_api(get_database_object):

#     # Setup (Mock the user database) (Write to the jobs database) (Cannot mock two functions with the same name)
    
#     # Stores a reference to the mock job data
#     mock_jobs_dictionary = mockJobs.jobs_dictionary

#     # Updates the jobs database with the mock job data
#     jobController.update_database_object(mock_jobs_dictionary)

#     # Call the function
#     jobsApi.saved_jobs()

#     # Assertion
#      # Opens the jobs output file to be read
#     with open("src/api/output/MyCollege_savedJobs.txt", "r") as file:

#         # Gets a list of lines from the file
#         file_lines = file.readlines()

#         # Assert that each line of the file is correct
#         assert file_lines[0] == "naruto\n"
#         assert file_lines[1] == "CTO\n"
#         assert file_lines[2] == "=====\n"
#         assert file_lines[3] == "sasuke\n"
#         assert file_lines[4] == "President of Software Development\n"
#         assert file_lines[5] == "=====\n"
#         assert file_lines[6] == "badukee\n"
#         assert file_lines[7] == "CTO\n"
#         assert file_lines[8] == "=====\n"

# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_output_user_profiles_api(get_database_object, update_database_object):
    
    # Setup (Mock the user database)

    # Call the function
    studentAccountApi.write_profiles()

    # Assertion
    # Opens the jobs output file to be read
    with open("src/api/output/MyCollege_profiles.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that each line of the output file is formatted correctly
        assert file_lines[0] == "Mr.\n"
        assert file_lines[1] == "CSE\n"
        assert file_lines[2] == "USF\n"
        assert file_lines[3] == "I am a ninja\n"
        assert file_lines[4] == "THE University of South Florida\tScience of Computers\t2022-2022\n"
        assert file_lines[5] == "Software developer VIII\tJane Street\tNew York\t1 week ago\t1 day ago\n"
        assert file_lines[6] == "=====\n"

        assert file_lines[7] == "Mr.\n"
        assert file_lines[8] == "CSE\n"
        assert file_lines[9] == "USF\n"
        assert file_lines[10] == "I am a ninja\n"
        assert file_lines[11] == "None\n"
        assert file_lines[12] == "None\n"
        assert file_lines[13] == "=====\n"


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_output_user_profiles_api_after_new_user_sign_up(get_database_object, update_database_object):
    
    # Setup (Create a mock profile)
    new_profile_dictionary = {
        "title": "Ms.", 
        "first_name": "Sakura", 
        "last_name": "Haruno", 
        "university": "USF", 
        "major": "CS", 
        "about": "I'm a ninja!",
        "education": [],
        "experience": []
    }

    # Call the function
    studentAccountApi.add_profile_output(new_profile_dictionary)

    # Assertion
    # Opens the jobs output file to be read
    with open("src/api/output/MyCollege_profiles.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that Sakura's profile was added to the profile output file
        assert file_lines[28] == "Ms.\n"


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
def test_output_users_api(get_database_object):
    
    # Setup (Mock the user database)

    # Call the function
    studentAccountApi.write_accounts()

    # Assertion
    # Opens the jobs output file to be read
    with open("src/api/output/MyCollege_users.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that each line of the output file is formatted correctly
        assert file_lines[0] == "naruto\tplus\n"
        assert file_lines[1] == "sasuke\tplus\n"
        assert file_lines[2] == "badukee\tplus\n"


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")                   
def test_output_users_api_after_new_user_sign_up(get_database_object, update_database_object):

    # Setup
    # Define a new user to add to the mock database
    new_user = userModel.User(username = "sakura", premium = True)

    # Call the function
    # Add the new user to the database
    userController.add_user(new_user)

    # Assertion
    # Opens the jobs output file to be read
    with open("src/api/output/MyCollege_users.txt", "r") as file:

        # Gets a list of lines from the file
        file_lines = file.readlines()

        # Assert that each line of the output file is formatted correctly
        # Note: Sakura was added on the fifth line of the file
        assert file_lines[0] == "naruto\tplus\n"
        assert file_lines[1] == "sasuke\tplus\n"
        assert file_lines[2] == "badukee\tplus\n"
        assert file_lines[3] == "TheRock\tstandard\n"
        assert file_lines[4] == "sakura\tplus\n"


