import src.constants.screen_names as screenNames
import src.services.user_controller as userController
import src.authentication.auth as auth
import src.routing.router as router


def display_controller(screen_options,
                       screen_description="",
                       previousScreen=True):
    display_screen(screen_description)
    handle_screen_notifcations()
    user_selection = display_screen_options(screen_options, previousScreen)
    clear_display()
    return user_selection


def display_screen_options(screen_options, previousScreen):
    formated_screen_options = format_page_options(screen_options)

    if previousScreen:
        formated_screen_options = add_previous_screen_option(
            formated_screen_options)

    for option_num in formated_screen_options:
        option_name = formated_screen_options[option_num]
        if option_name == screenNames.PREVIOUS_SCREEN or option_name == screenNames.CLEAR_SCREEN:
            print("\033[91m" + option_num + " - " + option_name + "\033[0m")
        elif option_name in screenNames.screens:
            print("\033[92m" + option_num + " - " + option_name + "\033[0m")
        else:
            print("\033[95m" + option_num + " - " + option_name + "\033[0m")

    user_selection = input("\nPlease select from the provided options: ")

    # Returns the value of the key/value pair in the formatted screen options dictionary (a string)
    return formated_screen_options.get(user_selection)


def handle_screen_notifcations():
    screen_notifications = []
    if auth.logged_in_user != None:
        user_notifications = userController.get_user_notifications(
            auth.logged_in_user['user_id'])

        for notification in user_notifications:
            screen_name = router.get_current_screen_name()
            if notification['screenName'] == screen_name:
                screen_notifications.append("\033[93m" +
                                            "Notification: " + "\033[0m" + notification['message'] + '\n')
                clear_screen_notification(
                    auth.logged_in_user['user_id'], notification['screenName'])
    screen_notifications = set(screen_notifications)
    for notification in screen_notifications:
        print(notification)


def add_previous_screen_option(screen_options):
    screen_options['0'] = screenNames.PREVIOUS_SCREEN
    return screen_options


def format_page_options(screen_options):
    formated_screen_options = {}

    option_num = 1

    for option in screen_options:
        formated_screen_options[str(option_num)] = option
        option_num += 1

    return formated_screen_options


def clear_display():
    print("\033[H\033[J", end="")


def clear_screen_notification(user_id, screenName):
    userController.delete_user_screen_notifications(user_id, screenName)


def display_screen(screen_description):
    print("\n" + "\033[94m" + screen_description + "\033[0m" + "\n")
