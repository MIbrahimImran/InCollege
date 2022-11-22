from unittest import mock
import src.authentication.auth as auth
import src.constants.error_messages as error_messages
import src.constants.screen_names as screen_names
import src.constants.success_messages as success_messages
import src.models.user_model as user_model
import src.services.user_controller as user_controller
import src.shared.password_validator as passwordValidator
import src.models.user_settings_model as userSettingsModel
import src.models.profile_model as profileModel

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


def test_add_user_to_db():

    user_controller.clear_users_list()

    database = user_controller.get_database_object()
    assert len(database["users"]) == 0

    test_user = user_model.User(
        "1", "user", "password", False, profileModel.Profile(), userSettingsModel.Settings())
    user_controller.add_user(test_user)

    database = user_controller.get_database_object()
    assert len(database["users"]) == 1


def test_authenticate_user():

    user_controller.clear_users_list()
    test_user = user_model.User(
        "1", "user", "password", False, profileModel.Profile(), userSettingsModel.Settings())
    assert auth.authenticate_user(test_user) == False

    user_controller.add_user(test_user)
    assert auth.authenticate_user(test_user) == True


# TEST FUNCTION
@mock.patch.object(user_controller,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(user_controller,
                   'update_database_object',
                   return_value="Success")
def test_get_user_by_username(get_database_object, update_database_object):
    assert user_controller.get_user_by_username(
        "naruto") == mock_user["users"][0]


def test_home_page():
    assert screen_names.JOB_SEARCH_SCREEN == "Job Search Screen"
    assert screen_names.LEARN_NEW_SKILL_SCREEN == "Learn New Skill"
    assert screen_names.INCOLLEGE_IMPORTANT_LINKS_SCREEN == "Important Links"
    assert screen_names.USEFUL_LINKS_SCREEN == "Useful Links"
    assert screen_names.SHOW_MY_NETWORK_SCREEN == "Show My Network"


def test_incorrect_login_details_message():
    assert error_messages.INCORRECT_LOGIN_DETAILS_MESSAGE == "Incorrect username / password, please try again"


# def test_password_validator():
def test_is_password_valid():
    # too short
    assert passwordValidator.is_password_valid("abc") == False

    # valid
    assert passwordValidator.is_password_valid("Validpas1!") == True

    # too long
    assert passwordValidator.is_password_valid("A1cdefghijklmnop!") == False

    # no number
    assert passwordValidator.is_password_valid("Abcdefgh!") == False

    # no special character
    assert passwordValidator.is_password_valid("Arabhdi1") == False

    assert passwordValidator.is_password_valid("password") == False
    assert passwordValidator.is_password_valid("Password") == False
    assert passwordValidator.is_password_valid("Password1") == False
    assert passwordValidator.is_password_valid("Password1@12345") == False
    assert passwordValidator.is_password_valid("Pass1@") == False
    assert passwordValidator.is_password_valid("Password1@") == True


def test_learn_new_skills():
    assert screen_names.WEB_DEVELOPMENT_SCREEN == "Web Development"
    assert screen_names.CODING_SCREEN == "Coding"
    assert screen_names.COMMUNICATION_SCREEN == "Communication"
    assert screen_names.RESUME_CRITIQUE_SCREEN == "Resume Critique"
    assert screen_names.MICROSOFT_EXCEL_SCREEN == "Microsoft Excel"
    assert screen_names.PREVIOUS_SCREEN == "Previous Screen"


def test_max_user_limit_message():
    assert error_messages.MAX_USER_LIMIT_MESSAGE == "All permitted accounts have been created, please come back later"


def test_successful_login_message():
    assert success_messages.SUCCESSFUL_LOGIN_MESSAGE == "You have successfully logged in"
