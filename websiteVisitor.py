# Website Vistor Automation
# This script will open up a website, wait 5 seconds
# Then open a new tab with the next url in the list
# After it loops through all the urls listed the process ends

import webbrowser
import sys
import time
from time import sleep
import os
import keyboard

##count = 0
urls = ['https://www.google.com/', 'https://twitter.com/jcwill415', 'https://youtube.com', 'https://www.coursera.org/learn/trading-algorithm/home/welcome', 'https://www.coursera.org/learn/python-statistics-financial-analysis/home/welcome', 'https://www.coursera.org/learn/r-programming/home/welcome', 'https://tdameritrade.com', 'https://www.linkedin.com/in/jenna-williams-04a8b7146/',
'https://www.facebook.com/profile.php?id=100013341725611', 'https://www.coursera.org/learn/dataviz-visual-analytics/home/welcome', 'https://www.google.com/docs/about/']

for url in urls:
  webbrowser.open(url, new =0)
  time.sleep(5)
#  keyboard.press_and_release(['Ctrl', 'W'])
##  os.system("killall 'Google Chrome'")
##  count = count + 0

##else:
##  pass      
