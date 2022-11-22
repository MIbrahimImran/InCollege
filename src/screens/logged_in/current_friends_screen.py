import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.shared.profile_display as profileDisplay

screen_options = ["Show Current Friends", "Unfriend", "Show Friend Profile"]


def screen():
    screen_display = "Current Friends Screen!"
    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection == "Show Current Friends":
        display_current_friends()
    elif user_selection == "Unfriend":
        handle_unfriend()
    elif user_selection == "Show Friend Profile":
        friend_id = input("Enter Friend ID: ")
        user = userController.get_user_by_id(friend_id)
        if user == None:
            notificationHandler.display_notification("Invalid Friend ID!")
        elif friend_id not in auth.logged_in_user['friends']:
            notificationHandler.display_notification(
                "This user is not your friend!")
        else:
            display_user_profile(user)
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def handle_unfriend():
    user_id = auth.logged_in_user['user_id']
    friend_ids = userController.get_user_friends(user_id)
    if (len(friend_ids) == 0):
        notificationHandler.display_notification(
            "You have no friends to unfriend!")
    else:
        friend_username = input(
            "Enter the username of the friend you want to unfriend: ")
        friend = userController.get_user_by_username(friend_username)
        if (friend == None):
            notificationHandler.display_notification(
                errorMessages.USER_NOT_FOUND_MESSAGE)
        else:
            friend_id = friend['user_id']
            if (friend_id in friend_ids):
                friend_id = friend['user_id']
                userController.delete_user_friend(user_id, friend_id)
                userController.delete_user_friend(friend_id, user_id)
                notificationHandler.display_notification("You have unfriended: " +
                                                         friend_username)
            else:
                notificationHandler.display_notification(
                    "You are not friends with this user!")


def display_current_friends():
    user_id = auth.logged_in_user['user_id']
    friend_ids = userController.get_user_friends(user_id)
    if (len(friend_ids) == 0):
        notificationHandler.display_notification("You have no friends!")
    else:
        for friend_id in friend_ids:
            user = userController.get_user_by_id(friend_id)
            print("Username: " + user['username'] + "\n" + "First Name: " + user['profile']['first_name'] + " " +
                  "Last Name: " + user['profile']['last_name'])
            if user['active_profile'] == True:
                print("\033[92m" + "Profile Available! | Friend ID: " +
                      user['user_id'] + "\033[0m")
            else:
                print("\033[90m" + "Profile Unavailable! | Friend ID: " +
                      user['user_id'] + "\033[0m")
            print("\n")


def display_user_profile(user):
    if user['active_profile'] == True:
        profile = profileDisplay.get_profile_display(user)
        print(profile)
    else:
        notificationHandler.display_notification("User doesn't have a profile")


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens
