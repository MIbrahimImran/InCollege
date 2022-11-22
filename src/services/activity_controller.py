import json
from datetime import datetime
import src.constants.activities as activitiesConstants
import src.shared.object_to_dict_converter as objectToDictConverter


def get_database_object():
    database_file = open('databases/activity_log.json')
    file_data = database_file.read()
    return json.loads(file_data)


def update_activity_log(activity):
    database = get_database_object()
    activity_dict = objectToDictConverter.job_to_dict(activity)
    activities = database['activities']
    for activity in activities:
        if activity['user_id'] == activity_dict['user_id'] and activity['type'] == activity_dict['type']:
            activity['time_stamp'] = activity_dict['time_stamp']
            update_database_object(database)
            return
    activities.append(activity_dict)
    update_database_object(database)


def is_last_job_application_over_week(user_id):
    current_date = datetime.now()
    database = get_database_object()
    activities = database['activities']
    for activity in activities:
        if activity['user_id'] == user_id and activity['type'] == activitiesConstants.JOB_APPLICATION:
            activity_date = datetime.strptime(
                activity['time_stamp'], '%Y-%m-%d %H:%M:%S.%f')
            if (current_date - activity_date).days < 7:
                return False
    return True


def update_database_object(updated_database):
    database_file = open('databases/activity_log.json', 'w')
    json.dump(updated_database, database_file, indent=2)
