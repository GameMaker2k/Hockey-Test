#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sqlite3
import sys

leaguename = "AHL"
getforday = "9"
getformonth = "10"
getforyear = "2015"

print("Creating " + leaguename + " Database.")

if (len(sys.argv) == 0):
    sqlcon = sqlite3.connect("./ahl15-16.db3")
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


MakeHockeyDivisions((sqlcur, sqlcon), "Atlantic", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "North", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "Central", "Western")
MakeHockeyDivisions((sqlcur, sqlcon), "Pacific", "Western")

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
print("Inserting " + leaguename + " Teams From Atlantic Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Bridgeport",
                "CT",
                "Sound Tigers",
                "Eastern",
                "Atlantic",
                "Webster Bank Arena",
                "Bridgeport",
                "ECHL:Missouri Mavericks,NHL:New York Islanders")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Hartford",
                "CT",
                "Wolf Pack",
                "Eastern",
                "Atlantic",
                "XL Center",
                "Hartford",
                "ECHL:Greenville Swamp Rabbits,NHL:New York Rangers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Hershey",
                "PA",
                "Bears",
                "Eastern",
                "Atlantic",
                "Giant Center",
                "Hershey",
                "ECHL:South Carolina Stingrays,NHL:Washington Capitals")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Allentown",
                "PA",
                "Phantoms",
                "Eastern",
                "Atlantic",
                "PPL Center",
                "Lehigh Valley",
                "ECHL:Reading Royals,NHL:Philadelphia Flyers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Portland",
                "ME",
                "Pirates",
                "Eastern",
                "Atlantic",
                "Cross Insurance Arena",
                "Portland",
                "ECHL:None,NHL:Florida Panthers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Providence",
                "RI",
                "Bruins",
                "Eastern",
                "Atlantic",
                "Dunkin' Donuts Center",
                "Providence",
                "ECHL:Atlanta Gladiators,NHL:Boston Bruins")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Springfield",
                "MA",
                "Falcons",
                "Eastern",
                "Atlantic",
                "MassMutual Center",
                "Springfield",
                "ECHL:Rapid City Rush,NHL:Arizona Coyotes")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Wilkes-Barre",
                "PA",
                "Penguins",
                "Eastern",
                "Atlantic",
                "Mohegan Sun Arena",
                "Wilkes-Barre/Scranton",
                "ECHL:Wheeling Nailers,NHL:Pittsburgh Penguins")

print("Inserting " + leaguename + " Teams From North Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Albany",
                "NY",
                "Devils",
                "Eastern",
                "North",
                "Times Union Center",
                "Albany",
                "ECHL:None,NHL:New Jersey Devils")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Binghamton",
                "NY",
                "Senators",
                "Eastern",
                "North",
                "Floyd L. Maines Veterans Memorial Arena",
                "Binghamton",
                "ECHL:Evansville IceMen,NHL:Ottawa Senators")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Rochester",
                "NY",
                "Americans",
                "Eastern",
                "North",
                "Blue Cross Arena",
                "Rochester",
                "ECHL:Elmira Jackals,NHL:Buffalo Sabres")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "St. John's",
                "NL",
                "IceCaps",
                "Eastern",
                "North",
                "Mile One Centre",
                "St. John's",
                "ECHL:Brampton Beast,NHL:Montreal Canadiens")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Syracuse",
                "NY",
                "Crunch",
                "Eastern",
                "North",
                "Oncenter War Memorial Arena",
                "Syracuse",
                "ECHL:None,NHL:Tampa Bay Lightning")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Toronto",
                "ON",
                "Marlies",
                "Eastern",
                "North",
                "Ricoh Coliseum",
                "Toronto",
                "ECHL:Orlando Solar Bears,NHL: 	Toronto Maple Leafs")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Utica",
                "NY",
                "Comets",
                "Eastern",
                "North",
                "Utica Memorial Auditorium",
                "Utica",
                "ECHL:None,NHL:Vancouver Canucks")

print("Inserting " + leaguename + " Teams From Western Conference.")
print("Inserting " + leaguename + " Teams From Central Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Charlotte",
                "NC",
                "Checkers",
                "Western",
                "Central",
                "Bojangles Coliseum",
                "Charlotte",
                "ECHL:Florida Everblades,NHL:Carolina Hurricanes")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Rosemont",
                "IL",
                "Wolves",
                "Western",
                "Central",
                "Allstate Arena",
                "Chicago",
                "ECHL:None,NHL:St. Louis Blues")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Grand Rapids",
                "MI",
                "Griffins",
                "Western",
                "Central",
                "Van Andel Arena",
                "Grand Rapids",
                "ECHL:Toledo Walleye,NHL:Detroit Red Wings")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Des Moines",
                "IA",
                "Wild",
                "Western",
                "Central",
                "Wells Fargo Arena",
                "Iowa",
                "ECHL:Quad City Mallards,NHL:Minnesota Wild")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Cleveland",
                "OH",
                "Monsters",
                "Western",
                "Central",
                "Quicken Loans Arena",
                "Lake Erie",
                "ECHL:Kalamazoo Wings,NHL:Columbus Blue Jackets")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Winnipeg",
                "MB",
                "Moose",
                "Western",
                "Central",
                "MTS Centre",
                "Manitoba",
                "ECHL:Tulsa Oilers,NHL:Winnipeg Jets")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Milwaukee",
                "WI",
                "Admirals",
                "Western",
                "Central",
                "BMO Harris Bradley Center",
                "Milwaukee",
                "ECHL:Cincinnati Cyclones,NHL:Nashville Predators")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Rockford",
                "IL",
                "IceHogs",
                "Western",
                "Central",
                "BMO Harris Bank Center",
                "Rockford",
                "ECHL:Indy Fuel,NHL:Chicago Blackhawks")

print("Inserting " + leaguename + " Teams From Pacific Division.\n")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Bakersfield",
                "CA",
                "Condors",
                "Western",
                "Pacific",
                "Rabobank Arena",
                "Bakersfield",
                "ECHL:Norfolk Admirals,NHL:Edmonton Oilers")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Ontario",
                "CA",
                "Reign",
                "Western",
                "Pacific",
                "Citizens Business Bank Arena",
                "Ontario",
                "ECHL:Manchester Monarchs,NHL:Los Angeles Kings")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "San Antonio",
                "TX",
                "Rampage",
                "Western",
                "Pacific",
                "AT&T Center",
                "San Antonio",
                "ECHL:Fort Wayne Komets,NHL:Colorado Avalanche")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "San Diego",
                "CA",
                "Gulls",
                "Western",
                "Pacific",
                "Valley View Casino Center",
                "San Diego",
                "ECHL:Utah Grizzlies,NHL:Anaheim Ducks")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "San Jose",
                "CA",
                "Barracuda",
                "Western",
                "Pacific",
                "SAP Center",
                "San Jose",
                "ECHL:Allen Americans,NHL:San Jose Sharks")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Stockton",
                "CA",
                "Heat",
                "Western",
                "Pacific",
                "Stockton Arena",
                "Stockton",
                "ECHL:Adirondack Thunder,NHL:Calgary Flames")
MakeHockeyTeams((sqlcur,
                 sqlcon),
                "Cedar Park",
                "TX",
                "Stars",
                "Western",
                "Pacific",
                "Cedar Park Center",
                "Texas",
                "ECHL:Idaho Steelheads,NHL:Dallas Stars")

MakeHockeyArena((sqlcur, sqlcon), "West Sacramento",
                "CA", "Raley Field", "West Sacramento")
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


print("Database Check Return: " +
      str(sqlcon.execute("PRAGMA integrity_check(100);").fetchone()[0]) + "\n")

sqlcon.close()

print("DONE! All Game Data Inserted.")

print("DONE! " + leaguename + " Database Created.")
