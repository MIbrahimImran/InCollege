from unittest import mock

import src.constants.error_messages as error_messages
import src.constants.screen_names as screen_names
import src.models.user_model as user_model
import src.services.user_controller as userController


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
        "friends": ['2', '3'],
        "friend_requests": [],
        "notifications": []
    }]
}


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_add_user_to_friends(get_database_object, update_database_object):
    userController.add_user_to_friends("1", "4")
    assert userController.get_user_friends("1") == ['2', '3', '4']


# TEST FUNCTION
def test_default_friends_list():

    # Clear the user list
    userController.clear_users_list()

    # Add new user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)

    # Read from the user database
    stored_user = userController.get_user_by_username("user")

    # Check that the new user's friends list is empty
    assert stored_user["friends"] == []


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_delete_user_friend(get_database_object, update_database_object):
    userController.delete_user_friend("1", "3")
    assert userController.get_user_friends("1") == ['2', '4']


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_id(get_database_object, update_database_object):
    assert userController.get_user_by_username(
        "naruto") == mock_user["users"][0]


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_friend_requests(get_database_object, update_database_object):
    assert userController.get_user_friend_requests("1") == []


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_user_friends(get_database_object, update_database_object):
    assert userController.get_user_friends("1") == ['2', '4']


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_last_name(get_database_object, update_database_object):
    assert userController.get_users_by_last_name(
        "Uzumaki") == mock_user["users"]


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_major(get_database_object, update_database_object):
    assert userController.get_users_by_major("CSE") == mock_user["users"]


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_get_users_by_university(get_database_object, update_database_object):
    assert userController.get_users_by_university("USF") == mock_user["users"]


# TEST FUNCTION
def test_show_my_network():
    assert screen_names.SHOW_MY_NETWORK_SCREEN == "Show My Network"


# TEST FUNCTION
def test_user_database_limit():
    assert error_messages.USER_DATABASE_LIMIT_MESSAGE == "All permitted accounts have been created, please come backlater"

    # Clear the user list
    userController.clear_users_list()

    # Check that more users can be added
    assert userController.is_database_limit_reached() == False

    # Add 10 users to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)

    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)
    userController.add_user(new_user)

    # Check that no more users can be added
    assert userController.is_database_limit_reached() == True
