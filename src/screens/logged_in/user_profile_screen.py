import src.shared.format_input_first_upper as formatToFirstUpper
import src.services.user_controller as userController
import src.models.education_model as educationModel
import src.models.job_model as jobModel

import src.shared.notification_handler as notificationHandler
import src.constants.error_messages as errorMessages
import src.shared.screen_display_handler as displayHandler
import src.constants.screen_names as screenNames
import src.routing.router as router
import src.authentication.auth as auth
import src.services.id_controller as idController
import src.shared.profile_display as profileDisplay
import src.api.student_account_api as studentAccountAPI


def screen():
    screen_options = []

    screen_display = "Create/View Your Profile"
    user = auth.logged_in_user

    if "Create Profile" not in screen_options:
        if user['active_profile'] == False:
            screen_options.append("Create User Profile")
        else:
            screen_display = profileDisplay.get_profile_display(user)
            for option in get_edit_profile_options():
                screen_options.append(option)

    user_selection = displayHandler.display_controller(screen_options,
                                                       screen_display)
    handle_user_selection(user_selection)


def handle_user_selection(user_selection):
    username = auth.logged_in_user['username']
    user_id = auth.logged_in_user['user_id']

    if (screen_exists(user_selection)):
        navigate_user(user_selection)

    elif user_selection == "Create User Profile":
        title, about, experience, education = get_user_profile_data()
        set_user_profile_data(username, title, about,
                              experience, education, True)

    elif user_selection == "Edit Title":
        title = input("\nEnter title: ")
        userController.set_user_title(username, title)

    elif user_selection == "Edit Major":
        major = input("\nEdit Major: ")
        major = formatToFirstUpper.format_input_first_upper(major)
        userController.set_user_major(username, major)

    elif user_selection == "Edit About":
        about = input("\nEdit About: ")
        userController.set_user_about(username, about)

    elif user_selection == "Edit Experience":
        if len(auth.logged_in_user['profile']['experience']) == 0:
            print("\n\033[92m" + "You have no experience to edit!" +
                  "\033[0m")
            experience = handle_get_experience()
            userController.set_user_experience(username, experience)
        else:
            print("\n\033[92m" + "Edit Your Experience!" + "\033[0m")
            job_id = input("Enter Job ID: ")
            if userController.is_valid_job_id(user_id, job_id) == False:
                notificationHandler.display_notification("Invalid Job ID!")
            else:
                experience = get_experience_data(generate_id=False)
                userController.update_user_experience(
                    username, job_id, experience)

    elif user_selection == "Edit Education":
        if len(auth.logged_in_user['profile']['education']) == 0:
            print("\n\033[92m" + "You have no education to edit!" +
                  "\033[0m")
            education = handle_get_education()
            userController.set_user_education(username, education)
        else:
            print("\n\033[92m" + "Edit Your Education!" + "\033[0m")
            edu_id = input("Enter Education ID: ")
            if userController.is_valid_edu_id(user_id, edu_id) == False:
                notificationHandler.display_notification(
                    "Invalid Education ID!")
            else:
                education = get_education_data(generate_id=False)
                userController.update_user_education(
                    username, edu_id, education)

    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)

    auth.update_logged_in_user()
    screen()


def navigate_user(screen):
    router.navigate_user(screen)


def screen_exists(user_selection):
    return user_selection in screenNames.screens


def get_user_profile_data():
    title, about = get_personal_data()
    if continue_editing() == False:
        return title, about, None, None

    education = handle_get_education()
    if continue_editing() == False:
        return title, about, None, education

    experience = handle_get_experience()
    return title, about, experience, education


def get_personal_data():
    print("\n\033[92m" + "Enter Details About You!" + "\033[0m")
    title = input("Enter title: ")
    about = input("Enter About: ")
    return title, about


def handle_get_education():
    print("\n\033[92m" + "Enter Details About Your Education! " + "\033[0m")
    education = []
    education.append(get_education_data())
    return education


def get_education_data(generate_id=True):
    edu_id = idController.generate_education_id()
    school = input("Enter School: ")
    degree = input("Enter Degree: ")
    years = input("Enter Years: ")

    if generate_id:
        return educationModel.Education(
            edu_id=edu_id, school=school, degree=degree, years=years)
    else:
        return educationModel.Education(
            school=school, degree=degree, years=years)


def handle_get_experience():
    print("\n\033[92m" + "Enter Details About Your Experience! " + "\033[0m")
    while (True):
        jobs_num = input("How many jobs do you want to list? (Maximum of 3): ")
        if jobs_num.isnumeric() == False:
            notificationHandler.display_notification(
                errorMessages.INVALID_SELECTION_MESSAGE)
        elif int(jobs_num) > 3 or int(jobs_num) < 1:
            notificationHandler.display_notification(
                errorMessages.INVALID_SELECTION_MESSAGE)
        else:
            break

    jobs = []
    while (int(jobs_num)):
        print("\n\033[92m" + "Enter Details About Job " +
              str(len(jobs) + 1) + "!" + "\033[0m")
        experience = get_experience_data()
        jobs.append(experience)
        jobs_num = int(jobs_num) - 1
        print('\n')

    return jobs


def get_experience_data(generate_id=True):
    job_id = idController.generate_job_id()
    title = input("Enter title: ")
    employer = input("Enter Employer: ")
    start_date = input("Enter Date Started: ")
    end_date = input("Enter Date Ended: ")
    location = input("Enter Location: ")
    description = input("Enter Description: ")

    if generate_id:
        return jobModel.Job(job_id=job_id, title=title, employer=employer,
                            start_date=start_date, end_date=end_date,
                            location=location, description=description)
    else:
        return jobModel.Job(title=title, employer=employer,
                            start_date=start_date, end_date=end_date,
                            location=location, description=description)


def set_user_profile_data(username, title, about, experience, education,
                          active_profile):
    userController.set_user_title(username, title)
    userController.set_user_about(username, about)
    if (education != None):
        userController.set_user_education(username, education)
    if (experience != None):
        userController.set_user_experience(username, experience)
    userController.set_active_profile(username, active_profile)
    studentAccountAPI.write_profiles()

def get_edit_profile_options():
    return [
        "Edit Title", "Edit Major", "Edit About", "Edit Experience",
        "Edit Education"
    ]


def continue_editing():
    user_input = input(
        "\n\033[93m" + "Enter s to save and c to continue!" + "\033[0m: ")
    if user_input == "s":
        return False
    elif user_input == "c":
        return True
    else:
        notificationHandler.display_notification(
            errorMessages.INVALID_SELECTION_MESSAGE)
        return continue_editing()
