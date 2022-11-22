import pytest
from unittest import mock

import src.services.user_controller as userController
import src.shared.password_validator as passwordValidator
import src.services.job_controller as jobController
import src.models.job_model as jobModel
import src.models.user_model as user_model

# note: I'm importing routes here instead of the actual module in screens because if I do, it results in a circular import error
import src.routing.routes as routes
import development.create_mock_user_data as mock_data

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
            "about": "I am a ninja",
            "education": [],
            "experience": [
                {
                    "edu_id": "10",
                    "school": "usf",
                    "degree": "comp sci",
                    "years": "2019-2023"
                }
            ]
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
        "friends": ['2', '3'],
        "friend_requests": [],
        "notifications": []
    }]
}

# Test Function


@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_title(get_database_object, update_database_object):
    userController.set_user_title("naruto", "Computer Science Student")
    assert userController.get_user_by_id(
        "1")['profile']["title"] == "Computer Science Student"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_about(get_database_object, update_database_object):
    userController.set_user_about("naruto", "I am a computer science student")
    assert userController.get_user_by_id(
        "1")['profile']["about"] == "I am a computer science student"

# Not sure what this does tbh, I'll have to look into it
# # Test Function
# @mock.patch.object(userController,
#                    'get_database_object',
#                    return_value=mock_user)
# @mock.patch.object(userController,
#                    'update_database_object',
#                    return_value="Success")
# def test_set_has_profile(get_database_object, update_database_object):
#     userController.set_has_profile("naruto", True)
#     assert userController.get_user_by_id("1")["has_profile"] == True


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_major(get_database_object, update_database_object):
    userController.set_user_major("naruto", "English")
    assert userController.get_user_by_id("1")['profile']["major"] == "English"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_user_university(get_database_object, update_database_object):
    userController.set_user_university("naruto", "UCF")
    assert userController.get_user_by_id("1")['profile']["university"] == "UCF"


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
@mock.patch('src.routing.routes.userprofileScreen.handle_user_selection')
@mock.patch('src.shared.screen_display_handler.handle_screen_notifcations')
def test_user_create_profile_option(get_database_object, update_database_object, handle_user_selection_mock, handle_screen_notifications_mock, capsys, monkeypatch):
    user = userController.get_user_by_id("1")
    routes.userprofileScreen.auth.logged_in_user = user
    handle_user_selection_mock.return_value = None
    monkeypatch.setattr('builtins.input', lambda selection: '', raising=False)
    routes.userprofileScreen.screen()
    stdout, stderr = capsys.readouterr()
    assert "1 - Create User Profile" in stdout

# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch('src.routing.routes.userprofileScreen.handle_user_selection')
@mock.patch('src.shared.screen_display_handler.handle_screen_notifcations')
def test_user_show_profile_option(get_database_object, handle_user_selection_mock, handle_screen_notifcations_mock, capsys,
                                  monkeypatch):
    user = get_database_object()
    user['active_profile'] = True
    routes.userprofileScreen.auth.logged_in_user = user
    handle_user_selection_mock.return_value = None
    monkeypatch.setattr('builtins.input', lambda selection: '', raising=False)
    routes.userprofileScreen.screen()
    stdout, stderr = capsys.readouterr()
    assert "This is the profile of {user['first_name']} {user['last_name']}!"
    assert "Title" and "University" and "Major" and "About" and "Experience" and "Education" in stdout


@mock.patch('src.routing.routes.userprofileScreen.continue_editing')
@mock.patch('src.routing.routes.userprofileScreen.handle_get_experience')
def test_enter_profile_information(continue_editing_mock, handle_get_experience_mock, capsys, monkeypatch):
    continue_editing_mock.return_value = True
    routes.userprofileScreen.auth.logged_in_user = mock_user['users'][0]
    inputs = iter([
        'Hokage',
        "I was the best ninja in the hidden leaf village but now i go to usf",
        'university of south florida', 'computer science', '2019 - 2023'
    ])
    monkeypatch.setattr('builtins.input', lambda selection: next(inputs))
    title, about, education, experience = routes.userprofileScreen.get_user_profile_data(
    )
    assert title == 'Hokage'
    assert about == "I was the best ninja in the hidden leaf village but now i go to usf"

# Test Function
def test_profile_contains_proper_information(monkeypatch):
    # user = mock_data.get_mock_user_data()['users'][0]
    user = userController.handle("1")
    assert user['profile'].get('education') != None
    assert user['profile'].get('experience') != None
    assert user['profile'].get('title') != None
    assert user['profile'].get('university') != None
    assert user['profile'].get('major') != None
    assert user['profile'].get('about') != None


# should I also test db functionality to see if the db is updated with the correct info as well?
# Test Function
def test_enter_job_information(monkeypatch):
    inputs = iter([
        'Hokage', 'Land of Fire', '??/??/??', '??/??/??', 'Hidden Leaf Village',
        'Leader of the village'
    ])
    monkeypatch.setattr('builtins.input', lambda input: next(inputs))
    job = routes.userprofileScreen.get_experience_data(False)
    assert job.title == 'Hokage'
    assert job.employer == 'Land of Fire'
    assert job.start_date == '??/??/??'
    assert job.end_date == '??/??/??'
    assert job.location == 'Hidden Leaf Village'
    assert job.description == 'Leader of the village'


# Test Function
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_set_past_job_title(get_database_object, update_database_object):
    # Set the title of Past Job #1
    user = get_database_object()['users'][0]
    userController.set_past_job_title(user['username'], 0, "My Dream Job")
    test_user = userController.get_user_by_username(user['username'])
    past_job_list = test_user['profile']["experience"]
    past_job_1 = past_job_list[0]
    assert past_job_1["job_title"] == "My Dream Job"


# Test Function
def test_set_past_job_employer():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the employer of Past Job #1
    userController.set_past_job_employer("user", 0, "My Dream Employer")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1["job_employer"] == "My Dream Employer"


# Test Function
def test_set_past_job_start_date():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the start date of Past Job #1
    userController.set_past_job_start_date("user", 0, "800 BC")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1["start_date"] == "800 BC"


# Test Function
def test_set_past_job_end_date():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the end date of Past Job #1
    userController.set_past_job_end_date("user", 0, "January 1st, 2076")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1["end_date"] == "January 1st, 2076"


# Test Function
def test_set_past_job_location():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the location of Past Job #1
    userController.set_past_job_location("user", 0, "Hidden Leaf Village")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1["end_date"] == "Hidden Leaf Village"


# Test Function
def test_set_past_job_location():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the location of Past Job #1
    userController.set_past_job_location("user", 0, "Hidden Leaf Village")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1["location"] == "Hidden Leaf Village"


# Test Function
def test_set_past_job_description():

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 1 user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Set the description of Past Job #1
    userController.set_past_job_description(
        "user", 0, "Wonderful. Couldn't be better! Tremendous!")

    test_user = userController.get_user_by_username("user")
    past_job_list = test_user["experience"]
    past_job_1 = past_job_list[0]

    assert past_job_1[
        "description"] == "Wonderful. Couldn't be better! Tremendous!"
