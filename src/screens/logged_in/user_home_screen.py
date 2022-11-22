from datetime import datetime

import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.services.activity_controller as activityController

screen_options = [
    screenNames.USER_PROFILE_SCREEN,
    screenNames.SHOW_MY_NETWORK_SCREEN,
    screenNames.JOB_SEARCH_SCREEN,
    screenNames.LEARN_NEW_SKILL_SCREEN,
    screenNames.INCOLLEGE_IMPORTANT_LINKS_SCREEN,
    screenNames.USEFUL_LINKS_SCREEN,
    screenNames.INBOX_SCREEN,
    "Sign Out"
]


def screen():
    screen_display = "Welcome to Incollege " + auth.logged_in_user[
        "username"] + "!" "\n"

    handle_friend_requests()

    # Extra feature - If user has not logged in for over a week, send them a notification.
    # if is_last_login_over_week():
    #     send_inactivity_notification()

    if activityController.is_last_job_application_over_week(auth.logged_in_user["user_id"]):
        send_job_application_notification()

    if auth.logged_in_user["active_profile"] == False:
        send_profile_completion_notification()

    if len(auth.logged_in_user["messages"]) >= 1:
        send_unread_message_notification()

    update_last_login()

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display,
                                                       previousScreen=False)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Sign Out":
        router.screen_history = []
        auth.logged_in_user = None
        notificationHandler.display_notification(
            errorMessages.SIGN_OUT_SUCCESS_MESSAGE)
        router.navigate_user(screenNames.STARTUP_SCREEN)
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
        screen()


def handle_friend_requests():
    friend_requests = auth.logged_in_user["friend_requests"]
    if len(friend_requests) >= 1:
        notificationHandler.display_notification(
            "You have pending friend request!")
        while len(friend_requests) >= 1:
            user_id = auth.logged_in_user["user_id"]
            request_id = friend_requests[-1]
            user = userController.get_user_by_id(request_id)
            user_selection = input(user['profile']['first_name'] +
                                   " Wants to be your friend! Accept request y/n: ")
            if user_selection == 'y':
                # Add both the send and reciever to each others friend list
                userController.add_user_to_friends(user_id, request_id)
                userController.add_user_to_friends(request_id, user_id)
                userController.delete_user_friend_request(user_id, request_id)
                friend_requests.pop()
            elif user_selection == 'n':
                userController.delete_user_friend_request(user_id, request_id)
                friend_requests.pop()
            else:
                notificationHandler.display_notification(
                    errorMessages.INVALID_SELECTION_MESSAGE)


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def is_last_login_over_week():
    current_date = datetime.now()
    last_login = datetime.strptime(
        auth.logged_in_user["last_login"], "%Y-%m-%d %H:%M:%S.%f")
    return (current_date - last_login).days >= 7


def update_last_login():
    userController.update_last_login(auth.logged_in_user["user_id"])


def send_inactivity_notification():
    userController.send_notification(
        auth.logged_in_user["user_id"],
        "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!",
        screenName=screenNames.USER_HOME_SCREEN)


def send_profile_completion_notification():
    userController.send_notification(
        auth.logged_in_user["user_id"],
        "Don't forget to create a profile",
        screenName=screenNames.USER_HOME_SCREEN)


def send_unread_message_notification():
    userController.send_notification(
        auth.logged_in_user["user_id"],
        "You have messages waiting for you!",
        screenName=screenNames.USER_HOME_SCREEN)


def send_job_application_notification():
    userController.send_notification(
        auth.logged_in_user["user_id"],
        "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!",
        screenName=screenNames.USER_HOME_SCREEN)
