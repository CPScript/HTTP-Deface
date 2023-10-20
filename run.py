from subprocess import call
import time
import os
from os import system
os.system('clear')

# welcome
print("Welcome to Ace. Your personal Web Defacer")
time.sleep(1)
print("Please use a VPN for your safety")
time.sleep(5)
time.sleep(0.5)
os.system('clear')

# selection
print("To get started please select a version of Ace:")
print("1 > Ace Version 1")
print("2 > Ace Version 2")
print(" ")

choice = input("")


if choice == "1":
    time.sleep(1)
    print("You have selected AceV1")
    print("Loading...")
    time.sleep(2)
    os.system('clear')
    os.system('python version/aceV1.py')

if choice == "2":
    time.sleep(1)
    print("You have selected AceV2")
    print("Loading...")
    time.sleep(2)
    os.system('clear')
    os.system('python version/aceV2.py')
