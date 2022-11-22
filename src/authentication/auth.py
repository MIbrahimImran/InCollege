import src.services.user_controller as userController
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

import src.models.user_model as userModel

logged_in_user = None


def authenticate_user(user):
    userFound = userController.get_user_by_username(user.username)
    if userFound:
        if (userFound["password"] == user.password):
            global logged_in_user
            logged_in_user = userFound
            return True
        else:
            notificationHandler.display_notification(
                errorMessages.INVALID_PASSWORD_MESSAGE)
    else:
        notificationHandler.display_notification(
            errorMessages.USER_NOT_FOUND_MESSAGE)
    return False


def update_logged_in_user():
    authenticate_user(
        userModel.User(username=logged_in_user['username'],
                       password=logged_in_user['password']))
