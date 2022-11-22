import json


def get_mock_user_data():
    return {
        "users": [{
            "last_login": "2022-11-07 15:36:18.575888",
            "messages": [],
            "user_id": "1",
            "username": "naruto",
            "password": "Password1@",
            "profile": {
                "title": "Mr.",
                "first_name": "Naruto",
                "last_name": "Uzumaki",
                "university": "USF",
                "major": "CSE",
                "about": "I am a ninja",
                "education": [],
                "experience": []
            },
            "active_profile": False,
            "settings": {
                "sms_notifications": True,
                "email_notifications": True,
                "ad_notifications": True,
                "language": "English"
            },
            "jobPosts": [],
            "appliedJobs": [],
            "savedJobs": [],
            "friends": [],
            "friend_requests": [],
            "notifications": []
        },
        {
            "last_login": "2022-11-07 15:36:18.575888x`",
            "messages": [],
            "user_id": "2",
            "username": "sasuke",
            "password": "Password1@",
            "profile": {
                "title": "Mr.",
                "first_name": "Sasuke",
                "last_name": "Uchiha",
                "university": "USF",
                "major": "CSE",
                "about": "I am a ninja",
                "education": [],
                "experience": []
            },
            "active_profile": False,
            "settings": {
                "sms_notifications": True,
                "email_notifications": True,
                "ad_notifications": True,
                "language": "English"
            },
            "jobPosts": [],
            "appliedJobs": [],
            "savedJobs": [],
            "friends": [],
            "friend_requests": [],
            "notifications": []
        }]
    }


def get_mock_unique_id_data():
    return {"unique_id": 3}


def update_user_credentials_object():
    database_file = open('databases/user_credentials.json', 'w')
    json.dump(get_mock_user_data(), database_file, indent=2)


def update_unique_id_object():
    database_file = open('databases/unique_id.json', 'w')
    json.dump(get_mock_unique_id_data(), database_file, indent=2)


update_user_credentials_object()
update_unique_id_object()
