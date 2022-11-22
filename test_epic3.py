import src.constants.screen_names as screen_names
import src.constants.screen_messages as screen_messages
import src.constants.success_messages as successMessages
import src.constants.error_messages as errorMessages
import src.models.user_model as user_model
import src.services.user_controller as user_controller
from unittest import mock


def test_accessibility_message():
    assert screen_messages.ACCESSIBILITY_MESSAGE == "You may use this app for purposes of meeting others who are in college. Through the app, you may perform functions such as connecting with other users, finding a job, learning skills, etc. From time to time this app may be updated to provide other features and functionality. Any unauthorized use of this app is prohibited"


def test_brand_policy():
    assert screen_messages.BRAND_POLICY == "InCollege users may only use InCollege trademarks in strict accordance with this policy. InCollege trademarks may be used on commercial merchandise and online only by persons and entities licensed by InCollege. InCollege should be consulted whenever it is not clear whether a proposed use is permissible. Any unauthorized use of the brand is prohibited."


def test_cookie_policy():
    assert screen_messages.COOKIE_POLICY == 'InCollege uses cookies to enhance the user experience in the application. This includes basic information on your current session and the pages you navigate to while logged in. Additional cookies are used for targeted advertising, bringing you ads that you would like to see. These may track your browsing on other sites. To turn off targeted advertising, navigate to InCollege Important Links -> Guest Controls then select Targeted Ads to toggle on or off, these are on by default'


def test_copyright_notice():
    assert screen_messages.COPYRIGHT_NOTICE == "The InCollege name and branding are protected under Copyright"


def test_copyright_policy():
    assert screen_messages.COPYRIGHT_POLICY == 'You may not share, distribute, or reproduce in any way any copyrighted material, trademarks, or other proprietary information belonging to InCollege without obtaining the prior written consent of InCollege.'


def test_default_guest_controls():

    # Clear the user list
    user_controller.clear_users_list()

    # Add a user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    user_controller.add_user(new_user)

    # Read from the user database
    stored_user = user_controller.get_user_by_username("user")

    # Check that all guest controls are enabled
    assert stored_user["settings"]["sms_notifications"] == True
    assert stored_user["settings"]["email_notifications"] == True
    assert stored_user["settings"]["ad_notifications"] == True


def test_default_language():

    # Clear the user list
    user_controller.clear_users_list()

    # Add a user to the database
    new_user = user_model.User(
        "1", "user", "password", False)
    user_controller.add_user(new_user)

    # Read from the user database
    stored_user = user_controller.get_user_by_username(
        "user")

    # Check that the default language is English
    assert stored_user["settings"]["language"] == "English"


def test_guest_controls():
    assert screen_names.GUEST_CONTROLS_SCREEN == "Guest Control"
    assert successMessages.SMS_CHANGE_SUCCESS_MESSAGE == "SMS notifications changed successfully"
    assert successMessages.EMAIL_CHANGE_SUCCESS_MESSAGE == "Email notifications changed successfully"
    assert successMessages.AD_CHANGE_SUCCESS_MESSAGE == "Ads changed successfully"
    assert errorMessages.INVALID_SELECTION_MESSAGE == "Invalid option selected, please make a selection from the menu"


def test_important_links():
    assert screen_names.INCOLLEGE_IMPORTANT_LINKS_SCREEN == "Important Links"
    assert screen_names.COPYRIGHT_NOTICE_SCREEN == "Copyright Notice"
    assert screen_names.ABOUT_SCREEN == "About"
    assert screen_names.ACCESSIBILITY_SCREEN == "Accessibility"
    assert screen_names.USER_AGREEMENT_SCREEN == "User Agreement"
    assert screen_names.PRIVACY_POLICY_SCREEN == "Privacy Policy"
    assert screen_names.COOKIE_POLICY_SCREEN == "Cookie Policy"
    assert screen_names.COPYRIGHT_POLICY_SCREEN == "Copyright Policy"
    assert screen_names.BRAND_POLICY_SCREEN == "Brand Policy"
    assert screen_names.GUEST_CONTROLS_SCREEN == "Guest Control"
    assert screen_names.LANGUAGE_SCREEN == "Language"


def test_language_options():
    assert screen_names.LANGUAGE_SCREEN == "Language"
    assert successMessages.LANGUAGE_CHANGE_SUCCESS_MESSAGE == "Language changed successfully"


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


@mock.patch.object(user_controller,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(user_controller,
                   'update_database_object',
                   return_value="Success")
def test_set_user_set_user_language(get_database_object,
                                    update_database_object):
    user_controller.set_user_language("1", "Spanish")
    assert user_controller.get_user_by_id("1")["language"] == "Spanish"


def test_privacy_policy():
    assert screen_messages.PRIVACY_POLICY == "InCollege will not sell your data to any 3rd parties.\nOnly the necessary data related to your account will be used when fulfilling site requests.\nThe data we store and use includes: \n- Username\n- Password Hash\n- First Name\n- Last Name\n- Language\n- Guest Controls\n  - SMS\n  - Email\n  - Targeted Ads"


def test_useful_links():
    assert screen_names.GENERAL_SCREEN == "General"
    assert screen_names.BROWSE_INCOLLEGE_SCREEN == "Browse InCollege"
    assert screen_names.BUSSINESS_SOLUTIONS_SCREEN == "Bussiness Solutions"
    assert screen_names.DIRECTORIES_SCREEN == "Directories"

    # test the under construction message
    assert screen_messages.BROWSE_INCOLLEGE_MESSAGE == "under construction"
    assert screen_messages.BUSINESS_SOLUTIONS_MESSAGE == "under construction"
    assert screen_messages.DIRECTORIES_MESSAGE == "under construction"


def test_useful_links_general():
    assert screen_names.SIGNUP_SCREEN == "Sign Up Screen"
    assert screen_names.HELP_CENTER_SCREEN == "Help Center"
    assert screen_names.ABOUT_SCREEN == "About"
    assert screen_names.PRESS_SCREEN == "Press"
    assert screen_names.BLOG_SCREEN == "Blog"
    assert screen_names.CAREERS_SCREEN == "Careers"
    assert screen_names.DEVELOPERS_SCREEN == "Developers"


@mock.patch.object(user_controller,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(user_controller,
                   'update_database_object',
                   return_value="Success")
def test_set_user_sms(get_database_object, update_database_object):
    user_controller.set_user_sms("1", True)
    assert user_controller.get_user_by_id(
        "1")['settings']["sms_notifications"] == True


@mock.patch.object(user_controller,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(user_controller,
                   'update_database_object',
                   return_value="Success")
def test_set_user_email(get_database_object, update_database_object):
    user_controller.set_user_email("1", True)
    assert user_controller.get_user_by_id(
        "1")['settings']["email_notifications"] == True


@mock.patch.object(user_controller,
                   'get_database_object',
                   return_value=mock_user)
@mock.patch.object(user_controller,
                   'update_database_object',
                   return_value="Success")
def test_set_user_ads(get_database_object, update_database_object):
    user_controller.set_user_ads("1", True)
    assert user_controller.get_user_by_id(
        "1")['settings']["ad_notifications"] == True
