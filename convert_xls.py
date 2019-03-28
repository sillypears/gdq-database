#!python

import os
import sys
import xlrd
from xlrd.sheet import ctype_text
import sqlite3

xel = "gdqs.xlsx"
db_file = "database.sqlite3"

db_players = {}
db_platforms = {}
db_runs = {}
db_games = {}

db = sqlite3.connect(db_file)

db_results = db.execute("SELECT name, id FROM platforms")
for res in db_results:
    db_platforms[res[0]] = int(res[1])

db_results = db.execute("SELECT name, id FROM players")
for res in db_results:
    db_players[res[0].lower()] = int(res[1])

db_results = db.execute("SELECT name, id FROM games")
for res in db_results:
    db_games[res[0]] = int(res[1])

# db_results = db.execute("SELECT MAX(id) FROM runs")
# max_id = int(db_results.fetchone()[0])


#sys.exit()
book = xlrd.open_workbook(filename=xel)

player_list = {}
platforms = []
runs = []
runs_players = []
games = {}

for sheet_idx in range(0, book.nsheets):
    sheet = book.sheet_by_index(sheet_idx)
    rows = sheet.nrows
    cols = sheet.ncols
    if rows > 1:
        headers = sheet.row(0)
        for r in range(1, rows):
            try:
                name = sheet.cell(r, 0).value.strip()
            except:
                print("name broken {}".format(sheet.cell(r, 0).value))
                name = ""
            try:
                plat = str(sheet.cell(r, 1).value.strip())
            except:
                print("plat broken {}".format(sheet.cell(r, 1).value))
                plat = ""
            try:
                players = sheet.cell(r, 2).value.strip().split(',')
            except:
                print("player broken {}".format(sheet.cell(r, 2).value))
                player = []
            try:
                event = sheet.cell(r, 3).value.strip()
            except:
                print("event broken {}".format(sheet.cell(r, 3).value))
                event = ""
            try:
                year = int(sheet.cell(r, 4).value)
            except Exception as e: 
                print("couldn't convert year")
            try:
                s_date = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 5).value, book.datemode)
            except:
                print("sdate broken {}".format(sheet.cell(r, 4).value))
                s_date = ""
            try:
                e_date = xlrd.xldate.xldate_as_datetime(sheet.cell(r, 6).value, book.datemode)
            except:
                print("edate broken {}".format(sheet.cell(r, 6).value))
                e_date = ""
            try:
                r_time = (e_date - s_date).total_seconds()
            except:
                print("why am i broken time substraction")
                r_time = -1
            
            for player in players:
                if player.strip() in player_list.keys():
                    player_list[player.strip()] += 1
                else:
                    player_list[player.strip()] = 1
            
            if name.strip() not in games.keys():
                try:
                    games[name.strip()] = {"name": name.strip(), "platform": db_platforms[plat.strip()]}
                except Exception as e:
                    games["blank"] = {"name": "blank", "platform": -1}

            if plat.strip() not in platforms:
                platforms.append(plat.strip())

            runs.append([db_games[name], db_platforms[plat], event, year, s_date, e_date, r_time])
            runs_players.append(players)
            
# for key in sorted(player_list.keys()):
    # print("INSERT INTO players (name) VALUES (\"{}\");".format(key))

# for plat in platforms:
#     print("INSERT INTO platforms (name) VALUES (\"{}\");".format(plat))

# for game in sorted(games.keys()):
#    print("INSERT INTO games (name, platform_id) VALUES (\"{}\", {});".format(games[game]["name"], games[game]["platform"]))


if len(runs) == len(runs_players):
    for i in range(0, len(runs)):
        print("INSERT INTO runs (id, game_id, platform_id, event, year, start_time, end_time, run_time) VALUES ({}, {}, {}, \"{}\", {}, \"{}Z\", \"{}Z\", {});".format(i+1, runs[i][0], runs[i][1], runs[i][2], runs[i][3], runs[i][4], runs[i][5], int(runs[i][6])))
        for player in runs_players[i]:
            print("INSERT INTO player_runs (run_id, player_id) VALUES ({}, {});".format(i+1, db_players[player.strip().lower()]))

# print(max_id)