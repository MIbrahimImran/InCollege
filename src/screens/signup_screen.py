import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.models.user_model as userModel
import src.authentication.auth as auth
import src.shared.password_validator as passwordValidator
import src.services.user_controller as userController
import src.services.id_controller as idController
import src.shared.format_input_first_upper as formatToFirstUpper
import src.models.profile_model as profileModel


def screen():
    screen_display = ""
    screen_options = get_screen_options()

    if auth.logged_in_user == None:
        screen_display = "Welcome to signup screen, select from the options below! \n\nStandard Sign Up is free, Plus Sign Up is $10/month! \nWith Plus you can send friend requests to any user in the system!"
    else:
        screen_display = "You are already signed in!"

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_signup(premium):
    user = get_user_signup_data(premium)
    if passwordValidator.is_password_valid(user.password):
        userController.add_user(user)
    else:
        notificationHandler.display_notification(
            errorMessages.WEAK_PASSWORD_MESSAGE)

    screen()


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Standard Sign Up":
        handle_signup(premium=False)
    elif user_selection == "Plus Sign Up":
        handle_signup(premium=True)
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
        screen()


def get_user_signup_data(premium):
    user_id = idController.generate_user_id()
    username = input("Username: ")
    password = input("Password: ")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    university = input("University: ")
    major = input("Major: ")

    major = formatToFirstUpper.format_input_first_upper(major)
    university = formatToFirstUpper.format_input_first_upper(university)

    profile = profileModel.Profile(
        first_name=first_name, last_name=last_name, university=university, major=major)

    return userModel.User(user_id=user_id,
                          username=username,
                          password=password,
                          profile=profile,
                          premium=premium)


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def get_screen_options():
    screen_options = []
    if auth.logged_in_user == None:
        screen_options.append("Standard Sign Up")
        screen_options.append("Plus Sign Up")
    return screen_options
