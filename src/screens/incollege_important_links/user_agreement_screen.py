import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

screen_options = []


def screen():
  screen_display = "By using InCollege you agree to abide by the terms and conditions listed below. If you violate these rules, then we reserve the right to suspend your account. \nPlatform Rules:\n- The use of our platform should be related to professional networking. This is not a general forum\n- No NSFW content\n  - Discrimination based on ethnicity, religion, or political opinions will not be tolerated'"
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
