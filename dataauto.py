"""Task 1- Open daily websites"""

import webbrowser
import time 

websites = [
    "https://www.google.com",
    "https://www.github.com"
]

for sites in websites:
    webbrowser.open(sites)
    
print("Sites opened")

"""Need to schedule it in windows task scheduler if want it to run at certain time """
"""taskschd.msc then create basic task"""
""" make sure to select python.exe and add path to script in argument box"""

"""mac and linux must open terminal and type crontab -e and add schedule and path"""