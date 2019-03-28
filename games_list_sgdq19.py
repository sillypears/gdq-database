#!python
import os
import sys
from bs4 import BeautifulSoup
import re

# Globals
URL = "https://gamesdonequick.com/tracker/runs/"
FILE = "games-list.html"
# FILE = "some_events.html"

class Game:
    def __init__(self, n, p, c, pl, e, y, st, et):
        self.name = n
        self.players = p
        self.category = c
        self.platform = pl
        self.event = e
        self.year = y
        self.start_time = st
        self.end_time = et

def main():
    print("reading file")
    soup = BeautifulSoup(open(FILE), 'html.parser')
    
    table = soup.find('tbody')
    for tr in table.find_all('tr'):
        py, ga, pl = ("", "", "")
        count = 0
        for td in tr.find_all('td'):

            if count in (0, 1):
                if count is 0:
                    py = td.text.strip()
                if count is 1:
                    # ga, pl = td.text.splitlines()
                    ga, pl = td.text.strip().splitlines()
                    
                    # ga = temp[0]
                    # pl = temp[1]
            
            count += 1
        print("{}~{}~{}".format(py, ga, pl))
        
        
    

if __name__ == "__main__":
    sys.exit(main())