def get_profile_display(user):
    first_name = user['profile']['first_name']
    last_name = user['profile']['last_name']
    title = user['profile']['title']
    about = user['profile']['about']
    major = user['profile']['major']
    university = user['profile']['university']
    experience = user['profile']['experience']
    education = user['profile']['education']

    display = ""

    display += "\n\033[92m" + "Profile: " + \
        "\033[0m" + first_name + " " + last_name

    display += "\n\033[94m" + "Title: " + "\033[0m" + title
    display += "\n\033[94m" + "About: " + "\033[0m" + about
    display += "\n\033[94m" + "Major: " + "\033[0m" + major
    display += "\n\033[94m" + "University: " + "\033[0m" + university + "\n"

    if len(education) > 0:
        display += "\n\033[92m" + "Education: " + "\033[0m"
        for edu in education:
            display += "\n\033[94m" + "Education ID: " + "\033[0m" + edu['edu_id'] + \
                "\n\033[94m" + "School: " + "\033[0m" + edu['school'] + \
                "\033[94m" + "\nDegree: " + "\033[0m" + edu['degree'] +  \
                "\033[94m" + "\nYears: " + "\033[0m" + edu['years'] + "\n"

    if len(experience) > 0:
        display += "\n\033[92m" + "Experience: " + "\033[0m"
        for job in experience:
            display += "\n\033[94m" + "Job ID: " + "\033[0m" + job['job_id'] + \
                "\n\033[94m" + "Employer: " + "\033[0m" + job['employer'] + \
                "\033[94m" + "\nTitle: " + "\033[0m" + job['title'] + \
                "\033[94m" + "\nDescription: " + \
                "\033[0m" + job['description'] + "\n"

    return display
