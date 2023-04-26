import requests
import colorama
from colorama import Fore


print(f'''
{Fore.RED}
/       \ /  |  /  |/      |/  \  /  |/      |/  |  /  |
$$$$$$$  |$$ |  $$ |$$$$$$/ $$  \ $$ |$$$$$$/ $$ |  $$ |
$$ |__$$ |$$ |__$$ |  $$ |  $$$  \$$ |  $$ |  $$  \/$$/ 
$$    $$/ $$    $$ |  $$ |  $$$$  $$ |  $$ |   $$  $$<  
$$$$$$$/  $$$$$$$$ |  $$ |  $$ $$ $$ |  $$ |    $$$$  \ 
$$ |      $$ |  $$ | _$$ |_ $$ |$$$$ | _$$ |_  $$ /$$  |
$$ |      $$ |  $$ |/ $$   |$$ | $$$ |/ $$   |$$ |  $$ |
$$/       $$/   $$/ $$$$$$/ $$/   $$/ $$$$$$/ $$/   $$/ 
{Fore.WHITE}
Devs : Aze , Rin
Github Repo : https://github.com/Aze27/phinix

''')

import os
import json

prs_key = False
try:
    with open("tokens.txt", "r") as f:
        tokens = f.read().splitlines()
except FileNotFoundError:

    print("tokens.txt not found. Creating file.")
    with open("tokens.txt", "w") as f:
        f.write("")
    prs_key = True

if not tokens:
    print("Please add your tokens in the tokens.txt file. It was found to be empty")
    prs_key = True
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:

    print("config.json not found. Creating file with default values.")
    config = {
        "role_names": [],
        "channel_names": [],
        "webhook_name": "",
        "nuker_name": ""
    }
    with open("config.json", "w") as f:
        json.dump(config, f)
    prs_key = True

import sys
import time

if prs_key:
    print(f"\n{Fore.RED}PLEASE DO THE REQUIRED CONFIGS AND RERUN THE PROGRAM {Fore.WHITE}")
    time.sleep(5)
    sys.exit()

role_names = config["role_names"]
channel_names = config["channel_names"]
webhook_name = config["webhook_name"]
nuker_name = config["nuker_name"]


if not role_names:
    role_names = input("Role names are missing. Please enter them, separated by commas: ").split(",")
if not channel_names:
    channel_names = input("Channel names are missing. Please enter them, separated by commas: ").split(",")
if not webhook_name:
    webhook_name = input("Webhook name is missing. Please enter it: ")
if not nuker_name:
    nuker_name = input("Nuker name is missing. Please enter it: ")


config["role_names"] = role_names
config["channel_names"] = channel_names
config["webhook_name"] = webhook_name
config["nuker_name"] = nuker_name


with open("config.json", "w") as f:
    json.dump(config, f)

print(f"\n{Fore.BLUE}Please Select your option from the following. {Fore.WHITE}")

print("\n")