db = {
    "users": [{
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
            "education": [
                {
                    "edu_id": "10",
                    "school": "THE University of South Florida",
                    "degree": "Science of Computers",
                    "years": "2022-2022"
                }
            ],
            "experience": [
                {
                    "title": "Software developer VIII",
                    "employer": "Jane Street",
                    "location": "New York",
                    "start_date": "1 week ago",
                    "end_date": "1 day ago"
                }
            ]
        },
        "active_profile": False,
        "settings": {
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "language": "English"
        },
        "jobPosts": [],
        "appliedJobs": ["1"],
        "savedJobs": ["1"],
        "premium": True,
        "friends": [],
        "friend_requests": [],
        "notifications": [],
        "messages": []
    },
        {
        "user_id": "2",
        "username": "sasuke",
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
        "active_profile": True,
        "settings": {
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "language": "English"
        },
        "jobPosts": [],
        "appliedJobs": [
            "1"
        ],
        "savedJobs": ["25"],
        "premium": True,
        "friends": ['3'],
        "friend_requests": [],
        "notifications": [
            {
                "screenName": "Home Screen"
            }
        ],
        "messages": [{
            "message_id": "38",
            "message": "hiiiii",
            "sender_id": "1",
            "receiver_id": "2",
            "read": False
        }]
    },
        {
        "user_id": "3",
        "username": "badukee",
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
        "active_profile": True,
        "settings": {
            "sms_notifications": True,
            "email_notifications": True,
            "ad_notifications": True,
            "language": "English"
        },
        "jobPosts": [],
        "appliedJobs": [
            "1"
        ],
        "savedJobs": [],
        "premium": True,
        "friends": ['2'],
        "friend_requests": [],
        "notifications": [
            {
                "screenName": "Home Screen"
            }
        ],
        "messages": [{
            "message_id": "38",
            "message": "hiiiii",
            "sender_id": "1",
            "receiver_id": "2",
            "read": False
        }]
    }
    ]
}

user1 = db['users'][0]
user2 = db['users'][1]
