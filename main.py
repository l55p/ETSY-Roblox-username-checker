import random
import string
import requests
import time
from clint.textui import colored
import ctypes
from colorama import Fore, init

init(autoreset=False)
purple = Fore.MAGENTA
white = Fore.WHITE
green = Fore.GREEN
red = Fore.RED
blue = Fore.BLUE

print(f""" {purple}
════════════════════════════════════════════════════════════════╗      
                                                                ║  
  _____ _             	                                        ║
 | ____| |_ ___ _   _ 		{white}╔═══════════════════════╗{purple}       ║
 |  _| | __/ __| | | |		{white}║ github.com/l55p       ║{purple}       ║
 | |___| |_\__ \ |_| |		{white}║ RBLX Username Checker ║{purple}       ║
 |_____|\__|___/\__, |		{white}╚═══════════════════════╝{purple}       ║
                |___/                                           ║
                                                                ║
════════════════════════════════════════════════════════════════╝
{purple}
 """)

ctypes.windll.kernel32.SetConsoleTitleW("made by l55p")

def generate_random_string(length, include_numbers):
    letters = string.ascii_lowercase
    if include_numbers:
        letters += string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def check_username_availability(username):
    time.sleep(1)
    url = f"https://auth.roblox.com/v1/usernames/validate?request.username={username}&request.birthday=1337-04-20"
    response = requests.get(url)
    data = response.json()
    if 'message' in data and data['message'] == 'Username is valid':
        return True
    return False

def generate_roblox_username(length, include_numbers, send_to_webhook_input, webhook_url, save_to_file=True):
    while True:
        username = generate_random_string(length, include_numbers)
        available = check_username_availability(username)
        if available:
            print(colored.green(f"{blue}[^-^]{green}{username} {purple}is available!"))
            if send_to_webhook_input.lower() == 'y':
                send_to_webhook(username, webhook_url)
            if save_to_file:
                with open("names.txt", "a") as file:
                    file.write(username + '\n')
            return  # Exit the loop once an available username is found
        else:
            print(colored.red(f"{blue}[^-^]{red}{username} {purple}is unavailable!"), end="\r")

def send_to_webhook(username, webhook_url):
    data = {
        "content": f"Available username: {username}"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 200:
        print(colored.red(f"{blue}[^-^]{red}Failed to send username to webhook."))
    else:
        print(colored.green(f"{blue}[^-^]{green}Username sent to webhook successfully!"))

# Function to check usernames from a file
def check_usernames_from_file(file_path, send_to_webhook_input, webhook_url):
    try:
        with open(file_path, "r") as file:
            for username in file:
                username = username.strip()
                available = check_username_availability(username)
                if available:
                    print(colored.green(f"{blue}[^-^]{green}{username} {purple}is available!"))
                    if send_to_webhook_input.lower() == 'y':
                        send_to_webhook(username, webhook_url)
                        with open("names.txt", "a") as file:
                            file.write(username + '\n')
                else:
                    print(colored.red(f"{blue}[^-^]{red}{username} {purple}is unavailable!"))
    except FileNotFoundError:
        print(colored.red(f"{blue}[^-^]{red}Error: File not found! Please check the file path."))

# Function to load webhook URL from file
def load_webhook_from_file():
    try:
        with open("webhook.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        print(colored.red(f"{blue}[^-^]{red}Error: 'webhook.txt' not found!"))
        return None

# Input for checking usernames from a file
check_file_input = input(f"{blue}[^-^]{purple}Would you like to check usernames.txt for available usernames? (y/n): ")
if check_file_input.lower() == 'y':
    file_path = "usernames.txt"  # Change this to your file path
    send_to_webhook_input = input(f"{blue}[^-^]{purple}Would you like to send the username to a webhook? (y/n): ")
    if send_to_webhook_input.lower() == 'y':
        use_saved_webhook = input(f"{blue}[^-^]{purple}Would you like to use the webhook URL saved in 'webhook.txt'? (y/n): ")
        if use_saved_webhook.lower() == 'y':
            webhook_url = load_webhook_from_file()
            if webhook_url is None:
                print(colored.red(f"{blue}[^-^]{red}Error: No webhook URL found in 'webhook.txt'!"))
                exit()
        else:
            webhook_url = input(f"{blue}[^-^]{purple}Enter the webhook URL: ")
            save_webhook_to_file_input = input(f"{blue}[^-^]{purple}Would you like to save the entered webhook URL to 'webhook.txt' for easier use? (y/n): ")
            if save_webhook_to_file_input.lower() == 'y':
                with open("webhook.txt", "w") as file:
                    file.write(webhook_url)
    else:
        webhook_url = ''  # Empty string for webhook URL
        print(colored.green(f"{blue}[^-^]{green}Skipping webhook option..."))
    check_usernames_from_file(file_path, send_to_webhook_input, webhook_url)
    input("Press Enter to exit...")
else:
    print(colored.green(f"{blue}[^-^]{green}Skipping checking usernames from file..."))

    # Rest of the code for generating usernames
    # Input for username length
    username_length = int(input(f"{blue}[^-^]{purple}How many characters? "))

    # Input for including numbers in the username
    include_numbers_input = input(f"{blue}[^-^]{purple}Include numbers in the username? (y/n): ")
    include_numbers = include_numbers_input.lower() == 'y'
    print()

    # Input for sending to webhook
    send_to_webhook_input = input(f"{blue}[^-^]{purple}Would you like to send the username to a webhook? (y/n): ")
    if send_to_webhook_input.lower() == 'y':
        use_saved_webhook = input(f"{blue}[^-^]{purple}Would you like to use the webhook URL saved in 'webhook.txt'? (y/n): ")
        if use_saved_webhook.lower() == 'y':
            webhook_url = load_webhook_from_file()
            if webhook_url is None:
                print(colored.red(f"{blue}[^-^]{red}Error: No webhook URL found in 'webhook.txt'!"))
                exit()
        else:
            webhook_url = input(f"{blue}[^-^]{purple}Enter the webhook URL: ")
            save_webhook_to_file_input = input(f"{blue}[^-^]{purple}Would you like to save the entered webhook URL to 'webhook.txt' for easier use? (y/n): ")
            if save_webhook_to_file_input.lower() == 'y':
                with open("webhook.txt", "w") as file:
                    file.write(webhook_url)
        print()
    else:
        webhook_url = ''  # Empty string for webhook URL
        print(colored.green(f"{blue}[^-^]{green}Skipping webhook option..."))

    # Input for number of usernames to generate
    num_usernames = 9999999999999999999999999999

    # Open file for writing
    with open("names.txt", "w") as file:
        for _ in range(num_usernames):
            generate_roblox_username(username_length, include_numbers, send_to_webhook_input, webhook_url)

    input("Press Enter to exit...")
