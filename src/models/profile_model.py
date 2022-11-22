import src.models.job_model as jobModel
import src.models.education_model as educationModel


class Profile:
    def __init__(self, title="", first_name="", last_name="", university="", major="", about="", education=[], experience=[]):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.university = university
        self.major = major
        self.about = about
        self.education = education
        self.experience = experience
