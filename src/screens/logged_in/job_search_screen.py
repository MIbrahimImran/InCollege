import src.routing.router as router
import src.authentication.auth as auth
import src.constants.screen_names as screenNames
import src.shared.screen_display_handler as displayHandler
import src.constants.error_messages as errorMessages
import src.constants.success_messages as successMessage
import src.shared.notification_handler as notificationHandler
import src.services.id_controller as idController
import src.models.job_model as jobModel
import src.services.user_controller as userController
import src.services.job_controller as jobController
import src.models.job_application_model as jobApplicationModel
import src.services.activity_controller as activityController
import src.models.activity_model as activityModel
import src.constants.activities as activities
screen_options = ["Display Job Posting",
                  "Display Applied Jobs", "Display Saved Jobs", "Display Unapplied Jobs", "Save a Job", "Post a Job", "Apply for a Job", "Delete a Job"]


def screen():
    screen_display = "Job Search & Internship"

    send_number_of_applied_jobs_notification()
    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    if (screen_exists(user_selection)):
        navigate_user(user_selection)
    elif user_selection in screen_options:
        if user_selection == "Post a Job":
            user_id = auth.logged_in_user['user_id']
            job = get_user_job_data()
            jobController.post_job(job)
            userController.add_job_to_user(user_id, job.job_id)
            userController.send_new_job_notification()
        elif user_selection == "Display Job Posting":
            display_all_jobs()
        elif user_selection == "Apply for a Job":
            job_id = input("Enter job id: ")
            if jobController.job_exists(job_id):
                if userController.has_applied_for_job(auth.logged_in_user['user_id'], job_id):
                    notificationHandler.display_notification(
                        errorMessages.JOB_ALREADY_APPLIED_MESSAGE)
                elif userController.is_self_posted_job(auth.logged_in_user['user_id'], job_id):
                    notificationHandler.display_notification(
                        errorMessages.SELF_POSTED_JOB_MESSAGE)
                else:
                    application = get_application_data()
                    userController.apply_for_job(
                        auth.logged_in_user['user_id'], job_id, application)

                    activityController.update_activity_log(activityModel.Activity(
                        type=activities.JOB_APPLICATION, user_id=auth.logged_in_user['user_id']))

                    notificationHandler.display_notification(
                        successMessage.SUCCESSFUL_JOB_APPLICATION)
            else:
                notificationHandler.display_notification(
                    errorMessages.INVALID_JOB_ID_MESSAGE)
        elif user_selection == "Display Applied Jobs":
            display_applied_jobs()
        elif user_selection == "Display Saved Jobs":
            display_saved_jobs()
        elif user_selection == "Display Unapplied Jobs":
            display_unapplied_jobs()
        elif user_selection == "Save a Job":
            handle_job_save()
        elif user_selection == "Delete a Job":
            handle_job_delete()
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
    screen()


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def get_user_job_data():
    user = auth.logged_in_user['username']
    title = input("Enter job title: ")
    description = input("Enter job description: ")
    employer = input("Enter employer: ")
    location = input("Enter location: ")
    salary = input("Enter salary: ")
    job_id = idController.generate_job_id()
    return jobModel.Job(job_id=job_id, user=user, title=title, description=description, employer=employer, location=location, salary=salary)


def get_application_data():
    user_id = auth.logged_in_user['user_id']
    graduation_date = input("Graduation Date (MM/DD/YYYY): ")
    start_date = input("Starting Date (mm/dd/yyyy): ")
    cover_letter = input(
        "Why do you think you are a good fit for this job? : ")
    return jobApplicationModel.JobApplication(user_id=user_id, graduation_date=graduation_date, start_date=start_date, cover_letter=cover_letter)


def display_all_jobs():
    jobs = jobController.get_all_jobs()
    if len(jobs) == 0:
        notificationHandler.display_notification(
            errorMessages.NO_JOBS_MESSAGE)
    else:
        for job in jobs:
            print("\n\033[92m" + "JobId: " + "\033[0m", job["job_id"])
            print("\033[94m" + "Title: " + "\033[0m", job["title"])
            print("\033[94m" + "Description: " + "\033[0m", job["description"])
            print("\033[94m" + "Employer: " + "\033[0m", job["employer"])
            print("\033[94m" + "Location: " + "\033[0m", job["location"])
            print("\033[94m" + "Salary: " + "\033[0m", job["salary"])
            print("\033[94m" + "Posted By: " + "\033[0m", job["user"])
            if userController.has_applied_for_job(auth.logged_in_user['user_id'], job["job_id"]):
                print(
                    "\033[91m" + "You have already applied for this job!" + "\033[0m")
            else:
                print(
                    "\033[92m" + "Open for Applications! " + "\033[0m")


def display_applied_jobs():
    jobs_ids = userController.get_applied_jobs(auth.logged_in_user['user_id'])
    if len(jobs_ids) == 0:
        notificationHandler.display_notification(
            errorMessages.NO_JOBS_MESSAGE)
    else:
        print("\033[92m" + "Applied Jobs: " + "\033[0m")
        for job_id in jobs_ids:
            job = jobController.get_job_by_id(job_id)
            print("\n\033[92m" + "JobId: " + "\033[0m", job["job_id"])
            print("\033[94m" + "Title: " + "\033[0m", job["title"])
            print("\033[94m" + "Description: " + "\033[0m", job["description"])
            print("\033[94m" + "Employer: " + "\033[0m", job["employer"])
            print("\033[94m" + "Location: " + "\033[0m", job["location"])
            print("\033[94m" + "Salary: " + "\033[0m", job["salary"])
            print("\033[94m" + "Posted By: " + "\033[0m", job["user"])


def display_saved_jobs():
    jobs_ids = userController.get_saved_jobs(auth.logged_in_user['user_id'])
    if len(jobs_ids) == 0:
        notificationHandler.display_notification(
            errorMessages.NO_JOBS_MESSAGE)
    else:
        print("\033[92m" + "Saved Jobs: " + "\033[0m")
        for job_id in jobs_ids:
            job = jobController.get_job_by_id(job_id)
            print("\n\033[92m" + "JobId: " + "\033[0m", job["job_id"])
            print("\033[94m" + "Title: " + "\033[0m", job["title"])
            print("\033[94m" + "Description: " + "\033[0m", job["description"])
            print("\033[94m" + "Employer: " + "\033[0m", job["employer"])
            print("\033[94m" + "Location: " + "\033[0m", job["location"])
            print("\033[94m" + "Salary: " + "\033[0m", job["salary"])
            print("\033[94m" + "Posted By: " + "\033[0m", job["user"])


def display_unapplied_jobs():
    jobs_ids = userController.get_unapplied_jobs(
        auth.logged_in_user['user_id'])
    if len(jobs_ids) == 0:
        notificationHandler.display_notification(
            errorMessages.NO_JOBS_MESSAGE)
    else:
        print("\033[92m" + "Unapplied Jobs: " + "\033[0m")
        for job_id in jobs_ids:
            job = jobController.get_job_by_id(job_id)
            print("\n\033[92m" + "JobId: " + "\033[0m", job["job_id"])
            print("\033[94m" + "Title: " + "\033[0m", job["title"])
            print("\033[94m" + "Description: " + "\033[0m", job["description"])
            print("\033[94m" + "Employer: " + "\033[0m", job["employer"])
            print("\033[94m" + "Location: " + "\033[0m", job["location"])
            print("\033[94m" + "Salary: " + "\033[0m", job["salary"])
            print("\033[94m" + "Posted By: " + "\033[0m", job["user"])


def handle_job_save():
    job_id = input("Enter Job Id: ")
    if jobController.job_exists(job_id):

        if userController.has_saved_job(auth.logged_in_user['user_id'], job_id):
            notificationHandler.display_notification(
                errorMessages.JOB_ALREADY_SAVED)
        else:
            userController.save_job(auth.logged_in_user['user_id'], job_id)
            notificationHandler.display_notification(
                successMessage.JOB_SAVED_MESSAGE)
    else:
        notificationHandler.display_notification(
            errorMessages.JOB_DOES_NOT_EXIST_MESSAGE)


def handle_job_delete():
    job_id = input("Enter Job Id: ")
    if jobController.job_exists(job_id):

        if userController.is_self_posted_job(auth.logged_in_user['user_id'], job_id):
            notify_users_of_job_deletion(job_id)

            if userController.has_saved_job(auth.logged_in_user['user_id'], job_id):
                userController.unsave_job(
                    auth.logged_in_user['user_id'], job_id)

            if userController.has_applied_for_job(auth.logged_in_user['user_id'], job_id):
                userController.unapply_for_job(
                    auth.logged_in_user['user_id'], job_id)

            if userController.is_self_posted_job(auth.logged_in_user['user_id'], job_id):
                userController.delete_job_post(
                    auth.logged_in_user['user_id'], job_id)

            jobController.delete_job(job_id)

            notificationHandler.display_notification(
                successMessage.JOB_DELETED_SUCCESSFULLY)
        else:
            notificationHandler.display_notification(
                errorMessages.JOB_NOT_SELF_POSTED)
    else:
        notificationHandler.display_notification(
            errorMessages.JOB_DOES_NOT_EXIST_MESSAGE)


def notify_users_of_job_deletion(job_id):
    applications = jobController.get_job_applications(job_id)
    for application in applications:
        userController.send_job_delete_notification(
            application['user_id'], job_id)


def send_number_of_applied_jobs_notification():
    number_of_applied_jobs = userController.get_number_of_applied_jobs(
        auth.logged_in_user['user_id'])
    userController.send_notification(
        auth.logged_in_user['user_id'], "You have applied for " + str(number_of_applied_jobs) + " job(s)", screenName=screenNames.JOB_SEARCH_SCREEN)
