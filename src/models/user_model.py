import datetime
import src.models.user_settings_model as userSettingsModel
import src.models.profile_model as profileModel


class User:

    def __init__(self,
                 last_login=datetime.datetime.now(),
                 user_id="",
                 username="",
                 password="",
                 active_profile=False,
                 profile=profileModel.Profile(),
                 settings=userSettingsModel.Settings(),
                 premium=False):
        self.last_login = last_login
        self.user_id = user_id
        self.username = username
        self.password = password
        self.profile = profile
        self.active_profile = active_profile
        self.settings = settings
        self.premium = premium
        self.jobPosts = []
        self.appliedJobs = []
        self.savedJobs = []
        self.friends = []
        self.friend_requests = []
        self.notifications = []
        self.messages = []
        self.activities = []
