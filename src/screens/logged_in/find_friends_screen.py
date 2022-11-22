import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.shared.profile_display as profileDisplay

screen_options = [
    "Find by University", "Find by Major", "Find by Last Name",
    "Send Friend Request"
]


def screen():
    screen_display = "Find friends!"

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Find by University":
        university = input("Enter University Name: ")
        users = userController.get_users_by_university(university)
        display_users(users)
    elif user_selection == "Find by Major":
        major = input("Enter Major: ")
        users = userController.get_users_by_major(major)
        display_users(users)
    elif user_selection == "Find by Last Name":
        last_name = input("Enter Last Name: ")
        users = userController.get_users_by_last_name(last_name)
        display_users(users)
    elif user_selection == "Send Friend Request":
        username = input("Enter Username: ")
        userController.send_friend_request(username)

    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def display_users(users):
    if len(users) < 1:
        notificationHandler.display_notification(
            errorMessages.USER_NOT_FOUND_MESSAGE)
    else:
        for user in users:
            print(profileDisplay.get_profile_display(user))
            print("----------------------------------------")


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
