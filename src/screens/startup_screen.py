import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler

import src.constants.student_success_story as story

screen_options = [
  screenNames.LOGIN_SCREEN, screenNames.SIGNUP_SCREEN,
  screenNames.PROMOTIONAL_VIDEO_SCREEN, screenNames.USEFUL_LINKS_SCREEN,
  screenNames.INCOLLEGE_IMPORTANT_LINKS_SCREEN, screenNames.FIND_CONTACT_SCREEN
]


def screen():
  screen_display = story.STUDENT_SUCCESS_STORY
  user_selection = displayHandler.display_controller(screen_options,
                                                     screen_display,
                                                     previousScreen=False)
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
