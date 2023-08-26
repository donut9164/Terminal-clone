import sys
import threading
import subprocess
import socket

import time
import string
import random

# ppm python

# welcome
print("Welcome to terminal clone v2.14")
print("type '.help' for more information!")


def main():
    # login
    global username
    global password
    global logged_in
    logged_in = False

    global internet_state
    internet_state = False

    while True:
        # login system
        def register_user(username, password):
            with open('source/users.txt', 'a') as file:
                file.write(f"{username}:{password}\n")

        def check_credentials(username, password):
            with open('source/users.txt', 'r') as file:
                for line in file:
                    stored_username, stored_password = line.strip().split(':')
                    if stored_username == username and stored_password == password:
                        return True
            return False

        # text color
        class Colors:
            RESET = "\033[0m"
            BLACK = "\033[30m"
            RED = "\033[31m"
            GREEN = "\033[32m"
            YELLOW = "\033[33m"
            BLUE = "\033[34m"
            MAGENTA = "\033[35m"
            CYAN = "\033[36m"
            WHITE = "\033[37m"
            BOLD = "\033[1m"
            UNDERLINE = "\033[4m"

        def color_text(text, color_code):
            return f"{color_code}{text}{Colors.RESET}"

        # Loading & Animation
        def spinning_text(text):
            spinner = ['|', '/', '-', '\\']
            spin_round = random.randint(10, 40)
            for i in range(spin_round):
                for char in spinner:
                    print(f"\r{char} {text}", end="")
                    time.sleep(0.1)

        def loading_bar(iterations, bar_length=50, text="Loading"):
            for i in range(iterations + 1):
                delay = random.randint(1, 6)
                percent = i / iterations
                hashes = '#' * int(round(percent * bar_length))
                spaces = '-' * (bar_length - len(hashes))
                percent_str = f"{int(percent * 100)}%"
                custom_text = f"{text} [{hashes}{spaces}] {percent_str}"
                print(f"\r{custom_text}", end='', flush=True)
                time.sleep(delay / 10)

        def countdown_timer(seconds, custom_text):
            for remaining in range(seconds, -1, -1):
                print(f"{custom_text} {remaining} seconds", end='\r')
                time.sleep(1)

        # Command process

        # system test
        process_name = ["System", "dwm.exe", "smss.exe", "csrss.exe", "lsass.exe", "svchost.exe", "conhost.exe",
                        "spoolsv.exe", "wininit.exe", "taskhost.exe", "explorer.exe", "services.exe", "winlogon.exe", "System Idle Process"]

        def process_list(text, process_name):
            for text_list in process_name:
                print(f"\r{text} {text_list}", end="")
                delay = random.randint(1, 10)
                time.sleep(delay/10)

        def encryption(length):
            characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
            random_characters = ''.join(random.choice(
                characters) for _ in range(length))
            return random_characters

        # all process display
        def system_test():
            # start timer
            start_time = time.time()

            print(color_text("DO NOT CLOSE THIS WINDOWS!!!", Colors.RED))
            time.sleep(2.5)
            print(color_text("This process will take a few minute", Colors.YELLOW))
            time.sleep(5)
            spinning_text("Preparing for test...")

            # file check
            loading_bar(100, bar_length=50, text="Checking system file")
            print("")

            # encryption test
            spinning_text("Preparing for encryption test...")
            for i in range(1000):
                random_combination = encryption(20)
                print(f"\rEncryption Key:", random_combination)
                delay = random.randint(1, 10)
                time.sleep(delay/100)

            # process test
            process_list("Checking system process", process_name)

            # timer stop
            end_time = time.time()
            elapsed_time = end_time - start_time

            # finish command
            print(
                f"\r{color_text('Checking system Complete', Colors.GREEN)} - Elapsed Time: {elapsed_time:.6f} seconds")

        # internet check
        def internet():
            global internet_state

            def internet_connect():
                try:
                    return True
                except OSError:
                    pass
                return False

            if internet_connect():
                time.sleep(2)
                spinning_text("connecting to server...")
                print(color_text("\nConnecting complete", Colors.GREEN))
                internet_state = True
            else:
                spinning_text("connecting...")
                print("\nconnecting fail...")
                countdown_timer(5, "cannot connect to server, try again in:")
                time.sleep(2)
                print("")
                connect = input("Type 'Y' to reconnect or 'n' to cancel: ")
                if connect == "Y":
                    internet()
                elif connect == "n":
                    pass

        # render 3d
        def render():
            script_path = '3d.py'
            return_code = subprocess.call(['python', script_path])

            if return_code != 0:
                print(
                    f"Error while running the script: Command '['python', '{script_path}']' returned non-zero exit status {return_code}")
            print("")

        # ppm install
        def ppm():
            script_path = 'ppm.py'
            subprocess.Popen(
                ['start', 'cmd', '/k', 'python', script_path], shell=True)

        # help
        def help_command():
            file_path = 'source/help.txt'

            try:
                # Open the file in read mode
                with open(file_path, 'r') as file:
                    # Read the contents of the file
                    file_contents = file.read()
                    print(file_contents)

            except FileNotFoundError:
                print(f"The file '{file_path}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

        def about():
            file_path = 'source/about.txt'

            try:
                # Open the file in read mode
                with open(file_path, 'r') as file:
                    # Read the contents of the file
                    file_contents = file.read()
                    print(file_contents)

            except FileNotFoundError:
                print(f"The file '{file_path}' does not exist.")
            except Exception as e:
                print(f"An error occurred: {e}")

        # contect
        def contect():
            link_fb = "https://www.facebook.com/ShadowWSsnow/"
            link_ig = "https://www.instagram.com/shadoww_ssnow/"
            link_rd = "https://www.reddit.com/user/ShadowW_Ssnow/"
            link_gh = "https://github.com/donut9164/"

            fb_text = "Facebook   : "
            ig_text = "Instragram : "
            rd_text = "Reddit     : "
            gh_text = "github     : "

            fb = f"{fb_text}{link_fb}"
            ig = f"{ig_text}{link_ig}"
            rd = f"{rd_text}{link_rd}"
            gh = f"{gh_text}{link_gh}"

            print(fb)
            print(ig)
            print(rd)
            print(gh)

        # login
        def register():
            global logged_in

            if not internet_state:
                print("Please connect to server before register")
            else:
                username = input(f"\rEnter username: ")
                password = input(f"\rEnter password: ")
                register_user(username, password)
                loading_bar(2, bar_length=50, text="Creating new profile")
                print("\nUser registered successfully!\n")

        def login():
            global logged_in

            if not internet_state:
                print("Please connect to server before login")
            else:
                username = input(f"\rEnter username: ")
                password = input(f"\rEnter password: ")

                if check_credentials(username, password):
                    logged_in = True
                    print("Login as " + "[" + username + "]")
                else:
                    print("Invalid username or password!\n")

        # main

        def default_command():
            global username
            global password
            global internet_state
            global logged_in
            username = ""

            command = input(">> ")
            
            if command == "/register":
                if not logged_in:
                    register()
                else:
                    print("Please logout before creating a new account")

            elif command == "/login":
                if not logged_in:
                    login()
                else:
                    print("Please logout before login a new account")

            elif command == "/logout":
                if logged_in:
                    logged_in = False
                    print("Logged out successfully!\n")
                else:
                    print("You didn't login type:")
                    print("/register to create new account")
                    print("/login    to login into your account")

            elif command == "/state":
                if not logged_in:
                    print("You didn't login type:")
                    print("/register to create new account")
                    print("/login    to login into your account")
                elif logged_in:
                    print("You login as " + "[" + username + "]")

            # internet command
            elif command == ".connect":
                internet()
            # system command
            elif command == ".help":
                help_command()
            elif command == ".test":
                system_test()
            elif command == ".render":
                render()
            elif command == "ppm":
                if internet_state:
                    if logged_in:
                        ppm()
                    else:
                        print("Please login before open ppm install package")

                else:
                    print(
                        "Please connect to server before open ppm install package")
                print("")

            elif command == ".exit":
                quit()

            # about
            elif command == ".about":
                about()
            elif command == ".contect":
                contect()
            else:
                print("error: '" + command + "' isn't a command")
        default_command()


if __name__ == "__main__":
    main()
