import requests
from datetime import datetime
import re
import time

while(True):
    r = requests.get('https://docs.google.com/spreadsheets/u/1/d/1o1lQ6FFqr6RALPZ6I48cuWDd1clrPOlks8f3sWKx-9s/pubhtml?gid=217361177')
    
    f = open('facility_counts.txt', 'a')
    f.write(str(datetime.now()))
    f.write("\n")
   
    # m[0]: name of room, m[1]: number of people
    for m in re.findall(r'\[\{\"v\":\"([a-zA-Z0-9 ]+)\"\},\{\"v\":(\d+)\.(\d+),\"f\":\"(\d+)\"\}\]', r.text):
        f.write(m[0] + "\n")
        f.write(m[1] + "\n")
    
    f.close()
    time.sleep(30*60)
