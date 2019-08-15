import pyshark
import ipapi
import time
import pyfiglet
import pyperclip

### WRITTEN BY https://github.com/SenoxCode ###
### YOU'RE NOT ALLOWED TO CHANGE THIS CODE AND PUBLISH IT ###

interface = "INTERFACE" ##### CHANGE THIS STRING TO YOUR INTERNET INTERFACE #####

pythonname = "UDP INFORMATION TRACKER"
version = 1.0


ascii_banner = pyfiglet.figlet_format(pythonname + " " +  str(version))
print(ascii_banner)
print("\n" + pythonname + " " + str(version) + " by Senox")
time.sleep(0.3)
print("https://github.com/SenoxCode\n\n\n")
time.sleep(0.3)


cap = pyshark.LiveCapture(internet, bpf_filter="udp")
iplist = []
for packet in cap.sniff_continuously():
    if 'IP' in packet:
        ip = packet['IP'].src

        if ip.startswith("192.168"):
            stop = 1
        else:
            if ip not in iplist:
                iplist.append(ip)
                print("\n\n")
                print("IP: " + ipapi.location(ip, None, 'ip'))
                print("Country: " + ipapi.location(ip, None, 'country'))
                print("Region: " + ipapi.location(ip, None, 'region'))
                print("City: " + ipapi.location(ip, None, 'city'))
                time.sleep(0.3)
                print("------")
                time.sleep(0.1)
                print("Copied to clipboard!")
                pyperclip.copy("IP: " + ipapi.location(ip, None, 'ip') + " | " + "Country: " + ipapi.location(ip, None, 'country') + " | " + "Region: " + ipapi.location(ip, None, 'region') + " | " + "City: " + ipapi.location(ip, None, 'city'))
                time.sleep(3)





