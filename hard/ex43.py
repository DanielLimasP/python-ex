# Python the hard way: excercise 43
import hashlib
from getpass import getpass


class Game_Engine:
    def __init__(self, scenario):
        self.scenario = scenario

    def play(self):
        self.scenario.start()

    def stop(self):
        exit(1)


class Hacker_Scenario:

    users = {}

    def __init__(self, user):
        self.user = user

    def welcome_scene(self):
        welcome_loop = True
        print("""
        --------------------------------------------------------------------------------------------------
        |                                                                                                |
        |       Welcome. Login to start hCKng, or signup to CTos to kickstart your hacking career.       |
        |                                                                                                |
        --------------------------------------------------------------------------------------------------       
                \n""")
        while welcome_loop:
            print("What do you want to do?")
            print("-login")
            print("-signup \n")
            action_login = input("> ")
            if action_login == "login":
                welcome_loop = self.login_scene()
            elif action_login == "signup":
                welcome_loop = self.signup_scene()
            else:
                print("\n")
        return "console"

    def login_scene(self):
        print("Please enter your credentials... \n")
        user = input("user> ")
        password = getpass("password> ")
        md5_encoded_password = hashlib.md5(password.encode())
        encoded = md5_encoded_password.hexdigest()
        if encoded == self.users[user]:
            print("login succesful \n")
            return False
        else:
            print("failed login \n")
            return True

    def signup_scene(self):
        print("Sign up")
        user = input("username > ")
        password = getpass("password > ")
        md5_encoded_password = hashlib.md5(password.encode())
        encoded = md5_encoded_password.hexdigest()
        self.users[user] = encoded
        print("Succesful signup! \n")
        print(self.users)
        print("\n")
        return "Good!"

    def start(self):
        self.welcome_scene()


if __name__ == "__main__":
    s = Hacker_Scenario("User")
    e = Game_Engine(s)
    e.play()
