import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.authentication.auth as auth
import src.constants.success_messages as successMessages

screen_options = []


def screen():
    global screen_options
    screen_options.clear()
    screen_display = "Welcome to guest controls!"
    if auth.logged_in_user == None:
        notificationHandler.display_notification(
            errorMessages.NOT_LOGGED_IN_MESSAGE)
    else:
        options = get_user_nofication_options()
        for option in options:
            screen_options.append(option)

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    user_id = None
    if auth.logged_in_user:
        user_id = auth.logged_in_user.get('user_id')
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Turn off sms":
        userController.set_user_sms(user_id, False)
        notificationHandler.display_notification(
            successMessages.SMS_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "Turn on sms":
        userController.set_user_sms(user_id, True)
        notificationHandler.display_notification(
            successMessages.SMS_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "Turn off email":
        userController.set_user_email(user_id, False)
        notificationHandler.display_notification(
            successMessages.EMAIL_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "Turn on email":
        userController.set_user_email(user_id, True)
        notificationHandler.display_notification(
            successMessages.EMAIL_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "Turn off ads":
        userController.set_user_ads(user_id, False)
        notificationHandler.display_notification(
            successMessages.AD_CHANGE_SUCCESS_MESSAGE)
    elif user_selection == "Turn on ads":
        userController.set_user_ads(user_id, True)
        notificationHandler.display_notification(
            successMessages.AD_CHANGE_SUCCESS_MESSAGE)
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def get_user_nofication_options():
    options = []
    user = userController.get_user_by_id(auth.logged_in_user['user_id'])
    if user['settings']['sms_notifications'] == False:
        options.append("Turn on sms")
    else:
        options.append("Turn off sms")

    if user['settings']['email_notifications'] == False:
        options.append("Turn on email")
    else:
        options.append("Turn off email")

    if user['settings']['ad_notifications'] == False:
        options.append("Turn on ads")
    else:
        options.append("Turn off ads")
    return options


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
