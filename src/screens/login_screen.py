import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.constants.success_messages as successMessages
import src.models.user_model as userModel
import src.authentication.auth as auth

screen_options = ["Login"]


def screen():
  screen_display = "Welcome to login screen, select from the options below!"
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)

  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  elif user_selection == "Login":
    handle_login()
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def handle_login():
  user = get_user_login_data()
  if auth.authenticate_user(user):
    notificationHandler.display_notification(
      successMessages.SUCCESSFUL_LOGIN_MESSAGE)
    navigate_user(screenNames.USER_HOME_SCREEN)
  else:
    screen()


def get_user_login_data():
  username = input("Username: ")
  password = input("Password: ")
  return userModel.User(username=username, password=password)


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
