import requests as rq
import socket
import os

from colorama import Fore, init
from typing import Union

# Initialize colorama to automatically reset color after each print
init(autoreset=True) 

def WebDirsCovery() -> None:

    def tool_intro() -> None:
        # Tool introductory information
        tool_name = Fore.LIGHTRED_EX + r"""
 __          __ ___   ______  _           ______                          
 \ \        / / | |   |  __ \(_)         / ____|                         
  \ \  /\  / /__| |__ | |  | |_ _ __ ___| |     _____   _____ _ __ _   _ 
   \ \/  \/ / _ \ '_ \| |  | | | '__/ __| |    / _ \ \ / / _ \ '__| | | |
    \  /\  /  __/ |_) | |__| | | |  \__ \ |___| (_) \ V /  __/ |  | |_| |
     \/  \/ \___|_.__/|_____/|_|_|  |___/\_____\___/ \_/ \___|_|   \__, |
                                                                    __/ |
                                                                   |___/ 
        """
        separator()
        print(tool_name) # Display tool's ASCII art and information
        separator()
        print(Fore.RED + f"[*] {Fore.YELLOW + "Tool Name:"} {Fore.LIGHTGREEN_EX + "WebDirsCovery"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Version:"} {Fore.LIGHTGREEN_EX + "1.0"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Coded By:"} {Fore.LIGHTGREEN_EX + "Reymond Joaquin"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Description:"} {Fore.LIGHTGREEN_EX + "WebDirsCovery is a tool designed to identify and discover hidden directories on web servers"}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Purpose:"} {Fore.LIGHTGREEN_EX + "For ethical hacking and penetration testing to uncover security vulnerabilities in web applications."}")
        print(Fore.RED + f"[*] {Fore.YELLOW + "Disclaimer:"} {Fore.LIGHTGREEN_EX + "Please use responsibly and ensure you have permission before scanning any website."}")
        separator()

    def enter_target() -> Union[str, socket.gethostbyname, None]:
        # Prompts user to enter a domain name
        while True:
            tool_intro()
            try:
                # Asking user to enter the domain name
                user: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + f"Enter the domain name (Type {Fore.BLUE + "'q'"} {Fore.WHITE + "to quit):"} "}").strip().lower()
                if user == "q": # If 'q' is entered, exit the program
                    exit()
                elif user == "":
                    separator()
                    print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please Enter Your Target"} {Fore.RED + "!!"}")
                else:
                    socket.gethostbyname(user) # Validate domain name
                    separator()
                    return user 
            except socket.gaierror:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Please type a valid domain name or check your internet connection"} {Fore.RED + "!!"}")

    def option() -> str:
         # Asks user to choose a scanning option
        while True:
            print(f"{Fore.RED + "[*]"} {Fore.YELLOW + "CHOOSE A DIRECTORY SCANNER:"}\n")

            print(f"{Fore.LIGHTMAGENTA_EX + "[1]"} {Fore.LIGHTCYAN_EX + "Automated Directory Scan (This will automatically scan common directories on a website)"}")
            print(f"{Fore.LIGHTMAGENTA_EX + "[2]"} {Fore.LIGHTCYAN_EX  + "Custom Directory Scan (You need to enter the path of a file containing list of directories)"}")
            print(f"{Fore.LIGHTMAGENTA_EX + "[3]"} {Fore.LIGHTCYAN_EX + "Manual Directory Scan (You need to enter a list of specific directory)"}")
            separator()

            user_option: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + f"Choose an option (Type {Fore.LIGHTMAGENTA_EX + "'1 - 3'"} {Fore.WHITE + "or"} {Fore.BLUE + "'q'"} {Fore.WHITE + "to quit)"}"}: ").strip().lower()
            
            if user_option in ["1", "2", "3", "q"]: # Check if input is valid
                return user_option
            else:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Invalid Option, Please try again"} {Fore.RED + "!!"}")
                separator()

    def Automated_Directory_Scan(user: str) -> list[str]:
        # Scans predefined list of directories on the target website
        OK_url: list[str] = []
        forbidden_url: list[str] = []
        moved_permanent_url: list[str] = []
        list_directories: list[str] = [
                            # General Directories
                            "admin",
                            "login",
                            "dashboard",
                            "config",
                            "backup",
                            "uploads",
                            "assets",
                            "css",
                            "js",
                            "images",

                            # Sensitive Files
                            ".git",
                            ".env",
                            ".htaccess",
                            ".htpasswd",
                            "config.php",
                            "database.php",
                            "wp-config.php",
                            "database.yml",
                            "settings.php",
                            "install.php",
                            "dump.sql",


                            # WordPress
                            "wp-admin",
                            "wp-content",
                            "wp-includes",
                            "wp-login.php",
                            "xmlrpc.php",

                            # Joomla
                            "administrator",
                            "components",
                            "modules",
                            "plugins",

                            # Deprecated Directories
                            "old",
                            "test",
                            "dev",
                            "staging",
                            "old-site",
                            "backup.tar.gz",

                            # Panels
                            "phpmyadmin",
                            "cpanel",
                            "adminer",

                            # Additional Sensitive Directories
                            "data",
                            "includes",
                            "cgi-bin",
                            "logs",
                            "scripts",
                            "api",
                            "swagger",
                            "var",
                            "shell"
                            ]

        separator()
        # Loop through each directory and check its status
        print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Scanning Automatically directories, checking status codes...."}\n")

        for directory in list_directories:
            try:
                full_url: str = f"https://{user}/{directory.strip()}"
                base_url = rq.get(full_url)
                status_code: int = base_url.status_code

                print(f"{Fore.LIGHTGREEN_EX + "[URL]"} {Fore.LIGHTCYAN_EX + full_url} {Fore.RED + "-"} {Fore.WHITE + "Status Code: "}{status_code_color(base_url)}")
                check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url)

            except rq.exceptions.ConnectionError:
                print(f"{Fore.LIGHTGREEN_EX + "[URL]"} {Fore.LIGHTCYAN_EX + full_url} {Fore.RED + "-"} {Fore.WHITE + "Status Code: "}{Fore.RED + "Connection Error"}")

        separator()
        return OK_url, forbidden_url, moved_permanent_url

    def Custom_Directory_Scan(user: str) -> None:
        # Allows user to input a file path with custom directory list for scanning
        OK_url: list = []
        forbidden_url: list = []
        moved_permanent_url: list = []

        while True:
            try:
                directories: str = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + f"Enter the file path containing your list of directory paths (Type {Fore.BLUE + "'q'"} {Fore.WHITE + "to quit):"}"} ").strip()
                if directories == "q": # If 'q' is entered, quit the process
                    separator()
                    return None

                separator()
                print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Scanning directories from your file, checking status codes..."}\n")

                with open(directories, "r") as file:
                    for directory in file.readlines():
                        full_url: str = f"https://{user}/{directory.strip()}"
                        base_url = rq.get(full_url)
                        status_code: int = base_url.status_code

                        print(f"{Fore.LIGHTGREEN_EX + "URL:"} {Fore.LIGHTCYAN_EX + full_url} {Fore.RED + "-"} {Fore.WHITE + "Status Code:"}{status_code_color(base_url)}")
                        check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url)

                    separator()
                    summary_result(OK_url, forbidden_url, moved_permanent_url)

            except FileNotFoundError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + f"The file '{directories}' was not found."} {Fore.RED + "!!"}")
                separator()
            except PermissionError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "You don't have permission to access that file"} {Fore.RED + "!!"}")
                separator()
            except rq.exceptions.ConnectionError:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Can't Connect to the target, Please check your internet connection"} {Fore.RED + "!!"}")
                separator()
            except Exception:
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Something went wrong, Please try again"} {Fore.RED + "!!"}")
                separator()

    def check_status_code(status_code, OK_url, forbidden_url, moved_permanent_url, full_url) -> None:
        # Categorizes URLs based on their HTTP status code
        if status_code == 200:
            OK_url.append(full_url)
        elif status_code == 301:
            moved_permanent_url.append(full_url)
        elif status_code == 403:
            forbidden_url.append(full_url)

    def Manual_Directory_Scan(user: str) -> None:
        # Allows user to manually input directories for scanning
        directories: list[str] = []
        separator()
        while True:
            try:
                enter_directory = input(f"{Fore.BLUE + "[*]"} {Fore.WHITE + f"Enter a directory to scan for [ {Fore.LIGHTCYAN_EX + f"https://{user}/"} {Fore.WHITE + "] (Type"} {Fore.GREEN + "'done'"} {Fore.WHITE + "to start scanning"} {Fore.WHITE + "or"} {Fore.BLUE + "'q'"} {Fore.WHITE + "to quit):"}"} ").strip()
                directories.append(enter_directory) # Add each directory to the list 

                if enter_directory.lower() == "q": # If 'q' is entered, quit the process
                    separator()
                    return None
                elif enter_directory.lower() == "done":
                    directories.remove("done")
                    separator()
                    print(f"{Fore.RED + "[*]"} {Fore.LIGHTGREEN_EX + "Scanning Directories in Progress..."}\n")
                    for num, directory in enumerate(directories):
                        full_url = f"https://{user}/{directory.strip()}"
                        base_url = rq.get(full_url)
                        status_code = status_code_color(base_url)
                        print(f"[{num +1}] {Fore.LIGHTCYAN_EX + full_url} {Fore.RED + "-"} {Fore.WHITE + "Status Code: "}{status_code}")
                    
                    directories: list[str] = [] # Reset directory list after scanning
                    separator()
                    
            except rq.exceptions.ConnectionError:
                separator()
                print(f"{Fore.RED + "!!"} {Fore.YELLOW + "Connection Error, Please check your internet connection"} {Fore.RED + "!!"}")
                separator()

    def status_code_color(base_url) -> str:
        # Returns color-coded status message based on the HTTP status code
        if  base_url.status_code == 200:
            return Fore.GREEN + f"{base_url.status_code} OK"
        elif base_url.status_code == 301:
            return Fore.YELLOW + f"{base_url.status_code} Moved Permanently"
        elif base_url.status_code == 401:
            return Fore.RED + f"{base_url.status_code} Unauthorized"
        elif base_url.status_code == 403:
            return Fore.RED + f"{base_url.status_code} Forbidden"
        elif base_url.status_code == 404:
            return Fore.LIGHTRED_EX + f"{base_url.status_code} Not Found"
        elif base_url.status_code == 405:
            return Fore.YELLOW + f"{base_url.status_code} Method Not Allowed"
        elif base_url.status_code == 406:
            return Fore.YELLOW + f"{base_url.status_code} Not Acceptable"
        elif base_url.status_code == 429:
            return Fore.RED + f"{base_url.status_code} Too many Requests"
        elif base_url.status_code == 500:
            return Fore.MAGENTA + f"{base_url.status_code} Internal Server Error"
        elif base_url.status_code == 503:
            return Fore.LIGHTMAGENTA_EX + f"{base_url.status_code} Service Unavailable"
        else:
            return Fore.LIGHTYELLOW_EX + f"{base_url.status_code} Unidentified"

    def summary_result(OK_url: list[str], forbidden_url: list[str], moved_permanent_url: list[str]) -> None:
         # Summary of scanned results
        def result(path_url, status_code, color) -> None:
            print(f"{Fore.GREEN + "[*]"} {Fore.LIGHTMAGENTA_EX + "Summary of"} {color + status_code} {Fore.LIGHTMAGENTA_EX + "Status Code Result:"}\n")
            for num, url in enumerate(path_url):
                print(f"{Fore.WHITE + f"[{num +1}]"} {Fore.LIGHTCYAN_EX + url} {Fore.RED + "-"} {Fore.WHITE + "Status Code: "}{color + status_code}")
            print()

        result(OK_url, "200 OK", color = Fore.GREEN)
        result(moved_permanent_url, "301 Moved Permanently", color = Fore.YELLOW)
        result(forbidden_url, "403 Forbidden", color = Fore.RED)
        separator()

    def separator() -> None:
        # Get the width of the terminal (how many characters fit in one line)
        terminal_width: int = os.get_terminal_size().columns

        # Make a line of '=' characters that is as wide as the terminal
        separator: int = Fore.RED + "=" * terminal_width

        # Print the line of '=' characters
        print(separator)
    
    def main() -> None:
        # Flow of the program
        while True:
            try:
                user = enter_target()

                while True:
                    user_choice = option()
                    if  user_choice == "q": # If option function returns 'q' it will break
                            break
                    # Options
                    while True:
                        if user_choice == "1":
                            OK_url, forbidden_url, moved_permanent_url = Automated_Directory_Scan(user)
                            summary_result(OK_url, forbidden_url, moved_permanent_url)
                            break
                        elif user_choice == "2":
                            if Custom_Directory_Scan(user) is None:
                                break
                        elif user_choice == "3":
                            if Manual_Directory_Scan(user) is None:
                                break
            except KeyboardInterrupt:
                print()
                continue
    main()

if __name__ == "__main__":
    WebDirsCovery()