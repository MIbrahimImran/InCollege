import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.constants.success_messages as successMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.models.profile_model as profileModel

screen_options = ["Find User"]


def screen():
    screen_display = "Find contacts!"
    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Find User":
        handle_find_contact()
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
        screen()


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def handle_find_contact():
    user = get_contact_data()
    user_found = userController.get_user_by_first_last_name(
        user.first_name, user.last_name)
    if user_found == None:
        notificationHandler.display_notification(
            errorMessages.USER_NOT_PART_OF_INCOLLEGE_MESSAGE)
    else:
        notificationHandler.display_notification(
            successMessages.USER_FOUND_SUCCESSFUL)
        navigate_user(screenNames.STARTUP_SCREEN)
    screen()


def get_contact_data():
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    return profileModel.Profile(first_name=first_name, last_name=last_name)
