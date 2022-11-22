import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.authentication.auth as auth

screen_options = ["Show Pending Requests"]


def screen():
    screen_display = "Welcome to pending requests screen!"
    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Show Pending Requests":
        handle_pending_requests()
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def handle_pending_requests():
    user_id = auth.logged_in_user['user_id']
    pending_requests = userController.get_user_friend_requests(user_id)
    if len(pending_requests) <= 0:
        notificationHandler.display_notification("No Pending friend requests!")


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
