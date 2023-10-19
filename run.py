from scripts.sprint import sprint
from scripts.colors import ran, y, r, g, c
from subprocess import call
import time
import os
from os import system
os.system('clear')

# welcome
sprint("Welcome to Ace. Your personal Web Defacer")
time.sleep(1)
sprint("Please use a VPN for your safety")
time.sleep(5)
print("Have fun!!!")
time.sleep(0.5)
os.system('clear')

# selection
print("To get started please select a version of Ace:")
hoice = input("")


if choice == "1":
    os.system('clear')
    time.sleep(1)
    sprint("You have selected AceV1")
    print("Loading...")
    time.sleep(2)
    os.system('clear')
    call(["python", "version/aceV1.py"])

if choice == "2":
    os.system('clear')
    time.sleep(1)
    sprint("You have selected AceV2")
    print("Loading...")
    time.sleep(2)
    os.system('clear')
    call(["python", "version/aceV2.py"])
