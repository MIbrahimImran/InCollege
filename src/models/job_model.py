class Job:

    def __init__(self, job_id="", user="", title="", description="", employer="", location="", salary="", start_date="", end_date=""):
        self.job_id = job_id
        self.user = user
        self.title = title
        self.description = description
        self.employer = employer
        self.location = location
        self.salary = salary
        self.start_date = start_date
        self.end_date = end_date
        self.applications = []
