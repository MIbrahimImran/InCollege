import src.api.student_account_api as studentAccountsAPI
import src.api.jobs_api as jobAPI

def api():
    studentAccountsAPI.get_accounts()
    jobAPI.get_jobs()

    studentAccountsAPI.write_accounts()
    studentAccountsAPI.write_profiles()
    jobAPI.write_jobs()
    jobAPI.applied_jobs()
    jobAPI.saved_jobs()
