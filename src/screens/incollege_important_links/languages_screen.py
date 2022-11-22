import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.authentication.auth as auth
import src.constants.success_messages as successMessages

screen_options = ["Spanish", "English"]


def screen():
    screen_display = "Select the language you want to use!"
    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Spanish":
        if auth.logged_in_user == None:
            notificationHandler.display_notification(
                errorMessages.NOT_LOGGED_IN_MESSAGE)
        else:
            userController.set_user_language(
                auth.logged_in_user['user_id'], "Spanish")
            notificationHandler.display_notification(
                successMessages.LANGUAGE_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "English":
        if auth.logged_in_user == None:
            notificationHandler.display_notification(
                errorMessages.NOT_LOGGED_IN_MESSAGE)
        else:
            userController.set_user_language(
                auth.logged_in_user['user_id'], "English")
            notificationHandler.display_notification(
                successMessages.LANGUAGE_CHANGE_SUCCESS_MESSAGE)
    else:

        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
