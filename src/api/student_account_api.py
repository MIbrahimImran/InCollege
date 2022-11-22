import src.services.user_controller as userController
import src.services.id_controller as idController
import src.models.user_model as userModel
import src.models.profile_model as profileModel


def get_accounts():
    # userController.clear_users_list()
    numAccounts = len(userController.get_all_users())
    try:
        with open("src/api/input/studentAccounts.txt", 'r') as file:
            studentAccounts = file.readlines()

            username = ''
            first_name = ''
            last_name = ''
            password = ''

            for i in range(len(studentAccounts)):
                if numAccounts == 10:
                    break
                if i % 3 == 0:
                    user_info = studentAccounts[i].split()
                    username = user_info[0]
                    first_name = user_info[1]
                    last_name = user_info[2]
                elif i % 3 == 1:
                    password = studentAccounts[i].strip()
                elif i % 3 == 2:
                    profile = profileModel.Profile(first_name=first_name, last_name=last_name)
                    newUser = userModel.User(user_id=idController.generate_user_id(), username=username, password=password, profile=profile)
                    userController.add_user(newUser)
                    numAccounts += 1
        file.close()
                    
    except (FileNotFoundError):
        print("File studentAccounts.txt does not exist")

def write_accounts():
    users = userController.get_all_users()

    with open('src/api/output/MyCollege_users.txt', 'w') as file:
        for user in users:
            file.write(f"{user['username']}\t{'plus' if user['premium'] else 'standard'}\n")

def add_account_output(user):
    with open('src/api/output/MyCollege_users.txt', 'a') as file:
        file.write(f"{user['username']}\t{'plus' if user['premium'] else 'standard'}\n")


def write_profiles():
    user_list = userController.get_all_users()
    profiles = [user['profile'] for user in user_list]

    with open('src/api/output/MyCollege_profiles.txt', 'w') as file:
        for profile in profiles:
            file.write(f"{profile['title']}\n{profile['major']}\n{profile['university']}\n{profile['about']}\n")

            if (profile['education'] != []):
                education = profile['education'][0]
                file.write(f"{education['school']}\t{education['degree']}\t{education['years']}\n")
            else:
                file.write("None\n")

            if (profile['experience'] != []):
                for exp in profile['experience']:
                    file.write(f"{exp['title']}\t{exp['employer']}\t{exp['location']}\t{exp['start_date']}\t{exp['end_date']}\n")
            else:
                file.write("None\n")
            
            file.write("=====\n")
            # TODO: figure out education and experience, the current implementation does not work amazingly and leaves a mostly blank file since most of the profiles aren't filled out

def add_profile_output(profile):
    with open('src/api/output/MyCollege_profiles.txt', 'a') as file:
        file.write(f"{profile['title']}\n{profile['major']}\n{profile['university']}\n{profile['about']}\n")

        if (profile['education'] != []):
            education = profile['education'][0]
            file.write(f"{education['school']}\t{education['degree']}\t{education['years']}\n")
        else:
            file.write("None\n")

        if (profile['experience'] != []):
            for exp in profile['experience']:
                file.write(f"{exp['title']}\t{exp['employer']}\t{exp['location']}\t{exp['start_date']}\t{exp['end_date']}\n")
        else:
            file.write("None\n")
        
        file.write("=====\n")