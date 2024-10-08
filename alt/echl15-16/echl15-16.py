#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sqlite3
import sys

leaguename = "ECHL"
getforday = "24"
getformonth = "10"
getforyear = "2015"

print("Creating " + leaguename + " Database.")

if (len(sys.argv) == 0):
    sqlcon = sqlite3.connect("./echl15-16.db3")
if (len(sys.argv) > 0):
    sqlcon = sqlite3.connect(sys.argv[1])
sqlcur = sqlcon.cursor()

sqlcon.execute("PRAGMA encoding = \"UTF-8\";")
sqlcon.execute("PRAGMA auto_vacuum = 1;")
sqlcon.execute("PRAGMA foreign_keys = 1;")


def GetLastTenGames(sqldatacon, teamname):
    global leaguename
    wins = 0
    losses = 0
    otlosses = 0
    getlastninegames = sqldatacon[0].execute(
        "SELECT NumberPeriods, TeamWin FROM " +
        leaguename +
        "Games WHERE (HomeTeam=\"" +
        str(teamname) +
        "\" OR AwayTeam=\"" +
        str(teamname) +
        "\") ORDER BY id DESC LIMIT 10").fetchall()
    nmax = len(getlastninegames)
    nmin = 0
    while (nmin < nmax):
        if (teamname == str(getlastninegames[nmin][1])):
            wins = wins + 1
        if (teamname != str(getlastninegames[nmin][1])):
            if (int(getlastninegames[nmin][0]) == 3):
                losses = losses + 1
            if (int(getlastninegames[nmin][0]) > 3):
                otlosses = otlosses + 1
        nmin = nmin + 1
    return str(wins) + ":" + str(losses) + ":" + str(otlosses)


def UpdateTeamData(sqldatacon, teamid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Teams WHERE id=" + str(teamid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Teams WHERE id=" + str(teamid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Teams SET " +
        dataname +
        "=" +
        str(TMPData) +
        " WHERE id=" +
        str(teamid))
    return int(TMPData)


def UpdateTeamDataString(sqldatacon, teamid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Teams SET " +
        dataname +
        "=\"" +
        str(newdata) +
        "\" WHERE id=" +
        str(teamid))
    return True


def GetTeamData(sqldatacon, teamid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Teams WHERE id=" +
                str(teamid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Teams WHERE id=" +
                str(teamid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Teams WHERE id=" +
                str(teamid)).fetchone()[0])
    return TMPData


def UpdateGameData(sqldatacon, gameid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Games WHERE id=" + str(gameid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Games WHERE id=" + str(gameid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Games SET " +
        dataname +
        "=" +
        str(TMPData) +
        " WHERE id=" +
        str(gameid))
    return int(TMPData)


def UpdateGameDataString(sqldatacon, gameid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Games SET " +
        dataname +
        "=\"" +
        str(newdata) +
        "\" WHERE id=" +
        str(gameid))
    return True


def GetGameData(sqldatacon, gameid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Games WHERE id=" +
                str(gameid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Games WHERE id=" +
                str(gameid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Games WHERE id=" +
                str(gameid)).fetchone()[0])
    return TMPData


def UpdateArenaData(sqldatacon, arenaid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Arenas WHERE id=" + str(arenaid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + \
                      leaguename + "Arenas WHERE id=" + str(arenaid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Arenas SET " +
        dataname +
        "=" +
        str(TMPData) +
        " WHERE id=" +
        str(arenaid))
    return int(TMPData)


def UpdateArenaDataString(sqldatacon, arenaid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Arenas SET " +
        dataname +
        "=\"" +
        str(newdata) +
        "\" WHERE id=" +
        str(arenaid))
    return True


def GetArenaData(sqldatacon, arenaid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Arenas WHERE id=" +
                str(arenaid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Arenas WHERE id=" +
                str(arenaid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(
            sqldatacon[0].execute(
                "SELECT " +
                dataname +
                " FROM " +
                leaguename +
                "Arenas WHERE id=" +
                str(arenaid)).fetchone()[0])
    return TMPData


def UpdateConferenceData(sqldatacon, conference, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename + \
                      "Conferences WHERE Conference=\"" + str(conference) + "\"").fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename + \
                      "Conferences WHERE Conference=\"" + str(conference) + "\"").fetchone()[0]) - addtodata
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Conferences SET " +
        dataname +
        "=" +
        str(TMPData) +
        " WHERE Conference=\"" +
        str(conference) +
        "\"")
    return int(TMPData)


def UpdateDivisionData(sqldatacon, division, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename +
                      "Divisions WHERE Division=\"" + str(division) + "\"").fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename +
                      "Divisions WHERE Division=\"" + str(division) + "\"").fetchone()[0]) - addtodata
    sqldatacon[0].execute(
        "UPDATE " +
        leaguename +
        "Divisions SET " +
        dataname +
        "=" +
        str(TMPData) +
        " WHERE Division=\"" +
        str(division) +
        "\"")
    return int(TMPData)


print("Creating " + leaguename + " Conference Table.")
print("Inserting " + leaguename + " Conference Data.")

sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Conferences")
sqlcur.execute(
    "CREATE TABLE " +
    leaguename +
    "Conferences(id INTEGER PRIMARY KEY, Conference TEXT, NumberOfTeams INTEGER)")
sqlcon.commit()


def MakeHockeyConferences(sqldatacon, conference):
    global leaguename
    print("Conference Name: " + conference)
    print(" ")
    sqldatacon[0].execute(
        "INSERT INTO " +
        leaguename +
        "Conferences(Conference, NumberOfTeams) VALUES(\"" +
        str(conference) +
        "\", 0)")
    return True


MakeHockeyConferences((sqlcur, sqlcon), "Eastern")
MakeHockeyConferences((sqlcur, sqlcon), "Western")
sqlcon.commit()

print("Creating " + leaguename + " Division Table.")
print("Inserting " + leaguename + " Division Data.")

sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Divisions")
sqlcur.execute(
    "CREATE TABLE " +
    leaguename +
    "Divisions(id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, NumberOfTeams INTEGER)")
sqlcon.commit()


def MakeHockeyDivisions(sqldatacon, division, conference):
    global leaguename
    print("Conference Name: " + conference)
    print("Division Name: " + division)
    print(" ")
    sqldatacon[0].execute(
        "INSERT INTO " +
        leaguename +
        "Divisions(Division, Conference, NumberOfTeams) VALUES(\"" +
        str(division) +
        "\", \"" +
        str(conference) +
        "\", 0)")
    return True


MakeHockeyDivisions((sqlcur, sqlcon), "East", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "North", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "South", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "Midwest", "Western")
MakeHockeyDivisions((sqlcur, sqlcon), "Central", "Western")
MakeHockeyDivisions((sqlcur, sqlcon), "West", "Western")

print("Creating " + leaguename + " Team Table.")
print("Inserting " + leaguename + " Team Data.")

sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Arenas")
sqlcur.execute(
    "CREATE TABLE " +
    leaguename +
    "Arenas(id INTEGER PRIMARY KEY, CityName TEXT, AreaName TEXT, FullCityName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER)")
sqlcon.commit()

sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Teams")
sqlcur.execute("CREATE TABLE " + leaguename + "Teams(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, Affiliates TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)")
sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Stats")
sqlcur.execute("CREATE TABLE " + leaguename + "Stats(id INTEGER PRIMARY KEY, TeamID  INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, Affiliates TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)")
sqlcon.commit()


def MakeHockeyTeams(
        sqldatacon,
        cityname,
        areaname,
        teamname,
        conference,
        division,
        arenaname,
        teamnameprefix,
        teamaffiliates):
    global leaguename
    print("Team Name: " + teamname)
    print("Arena Name: " + arenaname)
    print("City Name: " + cityname)
    print("Full City Name: " + cityname + ", " + areaname)
    print("Full Name: " + teamnameprefix + " " + teamname)
    print("Conference: " + conference)
    print("Division: " + division)
    print(" ")
    sqldatacon[0].execute("INSERT INTO " +
                          leaguename +
                          "Teams(Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) VALUES(\"20151001\", \"" +
                          str(teamnameprefix +
                              " " +
                              teamname) +
                          "\", \"" +
                          str(cityname) +
                          "\", \"" +
                          str(teamnameprefix) +
                          "\", \"" +
                          str(areaname) +
                          "\", \"" +
                          str(cityname +
                              ", " +
                              areaname) +
                          "\", \"" +
                          str(teamname) +
                          "\", \"" +
                          str(conference) +
                          "\", \"" +
                          str(division) +
                          "\", \"" +
                          str(arenaname) +
                          "\", \"" +
                          str(arenaname +
                              ", " +
                              cityname) +
                          "\", \"" +
                          str(teamaffiliates) +
                          "\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"None\")")
    sqldatacon[0].execute(
        "INSERT INTO " +
        leaguename +
        "Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM " +
        leaguename +
        "Teams WHERE FullName=\"" +
        teamnameprefix +
        " " +
        teamname +
        "\";")
    sqldatacon[0].execute("INSERT INTO " +
                          leaguename +
                          "Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\"" +
                          str(cityname) +
                          "\", \"" +
                          str(areaname) +
                          "\", \"" +
                          str(cityname +
                              ", " +
                              areaname) +
                          "\", \"" +
                          str(arenaname) +
                          "\", \"" +
                          str(arenaname +
                              ", " +
                              cityname) +
                          "\", 0)")
    UpdateConferenceData((sqlcur, sqlcon), conference, "NumberOfTeams", 1, "+")
    UpdateDivisionData((sqlcur, sqlcon), division, "NumberOfTeams", 1, "+")
    return True


def MakeHockeyArena(sqldatacon, cityname, areaname, arenaname, teamnameprefix):
    global leaguename
    print("Arena Name: " + arenaname)
    print("City Name: " + cityname)
    print("Full City Name: " + cityname + ", " + areaname)
    print(" ")
    sqldatacon[0].execute("INSERT INTO " +
                          leaguename +
                          "Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\"" +
                          str(cityname) +
                          "\", \"" +
                          str(areaname) +
                          "\", \"" +
                          str(cityname +
                              ", " +
                              areaname) +
                          "\", \"" +
                          str(arenaname) +
                          "\", \"" +
                          str(arenaname +
                              ", " +
                              cityname) +
                          "\", 0)")
    return True


print("Inserting " + leaguename + " Teams From Eastern Conference.")
print("Inserting " + leaguename + " Teams From East Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Elmira",
                "NY",
                "Jackals",
                "Eastern",
                "East",
                "First Arena",
                "Elmira",
                "AHL:Rochester Americans,NHL:Buffalo Sabres ")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Reading",
                "PA",
                "Royals",
                "Eastern",
                "East",
                "Santander Arena",
                "Reading",
                "AHL:Lehigh Valley Phantoms,NHL:Philadelphia Flyers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Norfolk",
                "VA",
                "Admirals",
                "Eastern",
                "East",
                "Norfolk Scope",
                "Norfolk",
                "AHL:Bakersfield Condors,NHL:Edmonton Oilers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Glens Falls",
                "NY",
                "Thunder",
                "Eastern",
                "East",
                "Glens Falls Civic Center",
                "Adirondack",
                "AHL:Stockton Heat,NHL:Calgary Flames")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Manchester",
                "NH",
                "Monarchs",
                "Eastern",
                "East",
                "Verizon Wireless Arena",
                "Manchester",
                "AHL:Ontario Reign,NHL:Los Angeles Kings")

print("Inserting " + leaguename + " Teams From North Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Kalamazoo",
                "MI",
                "Wings",
                "Eastern",
                "North",
                "Wings Event Center",
                "Kalamazoo",
                "AHL:Lake Erie Monsters,NHL:Columbus Blue Jackets")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Toledo",
                "OH",
                "Walleye",
                "Eastern",
                "North",
                "Huntington Center",
                "Toledo",
                "AHL:Grand Rapids Griffins,NHL:Detroit Red Wings")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Wheeling",
                "WV",
                "Nailers",
                "Eastern",
                "North",
                "WesBanco Arena",
                "Wheeling",
                "AHL:Wilkes-Barre/Scranton Penguins,NHL:Pittsburgh Penguins")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Brampton",
                "ON",
                "Beast",
                "Eastern",
                "North",
                "Powerade Centre",
                "Brampton",
                "AHL:St. John's IceCaps,NHL:Montreal Canadiens")

print("Inserting " + leaguename + " Teams From South Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Duluth",
                "GA",
                "Gladiators",
                "Eastern",
                "South",
                "Infinite Energy Arena",
                "Atlanta",
                "AHL:Providence Bruins,NHL:Boston Bruins")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Greenville",
                "SC",
                "Swamp Rabbits",
                "Eastern",
                "South",
                "Bon Secours Wellness Arena",
                "Greenville",
                "AHL:Hartford Wolf Pack,NHL:New York Rangers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Estero",
                "FL",
                "Everblades",
                "Eastern",
                "South",
                "Germain Arena",
                "Florida",
                "AHL:Charlotte Checkers,NHL:Carolina Hurricanes")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Orlando",
                "FL",
                "Solar Bears",
                "Eastern",
                "South",
                "Amway Center",
                "Orlando",
                "AHL:Toronto Marlies,NHL:Toronto Maple Leafs")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "North Charleston",
                "SC",
                "Stingrays",
                "Eastern",
                "South",
                "North Charleston Coliseum",
                "South Carolina",
                "AHL:Hershey Bears,NHL:Washington Capitals")

print("Inserting " + leaguename + " Teams From Western Conference.")
print("Inserting " + leaguename + " Teams From Midwest Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Moline",
                "IL",
                "Mallards",
                "Western",
                "Midwest",
                "iWireless Center",
                "Quad City",
                "AHL:Iowa Wild,NHL:Minnesota Wild")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Evansville",
                "IN",
                "IceMen",
                "Western",
                "Midwest",
                "Ford Center",
                "Evansville",
                "AHL:Binghamton Senators,NHL:Ottawa Senators")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Indianapolis",
                "IN",
                "Fuel",
                "Western",
                "Midwest",
                "Indiana Farmers Coliseum",
                "Indy",
                "AHL:Rockford IceHogs,NHL:Chicago Blackhawks")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Fort Wayne",
                "IN",
                "Komets",
                "Western",
                "Midwest",
                "Allen County War Memorial Coliseum",
                "Fort Wayne",
                "AHL:San Antonio Rampage,NHL:Colorado Avalanche")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Cincinnati",
                "OH",
                "Cyclones",
                "Western",
                "Midwest",
                "US Bank Arena",
                "Cincinnati",
                "AHL:Milwaukee Admirals,NHL:Nashville Predators")

print("Inserting " + leaguename + " Teams From Central Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Wichita",
                "KS",
                "Thunder",
                "Western",
                "Central",
                "Intrust Bank Arena",
                "Wichita",
                "AHL:None,NHL:None")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Allen",
                "TX",
                "Americans",
                "Western",
                "Central",
                "Allen Event Center",
                "Allen",
                "AHL:San Jose Barracuda,NHL:San Jose Sharks")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Tulsa",
                "OK",
                "Oilers",
                "Western",
                "Central",
                "BOK Center",
                "Tulsa",
                "AHL:Manitoba Moose,NHL:Winnipeg Jets")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Independence",
                "MO",
                "Mavericks",
                "Western",
                "Central",
                "Silverstein Eye Centers Arena",
                "Missouri",
                "AHL:Bridgeport Sound Tigers,NHL:New York Islanders")

print("Inserting " + leaguename + " Teams From West Division.\n")
MakeHockeyTeams((sqlcur, sqlcon), "Anchorage", "AK", "Aces", "Western",
                "West", "Sullivan Arena", "Alaska", "AHL:None,NHL:None")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Boise",
                "ID",
                "Steelheads",
                "Western",
                "West",
                "CenturyLink Arena",
                "Idaho",
                "AHL:Texas Stars,NHL:Dallas Stars")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "West Valley City",
                "UT",
                "Grizzlies",
                "Western",
                "West",
                "Maverik Center",
                "Utah",
                "AHL:San Diego Gulls,NHL:Anaheim Ducks")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Loveland",
                "CO",
                "Eagles",
                "Western",
                "West",
                "Budweiser Events Center",
                "Colorado",
                "AHL:None,NHL:None")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Rapid City",
                "SD",
                "Rush",
                "Western",
                "West",
                "Rushmore Plaza Civic Center",
                "Rapid City",
                "AHL:Springfield Falcons,NHL:Arizona Coyotes")

sqlcon.commit()


def GetNum2Team(sqldatacon, TeamNum, ReturnVar):
    global leaguename
    return str(
        sqldatacon[0].execute(
            "SELECT " +
            ReturnVar +
            " FROM " +
            leaguename +
            "Teams WHERE id=" +
            str(TeamNum)).fetchone()[0])


def GetTeam2Num(sqldatacon, TeamName):
    global leaguename
    return int(
        sqldatacon[0].execute(
            "SELECT id FROM " +
            leaguename +
            "Teams WHERE FullName=\"" +
            str(TeamName) +
            "\"").fetchone()[0])


def GetNum2Arena(sqldatacon, ArenaNum, ReturnVar):
    global leaguename
    return str(
        sqldatacon[0].execute(
            "SELECT " +
            ReturnVar +
            " FROM " +
            leaguename +
            "Arenas WHERE id=" +
            str(ArenaNum)).fetchone()[0])


def GetArena2Num(sqldatacon, ArenaName):
    global leaguename
    return int(
        sqldatacon[0].execute(
            "SELECT id FROM " +
            leaguename +
            "Arenas WHERE FullArenaName=\"" +
            str(ArenaName) +
            "\"").fetchone()[0])


print("DONE! All Team Data Inserted.")

print("Creating " + leaguename + " Game Table.")

sqlcon.execute("DROP TABLE IF EXISTS " + leaguename + "Games")
sqlcur.execute(
    "CREATE TABLE " +
    leaguename +
    "Games(id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam Text, AwayTeam Text, AtArena Text, TeamScorePeriods TEXT, TeamFullScore Text, ShotsOnGoal TEXT, FullShotsOnGoal TEXT, ShotsBlocked TEXT, FullShotsBlocked TEXT, NumberPeriods INTEGER, TeamWin Text, IsPlayOffGame INTEGER)")
sqlcon.commit()


def MakeHockeyGame(
        sqldatacon,
        date,
        hometeam,
        awayteam,
        periodsscore,
        shotsongoal,
        atarena,
        isplayoffgame):
    global leaguename
    isplayoffgsql = "0"
    if (isplayoffgame):
        isplayoffgsql = "1"
    if (isplayoffgame == False):
        isplayoffsql = "0"
    periodssplit = periodsscore.split(",")
    periodcounting = 0
    numberofperiods = int(len(periodssplit))
    homescore = 0
    awayscore = 0
    homeperiodscore = ""
    awayperiodscore = ""
    while (periodcounting < numberofperiods):
        periodscoresplit = periodssplit[periodcounting].split(":")
        homeperiodscore = homeperiodscore + " " + str(periodscoresplit[0])
        awayperiodscore = awayperiodscore + " " + str(periodscoresplit[1])
        if (periodcounting <= 3):
            homescore = homescore + int(periodscoresplit[0])
            awayscore = awayscore + int(periodscoresplit[1])
        if (isplayoffgame and periodcounting > 3):
            homescore = homescore + int(periodscoresplit[0])
            awayscore = awayscore + int(periodscoresplit[1])
        if (isplayoffgame == False and periodcounting > 3):
            if (periodscoresplit[0] > periodscoresplit[1]):
                homescore = homescore + 1
            if (periodscoresplit[0] < periodscoresplit[1]):
                awayscore = awayscore + 1
        periodcounting = periodcounting + 1
    totalscore = str(homescore) + ":" + str(awayscore)
    teamscores = totalscore.split(":")
    shotsongoalsplit = shotsongoal.split(",")
    periodssplits = periodsscore.split(",")
    numberofsogperiods = int(len(shotsongoalsplit))
    periodsogcounting = 0
    homesog = 0
    awaysog = 0
    hometsb = 0
    awaytsb = 0
    sbstr = ""
    homeperiodsog = ""
    awayperiodsog = ""
    while (periodsogcounting < numberofsogperiods):
        periodsogsplit = shotsongoalsplit[periodsogcounting].split(":")
        periodscoresplit = periodssplits[periodsogcounting].split(":")
        homesog = homesog + int(periodsogsplit[0])
        homesb = int(periodsogsplit[0]) - int(periodscoresplit[0])
        hometsb = homesb + hometsb
        awaysog = awaysog + int(periodsogsplit[1])
        awaysb = int(periodsogsplit[1]) - int(periodscoresplit[1])
        awaytsb = awaysb + awaytsb
        sbstr = sbstr + str(homesb) + ":" + str(awaysb) + " "
        periodsogcounting = periodsogcounting + 1
    sbstr = sbstr.rstrip()
    sbstr = sbstr.replace(" ", ",")
    tsbstr = str(hometsb) + ":" + str(awaytsb)
    totalsog = str(homesog) + ":" + str(awaysog)
    teamssog = totalsog.split(":")
    hometeamname = hometeam
    hometeam = GetTeam2Num(sqldatacon, hometeam)
    awayteamname = awayteam
    awayteam = GetTeam2Num(sqldatacon, awayteam)
    if (atarena == 0):
        atarena = hometeam
        atarenaname = GetTeamData(sqldatacon, hometeam, "FullArenaName", "str")
    if (isinstance(atarena, int) and atarena > 0):
        atarenaname = GetNum2Arena(sqldatacon, atarena, "FullArenaName")
    if (isinstance(atarena, str)):
        atarenaname = atarena
        atarena = GetArena2Num(sqldatacon, atarenaname)
    print("Home Arena: " + str(atarenaname))
    print("Home Team: " + GetNum2Team(sqldatacon, int(hometeam), "FullName"))
    print("Home Period Scores:" + homeperiodscore)
    print("Home Score: " + str(teamscores[0]))
    print("Away Team: " + GetNum2Team(sqldatacon, int(awayteam), "FullName"))
    print("Away Period Scores:" + awayperiodscore)
    print("Away Score: " + str(teamscores[1]))
    print("Number Of Periods: " + str(numberofperiods))
    if (teamscores[0] > teamscores[1]):
        print(
            "Winning Team: " +
            GetNum2Team(
                sqldatacon,
                int(hometeam),
                "FullName"))
        print(
            "Losing Team: " +
            GetNum2Team(
                sqldatacon,
                int(awayteam),
                "FullName"))
        losingteam = awayteam
        winningteam = hometeam
        winningteamname = hometeamname
        losingteamname = awayteamname
    if (teamscores[0] < teamscores[1]):
        print(
            "Winning Team: " +
            GetNum2Team(
                sqldatacon,
                int(awayteam),
                "FullName"))
        print(
            "Losing Team: " +
            GetNum2Team(
                sqldatacon,
                int(hometeam),
                "FullName"))
        losingteam = hometeam
        winningteam = awayteam
        winningteamname = awayteamname
        losingteamname = hometeamname
    print(" ")
    sqldatacon[0].execute(
        "INSERT INTO " +
        leaguename +
        "Games(Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, NumberPeriods, TeamWin, IsPlayOffGame) VALUES(" +
        str(date) +
        ", \"" +
        str(hometeamname) +
        "\", \"" +
        str(awayteamname) +
        "\", \"" +
        str(atarenaname) +
        "\", \"" +
        str(periodsscore) +
        "\", \"" +
        str(totalscore) +
        "\", \"" +
        str(shotsongoal) +
        "\", \"" +
        str(totalsog) +
        "\", \"" +
        str(sbstr) +
        "\", \"" +
        str(tsbstr) +
        "\", " +
        str(numberofperiods) +
        ", \"" +
        str(winningteamname) +
        "\", " +
        str(isplayoffgsql) +
        ")")
    UpdateArenaData(sqldatacon, atarena, "GamesPlayed", 1, "+")
    UpdateTeamData(sqldatacon, hometeam, "Date", int(date), "=")
    UpdateTeamData(sqldatacon, hometeam, "GamesPlayed", 1, "+")
    UpdateTeamData(sqldatacon, hometeam, "GamesPlayedHome", 1, "+")
    UpdateTeamData(sqldatacon, hometeam, "GoalsFor", int(teamscores[0]), "+")
    UpdateTeamData(sqldatacon, hometeam, "GoalsAgainst",
                   int(teamscores[1]), "+")
    UpdateTeamData(sqldatacon, hometeam, "GoalsDifference",
                   int(int(teamscores[0]) - int(teamscores[1])), "+")
    UpdateTeamData(sqldatacon, hometeam, "SOGFor", int(teamssog[0]), "+")
    UpdateTeamData(sqldatacon, hometeam, "SOGAgainst", int(teamssog[1]), "+")
    UpdateTeamData(sqldatacon, hometeam, "SOGDifference",
                   int(int(teamssog[0]) - int(teamssog[1])), "+")
    UpdateTeamData(sqldatacon, hometeam, "ShotsBlockedFor", int(hometsb), "+")
    UpdateTeamData(sqldatacon, hometeam,
                   "ShotsBlockedAgainst", int(awaytsb), "+")
    UpdateTeamData(sqldatacon, hometeam, "ShotsBlockedDifference",
                   int(int(hometsb) - int(awaytsb)), "+")
    UpdateTeamData(sqldatacon, awayteam, "Date", int(date), "=")
    UpdateTeamData(sqldatacon, awayteam, "GamesPlayed", 1, "+")
    UpdateTeamData(sqldatacon, awayteam, "GamesPlayedAway", 1, "+")
    UpdateTeamData(sqldatacon, awayteam, "GoalsFor", int(teamscores[1]), "+")
    UpdateTeamData(sqldatacon, awayteam, "GoalsAgainst",
                   int(teamscores[0]), "+")
    UpdateTeamData(sqldatacon, awayteam, "GoalsDifference",
                   int(int(teamscores[1]) - int(teamscores[0])), "+")
    UpdateTeamData(sqldatacon, awayteam, "SOGFor", int(teamssog[1]), "+")
    UpdateTeamData(sqldatacon, awayteam, "SOGAgainst", int(teamssog[0]), "+")
    UpdateTeamData(sqldatacon, awayteam, "SOGDifference",
                   int(int(teamssog[1]) - int(teamssog[0])), "+")
    UpdateTeamData(sqldatacon, awayteam, "ShotsBlockedFor", int(awaytsb), "+")
    UpdateTeamData(sqldatacon, awayteam,
                   "ShotsBlockedAgainst", int(hometsb), "+")
    UpdateTeamData(sqldatacon, awayteam, "ShotsBlockedDifference",
                   int(int(awaytsb) - int(hometsb)), "+")
    if (winningteam == hometeam and int(teamscores[1]) == 0):
        UpdateTeamData(sqldatacon, hometeam, "ShutoutWins", 1, "+")
        UpdateTeamData(sqldatacon, awayteam, "ShutoutLosses", 1, "+")
    if (winningteam == awayteam and int(teamscores[0]) == 0):
        UpdateTeamData(sqldatacon, awayteam, "ShutoutWins", 1, "+")
        UpdateTeamData(sqldatacon, hometeam, "ShutoutLosses", 1, "+")
    UpdateTeamDataString(sqldatacon, winningteam, "LastTen",
                         GetLastTenGames(sqldatacon, winningteamname))
    UpdateTeamDataString(sqldatacon, losingteam, "LastTen",
                         GetLastTenGames(sqldatacon, losingteamname))
    GetWinningStreak = GetTeamData(sqldatacon, winningteam, "Streak", "str")
    GetWinningStreakNext = "Won 1"
    if (GetWinningStreak != "None"):
        GetWinningStreakSplit = re.findall(
            "([a-zA-Z]+) ([0-9]+)", GetWinningStreak)
        if (GetWinningStreakSplit[0][0] == "Won"):
            GetWinningStreakNext = "Won " + \
                str(int(GetWinningStreakSplit[0][1]) + 1)
        if (GetWinningStreakSplit[0][0] == "Lost"):
            GetWinningStreakNext = "Won 1"
        if (GetWinningStreakSplit[0][0] == "OT"):
            GetWinningStreakNext = "Won 1"
    UpdateTeamDataString(sqldatacon, winningteam,
                         "Streak", GetWinningStreakNext)
    GetLosingStreak = GetTeamData(sqldatacon, losingteam, "Streak", "str")
    if (numberofperiods == 3):
        GetLosingStreakNext = "Lost 1"
    if (numberofperiods > 3):
        GetLosingStreakNext = "OT 1"
    if (GetLosingStreak != "None"):
        GetLosingStreakSplit = re.findall(
            "([a-zA-Z]+) ([0-9]+)", GetLosingStreak)
        if (GetLosingStreakSplit[0][0] == "Won"):
            if (numberofperiods == 3):
                GetLosingStreakNext = "Lost 1"
            if (numberofperiods > 3):
                GetLosingStreakNext = "OT 1"
        if (GetLosingStreakSplit[0][0] == "Lost"):
            if (numberofperiods == 3):
                GetLosingStreakNext = "Lost " + \
                    str(int(GetLosingStreakSplit[0][1]) + 1)
            if (numberofperiods > 3):
                GetLosingStreakNext = "OT 1"
        if (GetLosingStreakSplit[0][0] == "OS"):
            if (numberofperiods == 3):
                GetLosingStreakNext = "Lost 1"
            if (numberofperiods > 3):
                GetLosingStreakNext = "OT " + \
                    str(int(GetLosingStreakSplit[0][1]) + 1)
    UpdateTeamDataString(sqldatacon, losingteam, "Streak", GetLosingStreakNext)
    if ((isplayoffgame == False and numberofperiods < 5) or (isplayoffgame)):
        UpdateTeamData(sqldatacon, winningteam, "ROW", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "ROT", 1, "+")
    if (numberofperiods == 3):
        UpdateTeamData(sqldatacon, winningteam, "Wins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "TWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "Points", 2, "+")
        UpdateTeamData(sqldatacon, losingteam, "Losses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "TLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "Points", 0, "+")
        if (winningteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "HomeRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1) + ":" + \
                str(HTRSpit[1]) + ":" + str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "AwayRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0]) + ":" + \
                str(ATRSpit[1] + 1) + ":" + str(ATRSpit[2])
            UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR)
        if (losingteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "AwayRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1) + ":" + \
                str(HTRSpit[1]) + ":" + str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "HomeRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0]) + ":" + \
                str(ATRSpit[1] + 1) + ":" + str(ATRSpit[2])
            UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR)
    if (numberofperiods > 3):
        if ((numberofperiods == 4 and isplayoffgame == False)
                or (numberofperiods > 4 and isplayoffgame)):
            UpdateTeamData(sqldatacon, winningteam, "OTWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "OTSOWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "TWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "Points", 2, "+")
        if ((numberofperiods == 4 and isplayoffgame == False)
                or (numberofperiods > 4 and isplayoffgame)):
            UpdateTeamData(sqldatacon, losingteam, "OTLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "OTSOLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "TLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "Points", 1, "+")
        if (winningteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "HomeRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1) + ":" + \
                str(HTRSpit[1]) + ":" + str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "AwayRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0]) + ":" + str(ATRSpit[1]) + \
                ":" + str(ATRSpit[2] + 1)
            UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR)
        if (losingteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "AwayRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1) + ":" + \
                str(HTRSpit[1]) + ":" + str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "HomeRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0]) + ":" + str(ATRSpit[1]) + \
                ":" + str(ATRSpit[2] + 1)
            UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR)
    if (isplayoffgame == False and numberofperiods > 4):
        UpdateTeamData(sqldatacon, winningteam, "SOWins", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "SOLosses", 1, "+")
        WinningTeamShootouts = GetTeamData(
            sqldatacon, winningteam, "Shootouts", "str")
        WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")]
        NewWTSo = str(WTSoSplit[0] + 1) + ":" + str(WTSoSplit[1])
        UpdateTeamDataString(sqldatacon, winningteam, "Shootouts", NewWTSo)
        LosingTeamShootouts = GetTeamData(
            sqldatacon, losingteam, "Shootouts", "str")
        LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")]
        NewLTSo = str(LTSoSplit[0]) + ":" + str(LTSoSplit[1] + 1)
        UpdateTeamDataString(sqldatacon, losingteam, "Shootouts", NewLTSo)
    HomeOTLossesPCT = float(
        "%.2f" %
        float(
            float(0.5) *
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    hometeam,
                    "OTSOLosses",
                    "float"))))
    HomeWinsPCT = float(
        "%.3f" %
        float(
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    hometeam,
                    "TWins",
                    "float") +
                HomeOTLossesPCT) /
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    hometeam,
                    "GamesPlayed",
                    "float"))))
    AwayOTLossesPCT = float(
        "%.2f" %
        float(
            float(0.5) *
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    awayteam,
                    "OTSOLosses",
                    "float"))))
    AwayWinsPCT = float(
        "%.3f" %
        float(
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    awayteam,
                    "TWins",
                    "float") +
                AwayOTLossesPCT) /
            float(
                GetTeamData(
                    (sqlcur,
                     sqlcon),
                    awayteam,
                    "GamesPlayed",
                    "float"))))
    UpdateTeamData(sqldatacon, hometeam, "PCT", HomeWinsPCT, "=")
    UpdateTeamData(sqldatacon, awayteam, "PCT", AwayWinsPCT, "=")
    sqldatacon[1].commit()
    sqldatacon[0].execute("INSERT INTO " + leaguename + "Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM " + leaguename + "Teams WHERE FullName=\"" + hometeamname + "\";")
    sqldatacon[0].execute("INSERT INTO " + leaguename + "Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM " + leaguename + "Teams WHERE FullName=\"" + awayteamname + "\";")
    sqldatacon[1].commit()
    return True


print("Inserting " + leaguename + " Game Data From 10/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Indy Fuel",
               "Fort Wayne Komets", "2:0,0:1,1:0", "16:9,10:10,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Cincinnati Cyclones",
               "Wheeling Nailers", "0:1,2:0,4:0", "9:6,8:5,18:7", 0, False)

print("Inserting " + leaguename + " Game Data From 10/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Elmira Jackals",
               "Reading Royals", "1:1,3:1,1:0", "8:12,8:10,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "South Carolina Stingrays",
               "Greenville Swamp Rabbits", "0:1,0:2,0:2", "6:7,7:9,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Toledo Walleye",
               "Kalamazoo Wings", "1:0,2:0,0:0", "9:8,12:9,12:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151009,
               "Florida Everblades",
               "Orlando Solar Bears",
               "1:0,1:0,0:2,1:0",
               "15:6,11:8,9:13,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Wheeling Nailers",
               "Cincinnati Cyclones", "2:1,0:3,0:0", "6:9,11:9,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Fort Wayne Komets",
               "Evansville IceMen", "2:2,2:2,2:1", "15:11,13:10,14:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Colorado Eagles",
               "Rapid City Rush", "1:0,0:0,2:0", "13:7,9:5,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Idaho Steelheads",
               "Utah Grizzlies", "3:2,1:0,3:1", "7:6,10:10,8:7", 0, False)

print("Inserting " + leaguename + " Game Data From 10/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Wichita Thunder",
               "Allen Americans", "4:1,1:1,2:0", "12:15,6:10,15:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151010,
               "Adirondack Thunder",
               "Manchester Monarchs",
               "0:1,4:2,0:1,0:1",
               "13:9,12:6,5:11,1:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151010,
               "Florida Everblades",
               "Orlando Solar Bears",
               "1:0,0:2,1:0,0:1",
               "8:8,8:13,13:7,1:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Kalamazoo Wings",
               "Toledo Walleye", "0:1,1:1,0:0", "6:9,8:6,15:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Reading Royals",
               "Norfolk Admirals", "1:2,3:1,1:1", "12:15,9:13,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "South Carolina Stingrays",
               "Atlanta Gladiators", "0:1,0:3,0:0", "4:8,8:13,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Fort Wayne Komets",
               "Evansville IceMen", "2:1,1:0,3:1", "10:10,7:10,20:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Utah Grizzlies",
               "Idaho Steelheads", "1:3,1:0,1:1", "12:14,17:8,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Rapid City Rush",
               "Colorado Eagles", "0:2,1:1,2:2", "10:9,6:15,7:5", 0, False)

print("Inserting " + leaguename + " Game Data From 10/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Indy Fuel",
               "Quad City Mallards", "1:0,1:0,1:0", "11:7,7:6,7:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151011,
               "Manchester Monarchs",
               "Adirondack Thunder",
               "1:0,1:2,0:0,0:1",
               "11:9,5:7,8:7,1:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Atlanta Gladiators",
               "Greenville Swamp Rabbits", "0:2,2:1,2:2", "5:8,14:8,7:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151012, "Alaska Aces",
               "Missouri Mavericks", "1:1,1:2,0:2", "7:9,9:14,10:7", 0, False)

print("Inserting " + leaguename + " Game Data From 10/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Alaska Aces",
               "Missouri Mavericks", "0:1,1:0,2:0", "9:12,11:5,8:9", 0, False)

print("Inserting " + leaguename + " Game Data From 10/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Manchester Monarchs",
               "Brampton Beast", "0:0,0:1,2:0", "10:8,12:5,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Elmira Jackals",
               "Adirondack Thunder", "0:1,0:1,1:2", "10:6,8:12,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Kalamazoo Wings",
               "Fort Wayne Komets", "0:1,2:1,1:3", "10:8,18:10,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Norfolk Admirals",
               "Wheeling Nailers", "0:0,0:1,0:2", "10:9,6:20,7:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151016,
               "Florida Everblades",
               "Atlanta Gladiators",
               "3:1,0:0,0:2,1:0",
               "10:9,7:10,13:12,1:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Indy Fuel", "Toledo Walleye",
               "2:2,0:0,0:0,0:0,1:0", "8:7,4:11,10:11,1:2,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Tulsa Oilers",
               "Wichita Thunder", "0:0,0:2,2:1", "9:4,3:13,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Allen Americans",
               "Quad City Mallards", "0:1,0:1,1:0", "11:9,12:12,11:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151016,
               "Colorado Eagles",
               "Utah Grizzlies",
               "1:0,0:2,2:1,0:1",
               "6:10,13:8,17:10,5:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Idaho Steelheads",
               "Rapid City Rush", "1:0,1:0,3:1", "10:7,6:11,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Alaska Aces",
               "Missouri Mavericks", "1:0,1:0,1:1", "12:13,7:16,10:11", 0, False)

print("Inserting " + leaguename + " Game Data From 10/17/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151017,
               "Orlando Solar Bears",
               "Greenville Swamp Rabbits",
               "2:1,1:0,3:2",
               "7:9,13:7,10:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Florida Everblades",
               "Atlanta Gladiators", "3:1,3:0,0:0", "20:7,8:11,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Elmira Jackals",
               "Brampton Beast", "2:0,1:1,1:1", "17:4,7:10,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "South Carolina Stingrays",
               "Reading Royals", "1:0,1:0,0:1", "5:9,8:8,12:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Norfolk Admirals",
               "Wheeling Nailers", "3:0,0:0,1:2", "11:9,5:19,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Fort Wayne Komets",
               "Kalamazoo Wings", "2:1,0:0,1:0", "12:5,15:9,14:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Cincinnati Cyclones",
               "Toledo Walleye", "1:0,1:0,3:1", "12:8,11:8,8:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151017,
               "Wichita Thunder",
               "Quad City Mallards",
               "1:1,2:2,1:1,0:0,1:0",
               "11:6,6:11,4:11,3:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Allen Americans",
               "Tulsa Oilers", "1:1,1:0,2:1", "10:4,8:16,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Evansville IceMen",
               "Indy Fuel", "0:0,0:1,1:2", "9:11,10:8,15:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Colorado Eagles",
               "Utah Grizzlies", "1:1,1:2,0:2", "12:11,17:4,6:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151017,
               "Idaho Steelheads",
               "Rapid City Rush",
               "4:1,0:1,0:2,0:1",
               "14:12,6:8,7:10,2:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Alaska Aces",
               "Missouri Mavericks", "0:2,0:1,0:0", "10:13,11:10,4:7", 0, False)

print("Inserting " + leaguename + " Game Data From 10/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151018, "South Carolina Stingrays",
               "Reading Royals", "0:3,0:1,0:2", "11:17,6:6,3:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Tulsa Oilers",
               "Allen Americans", "1:1,1:0,1:0", "10:13,10:10,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Alaska Aces",
               "Missouri Mavericks", "0:0,0:2,1:1", "11:9,7:7,11:15", 0, False)

print("Inserting " + leaguename + " Game Data From 10/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Florida Everblades",
               "Norfolk Admirals", "0:0,3:1,3:0", "8:6,12:11,17:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Colorado Eagles",
               "Allen Americans", "0:0,1:0,0:3", "6:5,15:6,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Alaska Aces", "Idaho Steelheads",
               "1:2,0:0,2:1,0:0,0:1", "13:14,7:15,17:8,1:2,0:1", 0, False)

print("Inserting " + leaguename + " Game Data From 10/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Orlando Solar Bears",
               "Norfolk Admirals", "3:2,0:1,3:0", "11:14,14:13,13:16", 0, False)

print("Inserting " + leaguename + " Game Data From 10/23/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Greenville Swamp Rabbits",
               "South Carolina Stingrays", "3:1,0:1,2:1", "11:8,4:10,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Elmira Jackals",
               "Reading Royals", "1:1,0:2,0:2", "4:12,8:11,9:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151023,
               "Brampton Beast",
               "Adirondack Thunder",
               "2:2,1:2,1:0,0:1",
               "6:12,6:16,10:7,0:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Kalamazoo Wings",
               "Toledo Walleye", "1:2,0:1,1:2", "4:14,8:11,8:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Atlanta Gladiators",
               "Florida Everblades", "2:1,0:0,2:1", "14:8,8:6,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Fort Wayne Komets",
               "Indy Fuel", "0:0,0:0,3:0", "8:7,11:8,10:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Wichita Thunder",
               "Missouri Mavericks", "0:0,0:0,0:3", "6:9,12:10,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Quad City Mallards",
               "Tulsa Oilers", "0:0,0:1,0:0", "8:7,5:8,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Utah Grizzlies",
               "Allen Americans", "1:1,0:1,1:2", "9:10,6:5,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Rapid City Rush",
               "Colorado Eagles", "0:0,1:1,2:1", "12:12,12:10,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Alaska Aces",
               "Idaho Steelheads", "0:1,3:0,1:0", "8:13,25:3,10:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/24/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Reading Royals",
               "Elmira Jackals", "1:2,1:3,0:2", "7:8,12:7,4:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Adirondack Thunder",
               "Manchester Monarchs", "1:0,1:1,2:1", "10:8,4:14,10:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Orlando Solar Bears",
               "Norfolk Admirals", "1:0,1:1,4:2", "12:13,8:8,13:20", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Atlanta Gladiators",
               "Florida Everblades", "0:1,0:1,1:2", "7:12,9:14,4:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151024,
               "South Carolina Stingrays",
               "Greenville Swamp Rabbits",
               "0:0,1:1,1:1,0:1",
               "11:5,6:8,8:6,1:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Fort Wayne Komets",
               "Indy Fuel", "1:2,3:2,1:1,1:0", "13:11,17:8,19:8,4:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Cincinnati Cyclones",
               "Kalamazoo Wings", "0:0,2:1,2:0", "9:8,16:5,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Wheeling Nailers",
               "Brampton Beast", "1:0,3:1,1:0", "6:6,13:8,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Missouri Mavericks",
               "Wichita Thunder", "0:1,2:0,0:0", "9:4,11:3,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Quad City Mallards",
               "Tulsa Oilers", "1:1,2:1,2:1", "10:5,17:9,10:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Evansville IceMen",
               "Toledo Walleye", "0:1,0:1,1:0", "11:5,9:16,19:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151024,
               "Utah Grizzlies",
               "Allen Americans",
               "1:2,2:2,2:1,0:1",
               "14:16,15:15,14:6,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Colorado Eagles",
               "Rapid City Rush", "0:0,1:1,1:2", "6:5,16:7,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Alaska Aces",
               "Idaho Steelheads", "1:0,2:1,2:3", "11:6,16:16,13:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/25/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Brampton Beast",
               "Wheeling Nailers", "0:2,2:1,1:1", "7:10,10:17,16:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Manchester Monarchs",
               "Adirondack Thunder", "1:0,0:2,1:3", "8:6,14:12,17:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Greenville Swamp Rabbits",
               "Florida Everblades", "0:2,2:0,1:0", "8:7,8:10,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "South Carolina Stingrays",
               "Atlanta Gladiators", "0:2,0:0,3:3", "11:9,10:8,14:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Quad City Mallards",
               "Wichita Thunder", "2:1,1:1,2:0", "11:11,13:8,7:14", 0, False)

print("Inserting " + leaguename + " Game Data From 10/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Kalamazoo Wings",
               "Indy Fuel", "1:0,3:1,0:2", "15:20,13:14,6:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Missouri Mavericks",
               "Quad City Mallards", "0:0,3:1,2:1", "8:8,9:12,9:7", 0, False)

print("Inserting " + leaguename + " Game Data From 10/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Adirondack Thunder",
               "Orlando Solar Bears", "1:1,1:1,2:0", "5:10,13:7,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Reading Royals",
               "Elmira Jackals", "3:1,2:2,3:0", "11:3,7:7,9:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151028,
               "Florida Everblades",
               "South Carolina Stingrays",
               "1:0,0:3,1:1",
               "7:7,11:13,11:5",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Colorado Eagles",
               "Rapid City Rush", "2:0,1:0,1:0", "8:5,7:6,8:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Kalamazoo Wings",
               "Cincinnati Cyclones", "1:0,1:1,1:0", "10:8,13:9,4:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Greenville Swamp Rabbits",
               "Atlanta Gladiators", "1:1,0:2,1:0", "12:12,10:16,12:16", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151030,
               "Elmira Jackals",
               "Orlando Solar Bears",
               "0:1,1:2,2:0,1:0",
               "9:11,14:14,18:7,1:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Brampton Beast",
               "Toledo Walleye", "0:0,1:2,0:2", "13:12,12:11,11:4", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151030,
               "Norfolk Admirals",
               "Quad City Mallards",
               "1:0,1:0,0:2,0:0,1:0",
               "14:8,14:9,7:18,4:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Florida Everblades",
               "South Carolina Stingrays", "0:0,0:0,2:0", "4:7,7:10,6:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Indy Fuel",
               "Fort Wayne Komets", "2:1,2:1,0:0", "10:10,13:13,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Wheeling Nailers",
               "Adirondack Thunder", "1:2,0:1,0:1", "11:12,10:7,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Wichita Thunder",
               "Colorado Eagles", "3:1,1:0,1:1", "12:7,6:9,5:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151030,
               "Tulsa Oilers",
               "Missouri Mavericks",
               "1:0,1:2,1:1,0:0,1:0",
               "10:7,6:9,8:11,3:5,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Rapid City Rush",
               "Alaska Aces", "0:1,1:2,0:1", "9:16,9:5,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Idaho Steelheads",
               "Utah Grizzlies", "0:1,0:2,1:1", "16:6,15:7,17:2", 0, False)

print("Inserting " + leaguename + " Game Data From 10/31/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Wichita Thunder",
               "Colorado Eagles", "1:1,1:0,0:0", "4:18,7:7,3:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Greenville Swamp Rabbits",
               "Evansville IceMen", "2:0,0:0,0:3", "17:8,13:18,14:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Utah Grizzlies",
               "Idaho Steelheads", "0:1,0:2,1:0", "14:14,10:10,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Rapid City Rush",
               "Alaska Aces", "0:0,3:1,2:0", "8:8,14:11,15:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Reading Royals",
               "Orlando Solar Bears", "0:1,0:2,2:2", "11:9,12:4,13:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Elmira Jackals",
               "Manchester Monarchs", "0:1,0:2,2:1", "8:17,15:12,17:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Fort Wayne Komets",
               "Cincinnati Cyclones", "1:3,0:2,0:0", "14:9,12:7,11:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Wheeling Nailers",
               "Quad City Mallards", "2:0,0:1,0:0", "12:6,15:10,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Allen Americans",
               "Missouri Mavericks", "0:0,1:0,1:1", "8:6,11:10,9:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/1/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Brampton Beast",
               "Toledo Walleye", "0:1,2:1,3:0", "8:9,8:9,15:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Greenville Swamp Rabbits",
               "Florida Everblades", "0:2,0:3,0:2", "12:13,10:10,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "South Carolina Stingrays",
               "Evansville IceMen", "2:0,1:1,2:1", "8:4,11:8,8:13", 0, False)

print("Inserting " + leaguename + " Game Data From 11/2/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151102, "Utah Grizzlies",
               "Idaho Steelheads", "1:0,0:0,0:2", "17:9,19:12,12:6", 0, False)

print("Inserting " + leaguename + " Game Data From 11/3/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151103, "South Carolina Stingrays",
               "Florida Everblades", "0:0,1:0,1:0", "5:11,10:5,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Tulsa Oilers",
               "Allen Americans", "2:0,1:1,0:0", "10:3,5:7,5:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Evansville IceMen",
               "Indy Fuel", "0:1,0:1,0:1", "5:7,10:8,7:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151104,
               "Kalamazoo Wings",
               "Adirondack Thunder",
               "1:0,0:0,1:2,0:1",
               "11:10,9:12,7:8,0:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151104,
               "Quad City Mallards",
               "Missouri Mavericks",
               "2:1,0:2,1:0,0:1",
               "10:9,9:15,11:10,0:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151104,
               "Cincinnati Cyclones",
               "Toledo Walleye",
               "0:0,0:1,1:0,0:0,0:1",
               "10:7,6:10,11:10,4:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Idaho Steelheads",
               "Atlanta Gladiators", "2:3,2:0,0:2", "12:10,11:11,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Alaska Aces",
               "Utah Grizzlies", "1:2,1:1,0:1", "10:15,5:7,15:9", 0, False)

print("Inserting " + leaguename + " Game Data From 11/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151106, "South Carolina Stingrays",
               "Elmira Jackals", "0:1,0:1,0:0", "11:7,8:7,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Brampton Beast",
               "Manchester Monarchs", "1:2,1:0,2:0", "8:11,19:9,5:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151106,
               "Norfolk Admirals",
               "Greenville Swamp Rabbits",
               "2:0,0:2,2:0",
               "12:11,9:9,12:5",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Cincinnati Cyclones",
               "Adirondack Thunder", "2:1,0:0,2:1", "12:11,9:11,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Wheeling Nailers",
               "Kalamazoo Wings", "1:1,1:1,1:2", "12:8,17:11,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Fort Wayne Komets",
               "Toledo Walleye", "1:0,1:0,2:1", "12:5,14:10,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Quad City Mallards",
               "Wichita Thunder", "2:2,0:0,2:0", "8:5,4:14,12:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Evansville IceMen",
               "Indy Fuel", "1:2,2:0,1:0", "9:13,12:13,6:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Colorado Eagles",
               "Tulsa Oilers", "1:1,0:0,2:0", "16:2,10:5,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Rapid City Rush",
               "Allen Americans", "0:1,1:1,0:2", "8:9,8:8,9:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151106,
               "Idaho Steelheads",
               "Atlanta Gladiators",
               "2:2,1:1,1:1,0:1",
               "10:17,5:7,13:5,3:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Alaska Aces",
               "Utah Grizzlies", "0:0,0:1,1:3", "5:9,15:13,8:8", 0, False)

print("Inserting " + leaguename + " Game Data From 11/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Orlando Solar Bears",
               "Florida Everblades", "1:2,1:1,0:0", "9:14,9:11,10:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151107,
               "Reading Royals",
               "Greenville Swamp Rabbits",
               "1:0,4:1,0:0",
               "11:12,13:10,5:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "South Carolina Stingrays",
               "Elmira Jackals", "2:0,1:1,1:0", "10:3,16:13,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Brampton Beast",
               "Manchester Monarchs", "0:2,1:1,0:2", "7:19,7:9,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Toledo Walleye",
               "Adirondack Thunder", "0:1,0:0,0:0", "8:5,15:7,8:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Norfolk Admirals",
               "Wheeling Nailers", "3:2,1:0,2:0", "13:12,9:14,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Fort Wayne Komets",
               "Kalamazoo Wings", "2:1,1:2,1:3", "15:12,17:8,18:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Indy Fuel",
               "Quad City Mallards", "2:0,2:2,1:0", "8:9,12:4,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Cincinnati Cyclones",
               "Evansville IceMen", "0:0,0:0,2:1", "10:10,11:9,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Missouri Mavericks",
               "Wichita Thunder", "1:0,0:0,0:0", "4:6,10:13,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Colorado Eagles",
               "Tulsa Oilers", "1:0,0:1,1:0", "11:5,10:7,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Rapid City Rush",
               "Allen Americans", "0:2,2:2,0:3", "6:20,14:11,3:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Idaho Steelheads",
               "Atlanta Gladiators", "0:1,0:1,1:1", "5:10,16:5,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Alaska Aces",
               "Utah Grizzlies", "1:0,1:0,0:3", "11:13,17:10,8:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Brampton Beast",
               "Manchester Monarchs", "2:1,0:0,2:1", "12:10,16:11,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "South Carolina Stingrays",
               "Norfolk Admirals", "1:0,2:0,0:1", "17:6,15:6,2:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Kalamazoo Wings",
               "Fort Wayne Komets", "0:2,0:1,2:2", "10:10,6:8,18:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151108,
               "Reading Royals",
               "Greenville Swamp Rabbits",
               "2:0,0:0,3:0",
               "14:9,7:6,7:15",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Orlando Solar Bears",
               "Florida Everblades", "0:2,1:1,0:0", "16:19,15:9,11:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Wichita Thunder",
               "Missouri Mavericks", "0:1,1:1,0:0", "6:12,9:21,8:13", 0, False)

print("Inserting " + leaguename + " Game Data From 11/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Wheeling Nailers",
               "Cincinnati Cyclones", "1:2,1:1,5:2", "10:10,18:7,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Kalamazoo Wings",
               "Manchester Monarchs", "2:3,0:3,1:1", "7:14,4:7,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Atlanta Gladiators",
               "Florida Everblades", "0:3,1:2,1:3", "6:14,11:9,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Norfolk Admirals",
               "Elmira Jackals", "1:1,0:1,2:2", "19:11,9:14,4:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Allen Americans",
               "Wichita Thunder", "1:1,2:0,2:1", "9:9,12:5,11:9", 0, False)

print("Inserting " + leaguename + " Game Data From 11/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Reading Royals",
               "Wheeling Nailers", "1:1,1:0,0:0", "10:7,10:4,4:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Quad City Mallards",
               "Alaska Aces", "2:1,2:2,3:1", "12:10,12:14,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Cincinnati Cyclones",
               "Fort Wayne Komets", "2:0,1:0,0:1", "10:16,10:7,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Wichita Thunder", "Tulsa Oilers",
               "0:1,1:0,0:0,0:0,1:0", "6:12,12:9,10:10,3:0,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Utah Grizzlies",
               "Colorado Eagles", "1:1,1:1,2:0", "15:10,14:11,11:8", 0, False)

print("Inserting " + leaguename + " Game Data From 11/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Greenville Swamp Rabbits",
               "Atlanta Gladiators", "2:0,1:1,3:2", "14:9,9:12,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Orlando Solar Bears",
               "Idaho Steelheads", "0:1,2:0,3:3", "12:13,11:11,7:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Kalamazoo Wings",
               "Evansville IceMen", "0:0,2:0,2:2", "7:14,13:9,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Manchester Monarchs",
               "Toledo Walleye", "2:1,0:2,3:1", "9:11,18:11,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Elmira Jackals",
               "Norfolk Admirals", "0:2,0:0,1:2", "9:8,13:3,15:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "South Carolina Stingrays",
               "Orlando Solar Bears",
               "1:0,0:0,0:1,0:0,1:0",
               "9:4,7:8,13:9,5:1,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Florida Everblades",
               "Idaho Steelheads", "0:2,3:1,0:0,1:0", "6:11,9:6,14:4,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Indy Fuel",
               "Alaska Aces", "1:2,2:0,0:0", "10:12,12:13,4:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Cincinnati Cyclones",
               "Quad City Mallards", "2:0,0:0,1:1", "12:8,10:11,6:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Wheeling Nailers",
               "Reading Royals", "3:1,2:0,1:0", "12:8,12:11,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Atlanta Gladiators",
               "Adirondack Thunder", "1:2,0:1,0:1", "5:10,13:2,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Wichita Thunder",
               "Missouri Mavericks", "1:5,0:1,1:1", "5:21,5:11,10:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Tulsa Oilers",
               "Allen Americans", "0:1,1:1,1:1", "7:9,16:9,7:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "Utah Grizzlies",
               "Rapid City Rush",
               "1:1,3:0,0:3,1:0",
               "16:3,11:9,11:9,2:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 11/14/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "Kalamazoo Wings",
               "Cincinnati Cyclones",
               "1:0,0:0,0:1,1:0",
               "7:13,5:14,13:11,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Reading Royals",
               "Norfolk Admirals", "0:0,1:2,2:0", "20:8,9:8,17:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Manchester Monarchs",
               "Toledo Walleye", "2:2,0:3,0:1", "13:12,13:17,12:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Greenville Swamp Rabbits",
               "Adirondack Thunder", "1:1,0:0,2:1", "10:10,8:7,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Florida Everblades",
               "Idaho Steelheads", "0:0,2:0,1:0", "12:6,9:4,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Elmira Jackals",
               "Brampton Beast", "0:0,1:2,0:2", "9:10,8:8,5:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "South Carolina Stingrays",
               "Orlando Solar Bears",
               "1:0,0:1,0:0,0:0,0:1",
               "6:7,12:8,6:6,6:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Indy Fuel", "Alaska Aces",
               "1:1,1:0,0:1,0:0,1:0", "11:5,14:10,4:10,4:4,1:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "Wheeling Nailers",
               "Evansville IceMen",
               "0:1,0:0,1:0,0:1",
               "10:8,9:7,10:8,3:3",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "Wichita Thunder",
               "Missouri Mavericks",
               "1:0,1:1,0:1,0:0,0:1",
               "6:10,5:9,9:6,1:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Allen Americans",
               "Colorado Eagles", "0:1,0:3,1:4", "10:15,4:15,16:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Utah Grizzlies",
               "Rapid City Rush", "0:1,0:0,0:1", "6:9,8:2,22:5", 0, False)

print("Inserting " + leaguename + " Game Data From 11/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Brampton Beast",
               "Kalamazoo Wings", "2:0,2:2,2:1", "13:4,15:7,10:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151115,
               "Atlanta Gladiators",
               "Greenville Swamp Rabbits",
               "0:0,3:0,1:1",
               "19:6,18:6,11:18",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151115,
               "Manchester Monarchs",
               "Toledo Walleye",
               "1:2,2:0,0:1,0:0,1:0",
               "13:8,13:10,6:6,3:0,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Wheeling Nailers",
               "Evansville IceMen", "1:0,2:2,1:0", "17:9,14:10,9:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Reading Royals",
               "Norfolk Admirals", "0:1,2:1,2:0", "11:16,15:4,9:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Allen Americans",
               "Colorado Eagles", "0:2,2:0,2:1", "6:12,10:7,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Quad City Mallards",
               "Fort Wayne Komets", "0:1,1:0,1:0", "10:14,16:9,10:5", 0, False)

print("Inserting " + leaguename + " Game Data From 11/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Cincinnati Cyclones",
               "Alaska Aces", "1:0,1:0,1:1", "10:9,10:9,6:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151117,
               "Greenville Swamp Rabbits",
               "Orlando Solar Bears",
               "1:4,3:0,1:1,0:1",
               "13:11,20:6,14:11,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Missouri Mavericks",
               "Allen Americans", "1:1,1:0,2:0", "16:8,13:3,13:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Adirondack Thunder",
               "Norfolk Admirals", "2:1,1:1,0:0", "15:11,14:8,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Manchester Monarchs",
               "Elmira Jackals", "0:1,1:1,0:0", "7:5,22:9,18:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Evansville IceMen",
               "Alaska Aces", "0:1,0:4,2:1", "12:8,11:16,17:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Florida Everblades",
               "Wheeling Nailers", "2:3,1:3,2:0", "11:10,11:10,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Rapid City Rush", "Utah Grizzlies",
               "1:1,0:0,1:1,0:0,0:1", "11:13,8:6,5:9,4:2,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Colorado Eagles",
               "Idaho Steelheads", "0:0,0:0,1:1,0:1", "8:3,7:6,14:4,1:1", 0, False)

print("Inserting " + leaguename + " Game Data From 11/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Toledo Walleye", "Kalamazoo Wings",
               "2:1,0:0,0:1,0:0,0:1", "10:5,7:4,10:15,4:6,0:1", 0, False)

print("Inserting " + leaguename + " Game Data From 11/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Reading Royals",
               "Elmira Jackals", "2:3,1:2,1:0", "10:8,8:9,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Manchester Monarchs",
               "Norfolk Admirals", "0:0,0:0,2:1", "11:21,18:7,17:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Greenville Swamp Rabbits",
               "South Carolina Stingrays", "0:0,3:0,0:2", "5:14,13:4,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Brampton Beast",
               "Toledo Walleye", "1:0,0:1,1:2", "9:8,7:9,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Florida Everblades",
               "Wheeling Nailers", "2:3,0:1,1:1", "24:7,8:9,19:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Cincinnati Cyclones",
               "Indy Fuel", "1:0,0:1,0:1", "10:6,6:13,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Fort Wayne Komets",
               "Kalamazoo Wings", "2:1,1:0,0:0", "12:9,13:9,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Wichita Thunder",
               "Allen Americans", "0:1,0:1,0:1", "21:7,7:14,16:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151120,
               "Tulsa Oilers",
               "Missouri Mavericks",
               "1:1,0:2,3:1,0:1",
               "9:9,7:7,8:6,2:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Quad City Mallards",
               "Alaska Aces", "1:1,0:1,3:0", "5:10,13:13,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Evansville IceMen",
               "Orlando Solar Bears", "1:2,3:1,0:3", "11:12,12:9,11:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151120,
               "Colorado Eagles",
               "Idaho Steelheads",
               "2:2,1:1,1:1,1:0",
               "10:8,14:10,13:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Rapid City Rush",
               "Utah Grizzlies", "2:1,2:0,1:0", "9:7,12:9,6:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Manchester Monarchs",
               "Norfolk Admirals", "1:0,2:1,2:0", "8:6,13:9,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Florida Everblades",
               "Wheeling Nailers", "0:1,2:1,3:0", "16:6,9:12,18:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Elmira Jackals",
               "Reading Royals", "0:1,4:0,1:3", "7:8,13:12,8:15", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151121,
               "Atlanta Gladiators",
               "South Carolina Stingrays",
               "0:2,0:0,0:1",
               "11:14,13:8,15:5",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Toledo Walleye",
               "Fort Wayne Komets", "3:2,2:1,1:1", "12:10,10:16,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Indy Fuel",
               "Quad City Mallards", "0:0,2:1,1:1", "6:12,6:9,10:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151121,
               "Cincinnati Cyclones",
               "Orlando Solar Bears",
               "1:0,1:1,1:2,0:0,1:0",
               "6:6,8:9,8:8,2:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Wichita Thunder",
               "Missouri Mavericks", "2:3,0:1,0:1", "6:13,6:24,14:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Evansville IceMen",
               "Kalamazoo Wings", "0:1,2:0,1:1", "14:14,15:15,11:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Allen Americans",
               "Tulsa Oilers", "0:3,1:2,0:1", "5:14,11:14,4:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Colorado Eagles",
               "Idaho Steelheads", "1:0,1:0,0:0", "7:6,4:8,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Rapid City Rush",
               "Utah Grizzlies", "1:1,0:0,2:2,1:0", "6:9,8:4,7:13,2:1", 0, False)

print("Inserting " + leaguename + " Game Data From 11/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Brampton Beast",
               "Fort Wayne Komets", "0:0,0:0,2:0", "8:7,9:9,12:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Manchester Monarchs",
               "Norfolk Admirals", "2:0,0:1,2:1", "15:6,13:15,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Tulsa Oilers",
               "Allen Americans", "0:1,1:2,2:1", "6:8,4:13,11:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Quad City Mallards",
               "Indy Fuel", "1:1,1:0,0:0", "5:12,15:18,12:11", 0, False)

print("Inserting " + leaguename + " Game Data From 11/23/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Greenville Swamp Rabbits",
               "Atlanta Gladiators", "1:1,0:2,2:1", "9:11,8:16,13:8", 0, False)

print("Inserting " + leaguename + " Game Data From 11/24/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151124,
               "Orlando Solar Bears",
               "South Carolina Stingrays",
               "0:0,2:3,1:3",
               "10:16,9:17,8:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Atlanta Gladiators",
               "Manchester Monarchs", "2:0,0:1,1:1", "15:4,4:9,5:16", 0, False)

print("Inserting " + leaguename + " Game Data From 11/25/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Adirondack Thunder",
               "Elmira Jackals", "2:1,0:0,0:0", "6:16,13:10,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Wheeling Nailers",
               "Reading Royals", "0:0,1:0,0:0", "12:6,11:8,2:14", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Norfolk Admirals",
               "Greenville Swamp Rabbits",
               "0:0,0:3,0:3",
               "11:9,8:12,7:10",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Cincinnati Cyclones",
               "Fort Wayne Komets",
               "1:1,0:0,1:1,0:1",
               "10:8,6:8,12:7,1:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Wichita Thunder",
               "Indy Fuel", "1:0,2:0,2:1", "14:7,16:11,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Missouri Mavericks",
               "Quad City Mallards", "1:1,1:0,2:0", "9:10,9:8,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Rapid City Rush",
               "Idaho Steelheads", "1:1,3:0,0:0", "7:13,9:14,1:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Colorado Eagles",
               "Florida Everblades", "0:0,0:1,0:2", "10:11,7:10,13:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/26/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151126, "Atlanta Gladiators",
               "Manchester Monarchs", "1:1,0:1,1:1", "9:16,6:11,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151126, "Fort Wayne Komets",
               "Cincinnati Cyclones", "1:1,0:1,0:3", "12:5,11:7,11:9", 0, False)

print("Inserting " + leaguename + " Game Data From 11/27/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151127,
               "Atlanta Gladiators",
               "Orlando Solar Bears",
               "1:1,2:0,0:2,0:0,1:0",
               "12:11,13:12,9:13,2:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Reading Royals",
               "Greenville Swamp Rabbits", "2:2,0:2,1:2", "6:13,5:9,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Toledo Walleye",
               "Brampton Beast", "0:0,2:1,2:0", "10:8,12:10,10:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151127,
               "Norfolk Admirals",
               "Manchester Monarchs",
               "1:1,1:3,3:1,0:0,0:1",
               "10:13,10:17,15:9,2:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Tulsa Oilers",
               "Wichita Thunder", "1:0,0:0,1:0", "7:3,7:16,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Missouri Mavericks",
               "Indy Fuel", "1:1,2:0,1:1", "12:9,15:10,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Quad City Mallards",
               "Kalamazoo Wings", "2:1,1:0,0:0", "11:10,8:12,2:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Utah Grizzlies",
               "Allen Americans", "4:1,2:1,1:1", "18:7,12:14,10:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Colorado Eagles",
               "Florida Everblades", "0:0,0:1,0:1", "8:11,6:12,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Rapid City Rush",
               "Idaho Steelheads", "1:2,0:0,0:1", "5:14,7:9,2:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Alaska Aces",
               "Evansville IceMen", "1:0,1:4,0:0", "11:4,15:10,14:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/28/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151128,
               "Reading Royals",
               "Greenville Swamp Rabbits",
               "1:1,1:2,1:0,0:0,0:1",
               "9:9,16:6,18:7,1:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151128,
               "Orlando Solar Bears",
               "South Carolina Stingrays",
               "0:1,1:1,0:0",
               "15:9,9:13,9:12",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151128,
               "Elmira Jackals",
               "Adirondack Thunder",
               "1:2,3:1,0:1,0:0,1:0",
               "14:12,15:18,4:17,4:1,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Norfolk Admirals",
               "Manchester Monarchs", "0:0,2:2,1:2", "8:12,4:18,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Fort Wayne Komets",
               "Toledo Walleye", "0:0,0:0,0:0,1:0", "13:3,8:9,7:3,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Wheeling Nailers",
               "Brampton Beast", "2:2,1:3,0:1", "11:12,14:10,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Wichita Thunder",
               "Tulsa Oilers", "2:1,0:1,0:2", "9:10,5:8,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Missouri Mavericks",
               "Indy Fuel", "1:2,2:0,1:0", "7:8,11:8,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Quad City Mallards",
               "Cincinnati Cyclones", "1:0,1:0,0:1", "11:7,10:10,8:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Utah Grizzlies",
               "Allen Americans", "0:0,2:2,2:0", "10:9,9:14,20:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Colorado Eagles",
               "Florida Everblades", "1:0,2:0,2:1", "8:13,9:10,5:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Rapid City Rush",
               "Idaho Steelheads", "1:0,1:0,0:1", "7:8,8:15,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Alaska Aces",
               "Evansville IceMen", "1:0,0:0,3:1", "17:7,15:13,14:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Brampton Beast",
               "Elmira Jackals", "0:2,1:1,1:2", "10:6,11:5,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Adirondack Thunder",
               "Greenville Swamp Rabbits", "1:0,0:0,1:0", "8:9,5:13,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Kalamazoo Wings", "Toledo Walleye",
               "0:0,3:1,0:2,0:0,0:1", "8:9,9:15,5:23,2:6,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Reading Royals",
               "Wheeling Nailers", "0:1,3:0,0:1", "12:13,20:10,7:21", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Tulsa Oilers",
               "Missouri Mavericks", "0:1,1:0,0:1", "2:10,15:12,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Quad City Mallards",
               "Indy Fuel", "0:1,0:0,2:1,1:0", "7:10,10:6,14:8,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Alaska Aces",
               "Evansville IceMen", "1:1,0:3,2:1", "14:6,9:15,21:5", 0, False)

print("Inserting " + leaguename + " Game Data From 11/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151130, "Orlando Solar Bears",
               "South Carolina Stingrays", "0:2,0:0,0:1", "5:13,6:5,11:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/1/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151201,
               "Cincinnati Cyclones",
               "Quad City Mallards",
               "0:0,0:1,1:0,0:0,0:1",
               "8:6,7:9,13:7,0:1,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/2/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Elmira Jackals",
               "Kalamazoo Wings", "1:1,2:0,1:0", "12:9,15:6,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Evansville IceMen",
               "Missouri Mavericks", "0:3,0:0,0:0", "3:9,5:6,10:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151202,
               "Norfolk Admirals",
               "South Carolina Stingrays",
               "0:0,0:1,3:0",
               "3:10,6:12,9:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Tulsa Oilers",
               "Rapid City Rush", "1:1,0:0,1:3", "6:8,11:7,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Idaho Steelheads",
               "Florida Everblades", "0:1,1:2,0:1", "5:18,14:7,14:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151202,
               "Alaska Aces",
               "Colorado Eagles",
               "0:1,0:0,1:0,0:1",
               "10:10,16:7,9:6,5:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/3/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Greenville Swamp Rabbits",
               "Cincinnati Cyclones", "1:0,2:0,1:3", "10:10,10:8,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Indy Fuel",
               "Toledo Walleye", "1:0,0:1,1:3", "5:9,4:7,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Brampton Beast",
               "Adirondack Thunder", "0:1,0:3,0:0", "13:9,8:14,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Tulsa Oilers",
               "Utah Grizzlies", "4:0,1:1,0:0", "13:9,10:10,5:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Adirondack Thunder",
               "Brampton Beast", "0:2,2:0,3:0", "7:19,15:5,9:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Manchester Monarchs",
               "Reading Royals", "0:0,2:1,1:1", "10:4,13:7,5:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Greenville Swamp Rabbits",
               "Cincinnati Cyclones",
               "4:2,1:2,1:2,0:1",
               "16:9,12:17,16:6,0:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Elmira Jackals",
               "Kalamazoo Wings", "1:0,0:1,1:2", "12:8,20:9,17:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Indy Fuel",
               "Toledo Walleye", "1:2,1:1,0:2", "11:6,7:8,13:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Wheeling Nailers",
               "South Carolina Stingrays",
               "1:1,1:0,1:1",
               "7:14,10:12,8:14",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Allen Americans",
               "Rapid City Rush", "2:0,0:1,1:0", "5:10,15:8,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Evansville IceMen",
               "Fort Wayne Komets", "1:1,1:3,3:3", "16:9,6:5,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Idaho Steelheads",
               "Florida Everblades", "1:0,3:1,1:0", "11:8,9:5,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Alaska Aces",
               "Colorado Eagles", "2:0,1:1,3:3", "15:11,7:14,12:11", 0, False)

print("Inserting " + leaguename + " Game Data From 12/5/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Manchester Monarchs",
               "Reading Royals", "0:1,0:1,0:1", "11:8,6:16,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Greenville Swamp Rabbits",
               "Norfolk Admirals", "0:2,0:0,0:1", "6:10,13:13,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Orlando Solar Bears",
               "Atlanta Gladiators", "0:0,2:0,2:0", "7:9,13:8,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Elmira Jackals",
               "Kalamazoo Wings", "0:0,2:0,1:1", "10:10,18:4,9:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151205,
               "Wheeling Nailers",
               "South Carolina Stingrays",
               "0:3,0:2,1:1",
               "6:18,10:10,8:13",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Allen Americans",
               "Utah Grizzlies", "4:1,1:1,2:1", "9:18,4:10,5:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Missouri Mavericks",
               "Wichita Thunder", "2:1,3:1,0:0", "7:8,11:5,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Idaho Steelheads",
               "Florida Everblades", "0:2,1:0,0:1", "11:10,12:3,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Alaska Aces",
               "Colorado Eagles", "0:2,3:0,1:1", "7:3,7:12,8:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Brampton Beast",
               "Kalamazoo Wings", "0:0,0:0,3:0", "9:4,8:12,16:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Manchester Monarchs",
               "Reading Royals", "0:1,2:1,2:0", "7:8,7:15,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Orlando Solar Bears",
               "Atlanta Gladiators", "1:1,0:0,2:3", "10:18,10:5,13:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151206,
               "Indy Fuel",
               "South Carolina Stingrays",
               "0:1,1:0,0:2",
               "10:10,9:5,6:8",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151206,
               "Wheeling Nailers",
               "Elmira Jackals",
               "0:2,2:0,0:0,0:0,0:1",
               "13:7,15:8,13:7,3:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151206,
               "Evansville IceMen",
               "Quad City Mallards",
               "1:1,3:1,1:3,0:1",
               "12:8,19:12,12:12,1:3",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Brampton Beast",
               "Manchester Monarchs", "1:0,1:1,1:3", "7:7,11:9,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Elmira Jackals",
               "Norfolk Admirals", "1:0,2:1,1:2", "10:18,10:21,13:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Toledo Walleye",
               "Evansville IceMen", "1:0,1:1,0:2", "11:7,9:13,11:15", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151209,
               "Florida Everblades",
               "Reading Royals",
               "0:0,0:2,2:0,0:0,1:0",
               "11:4,9:11,11:8,3:5,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Allen Americans",
               "Idaho Steelheads", "2:0,0:0,2:0", "8:9,9:8,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Utah Grizzlies",
               "Alaska Aces", "0:0,1:0,4:0", "7:9,13:7,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Colorado Eagles",
               "Wichita Thunder", "1:0,1:0,0:1", "15:7,8:8,10:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Rapid City Rush",
               "Wichita Thunder", "1:1,4:0,2:1", "9:5,10:10,6:11", 0, False)

print("Inserting " + leaguename + " Game Data From 12/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Greenville Swamp Rabbits",
               "Orlando Solar Bears", "2:0,1:0,3:2", "10:12,15:10,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Indy Fuel",
               "Wheeling Nailers", "1:1,0:0,0:1", "14:8,9:12,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Tulsa Oilers",
               "Idaho Steelheads", "0:0,3:0,1:2", "5:7,16:10,7:10", 0, False)

print("Inserting " + leaguename + " Game Data From 12/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Kalamazoo Wings",
               "Brampton Beast", "3:0,0:0,1:0", "16:13,8:6,12:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Adirondack Thunder",
               "Norfolk Admirals", "0:0,1:2,0:4", "11:5,7:10,11:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151211,
               "Greenville Swamp Rabbits",
               "Orlando Solar Bears",
               "0:1,1:0,1:1,0:1",
               "9:9,11:8,8:16,2:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151211,
               "Elmira Jackals",
               "Manchester Monarchs",
               "1:1,0:0,0:0,0:0,1:0",
               "10:13,10:18,12:12,5:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151211,
               "Toledo Walleye",
               "Wheeling Nailers",
               "0:0,1:0,0:1,0:0,1:0",
               "13:9,14:8,5:13,5:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Florida Everblades",
               "Reading Royals", "2:0,0:0,0:2,1:0", "14:8,10:7,5:8,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Atlanta Gladiators",
               "South Carolina Stingrays", "1:1,2:1,0:0", "6:16,9:10,6:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Fort Wayne Komets",
               "Indy Fuel", "1:1,1:1,0:0,0:1", "9:10,9:11,12:8,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Tulsa Oilers",
               "Idaho Steelheads", "1:1,1:1,0:2", "12:16,5:14,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Evansville IceMen",
               "Cincinnati Cyclones", "2:0,4:2,1:1", "12:9,13:11,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Utah Grizzlies",
               "Alaska Aces", "2:0,0:1,1:1", "10:9,8:9,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Colorado Eagles",
               "Wichita Thunder", "0:1,3:0,0:1", "9:9,13:11,4:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Rapid City Rush",
               "Quad City Mallards", "1:1,2:1,2:0", "7:13,8:9,7:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Kalamazoo Wings",
               "Brampton Beast", "3:0,0:1,0:0", "11:11,5:11,5:16", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "Adirondack Thunder",
               "Manchester Monarchs",
               "1:0,1:1,1:2,0:1",
               "11:14,15:14,6:9,0:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Florida Everblades",
               "Reading Royals", "0:2,1:0,0:0", "5:10,10:16,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Elmira Jackals",
               "Norfolk Admirals", "1:0,1:0,2:0", "9:6,6:12,8:28", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "Atlanta Gladiators",
               "Orlando Solar Bears",
               "1:1,0:0,0:0,1:0",
               "13:9,12:5,11:6,3:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "South Carolina Stingrays",
               "Greenville Swamp Rabbits",
               "3:0,1:1,1:0",
               "15:13,6:10,11:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Indy Fuel",
               "Fort Wayne Komets", "1:2,0:0,1:1", "7:19,14:8,12:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Cincinnati Cyclones",
               "Evansville IceMen", "2:1,2:2,2:1", "9:6,13:9,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Wheeling Nailers",
               "Toledo Walleye", "1:1,4:1,1:0", "11:7,14:7,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Utah Grizzlies",
               "Alaska Aces", "2:1,0:1,2:0", "9:15,13:5,9:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Colorado Eagles",
               "Wichita Thunder", "1:0,3:0,0:0", "16:8,12:6,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Rapid City Rush",
               "Quad City Mallards", "1:0,0:0,0:2", "7:14,10:10,3:13", 0, False)

print("Inserting " + leaguename + " Game Data From 12/13/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151213,
               "Brampton Beast",
               "Norfolk Admirals",
               "3:1,0:3,2:1,0:1",
               "12:6,10:12,13:17,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Manchester Monarchs",
               "Adirondack Thunder", "0:0,0:0,0:2", "9:8,14:10,7:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "South Carolina Stingrays",
               "Atlanta Gladiators", "1:1,1:1,1:0", "13:9,13:10,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Fort Wayne Komets",
               "Evansville IceMen", "2:1,1:2,1:3", "12:8,11:6,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Allen Americans",
               "Idaho Steelheads", "0:1,1:1,1:0,0:1", "1:14,8:9,8:5,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Tulsa Oilers",
               "Missouri Mavericks", "1:2,2:0,1:1", "14:7,19:7,8:10", 0, False)

print("Inserting " + leaguename + " Game Data From 12/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Toledo Walleye",
               "Indy Fuel", "1:1,2:0,2:0", "12:12,9:7,5:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Adirondack Thunder",
               "Elmira Jackals", "3:3,0:1,1:2", "6:7,20:5,12:4", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151216,
               "Evansville IceMen",
               "Atlanta Gladiators",
               "2:1,2:2,1:2,0:1",
               "7:5,13:14,10:17,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Norfolk Admirals",
               "Reading Royals", "1:2,2:1,0:3", "7:9,17:8,3:20", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Florida Everblades",
               "Orlando Solar Bears", "0:0,2:1,1:1", "14:13,19:6,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Colorado Eagles",
               "Allen Americans", "0:0,3:0,1:1", "11:4,10:13,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Idaho Steelheads",
               "Utah Grizzlies", "1:4,4:0,3:1", "7:6,20:7,9:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/17/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151217,
               "Kalamazoo Wings",
               "Manchester Monarchs",
               "1:0,0:0,0:1,0:1",
               "8:12,7:15,10:7,1:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Brampton Beast", "Toledo Walleye",
               "1:1,2:1,0:1,0:0,0:1", "11:10,8:8,12:10,3:2,0:1", 0, False)

print("Inserting " + leaguename + " Game Data From 12/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Kalamazoo Wings",
               "Atlanta Gladiators", "1:1,0:1,0:1", "8:13,4:12,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Reading Royals",
               "Elmira Jackals", "1:1,0:2,1:2", "11:10,8:7,15:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151218,
               "South Carolina Stingrays",
               "Florida Everblades",
               "0:1,0:0,1:0,0:1",
               "7:13,14:7,8:6,3:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Norfolk Admirals",
               "Adirondack Thunder", "1:2,1:1,1:2", "10:14,14:9,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Fort Wayne Komets",
               "Manchester Monarchs", "0:1,1:3,2:1", "7:8,7:13,11:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151218,
               "Tulsa Oilers",
               "Wichita Thunder",
               "0:1,0:1,2:0,0:1",
               "7:10,6:8,10:5,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Missouri Mavericks",
               "Cincinnati Cyclones", "3:0,1:2,1:0", "16:7,6:11,4:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Quad City Mallards",
               "Wheeling Nailers", "0:0,0:2,1:2", "11:10,13:17,16:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Evansville IceMen",
               "Indy Fuel", "0:1,0:0,2:0", "7:13,6:6,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Utah Grizzlies",
               "Colorado Eagles", "0:0,3:0,1:0", "13:3,11:11,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Idaho Steelheads",
               "Allen Americans", "1:1,1:1,4:1", "5:15,9:11,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Alaska Aces",
               "Rapid City Rush", "0:0,2:2,3:0", "15:4,12:9,18:8", 0, False)

print("Inserting " + leaguename + " Game Data From 12/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Kalamazoo Wings",
               "Atlanta Gladiators", "0:2,3:1,0:2", "5:6,12:3,8:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Reading Royals",
               "Elmira Jackals", "1:0,0:0,1:0", "14:10,13:10,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Greenville Swamp Rabbits",
               "Orlando Solar Bears", "2:0,0:1,4:0", "11:5,8:14,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "South Carolina Stingrays",
               "Florida Everblades", "0:1,0:0,1:3", "9:7,9:7,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Toledo Walleye",
               "Manchester Monarchs", "0:0,2:0,0:0", "5:5,14:2,4:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Norfolk Admirals",
               "Adirondack Thunder", "2:1,0:0,0:0", "14:13,9:7,5:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Fort Wayne Komets",
               "Brampton Beast", "2:0,3:1,0:0", "9:7,13:10,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Tulsa Oilers", "Wichita Thunder",
               "1:1,0:0,1:1,0:0,1:0", "10:7,7:7,8:7,4:1,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Missouri Mavericks",
               "Cincinnati Cyclones", "1:0,2:0,0:2", "15:4,11:9,8:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Quad City Mallards",
               "Wheeling Nailers", "2:1,1:2,2:0", "7:16,12:11,12:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Evansville IceMen",
               "Indy Fuel", "0:1,1:1,0:1", "14:14,16:13,15:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Utah Grizzlies",
               "Colorado Eagles", "3:2,1:0,2:1", "11:9,10:9,7:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151219,
               "Idaho Steelheads",
               "Allen Americans",
               "0:2,2:0,0:0,0:0,0:1",
               "9:4,14:4,9:4,1:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Alaska Aces",
               "Rapid City Rush", "4:1,0:0,0:0", "15:5,8:10,8:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Greenville Swamp Rabbits",
               "Orlando Solar Bears", "0:0,3:3,4:1", "10:17,10:14,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Indy Fuel",
               "Toledo Walleye", "0:1,3:2,0:1", "17:10,11:6,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Missouri Mavericks",
               "Quad City Mallards", "1:1,1:1,2:0", "16:7,10:10,14:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Wichita Thunder",
               "Cincinnati Cyclones", "0:2,1:2,0:2", "5:10,6:11,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Alaska Aces",
               "Rapid City Rush", "0:0,1:2,1:1", "11:8,13:6,18:2", 0, False)

print("Inserting " + leaguename + " Game Data From 12/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Fort Wayne Komets",
               "Atlanta Gladiators", "1:0,1:0,2:0", "11:11,11:5,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Allen Americans",
               "Tulsa Oilers", "1:0,0:1,0:2", "8:10,6:5,6:11", 0, False)

print("Inserting " + leaguename + " Game Data From 12/26/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Adirondack Thunder",
               "Manchester Monarchs", "3:0,1:0,2:1", "9:3,10:14,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Elmira Jackals",
               "Reading Royals", "0:1,0:0,0:3", "10:7,18:8,17:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151226,
               "Atlanta Gladiators",
               "Greenville Swamp Rabbits",
               "0:0,1:2,1:0,0:1",
               "9:7,12:14,12:7,3:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "South Carolina Stingrays",
               "Norfolk Admirals", "2:0,1:2,2:0", "10:5,15:5,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Toledo Walleye",
               "Wheeling Nailers", "1:0,1:0,2:1", "9:8,11:15,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Fort Wayne Komets",
               "Kalamazoo Wings", "2:1,0:1,3:0", "17:6,7:8,18:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Wichita Thunder", "Tulsa Oilers",
               "0:1,1:0,0:0,0:0,0:1", "11:13,15:9,9:9,3:1,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Allen Americans",
               "Missouri Mavericks", "1:1,0:1,0:1", "15:8,9:9,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Quad City Mallards",
               "Indy Fuel", "1:1,0:0,0:3", "9:17,6:13,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Evansville IceMen",
               "Cincinnati Cyclones", "0:1,2:1,2:0", "16:6,14:8,21:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Colorado Eagles",
               "Rapid City Rush", "0:1,2:1,1:1,1:0", "12:5,15:7,6:9,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Idaho Steelheads",
               "Utah Grizzlies", "1:0,2:2,2:0", "11:11,8:9,5:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/27/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151227,
               "Brampton Beast",
               "Reading Royals",
               "0:1,1:2,4:2,1:0",
               "10:5,10:10,19:5,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Manchester Monarchs",
               "Adirondack Thunder", "1:0,1:0,0:0", "10:13,11:13,5:18", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151227,
               "Greenville Swamp Rabbits",
               "Atlanta Gladiators",
               "1:1,1:0,0:1,0:1",
               "9:8,8:18,7:15,3:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Indy Fuel",
               "Quad City Mallards", "2:1,0:0,0:0", "6:7,7:10,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "South Carolina Stingrays",
               "Norfolk Admirals", "1:0,0:0,2:0", "8:4,8:11,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Wheeling Nailers",
               "Kalamazoo Wings", "0:1,1:5,3:1", "13:11,14:11,12:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Orlando Solar Bears",
               "Florida Everblades", "2:1,1:3,0:0", "8:12,12:15,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Rapid City Rush",
               "Colorado Eagles", "0:0,0:1,0:2", "6:7,6:9,14:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151227,
               "Wichita Thunder",
               "Allen Americans",
               "0:1,1:1,1:0,0:1",
               "10:11,14:7,7:14,3:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Brampton Beast",
               "Reading Royals", "0:1,2:1,0:0,0:1", "8:4,12:4,4:7,4:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Utah Grizzlies",
               "Idaho Steelheads", "0:0,1:2,0:2", "10:9,8:14,7:5", 0, False)

print("Inserting " + leaguename + " Game Data From 12/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Adirondack Thunder",
               "Greenville Swamp Rabbits", "1:1,0:0,0:2", "14:7,8:7,12:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151229,
               "Orlando Solar Bears",
               "South Carolina Stingrays",
               "1:3,2:0,0:2",
               "7:14,13:16,4:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Atlanta Gladiators",
               "Norfolk Admirals", "0:0,1:0,3:0", "7:11,8:11,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Fort Wayne Komets",
               "Brampton Beast", "1:1,1:2,1:0,0:1", "12:7,7:15,20:5,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Cincinnati Cyclones",
               "Indy Fuel", "1:2,0:1,0:2", "9:11,8:9,6:5", 0, False)

print("Inserting " + leaguename + " Game Data From 12/30/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151230,
               "Atlanta Gladiators",
               "Norfolk Admirals",
               "2:2,1:1,0:0,1:0",
               "15:15,6:14,8:8,3:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Quad City Mallards",
               "Evansville IceMen", "1:1,1:2,0:0", "10:15,18:15,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Toledo Walleye",
               "Elmira Jackals", "0:0,1:1,0:1", "11:13,14:9,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Wichita Thunder",
               "Allen Americans", "1:1,1:1,1:2", "11:10,17:7,11:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Idaho Steelheads",
               "Colorado Eagles", "2:1,3:2,1:0", "10:7,13:11,4:13", 0, False)

print("Inserting " + leaguename + " Game Data From 12/31/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151231,
               "Adirondack Thunder",
               "Reading Royals",
               "1:0,0:1,0:0,0:0,1:0",
               "15:14,9:6,7:5,9:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Kalamazoo Wings",
               "Elmira Jackals", "3:2,1:1,1:0", "11:13,17:14,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Cincinnati Cyclones",
               "Toledo Walleye", "0:0,1:0,3:0", "7:7,6:9,10:2", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151231,
               "Wheeling Nailers",
               "Brampton Beast",
               "1:1,0:2,2:0,0:1",
               "9:10,11:12,13:3,1:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151231,
               "Manchester Monarchs",
               "Greenville Swamp Rabbits",
               "0:0,1:0,1:2,1:0",
               "9:3,11:9,6:13,4:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Fort Wayne Komets",
               "Indy Fuel", "2:0,5:0,0:0", "8:12,16:12,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Missouri Mavericks",
               "Wichita Thunder", "3:1,3:0,1:0", "9:6,17:4,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Evansville IceMen",
               "Quad City Mallards", "0:2,3:2,1:2", "14:12,12:10,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Rapid City Rush",
               "Tulsa Oilers", "0:1,0:1,1:0", "8:9,8:9,10:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Alaska Aces",
               "Utah Grizzlies", "0:2,2:1,1:3", "18:7,11:10,11:10", 0, False)

print("Inserting " + leaguename + " Game Data From 1/1/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Missouri Mavericks",
               "Allen Americans", "1:0,3:1,0:0", "13:6,5:13,13:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Florida Everblades",
               "Orlando Solar Bears", "1:1,0:2,2:2", "10:8,7:11,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Indy Fuel",
               "Fort Wayne Komets", "0:0,1:1,0:1", "10:7,11:13,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Idaho Steelheads",
               "Colorado Eagles", "0:2,1:0,0:1", "6:7,8:7,15:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Alaska Aces",
               "Utah Grizzlies", "0:0,1:1,0:1", "10:12,9:13,10:5", 0, False)

print("Inserting " + leaguename + " Game Data From 1/2/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Manchester Monarchs",
               "Greenville Swamp Rabbits",
               "0:1,0:1,2:0,0:0,0:1",
               "8:11,13:20,17:5,6:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Kalamazoo Wings",
               "Elmira Jackals", "0:2,2:3,2:0", "6:10,9:14,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Reading Royals",
               "Adirondack Thunder", "0:0,3:0,2:0", "10:6,11:8,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Orlando Solar Bears",
               "Florida Everblades", "1:0,0:0,2:1", "12:12,12:8,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "South Carolina Stingrays",
               "Cincinnati Cyclones", "1:0,0:0,3:1", "12:6,9:14,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Toledo Walleye",
               "Fort Wayne Komets", "1:0,0:2,0:0", "16:7,6:12,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Norfolk Admirals",
               "Atlanta Gladiators", "0:0,2:2,1:0", "8:10,9:15,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Indy Fuel",
               "Wichita Thunder", "1:1,0:1,0:0", "9:9,9:11,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Wheeling Nailers",
               "Brampton Beast", "1:0,2:0,2:1", "10:9,11:10,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Quad City Mallards",
               "Allen Americans", "0:1,1:1,0:2", "8:6,6:18,5:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Evansville IceMen",
               "Missouri Mavericks",
               "2:1,1:0,0:2,0:1",
               "8:14,11:5,9:10,2:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Rapid City Rush",
               "Tulsa Oilers", "2:1,0:1,2:1", "13:11,7:8,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Idaho Steelheads",
               "Colorado Eagles", "1:0,0:0,0:0", "12:10,7:10,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Alaska Aces",
               "Utah Grizzlies", "1:1,2:0,0:1", "16:8,14:9,8:15", 0, False)

print("Inserting " + leaguename + " Game Data From 1/3/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Manchester Monarchs",
               "Greenville Swamp Rabbits",
               "0:0,1:0,1:2,0:0,0:1",
               "14:7,12:12,8:12,2:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "South Carolina Stingrays",
               "Cincinnati Cyclones", "0:1,1:1,1:2", "19:6,12:13,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Reading Royals",
               "Adirondack Thunder", "0:2,0:0,2:1", "9:5,14:9,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Wheeling Nailers",
               "Norfolk Admirals", "2:1,1:4,0:0", "12:9,7:21,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Toledo Walleye",
               "Elmira Jackals", "1:0,3:0,0:1", "13:4,13:7,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Orlando Solar Bears",
               "Florida Everblades", "1:1,0:0,0:3", "7:12,4:7,8:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Evansville IceMen",
               "Wichita Thunder",
               "0:1,1:1,1:0,0:0,0:1",
               "3:9,7:5,12:8,1:3,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/6/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Adirondack Thunder",
               "Manchester Monarchs", "1:0,2:0,2:2", "15:12,12:7,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Atlanta Gladiators",
               "Cincinnati Cyclones", "2:0,3:1,0:1", "7:8,18:15,8:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Norfolk Admirals",
               "Orlando Solar Bears", "0:3,2:1,0:0", "18:11,14:12,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Utah Grizzlies",
               "Rapid City Rush", "0:1,0:0,1:2", "14:13,14:3,14:12", 0, False)

print("Inserting " + leaguename + " Game Data From 1/5/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160105,
               "Tulsa Oilers",
               "Missouri Mavericks",
               "0:2,3:1,0:0,0:0,0:1",
               "5:13,20:6,7:4,0:2,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/7/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Greenville Swamp Rabbits",
               "Florida Everblades", "0:1,0:0,1:1", "6:13,7:15,9:13", 0, False)

print("Inserting " + leaguename + " Game Data From 1/8/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Reading Royals",
               "Toledo Walleye", "0:1,0:1,1:1", "14:6,21:4,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Kalamazoo Wings",
               "Brampton Beast", "1:1,1:1,1:1,1:0", "4:13,6:17,8:7,2:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160108,
               "Adirondack Thunder",
               "South Carolina Stingrays",
               "0:3,1:2,0:0",
               "13:10,8:7,10:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160108,
               "Greenville Swamp Rabbits",
               "Florida Everblades",
               "1:1,1:1,0:0,0:1",
               "10:7,15:10,13:5,2:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Elmira Jackals",
               "Manchester Monarchs", "1:3,0:2,0:1", "12:17,11:15,13:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Norfolk Admirals",
               "Cincinnati Cyclones", "0:1,1:0,2:0", "8:7,12:9,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Indy Fuel",
               "Evansville IceMen", "0:1,2:1,1:0", "12:6,13:8,11:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Wheeling Nailers",
               "Orlando Solar Bears", "2:0,0:2,0:3", "13:5,7:11,7:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160108,
               "Atlanta Gladiators",
               "Alaska Aces",
               "2:0,0:2,0:0,0:0,1:0",
               "9:3,12:9,5:7,2:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Allen Americans",
               "Colorado Eagles", "0:1,0:0,0:0", "11:11,6:15,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Wichita Thunder", "Tulsa Oilers",
               "0:1,1:0,0:0,0:0,0:1", "3:12,10:9,8:11,4:0,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Quad City Mallards",
               "Fort Wayne Komets", "1:2,2:2,1:3", "3:14,11:15,16:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Utah Grizzlies",
               "Idaho Steelheads", "0:1,0:0,0:0", "9:12,8:5,20:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160108,
               "Rapid City Rush",
               "Missouri Mavericks",
               "1:0,0:0,0:1,1:0",
               "6:8,14:9,11:10,1:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/9/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Reading Royals",
               "Toledo Walleye", "1:0,1:3,0:1", "8:8,12:11,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Adirondack Thunder",
               "South Carolina Stingrays", "0:1,3:0,1:1", "9:7,20:7,8:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160109,
               "Greenville Swamp Rabbits",
               "Florida Everblades",
               "0:0,1:0,0:1,0:0,1:0",
               "12:14,13:11,2:9,2:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Elmira Jackals",
               "Manchester Monarchs", "0:1,0:0,1:3", "12:14,14:12,17:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Brampton Beast", "Kalamazoo Wings",
               "0:1,2:1,0:0,0:0,0:1", "12:6,12:8,6:12,3:1,0:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160109,
               "Norfolk Admirals",
               "Cincinnati Cyclones",
               "0:1,1:0,1:1,1:0",
               "7:17,16:7,12:11,2:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Indy Fuel",
               "Evansville IceMen", "1:0,1:0,1:0", "9:11,8:16,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Wheeling Nailers",
               "Orlando Solar Bears", "1:2,1:0,1:4", "9:6,12:5,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Tulsa Oilers",
               "Wichita Thunder", "1:1,3:1,2:2", "19:5,16:13,10:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Utah Grizzlies",
               "Idaho Steelheads", "1:0,1:0,1:1", "7:4,10:10,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Rapid City Rush",
               "Missouri Mavericks", "0:3,0:0,1:0", "8:14,9:10,11:7", 0, False)

print("Inserting " + leaguename + " Game Data From 1/10/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Brampton Beast",
               "Kalamazoo Wings", "1:0,3:2,3:1", "11:11,14:9,11:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Atlanta Gladiators",
               "Alaska Aces", "0:1,0:0,1:1", "12:11,8:18,13:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160110,
               "Reading Royals",
               "South Carolina Stingrays",
               "0:0,2:0,1:1",
               "8:4,11:14,8:20",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Wheeling Nailers",
               "Indy Fuel", "1:1,1:1,0:1", "11:4,13:14,17:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Allen Americans",
               "Colorado Eagles", "1:1,3:0,1:1", "10:6,9:9,11:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Quad City Mallards",
               "Fort Wayne Komets", "0:0,1:0,1:0", "9:7,10:12,4:23", 0, False)

print("Inserting " + leaguename + " Game Data From 1/12/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Kalamazoo Wings",
               "Orlando Solar Bears", "0:1,2:3,0:2", "9:13,9:17,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Adirondack Thunder",
               "Norfolk Admirals", "1:0,0:0,0:0", "12:15,7:11,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Atlanta Gladiators",
               "Alaska Aces", "2:0,1:1,0:2,1:0", "19:5,11:11,13:8,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Wichita Thunder",
               "Missouri Mavericks", "0:1,1:1,0:2", "13:11,8:6,12:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/13/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Evansville IceMen",
               "Rapid City Rush", "0:0,3:2,1:0", "11:8,13:10,6:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Florida Everblades",
               "Brampton Beast", "2:1,1:1,1:0", "7:9,8:17,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Cincinnati Cyclones",
               "Fort Wayne Komets", "0:0,1:3,0:1", "10:9,11:13,10:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Utah Grizzlies",
               "Tulsa Oilers", "1:1,0:0,4:1", "9:12,10:9,12:8", 0, False)

print("Inserting " + leaguename + " Game Data From 1/14/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Greenville Swamp Rabbits",
               "Alaska Aces", "1:0,0:1,1:2", "8:13,6:16,6:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Elmira Jackals",
               "Norfolk Admirals", "1:0,0:2,0:2", "10:8,9:20,7:11", 0, False)

print("Inserting " + leaguename + " Game Data From 1/15/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Elmira Jackals",
               "Reading Royals", "0:1,0:1,0:2", "6:9,7:7,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Toledo Walleye",
               "Evansville IceMen", "1:1,3:0,1:0", "10:10,16:8,13:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Florida Everblades",
               "Brampton Beast", "0:0,3:0,2:1", "12:11,7:10,9:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Indy Fuel",
               "Rapid City Rush", "0:0,0:3,0:1", "11:8,6:14,9:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160115,
               "Atlanta Gladiators",
               "South Carolina Stingrays",
               "1:0,0:1,3:0",
               "8:10,12:8,12:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Fort Wayne Komets",
               "Orlando Solar Bears", "2:1,2:1,1:0", "15:11,13:11,11:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160115,
               "Quad City Mallards",
               "Kalamazoo Wings",
               "0:0,2:2,0:0,1:0",
               "13:8,11:18,10:7,7:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Utah Grizzlies",
               "Wichita Thunder", "3:0,2:2,2:1", "12:6,9:8,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Colorado Eagles",
               "Missouri Mavericks", "1:2,2:2,1:1", "6:4,12:10,16:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Idaho Steelheads",
               "Tulsa Oilers", "1:1,1:0,0:0", "12:10,11:6,7:12", 0, False)

print("Inserting " + leaguename + " Game Data From 1/16/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Adirondack Thunder",
               "Reading Royals", "1:0,1:0,0:0", "9:8,8:10,7:18", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160116,
               "Manchester Monarchs",
               "Norfolk Admirals",
               "0:2,0:0,2:0,0:1",
               "9:8,12:11,15:3,3:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Florida Everblades",
               "Brampton Beast", "0:0,1:1,0:0,1:0", "6:5,11:12,6:13,3:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Atlanta Gladiators",
               "Greenville Swamp Rabbits", "2:1,1:1,2:1", "9:7,9:12,16:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "South Carolina Stingrays",
               "Alaska Aces", "0:3,3:0,1:1,0:1", "14:8,9:4,14:8,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Toledo Walleye",
               "Wheeling Nailers", "3:1,1:1,0:1", "14:12,13:8,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Fort Wayne Komets",
               "Rapid City Rush", "0:0,0:0,1:0", "8:9,11:5,16:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Indy Fuel",
               "Orlando Solar Bears", "0:1,0:1,0:0", "11:10,9:10,18:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Allen Americans",
               "Cincinnati Cyclones", "1:2,2:0,0:0", "3:9,7:11,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Evansville IceMen",
               "Quad City Mallards", "0:1,1:0,0:1", "14:8,12:8,13:15", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160116,
               "Utah Grizzlies",
               "Wichita Thunder",
               "0:1,2:1,0:0,1:0",
               "11:5,15:12,11:8,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Colorado Eagles",
               "Missouri Mavericks", "1:1,1:1,3:1", "8:12,14:6,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Idaho Steelheads",
               "Tulsa Oilers", "1:1,0:1,1:2", "17:13,14:7,7:12", 0, False)

print("Inserting " + leaguename + " Game Data From 1/17/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160117,
               "Manchester Monarchs",
               "Norfolk Admirals",
               "1:1,3:2,0:1,0:0,0:1",
               "15:5,15:10,8:8,2:7,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Indy Fuel",
               "Wheeling Nailers", "1:0,1:1,1:1", "8:8,17:10,11:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160117,
               "South Carolina Stingrays",
               "Alaska Aces",
               "0:1,1:2,2:0,0:0,0:1",
               "8:10,13:14,10:18,2:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Elmira Jackals",
               "Adirondack Thunder", "0:1,0:0,0:0", "6:16,12:14,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Fort Wayne Komets",
               "Rapid City Rush", "2:0,0:1,1:0", "14:8,9:11,9:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160117,
               "Allen Americans",
               "Cincinnati Cyclones",
               "2:2,1:0,0:1,0:0,0:1",
               "7:8,9:6,12:11,1:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Quad City Mallards",
               "Kalamazoo Wings", "0:4,2:0,0:3", "9:14,12:8,12:11", 0, False)

print("Inserting " + leaguename + " Game Data From 1/18/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160118,
               "Atlanta Gladiators",
               "Greenville Swamp Rabbits",
               "0:0,0:0,0:1",
               "8:10,14:8,9:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Reading Royals",
               "Adirondack Thunder", "0:0,0:2,1:1", "8:9,14:13,22:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Elmira Jackals", "Brampton Beast",
               "0:1,0:0,1:0,0:0,1:0", "11:7,19:4,9:8,3:0,1:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160118,
               "Allen Americans",
               "Cincinnati Cyclones",
               "2:1,1:2,0:0,0:1",
               "7:8,7:6,5:12,1:5",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160118,
               "Utah Grizzlies",
               "Wichita Thunder",
               "0:1,2:0,0:1,1:0",
               "13:7,12:7,5:16,6:4",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/19/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Greenville Swamp Rabbits",
               "Atlanta Gladiators", "0:2,1:1,1:3", "10:14,11:11,12:12", 0, False)

print("Inserting " + leaguename + " Game Data From 1/22/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Reading Royals",
               "Brampton Beast", "0:0,1:0,0:1,0:1", "13:4,14:9,8:7,1:2", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Adirondack Thunder",
               "Manchester Monarchs",
               "1:1,3:4,1:0,0:0,0:1",
               "15:11,11:25,15:15,5:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Greenville Swamp Rabbits",
               "Evansville IceMen", "1:0,0:3,2:3", "11:10,9:12,16:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "South Carolina Stingrays",
               "Atlanta Gladiators", "2:0,1:0,1:1", "14:5,12:9,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Toledo Walleye",
               "Utah Grizzlies", "1:1,2:1,0:0", "9:9,10:13,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Norfolk Admirals",
               "Elmira Jackals", "1:0,0:2,1:0,1:0", "9:11,8:12,12:4,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Florida Everblades",
               "Orlando Solar Bears", "1:1,1:0,2:0", "9:11,22:4,18:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Indy Fuel",
               "Quad City Mallards", "2:0,0:1,0:0", "11:11,12:8,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Cincinnati Cyclones",
               "Fort Wayne Komets", "0:1,0:3,1:1", "6:11,4:15,8:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Wheeling Nailers",
               "Kalamazoo Wings",
               "0:0,0:1,1:0,1:0",
               "16:7,5:12,13:9,4:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Wichita Thunder",
               "Allen Americans",
               "0:0,3:2,0:1,0:1",
               "5:14,14:10,15:14,1:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Missouri Mavericks",
               "Tulsa Oilers", "1:1,0:0,1:0", "5:7,10:10,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Rapid City Rush",
               "Colorado Eagles", "0:1,1:3,0:1", "6:17,6:9,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Alaska Aces",
               "Idaho Steelheads", "0:1,0:0,0:1", "8:6,16:12,10:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/23/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Manchester Monarchs",
               "Adirondack Thunder", "0:1,1:0,1:0", "9:14,16:11,11:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Atlanta Gladiators",
               "Evansville IceMen", "0:2,3:0,0:2", "15:8,19:12,3:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "South Carolina Stingrays",
               "Greenville Swamp Rabbits", "1:0,2:3,0:1", "11:13,7:8,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Toledo Walleye",
               "Utah Grizzlies", "0:1,2:1,1:3", "3:9,9:5,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Norfolk Admirals",
               "Elmira Jackals", "0:1,1:1,1:1", "3:12,19:10,24:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Indy Fuel",
               "Quad City Mallards", "1:0,0:0,2:1", "10:4,5:12,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Cincinnati Cyclones",
               "Fort Wayne Komets", "0:0,4:2,2:2", "11:7,14:11,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Wheeling Nailers",
               "Kalamazoo Wings", "0:1,1:0,0:3", "11:14,10:4,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Missouri Mavericks",
               "Tulsa Oilers", "1:0,1:1,1:5", "8:5,10:15,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Wichita Thunder",
               "Allen Americans", "0:1,1:0,0:2", "8:7,13:10,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Rapid City Rush",
               "Colorado Eagles", "0:2,1:0,1:2", "8:10,6:14,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Alaska Aces",
               "Idaho Steelheads", "0:1,0:2,1:0", "17:11,10:8,11:7", 0, False)

print("Inserting " + leaguename + " Game Data From 1/24/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160124,
               "Manchester Monarchs",
               "Adirondack Thunder",
               "0:2,1:0,1:0,1:0",
               "10:11,10:10,14:7,1:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Indy Fuel",
               "Fort Wayne Komets", "0:1,1:0,2:0", "10:19,13:9,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Allen Americans",
               "Wichita Thunder", "0:1,1:0,4:3", "2:9,12:6,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Toledo Walleye",
               "Utah Grizzlies", "2:0,0:2,3:0", "11:9,8:8,9:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Alaska Aces",
               "Idaho Steelheads", "2:1,1:0,0:1", "16:10,13:12,9:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/25/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160125,
               "Reading Royals",
               "Brampton Beast",
               "0:1,1:1,1:0,0:1",
               "14:9,9:13,12:10,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/26/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160126,
               "Missouri Mavericks",
               "Evansville IceMen",
               "1:3,3:1,1:1,1:0",
               "10:14,9:9,11:6,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Tulsa Oilers",
               "Allen Americans", "1:0,1:0,0:0", "14:10,19:6,10:9", 0, False)

print("Inserting " + leaguename + " Game Data From 1/27/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Orlando Solar Bears",
               "Manchester Monarchs", "0:1,0:1,0:1", "5:16,9:8,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Elmira Jackals",
               "Reading Royals", "1:1,3:4,1:2", "8:17,16:20,15:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Cincinnati Cyclones",
               "Indy Fuel", "2:0,0:0,1:1", "7:5,10:10,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Wichita Thunder",
               "Evansville IceMen", "3:1,0:1,1:0", "13:9,9:12,3:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Colorado Eagles",
               "Utah Grizzlies", "2:0,2:1,2:2", "9:7,10:12,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Idaho Steelheads",
               "Rapid City Rush", "1:0,3:2,1:0", "12:8,13:9,11:10", 0, False)

print("Inserting " + leaguename + " Game Data From 1/28/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160128, "Orlando Solar Bears",
               "Manchester Monarchs", "0:0,0:3,1:0", "6:7,13:19,21:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/29/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Kalamazoo Wings",
               "Quad City Mallards", "0:1,5:1,1:3", "10:11,14:9,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Adirondack Thunder",
               "Reading Royals", "0:0,2:0,1:0", "12:10,10:18,6:14", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Orlando Solar Bears",
               "Manchester Monarchs",
               "0:2,3:0,0:1,0:0,0:1",
               "11:14,11:10,7:7,4:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Elmira Jackals",
               "Wheeling Nailers", "0:1,1:1,0:2", "14:7,15:8,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Toledo Walleye",
               "Brampton Beast", "2:0,2:0,0:0", "8:12,13:6,8:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Norfolk Admirals",
               "South Carolina Stingrays",
               "4:0,1:1,3:1",
               "14:6,5:12,9:10",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Florida Everblades",
               "Greenville Swamp Rabbits",
               "0:2,3:0,1:0",
               "8:11,11:10,8:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Indy Fuel",
               "Evansville IceMen", "4:0,2:0,1:3", "12:5,15:10,3:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Atlanta Gladiators",
               "Idaho Steelheads", "0:0,0:2,1:2", "9:9,6:13,16:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Fort Wayne Komets",
               "Cincinnati Cyclones", "2:0,0:0,2:1", "12:9,9:9,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Allen Americans",
               "Tulsa Oilers", "0:0,4:0,3:1", "16:5,11:9,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Missouri Mavericks",
               "Wichita Thunder", "2:0,0:1,0:0", "8:6,10:8,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Utah Grizzlies",
               "Rapid City Rush", "1:0,3:1,0:0", "17:12,18:11,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Colorado Eagles",
               "Alaska Aces", "1:2,2:0,2:0", "8:12,15:4,8:14", 0, False)

print("Inserting " + leaguename + " Game Data From 1/30/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Adirondack Thunder",
               "Reading Royals", "0:1,1:0,1:2", "10:9,7:11,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Florida Everblades",
               "Greenville Swamp Rabbits", "1:0,0:2,0:0", "12:5,7:7,7:4", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Elmira Jackals",
               "Wheeling Nailers",
               "1:2,2:1,0:0,0:0,1:0",
               "9:13,13:15,12:11,4:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Atlanta Gladiators",
               "Idaho Steelheads",
               "1:0,0:1,0:0,0:0,0:1",
               "7:9,6:9,11:7,3:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Norfolk Admirals",
               "South Carolina Stingrays",
               "1:2,0:2,0:2",
               "15:9,11:12,12:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Toledo Walleye",
               "Fort Wayne Komets", "0:0,1:1,1:0", "5:7,9:13,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Indy Fuel",
               "Evansville IceMen", "1:0,0:1,2:1", "10:7,7:16,11:14", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Cincinnati Cyclones",
               "Quad City Mallards",
               "0:2,1:0,1:0,1:0",
               "14:5,14:4,13:3,1:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Tulsa Oilers",
               "Allen Americans", "1:0,2:0,2:2", "16:9,7:11,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Missouri Mavericks",
               "Wichita Thunder", "2:0,1:1,2:1", "14:9,10:10,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Utah Grizzlies",
               "Rapid City Rush", "3:1,2:2,0:1", "13:6,15:10,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Colorado Eagles",
               "Alaska Aces", "2:0,4:0,1:2", "8:8,15:13,9:11", 0, False)

print("Inserting " + leaguename + " Game Data From 1/31/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Brampton Beast",
               "Wheeling Nailers", "1:0,1:0,0:2,0:1", "9:7,9:9,3:14,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Atlanta Gladiators",
               "Idaho Steelheads", "1:1,1:1,0:3", "13:9,13:14,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Kalamazoo Wings",
               "Fort Wayne Komets", "1:2,1:0,0:4", "6:17,13:5,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Allen Americans",
               "Tulsa Oilers", "2:0,0:1,0:0", "7:1,6:14,6:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160131,
               "Toledo Walleye",
               "Quad City Mallards",
               "2:0,0:2,0:0,1:0",
               "9:11,3:12,7:8,1:0",
               0,
               False)

print("Database Check Return: " +
      str(sqlcon.execute("PRAGMA integrity_check(100);").fetchone()[0]) + "\n")

sqlcon.close()

print("DONE! All Game Data Inserted.")

print("DONE! " + leaguename + " Database Created.")
