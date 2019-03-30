#!python

# Good luck trying to figure out what the hell you did here when you see this again in 3 months

import os
import sys
import json
import sqlite3

OFF_EVENTS = {
    "cgdq": 2010,
    "gowdq": 2015,
    "hrdq": 2017,
    "gdqx": 2018,
    "jrdq": 2011
}

j_file = "gdqs_edited.json"
db_file = "json_database.sqlite3"

db_events = {}
db_games = {}
db_genres = {}
db_platforms = {}
db_runners = {}
db_runs = {}

db = sqlite3.connect(db_file)

db_res = db.execute("SELECT name, id FROM events")
for res in db_res:
    db_events[res[0]] = int(res[1])   

db_res = db.execute("SELECT name, id FROM games")
for res in db_res:
    db_games[res[0]] = int(res[1])

db_res = db.execute("SELECT name, id FROM genres")
for res in db_res:
    db_genres[res[0]] = int(res[1])

db_res = db.execute("SELECT name, id FROM platforms")
for res in db_res:
    db_platforms[res[0]] = int(res[1])

db_res = db.execute("SELECT name, id FROM runners")
for res in db_res:
    db_runners[res[0]] = int(res[1])
 
db_res = db.execute("SELECT run_game_key, id FROM runs")
for res in db_res:
    db_runs[res[0]] = int(res[1])

with open(j_file, 'r', encoding='utf8', errors='ignore') as f:
    j_data = json.loads(f.read())

runners = {}
platforms = []
runs = {}
games = {}
genres = []
runs_runners = {}
for r in j_data:
    run = j_data[r]

    if run['platform_id'] not in platforms:
        platforms.append(run['platform_id'])
    
    if run['genre_id'] not in genres:
        genres.append(run['genre_id'])

    for runner_entry in run["runners"]:
        runner_id = runner_entry["id"]
        try:
            display_name = runner_entry["name"]
        except:
            display_name = ""
        try:
            twitch = runner_entry["twitch"]
        except:
            twitch = ""
        try:
            twitter = runner_entry["twitter"]
        except:
            twitter = ""
        try:
            youtube = runner_entry["youtube"]
        except:
            youtube = ""

        runner = {
            "name": runner_entry["id"],
            "display_name": display_name,
            "twitch": twitch,
            "twitter": twitter,
            "youtube": youtube
        }
        if runner_id not in runners.keys():
            runners[runner_id] = runner

        if run["id"] in db_runs.keys():
            run_id = db_runs[run["id"]]
            runner_id = db_runners[runner["name"]]
            runs_runners[run["id"]+runner["name"]] = {"run_id": run_id, "runner_id": runner_id}

    if not games.get(run["game"]["id"]):
        games[run["game"]["id"]] = {
            "name": run["game"]["name"],
            "platform": run["game"]["platform"]["id"],
            "year": run["game"]["year"],
            "genre": run["game"]["genre"]["id"]
        }
    
    if not runs.get(r):
        game_id = db_games[run["game_id"]]
        game_key = run["id"]
        category = run["category"]
        race = int(run["race"])
        event_id = db_events[run["event_id"].split("-")[0]]
        year = int(OFF_EVENTS[run["event_id"].split("-")[0]]) if run["event_id"].split("-")[0] in OFF_EVENTS.keys() else int(run["event_id"].split("-")[1])
        duration = run["duration"]
        start_time = run["start_time"]
        awful = int(run["awful"])
        handicapped = int(run["handicapped"])
        silly = int(run["silly"])
        highlight = int(run["highlight"])
        wr = int(run["wr"])
        tas = int(run["tas"])
        dev_comm = int(run["dev_commentary"])
        runs[r] = {
            "game_id": game_id,
            "run_game_key": game_key,
            "category": category,
            "race": race,
            "event_id": event_id,
            "year": year,
            "start_time": start_time,
            "duration": duration,
            "awful": awful,
            "handicapped": handicapped,
            "silly": silly,
            "highlight": highlight,
            "wr": wr,
            "tas": tas,
            "dev_commentary": dev_comm
        }
        
# for item in sorted(platforms):
#     print(item)

# for genre in sorted(genres):
#     print(genre)

# for r in sorted(runners.keys()):
#     print("INSERT INTO runners (name, display_name, twitch, twitter, youtube) VALUES (\"{}\", \"{}\", \"{}\", \"{}\", \"{}\");".format(r, runners[r]["name"], runners[r]["twitch"], runners[r]["twitter"], runners[r]["youtube"]))

# for g in sorted(games.keys()):
#     print("INSERT INTO games (name, display_name, platform, year, genre) VALUES (\"{}\", \"{}\", {}, {}, {});".format(g, games[g]["name"], db_platforms[games[g]["platform"]], int(games[g]["year"]), db_genres[games[g]["genre"]]))

# for r in sorted(runs.keys()):
#     run = runs[r]
#     print("INSERT INTO runs (game_id, run_game_key, category, race, event_id, year, start_time, duration, awful, handicapped, silly, highlight, wr, tas, dev_commentary) VALUES ({}, \"{}\", \"{}\", {}, {}, {}, {}, \"{}\", {}, {}, {}, {}, {}, {}, {});".format(run["game_id"], run["run_game_key"], run["category"], run["race"], run["event_id"], run["year"], int(run["start_time"]), run["duration"], run["awful"], run["handicapped"], run["silly"], run["highlight"], run["wr"], run["tas"], run["dev_commentary"]))

# for r in runs_runners:
#     print("INSERT INTO runs_runners (run_id, runner_id) VALUES ({}, {});".format(int(runs_runners[r]["run_id"]), int(runs_runners[r]["runner_id"])))
    