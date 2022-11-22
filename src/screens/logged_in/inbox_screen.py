from webbrowser import get
import src.routing.router as router
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.shared.notification_handler as notificationHandler
import src.services.user_controller as userController
import src.authentication.auth as auth
import src.models.message_model as messageModel
import src.services.id_controller as idController

screen_options = ["Display Messages",
                  "Open a Message", "Send Message", "Delete Message", "Show Friends"]


def screen():
    screen_display = "Welcome To your Inbox!"

    screen_options = get_screen_options()

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif (user_selection == "Display Messages"):
        handle_display_messages()
    elif (user_selection == "Open a Message"):
        handle_open_message()
    elif (user_selection == "Send Message"):
        handle_send_message()
    elif (user_selection == "Show Friends"):
        handle_show_friends()
    elif (user_selection == "Show All Users"):
        handle_show_all_users()
    elif (user_selection == "Delete Message"):
        handle_delete_message()
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def handle_display_messages():
    messages = userController.get_messages(auth.logged_in_user["user_id"])
    if len(messages) == 0:
        notificationHandler.display_notification("No Messages!")
    else:
        for message in messages:
            print("\033[93m" + "Message ID: " +
                  "\033[0m", message["message_id"])
            sender_username = userController.get_user_by_id(
                message["sender_id"])['username']
            print("\033[94m" + "Sender: " + "\033[0m", sender_username)
            if message["read"]:
                print("\x1b[0;30;41mREAD\x1b[0m\n")
            else:
                print("\x1b[0;30;42mUNREAD\x1b[0m\n")


def handle_open_message():
    message_id = input("Enter Message ID: ")
    message = userController.get_message(
        auth.logged_in_user["user_id"], message_id)
    if message is None:
        notificationHandler.display_notification("Invalid Message ID!")
    else:
        print("\033[93m" + "Message ID: " +
              "\033[0m", message["message_id"])
        sender_username = userController.get_user_by_id(
            message["sender_id"])['username']
        print("\033[94m" + "Sender: " + "\033[0m", sender_username)
        print("\033[94m" + "Message: " + "\033[0m", message["message"])
        print("\x1b[0;30;41mREAD\x1b[0m\n")
        userController.mark_message_as_read(
            auth.logged_in_user["user_id"], message_id)


def handle_send_message():
    recipient_id = input("Enter User ID: ")
    if sending_self_message(recipient_id) == True:
        notificationHandler.display_notification(
            "You cannot send a message to yourself!")
    elif is_recipient_a_friend(recipient_id) or is_recipient_message_in_inbox(recipient_id) or is_sender_premium_user():
        messageInput = input("Enter Message: ")
        message_id = idController.generate_message_id()
        message = messageModel.Message(
            message_id, messageInput, auth.logged_in_user["user_id"], recipient_id, False)
        userController.send_message(recipient_id, message.__dict__)
        userController.send_message_notification(
            recipient_id, message.__dict__)
        notificationHandler.display_notification("Message Sent Successfully!")
    else:
        notificationHandler.display_notification(
            "I'm sorry, you are not friends with that person!")


def handle_show_friends():
    friends = userController.get_user_friends(auth.logged_in_user["user_id"])
    if len(friends) == 0:
        notificationHandler.display_notification("No Friends!")
    else:
        for friend in friends:
            print("\033[93m" + "Friend ID: " + "\033[0m", friend)
            print("\033[94m" + "Username: " + "\033[0m",
                  userController.get_user_by_id(friend)['username'])


def handle_show_all_users():
    users = userController.get_all_users()
    for user in users:
        print("\033[93m" + "User ID: " + "\033[0m", user["user_id"])
        print("\033[94m" + "Username: " + "\033[0m", user["username"] + "\n")


def handle_delete_message():
    message_id = input("Enter Message ID: ")
    message = userController.get_message(
        auth.logged_in_user["user_id"], message_id)
    if message is None:
        notificationHandler.display_notification("Invalid Message ID!")
    else:
        userController.delete_message(
            auth.logged_in_user["user_id"], message_id)
        notificationHandler.display_notification(
            "Message Deleted Successfully!")


def is_recipient_a_friend(recipient_id):
    friends = userController.get_user_friends(auth.logged_in_user["user_id"])
    return recipient_id in friends


def is_recipient_message_in_inbox(recipient_id):
    for message in auth.logged_in_user['messages']:
        if message['sender_id'] == recipient_id:
            return True
    return False


def is_sender_premium_user():
    return auth.logged_in_user['premium']


def sending_self_message(recipient_id):
    return recipient_id == auth.logged_in_user["user_id"]


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def get_screen_options():
    screen_options = ["Display Messages",
                      "Open a Message", "Send Message", "Delete Message", "Show Friends"]
    if auth.logged_in_user['premium']:
        screen_options.append('Show All Users')
    return screen_options
