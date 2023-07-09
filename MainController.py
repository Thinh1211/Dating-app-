from GUI import *
from database_controller import delete_invalid_id

def main():
    status = "none"
    while status != "login success" and status != "exit":
        delete_invalid_id() #if user do not finish their sign up, that account will be delete
        start = login.Login()
        start.login_screen()
        user_id = start.get_user_id()
        status = start.get_status()
    if status == "login success":
        user = App_UI.User(user_id, "profile") #set the default page to user profile
        user.Profile_screen()

if __name__ == "__main__":
    main()