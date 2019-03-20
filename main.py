#!python
import os
import sys
from bs4 import BeautifulSoup

# Globals
URL = "https://gamesdonequick.com/tracker/runs/"
FILE = "all_events.html"
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
    
    table = soup.find('table')
    for tr in table.find_all('tr'):
        g, p, s, e = ("", "", "", "")

        count = 0
        for td in tr.find_all('td'):
            if count in (0, 1, 3, 4):
                if count is 0:
                    g = td.text.strip()
                if count is 1:
                    p = td.text.strip()
                if count is 3:
                    s = td.text.strip()
                if count is 4:
                    e = td.text.strip()
            count += 1
        print("{}~{}~{}~{}".format(g, p, s, e))
        
        
    

if __name__ == "__main__":
    sys.exit(main())