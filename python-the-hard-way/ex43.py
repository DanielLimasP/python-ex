# Python the hard way: excercise 43
# This is pretty much a console sim, with ls, cd and pwd commands.
import hashlib
from getpass import getpass
import random as rand
import datetime


class GameEngine:
    def __init__(self, scenario):
        self.scenario = scenario

    def play(self):
        self.scenario.start()

    def stop(self):
        exit(1)


class HackerScenario:

    user = ""
    passwords = {}

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

        user_file_directory = FileDirectory(self.user)
        while True:
            user_file_directory.render_Terminal()

        return "console"

    def login_scene(self):
        print("Please enter your credentials... \n")
        user_login = input("user: ")
        password = getpass("password: ")
        md5_encoded_password = hashlib.md5(password.encode())
        encoded = md5_encoded_password.hexdigest()
        if user_login in self.passwords:
            if encoded == self.passwords[user_login]:
                print("login succesful \n")
                return False
            else:
                print("failed login \n")
                return True
        else:
            print("The user doesn't exist")
            return True

    def signup_scene(self):
        print("Sign up")
        self.user = input("username: ")
        password = getpass("password: ")
        md5_encoded_password = hashlib.md5(password.encode())
        encoded = md5_encoded_password.hexdigest()
        self.passwords[self.user] = encoded
        print("Succesful signup! \n")
        print(self.passwords)
        print("\n")
        return "Good!"

    def start(self):
        self.welcome_scene()


class FileDirectory:
    rand.seed(10)

    def __init__(self, user):
        self.root_name = 'CNT D:/' + user
        self.current_dir = "CNT D:/" + user + "> "
        self.last_dir = ''
        self.user = user

        self.fd = {
            "CNT D:/" + user + "> ": {"Downloads", "Documents", "catpics", "Master_Hacker_Things"},
            "CNT D:/" + user + "/Downloads> ": {"Cat1.png", "Netbong.exe", "Win10-iso-by-progarms-gratis.ocm", "top_secret"},
            "CNT D:/" + user + "/Documents> ": {"Notes", "Projects", "Images", "Videos"},
            "CNT D:/" + user + "/catpics> ": {"cat.png", "cot.png", "cut cat.jpg", "beautiful cat.png", "nyan.png", "Reddit cat OWO.png"},
            "CNT D:/" + user + "/Master_Hacker_Things> ": {"Ghislaine Maxwell is a giant Lizard.jpg", "proof.avi", "Video of Bill Clinton being weird.avi", "destroy_fbi_choppers.exe", "hack_nasa.exe"}
        }

    def render_Terminal(self):
        next_command = input(self.current_dir)
        self.command_Interpreter(next_command)

    # Command Section and fun
    def list_Directory(self):
        # Gotta parse the current directory
        if self.current_dir in self.fd:
            print("""
                        |Name                                                                     |Length                   
                    ------------------------------------------------------------------------------------------
                    """)
            for f in self.fd[self.current_dir]:
                print("""
                    {}                                              {} kb
                    """.format(f.ljust(32), str(rand.randint(100, 1000000))).ljust(10))
        else:
            print("Error of some sort. I doubt that there will ever be an error.")

    def command_Interpreter(self, command):

        splitted_comm = command.split(' ')[0]
        new_dir = self.root_name

        if splitted_comm == 'pwd':
            print(self.current_dir)

        if len(command.split(' ')) > 1:
            aux = command.split(' ')[1]

        if splitted_comm == 'ls':
            self.list_Directory()

        if splitted_comm == 'cd':
            print(splitted_comm, aux)
            if aux != None and aux in self.fd[self.current_dir]:
                self.last_dir = self.current_dir
                self.current_dir = new_dir + "/" + aux + "> "

            if aux == '../' or aux == '..':
                self.current_dir = self.last_dir

        if splitted_comm == 'exit()':
            exit(1)


if __name__ == "__main__":
    s = HackerScenario("User")
    e = GameEngine(s)
    e.play()
