import src.services.job_controller as jobController
import src.services.id_controller as idController
import src.models.job_model as jobModel
import src.services.user_controller as userController


def get_jobs():
    # jobController.clear_jobs_list()

    job_list = jobController.get_all_jobs()
    job_titles = [job['title'] for job in job_list]

    numJobs = len(job_list)
    try:
        with open("src/api/input/newJobs.txt", 'r') as file:
            title = ''
            description = ''
            poster = ''
            employer = ''
            location = ''
            salary = ''

            jobs = file.readlines()

            while len(jobs) > 0 and numJobs < 10:
                job_info = jobs[0:jobs.index('=====\n')]

                title = job_info[0].strip()
                # check to see if job title exists (If the job title in the file exists in the database)
                if title in job_titles:
                    # goes to next iteration (Removes all file data associated with that job title)
                    for i in range(len(job_info) + 1):
                        jobs.pop(0)
                    continue

                # handles multi-line descriptions
                if '&&&\n' in job_info:
                    idx = job_info.index('&&&\n')
                    description = "".join(
                        job_info[1:idx]).replace('\n', ' ').strip()
                    poster = job_info[idx + 1].strip()
                    employer = job_info[idx + 2].strip()
                    location = job_info[idx + 3].strip()
                    salary = job_info[idx + 4].strip()
                else:
                    description = job_info[1].strip()
                    poster = job_info[2].strip()
                    employer = job_info[3].strip()
                    location = job_info[4].strip()
                    salary = job_info[5].strip()

                newJob = jobModel.Job(job_id=idController.generate_job_id(
                ), user=poster, title=title, description=description, employer=employer, location=location, salary=salary)
                jobController.post_job(newJob)
                numJobs += 1

                for i in range(len(job_info) + 1):
                    jobs.pop(0)
            file.close()
    except (FileNotFoundError):
        print("File newJobs.txt does not exist")


def write_jobs():
    jobs = jobController.get_database_object()['jobs']
    with open("src/api/output/MyCollege_jobs.txt", 'w') as file:
        for job in jobs:
           # append job variable to InCollege_jobs.txt
            file.write(
                f"{job['title']}\n{job['description']}\n{job['employer']}\n{job['location']}\n{job['salary']}\n=====\n")
        file.close()

# update jobs text file by adding or removing a job


def update_jobs(job):
    with open("src/api/output/MyCollege_jobs.txt", 'a') as file:
        file.write(
            f"{job.title}\n{job.description}\n{job.employer}\n{job.location}\n{job.salary}\n=====\n")


def applied_jobs():
    # open jobs database
    jobs = jobController.get_database_object()['jobs']

    # open InCollege_jobs.txt
    with open("src/api/output/MyCollege_appliedJobs.txt", 'w') as file:

        # save job into variables
        for job in jobs:
            # read job posts and append job variable to InCollege_appliedJobs.txt
            file.write(job['title'])
            for application in job['applications']:

                userid = application['user_id']
                description = application['cover_letter']
                user = userController.get_user_by_id(userid)
                file.write(f"\n{user['username']}\n{description}")

            file.write("\n=====\n")

        file.close()


def saved_jobs():
    users = userController.get_database_object()['users']

    # open InCollege_jobs.txt
    with open("src/api/output/MyCollege_savedJobs.txt", 'w') as file:
        for user in users:
            file.write(f"{user['username']}\n")
            for savedJob_id in user['savedJobs']:
                job = jobController.get_job_by_id(savedJob_id)
                file.write(f"{job['title']}\n")

            file.write("\n=====\n")
        file.close()
