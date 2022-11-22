from unittest import mock

#import src.screens.logged_in.inbox_screen as inboxScreen
import src.models.message_model as messageModel
import src.models.profile_model as profileModel
import src.models.user_model as userModel
import src.services.user_controller as userController
import src.shared.password_validator as passwordValidator
import src.routing.routes as routes
import src.authentication.auth as auth
import src.screens.signup_screen as signupScreen
import src.constants.mock_user_credentials_db as mockUserDatabase
import src.shared.notification_handler as notifHandler


# TEST FUNCTION
def test_user_premium_signup(monkeypatch):
  inputs = iter(['username', 'password', 'first', 'last', 'uni', 'major'])
  monkeypatch.setattr('builtins.input', lambda val: next(inputs))
  user = routes.signupScreen.get_user_signup_data(True)
  assert user.premium == True


# TEST FUNCTION
def test_user_standard_signup(monkeypatch):
  inputs = iter(['username', 'password', 'first', 'last', 'uni', 'major'])
  monkeypatch.setattr('builtins.input', lambda val: next(inputs))
  user = routes.signupScreen.get_user_signup_data(False)
  assert user.premium == False

# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
def test_send_message(get_database_object):
  userController.send_message('1', 'hiiiiii')
  assert mockUserDatabase.user1['messages'] == ['hiiiiii']


def test_is_sender_premium_user():
  routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user1
  premium_boolean = routes.inboxScreen.is_sender_premium_user()
  assert premium_boolean == True


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'get_user_by_id',
                   return_value=mockUserDatabase.user1)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_notify_user_new_message(get_database_object, get_user_by_id,
                                 update_database_object):
  
  mockUserDatabase.user2['notifications'] = []
  
  message = messageModel.Message('21', 'hiiii', '1', '2', False)

  userController.send_message_notification('2', message.__dict__)
  
  assert mockUserDatabase.user2['notifications'] == [
    {
      "screenName": "Home Screen", 
      "message": "You have a new message from naruto." 
    }
  ]


# TEST FUNCTION
def test_is_recipient_message_in_inbox():
  routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user2
  sender_id = "1"
  assert routes.inboxScreen.is_recipient_message_in_inbox(sender_id) == True

# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
@mock.patch.object(userController,
                   'update_database_object',
                   return_value="Success")
def test_delete_received_message_option(get_database_object,
                                        update_database_object):
  userController.delete_message('2', '38')

  assert ['"message_id": "38"'] not in mockUserDatabase.user2['messages']


# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
def test_is_recipient_a_friend(get_database_object):
  routes.inboxScreen.auth.logged_in_user = mockUserDatabase.user2
  user_id = "3"
  assert routes.inboxScreen.is_recipient_a_friend(user_id) == True


# TEST FUNCTION
def test_send_message_to_nonfriend(capsys):
  notifHandler.display_notification(
    "I'm sorry, you are not friends with that person!")
  stdout, stderr = capsys.readouterr()
  assert "I'm sorry, you are not friends with that person!" in stdout

# TEST FUNCTION
@mock.patch.object(userController,
                   'get_database_object',
                   return_value=mockUserDatabase.db)
def test_get_all_users(get_database_object):
  assert userController.get_all_users() == mockUserDatabase.db['users']