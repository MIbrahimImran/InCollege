import src.constants.error_messages as errorMessages
import src.constants.screen_messages as screen_messages
import src.constants.screen_names as screenNames
import src.routing.router as router
import src.shared.screen_display_handler as displayHandler
import src.shared.notification_handler as notificationHandler

screen_options = []


def screen():
  screen_display = screen_messages.BRAND_POLICY
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display)
  handle_user_selection(user_selection)


def handle_user_selection(user_selection):
  if (screen_exists(user_selection)):
    navigate_user(user_selection)
  else:
    notificationHandler.display_notification(
      errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
  router.navigate_user(screen)


def screen_exists(user_selection):
  return user_selection in screenNames.screens
