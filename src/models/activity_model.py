import datetime


class Activity:
    def __init__(self, type, user_id, time_stamp=datetime.datetime.now(),):
        self.type = type
        self.user_id = user_id
        self.time_stamp = time_stamp
