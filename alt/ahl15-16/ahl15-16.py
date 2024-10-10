#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sqlite3
import sys

leaguename = "AHL"
getforday = "24"
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
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
                      leaguename + "Teams WHERE id=" + str(teamid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
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
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
                      leaguename + "Games WHERE id=" + str(gameid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
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
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
                      leaguename + "Arenas WHERE id=" + str(arenaid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " +
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
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename +
                      "Conferences WHERE Conference=\"" + str(conference) + "\"").fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT " + dataname + " FROM " + leaguename +
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


print("Inserting " + leaguename + " Game Data From 10/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Toronto Marlies",
               "Manitoba Moose", "1:1,3:1,1:1", "11:6,17:9,6:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151009,
               "Providence Bruins",
               "Wilkes-Barre/Scranton Penguins",
               "0:0,0:1,1:0,0:1",
               "17:9,13:12,10:16,1:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Rochester Americans",
               "Lake Erie Monsters", "3:1,0:2,3:0", "12:9,6:15,6:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Bakersfield Condors",
               "Grand Rapids Griffins", "0:0,0:0,1:0", "14:12,13:4,13:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "San Jose Barracuda",
               "Rockford IceHogs", "1:2,1:0,0:2", "13:14,10:14,9:13", 0, False)

print("Inserting " + leaguename + " Game Data From 10/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Toronto Marlies", "Manitoba Moose",
               "0:1,2:0,0:1,0:0,1:0", "20:6,13:10,5:12,3:1,1:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151010,
               "Bridgeport Sound Tigers",
               "Wilkes-Barre/Scranton Penguins",
               "1:0,1:1,2:0",
               "11:10,12:11,5:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Hartford Wolf Pack",
               "St. John's IceCaps", "0:1,0:1,1:1", "10:8,11:13,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Springfield Falcons",
               "Hershey Bears", "1:2,0:2,0:1", "7:8,2:17,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Binghamton Senators",
               "Albany Devils", "1:1,1:0,2:0", "10:16,10:12,12:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Lehigh Valley Phantoms",
               "Syracuse Crunch", "1:3,1:1,1:0", "9:16,8:7,12:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Rochester Americans",
               "Utica Comets", "0:0,2:0,0:1", "7:12,11:10,4:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Chicago Wolves",
               "Milwaukee Admirals", "3:1,2:0,0:0", "10:9,12:3,15:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Iowa Wild",
               "Charlotte Checkers", "0:2,1:0,0:2", "6:19,9:11,8:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151010,
               "Texas Stars",
               "San Antonio Rampage",
               "0:2,1:1,3:1,1:0",
               "7:12,8:10,12:15,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Bakersfield Condors",
               "Ontario Reign", "0:2,0:3,0:0", "7:12,10:20,4:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "San Diego Gulls",
               "Grand Rapids Griffins", "1:0,1:0,2:2", "7:15,17:6,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Stockton Heat",
               "Rockford IceHogs", "4:0,1:0,2:0", "15:8,8:3,8:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Providence Bruins",
               "Portland Pirates", "2:0,1:3,3:1", "11:4,4:21,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Bridgeport Sound Tigers",
               "St. John's IceCaps", "1:0,0:1,5:0", "6:10,10:11,13:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Iowa Wild", "Charlotte Checkers",
               "1:1,2:0,1:3,0:0,0:1", "12:10,3:17,5:11,3:6,0:1", 0, False)

print("Inserting " + leaguename + " Game Data From 10/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Bridgeport Sound Tigers",
               "Springfield Falcons", "1:0,1:2,3:1", "9:8,7:13,12:12", 0, False)

print("Inserting " + leaguename + " Game Data From 10/14/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151014,
               "Hartford Wolf Pack",
               "Providence Bruins",
               "1:0,2:3,0:0,1:0",
               "9:16,11:8,5:12,5:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Manitoba Moose",
               "Ontario Reign", "0:1,0:1,1:2", "3:6,7:9,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Stockton Heat",
               "San Jose Barracuda", "0:0,0:3,1:1", "5:4,7:11,14:10", 0, False)

print("Inserting " + leaguename + " Game Data From 10/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151016, "St. John's IceCaps",
               "Rochester Americans", "1:1,2:0,2:1", "10:8,12:12,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Grand Rapids Griffins",
               "San Antonio Rampage", "1:1,1:0,0:2", "16:6,12:14,13:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Lake Erie Monsters",
               "Iowa Wild", "0:0,1:1,3:0", "20:7,15:11,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Springfield Falcons",
               "Lehigh Valley Phantoms", "0:1,1:1,0:2", "5:11,12:8,3:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Providence Bruins",
               "Bridgeport Sound Tigers", "2:2,2:2,0:1", "8:7,8:7,6:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Chicago Wolves",
               "Texas Stars", "0:2,2:2,1:3", "8:11,12:11,6:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Milwaukee Admirals",
               "Charlotte Checkers", "0:1,0:2,2:4", "9:11,6:11,9:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151016,
               "San Diego Gulls",
               "Bakersfield Condors",
               "3:3,2:2,0:0,0:0,1:0",
               "17:10,9:14,9:13,5:2,1:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Toronto Marlies",
               "Albany Devils", "1:1,0:1,1:0,1:0", "11:11,8:7,14:3,4:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151017,
               "Wilkes-Barre/Scranton Penguins",
               "Lehigh Valley Phantoms",
               "1:3,4:0,1:1",
               "13:7,9:7,9:12",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151017,
               "Lake Erie Monsters",
               "Iowa Wild",
               "0:0,0:0,0:0,0:0,0:1",
               "11:5,16:5,6:6,4:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "St. John's IceCaps",
               "Rochester Americans", "2:0,0:1,4:1", "14:8,9:9,13:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Bridgeport Sound Tigers",
               "Providence Bruins", "1:1,0:0,2:0", "8:13,7:7,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Grand Rapids Griffins",
               "San Antonio Rampage", "0:3,0:0,0:1", "11:15,12:11,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Hartford Wolf Pack",
               "Utica Comets", "1:0,0:0,2:0", "14:11,6:11,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Portland Pirates",
               "Hershey Bears", "0:1,3:1,0:0", "8:7,10:4,6:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Syracuse Crunch",
               "Binghamton Senators", "1:0,0:1,1:0", "8:7,12:9,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Chicago Wolves",
               "Charlotte Checkers", "5:2,2:0,2:3", "14:11,6:6,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Manitoba Moose",
               "Ontario Reign", "0:0,0:0,0:0,0:1", "5:14,8:6,6:18,1:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Rockford IceHogs",
               "Texas Stars", "1:2,0:1,1:2", "8:14,9:11,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Bakersfield Condors",
               "San Jose Barracuda", "0:1,2:1,1:2", "13:7,10:4,10:11", 0, False)

print("Inserting " + leaguename + " Game Data From 10/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Portland Pirates",
               "Hershey Bears", "1:0,3:1,1:1", "8:7,11:9,9:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Toronto Marlies",
               "Albany Devils", "0:0,2:2,0:1", "12:9,10:17,6:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151018,
               "Bridgeport Sound Tigers",
               "Wilkes-Barre/Scranton Penguins",
               "0:2,1:2,0:1",
               "9:11,14:9,13:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Hartford Wolf Pack",
               "Syracuse Crunch", "0:1,2:0,3:1", "7:9,17:9,9:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Rockford IceHogs",
               "Texas Stars", "0:3,0:1,2:3", "11:10,8:10,17:10", 0, False)

print("Inserting " + leaguename + " Game Data From 10/20/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151020,
               "St. John's IceCaps",
               "Binghamton Senators",
               "0:0,3:2,1:2,0:1",
               "9:14,9:7,10:14,0:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151020,
               "Iowa Wild",
               "Milwaukee Admirals",
               "0:0,2:0,0:2,0:1",
               "6:10,11:9,7:14,1:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151021, "St. John's IceCaps",
               "Binghamton Senators", "3:0,0:2,0:0", "11:16,5:14,5:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Grand Rapids Griffins",
               "Charlotte Checkers", "1:1,1:0,2:2", "16:10,9:8,10:22", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Utica Comets",
               "Rochester Americans", "1:1,1:0,2:1", "19:6,13:5,15:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Rockford IceHogs",
               "Iowa Wild", "0:0,2:1,1:1", "16:6,9:4,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Texas Stars",
               "Stockton Heat", "0:0,0:0,0:1", "13:11,11:11,12:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151021,
               "San Jose Barracuda",
               "San Diego Gulls",
               "2:1,0:1,0:0,0:0,0:1",
               "12:5,6:14,7:10,2:2,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Manitoba Moose",
               "Lake Erie Monsters", "1:0,0:2,0:1", "9:13,2:15,7:8", 0, False)

print("Inserting " + leaguename + " Game Data From 10/23/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Grand Rapids Griffins",
               "Charlotte Checkers", "0:1,0:0,1:2", "12:11,10:6,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Portland Pirates",
               "Albany Devils", "0:2,2:0,2:0", "9:10,11:7,7:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151023,
               "Springfield Falcons",
               "Wilkes-Barre/Scranton Penguins",
               "0:0,0:2,0:3",
               "17:11,10:6,11:15",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Syracuse Crunch",
               "Hartford Wolf Pack", "1:1,0:2,2:1", "15:6,8:16,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Utica Comets",
               "Hershey Bears", "0:0,0:0,0:1", "8:6,6:12,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Providence Bruins",
               "Lehigh Valley Phantoms", "1:0,2:2,2:1", "8:10,8:14,13:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Rochester Americans",
               "Toronto Marlies", "1:3,1:2,0:3", "9:15,7:10,7:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151023,
               "Rockford IceHogs",
               "Chicago Wolves",
               "2:0,0:1,1:2,0:0,1:0",
               "7:13,6:9,6:14,5:0,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Ontario Reign",
               "Bakersfield Condors", "0:2,4:1,1:1", "10:12,16:11,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "San Jose Barracuda",
               "San Diego Gulls", "0:2,0:1,0:0", "8:10,5:15,10:9", 0, False)

print("Inserting " + leaguename + " Game Data From 10/24/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Albany Devils",
               "Portland Pirates", "0:0,2:0,1:1", "12:5,12:8,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "St. John's IceCaps",
               "Bridgeport Sound Tigers", "3:2,2:0,0:2", "11:14,9:6,6:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151024,
               "Hershey Bears",
               "Hartford Wolf Pack",
               "0:0,1:1,1:1,1:0",
               "7:3,7:9,15:12,2:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Utica Comets",
               "Syracuse Crunch", "2:0,1:0,1:0", "12:9,7:8,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Binghamton Senators",
               "Toronto Marlies", "2:0,1:0,2:1", "13:9,11:9,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Lehigh Valley Phantoms",
               "Providence Bruins", "1:0,1:1,1:0", "10:9,8:7,7:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151024,
               "Wilkes-Barre/Scranton Penguins",
               "Springfield Falcons",
               "1:1,0:1,1:0,1:0",
               "5:15,11:14,9:6,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Iowa Wild",
               "Texas Stars", "2:1,0:0,1:1", "10:8,4:13,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Manitoba Moose",
               "Lake Erie Monsters", "0:1,0:0,0:1", "12:13,8:6,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Milwaukee Admirals",
               "Rockford IceHogs", "1:0,0:2,1:2", "9:13,9:10,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "San Antonio Rampage",
               "Stockton Heat", "2:0,3:0,0:1", "12:7,13:6,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Ontario Reign",
               "San Jose Barracuda", "1:0,0:0,2:0", "12:5,9:10,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Bakersfield Condors",
               "San Diego Gulls", "1:0,1:0,1:0", "7:8,10:6,4:10", 0, False)

print("Inserting " + leaguename + " Game Data From 10/25/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151025,
               "St. John's IceCaps",
               "Bridgeport Sound Tigers",
               "0:0,0:0,2:2,0:0,0:1",
               "6:9,2:17,16:10,3:1,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Albany Devils",
               "Binghamton Senators", "0:1,2:0,2:0", "16:11,11:6,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Chicago Wolves",
               "Charlotte Checkers", "1:0,2:0,0:0", "8:7,12:6,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Iowa Wild",
               "Texas Stars", "0:1,1:1,0:2", "11:19,8:10,11:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151025,
               "Hershey Bears",
               "Hartford Wolf Pack",
               "1:1,0:0,1:1,0:0,0:1",
               "7:9,10:6,7:10,2:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Lehigh Valley Phantoms",
               "Toronto Marlies", "1:3,0:0,0:0", "5:14,8:8,9:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151025,
               "Rochester Americans",
               "Syracuse Crunch",
               "1:0,1:2,1:1,0:0,1:0",
               "19:9,9:12,7:9,5:3,1:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/27/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151027,
               "Rockford IceHogs",
               "Charlotte Checkers",
               "0:0,0:0,1:1,0:0,0:1",
               "9:8,18:10,6:9,4:2,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Milwaukee Admirals", "Texas Stars",
               "0:1,1:1,2:1,0:0,1:0", "14:10,11:5,15:11,6:2,1:0", 0, False)

print("Inserting " + leaguename + " Game Data From 10/28/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151028,
               "Springfield Falcons",
               "Bridgeport Sound Tigers",
               "1:1,1:0,3:0",
               "14:10,9:14,6:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Toronto Marlies",
               "Syracuse Crunch", "1:1,0:1,0:1", "13:7,6:15,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Lehigh Valley Phantoms",
               "St. John's IceCaps", "1:1,3:0,1:0", "14:3,10:8,4:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151028,
               "Wilkes-Barre/Scranton Penguins",
               "Binghamton Senators",
               "1:0,2:3,1:0",
               "6:13,10:10,15:6",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 10/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Lake Erie Monsters",
               "Charlotte Checkers", "1:0,2:1,0:1", "13:13,11:14,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Milwaukee Admirals",
               "Manitoba Moose", "2:2,0:1,0:0", "13:9,10:20,18:4", 0, False)

print("Inserting " + leaguename + " Game Data From 10/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Albany Devils",
               "Bridgeport Sound Tigers", "2:1,0:1,0:1", "3:11,7:3,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Springfield Falcons",
               "Rochester Americans", "2:1,1:0,3:0", "9:10,17:6,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Syracuse Crunch",
               "Hershey Bears", "0:1,2:0,2:0", "8:11,18:10,6:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151030,
               "Toronto Marlies",
               "Grand Rapids Griffins",
               "2:0,2:0,2:1",
               "13:12,10:17,11:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Binghamton Senators",
               "Utica Comets", "2:2,1:2,2:3", "10:12,8:8,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Lehigh Valley Phantoms",
               "St. John's IceCaps", "0:0,1:2,1:1", "10:12,7:6,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Providence Bruins",
               "Portland Pirates", "2:3,2:0,2:1", "10:18,11:10,15:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Wilkes-Barre/Scranton Penguins",
               "Hartford Wolf Pack", "1:1,1:0,2:0", "6:12,14:14,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Chicago Wolves",
               "Manitoba Moose", "0:0,1:0,2:1", "10:11,8:2,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Rockford IceHogs",
               "Iowa Wild", "1:0,2:0,1:0", "8:6,16:9,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Texas Stars",
               "Bakersfield Condors", "1:2,3:1,1:1", "10:12,16:9,10:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151030,
               "Ontario Reign",
               "San Antonio Rampage",
               "0:0,1:1,1:1,0:1",
               "12:12,7:4,14:8,4:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "San Diego Gulls", "Stockton Heat",
               "0:0,2:1,0:1,0:0,1:0", "8:9,11:10,6:12,1:2,1:0", 0, False)

print("Inserting " + leaguename + " Game Data From 10/31/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Portland Pirates",
               "Rochester Americans", "1:0,1:3,1:1", "8:9,13:11,19:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Albany Devils",
               "Utica Comets", "1:0,2:1,3:0", "9:5,9:6,6:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151031,
               "Ontario Reign",
               "San Antonio Rampage",
               "0:1,0:0,1:0,0:1",
               "21:4,8:4,7:11,2:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Hershey Bears",
               "St. John's IceCaps", "0:1,1:1,3:0", "5:14,14:7,11:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151031,
               "Lake Erie Monsters",
               "Charlotte Checkers",
               "2:1,1:2,2:2,0:0,0:1",
               "8:11,8:11,8:8,0:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151031,
               "Hartford Wolf Pack",
               "Providence Bruins",
               "1:1,0:0,0:0,1:0",
               "2:5,10:7,11:6,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Iowa Wild", "Milwaukee Admirals",
               "0:1,2:0,0:1,1:0", "6:12,16:13,2:17,6:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "San Diego Gulls",
               "Stockton Heat", "1:1,0:0,2:1", "8:11,16:11,12:14", 0, False)

print("Inserting " + leaguename + " Game Data From 11/1/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Albany Devils",
               "Toronto Marlies", "2:2,0:0,0:0,0:1", "6:4,4:9,12:7,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Providence Bruins",
               "Springfield Falcons", "1:1,1:0,0:4", "8:7,13:8,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Bridgeport Sound Tigers",
               "Utica Comets", "1:1,1:1,0:0,1:0", "9:7,9:6,9:5,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Chicago Wolves",
               "Manitoba Moose", "0:0,1:0,1:0", "5:10,18:4,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Hartford Wolf Pack",
               "Rochester Americans", "1:2,1:1,0:0", "11:10,5:9,8:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151101,
               "Hershey Bears",
               "Lehigh Valley Phantoms",
               "0:1,2:3,2:0,0:0,0:1",
               "8:17,10:8,13:12,2:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Iowa Wild",
               "Rockford IceHogs", "0:1,0:0,0:1", "17:8,12:13,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "San Jose Barracuda",
               "Ontario Reign", "1:1,1:1,2:0", "10:13,9:9,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Texas Stars",
               "Bakersfield Condors", "1:2,1:0,2:0", "12:13,7:7,11:17", 0, False)

print("Inserting " + leaguename + " Game Data From 11/3/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151103,
               "San Diego Gulls",
               "San Antonio Rampage",
               "1:0,1:0,0:2,1:0",
               "10:12,8:9,14:10,5:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 11/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Bridgeport Sound Tigers",
               "Hershey Bears", "1:1,0:1,1:2", "13:7,9:7,19:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Hartford Wolf Pack",
               "Toronto Marlies", "0:1,0:0,0:4", "11:8,11:6,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Utica Comets",
               "Portland Pirates", "2:1,1:1,0:0", "6:13,8:5,8:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151104,
               "Wilkes-Barre/Scranton Penguins",
               "St. John's IceCaps",
               "1:1,4:0,0:1",
               "10:12,7:10,5:21",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 11/5/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Iowa Wild",
               "Milwaukee Admirals", "0:1,0:1,0:1", "7:11,5:12,11:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Ontario Reign",
               "San Diego Gulls", "1:0,3:1,0:0", "10:7,9:12,6:2", 0, False)

print("Inserting " + leaguename + " Game Data From 11/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Grand Rapids Griffins",
               "Rockford IceHogs", "1:1,0:1,0:2", "11:10,16:3,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Syracuse Crunch",
               "Albany Devils", "0:1,2:1,1:2", "9:10,11:9,10:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Utica Comets", "Toronto Marlies",
               "2:2,0:1,2:1,0:0,0:1", "13:10,11:8,6:10,6:6,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Lehigh Valley Phantoms",
               "Hershey Bears", "1:1,0:1,1:2", "8:12,11:9,3:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Rochester Americans",
               "Binghamton Senators", "1:0,2:1,0:0", "14:8,8:9,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Wilkes-Barre/Scranton Penguins",
               "St. John's IceCaps", "0:1,1:0,3:0", "6:11,12:5,12:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Portland Pirates",
               "Springfield Falcons", "0:1,0:3,1:2", "11:6,10:10,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Milwaukee Admirals",
               "Lake Erie Monsters", "1:0,1:0,1:1", "7:11,11:8,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "San Antonio Rampage",
               "Chicago Wolves", "1:0,2:2,0:1,0:1", "9:11,17:12,11:8,3:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Stockton Heat",
               "Bakersfield Condors", "0:0,0:2,1:0", "9:9,6:13,17:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151107, "San Jose Barracuda",
               "San Diego Gulls", "0:2,1:0,1:1", "6:11,15:9,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Bridgeport Sound Tigers",
               "Springfield Falcons", "0:0,1:0,3:0", "6:14,20:6,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Charlotte Checkers",
               "Manitoba Moose", "0:0,0:1,0:2", "9:6,10:8,11:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151107,
               "Hershey Bears",
               "St. John's IceCaps",
               "3:0,0:2,0:1,0:0,0:1",
               "16:9,11:15,7:12,4:1,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151107,
               "Syracuse Crunch",
               "Lehigh Valley Phantoms",
               "2:0,0:1,0:0",
               "11:8,10:11,12:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Utica Comets",
               "Providence Bruins", "3:1,1:0,1:0", "10:7,6:10,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Binghamton Senators",
               "Toronto Marlies", "0:0,0:3,1:3", "12:14,11:15,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Hartford Wolf Pack",
               "Albany Devils", "0:1,0:3,0:0", "5:9,7:11,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Iowa Wild", "Lake Erie Monsters",
               "1:1,0:1,1:0,0:0,0:1", "12:16,10:10,12:7,3:2,0:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151107,
               "Rockford IceHogs",
               "Milwaukee Admirals",
               "1:1,0:1,1:0,0:1",
               "15:12,10:12,11:12,1:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Texas Stars",
               "San Antonio Rampage", "0:0,1:3,2:1", "17:7,11:9,20:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Stockton Heat",
               "Ontario Reign", "0:3,0:1,0:0", "12:11,18:12,8:6", 0, False)

print("Inserting " + leaguename + " Game Data From 11/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Charlotte Checkers",
               "Manitoba Moose", "2:0,0:0,1:2", "13:2,13:8,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Iowa Wild",
               "Lake Erie Monsters", "2:1,0:2,0:0", "8:5,7:8,1:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Bridgeport Sound Tigers",
               "Hartford Wolf Pack", "0:0,1:0,0:0", "3:10,9:8,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "San Antonio Rampage",
               "Chicago Wolves", "1:0,0:0,2:3,0:1", "12:5,12:9,7:10,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Lehigh Valley Phantoms",
               "Binghamton Senators", "0:1,1:1,0:2", "10:6,14:10,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "San Jose Barracuda",
               "Bakersfield Condors", "2:3,0:2,0:1", "18:10,10:15,14:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Milwaukee Admirals",
               "Lake Erie Monsters", "3:0,1:2,2:1", "11:6,12:11,13:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Bridgeport Sound Tigers",
               "Providence Bruins", "0:0,2:2,2:1", "7:11,12:12,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Grand Rapids Griffins",
               "Iowa Wild", "1:1,3:1,1:0", "8:9,9:8,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Portland Pirates",
               "Hartford Wolf Pack", "2:1,2:1,2:0", "11:9,8:12,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Binghamton Senators",
               "Lehigh Valley Phantoms", "2:3,1:2,0:1", "16:11,6:14,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Texas Stars",
               "San Antonio Rampage", "4:0,1:1,1:2", "14:5,14:15,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Ontario Reign",
               "San Jose Barracuda", "2:0,0:1,0:0", "11:5,8:5,4:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "San Diego Gulls",
               "Bakersfield Condors", "3:0,1:0,2:1", "10:9,8:13,5:9", 0, False)

print("Inserting " + leaguename + " Game Data From 11/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Manitoba Moose",
               "Chicago Wolves", "1:2,1:1,1:2", "13:8,10:4,13:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151113, "St. John's IceCaps",
               "Toronto Marlies", "0:0,1:0,1:2,1:0", "6:8,7:16,14:13,2:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "Lake Erie Monsters",
               "Grand Rapids Griffins",
               "1:0,1:1,0:1,0:0,1:0",
               "11:3,7:11,15:8,1:1,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Portland Pirates",
               "Hartford Wolf Pack", "1:0,2:1,0:1", "13:9,8:10,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Springfield Falcons",
               "Utica Comets", "4:1,1:0,1:2", "18:7,11:8,5:15", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "Syracuse Crunch",
               "Binghamton Senators",
               "1:2,0:1,2:0,1:0",
               "5:15,6:10,8:9,3:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Lehigh Valley Phantoms",
               "Rochester Americans", "2:0,3:1,2:0", "11:6,13:16,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Providence Bruins",
               "Albany Devils", "0:2,1:1,1:1", "4:7,8:2,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Wilkes-Barre/Scranton Penguins",
               "Hershey Bears", "1:0,3:0,3:0", "10:7,9:13,13:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Charlotte Checkers",
               "Milwaukee Admirals", "1:1,1:2,1:1", "12:13,5:13,15:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Iowa Wild",
               "Rockford IceHogs", "0:1,2:2,0:2", "9:10,13:18,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Manitoba Moose",
               "Chicago Wolves", "1:1,0:1,1:0,1:0", "10:10,8:9,11:4,2:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "San Antonio Rampage",
               "Stockton Heat",
               "2:1,1:1,1:2,0:0,1:0",
               "10:13,9:10,12:9,3:6,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151113,
               "San Diego Gulls",
               "San Jose Barracuda",
               "2:0,0:2,1:1,0:0,0:1",
               "10:4,6:13,10:9,4:3,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 11/14/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "St. John's IceCaps",
               "Toronto Marlies",
               "1:3,5:1,2:4,0:1",
               "16:13,15:10,6:15,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Hershey Bears",
               "Bridgeport Sound Tigers", "0:2,0:2,0:1", "4:7,14:8,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Lake Erie Monsters",
               "Grand Rapids Griffins", "3:0,2:0,0:1", "15:7,9:14,6:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Syracuse Crunch",
               "Utica Comets", "0:0,1:1,1:0", "14:19,8:13,6:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Binghamton Senators",
               "Springfield Falcons", "1:1,1:0,1:3", "9:13,12:10,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Lehigh Valley Phantoms",
               "Albany Devils", "0:1,0:0,1:0,0:1", "3:14,5:7,14:6,0:2", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151114,
               "Wilkes-Barre/Scranton Penguins",
               "Rochester Americans",
               "0:0,2:0,1:1",
               "16:4,16:4,10:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Charlotte Checkers",
               "Milwaukee Admirals", "0:2,0:1,1:0", "10:9,8:11,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Iowa Wild",
               "Rockford IceHogs", "1:1,2:2,0:1", "8:9,13:8,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Texas Stars",
               "Stockton Heat", "0:3,2:0,1:2", "12:16,15:6,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Bakersfield Condors",
               "Ontario Reign", "2:0,0:0,1:0", "9:10,9:5,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "San Diego Gulls",
               "San Jose Barracuda", "0:2,1:2,2:0", "8:6,6:13,21:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/15/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151115,
               "Providence Bruins",
               "Portland Pirates",
               "1:1,0:0,1:1,0:0,0:1",
               "8:6,12:3,5:3,2:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151115,
               "Hartford Wolf Pack",
               "Wilkes-Barre/Scranton Penguins",
               "5:1,0:5,1:0,0:1",
               "14:7,6:21,10:6,0:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Hershey Bears",
               "Rochester Americans", "0:0,1:0,2:1", "12:2,9:11,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "San Antonio Rampage",
               "Texas Stars", "2:0,0:1,1:0", "11:13,8:16,8:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Springfield Falcons",
               "Albany Devils", "1:0,0:0,0:1,1:0", "11:9,11:15,13:6,2:4", 0, False)

print("Inserting " + leaguename + " Game Data From 11/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151117, "San Antonio Rampage",
               "Texas Stars", "1:0,4:0,0:2", "12:8,15:7,2:9", 0, False)

print("Inserting " + leaguename + " Game Data From 11/18/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151118,
               "Bakersfield Condors",
               "San Jose Barracuda",
               "1:0,0:0,0:1,0:0,1:0",
               "5:5,7:18,13:13,3:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Grand Rapids Griffins",
               "Rockford IceHogs", "0:0,2:1,1:1", "14:12,10:9,10:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Syracuse Crunch",
               "Portland Pirates", "0:2,0:1,1:1", "6:10,10:10,5:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151118,
               "Rochester Americans",
               "Toronto Marlies",
               "0:0,0:0,0:0,0:1",
               "10:11,7:12,6:13,0:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Milwaukee Admirals",
               "Chicago Wolves", "0:0,3:3,2:0", "10:12,16:14,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Stockton Heat",
               "San Diego Gulls", "1:0,0:0,3:0", "16:9,14:5,10:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151120, "St. John's IceCaps",
               "Syracuse Crunch", "0:0,2:1,1:2,1:0", "11:7,6:18,8:21,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Albany Devils",
               "Springfield Falcons", "1:0,0:0,3:0", "4:10,11:16,13:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Grand Rapids Griffins",
               "San Diego Gulls", "4:1,0:1,3:2", "13:9,9:16,18:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Hershey Bears",
               "Portland Pirates", "0:1,1:0,2:1", "9:8,8:6,15:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Utica Comets",
               "Hartford Wolf Pack", "1:2,0:1,1:0", "15:7,8:11,8:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151120,
               "Binghamton Senators",
               "Wilkes-Barre/Scranton Penguins",
               "2:0,0:1,1:0",
               "7:16,11:18,13:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Providence Bruins",
               "Lehigh Valley Phantoms", "0:1,1:1,0:2", "11:11,9:6,10:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151120,
               "Rochester Americans",
               "Bridgeport Sound Tigers",
               "1:0,1:1,0:1,1:0",
               "9:9,8:8,3:8,2:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Iowa Wild",
               "Lake Erie Monsters", "0:0,1:1,1:2", "10:12,10:15,13:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Manitoba Moose",
               "Bakersfield Condors", "1:1,0:0,0:1", "11:13,8:11,14:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151120,
               "Milwaukee Admirals",
               "Rockford IceHogs",
               "0:0,0:0,1:1,0:0,1:0",
               "8:9,9:7,9:12,7:1,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "San Antonio Rampage",
               "Ontario Reign", "0:2,1:1,2:0,0:1", "7:13,12:8,11:17,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Texas Stars",
               "Charlotte Checkers", "2:0,0:2,4:0", "13:3,14:12,10:14", 0, False)

print("Inserting " + leaguename + " Game Data From 11/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Iowa Wild",
               "Lake Erie Monsters", "1:1,1:1,0:1", "8:11,5:14,8:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151121,
               "Albany Devils",
               "Wilkes-Barre/Scranton Penguins",
               "0:0,1:3,2:2",
               "3:10,14:11,11:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Toronto Marlies",
               "Rochester Americans", "1:0,1:0,3:1", "6:11,15:12,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "St. John's IceCaps",
               "Syracuse Crunch", "0:0,1:1,0:0,0:1", "7:14,8:13,12:3,3:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Hartford Wolf Pack",
               "Lehigh Valley Phantoms", "2:0,0:1,1:0", "9:10,12:9,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Hershey Bears",
               "Portland Pirates", "3:0,1:0,0:2", "13:5,6:9,11:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Springfield Falcons",
               "Providence Bruins", "0:1,1:1,0:2", "4:11,6:10,11:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151121,
               "Utica Comets",
               "Bridgeport Sound Tigers",
               "1:0,1:2,0:2",
               "10:12,9:10,6:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Chicago Wolves",
               "Grand Rapids Griffins", "0:1,0:0,1:1", "10:6,8:4,10:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Milwaukee Admirals",
               "San Diego Gulls", "1:1,1:0,1:0", "16:10,11:12,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Texas Stars",
               "Ontario Reign", "2:4,2:2,2:1", "13:13,13:9,11:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Hartford Wolf Pack",
               "Utica Comets", "2:0,0:2,0:1", "7:11,7:10,4:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Manitoba Moose",
               "Bakersfield Condors", "1:1,1:0,1:0", "11:11,6:11,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Toronto Marlies",
               "Binghamton Senators", "1:2,3:0,2:2", "4:10,22:10,14:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Providence Bruins",
               "Lehigh Valley Phantoms", "0:1,1:1,1:3", "15:4,8:9,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Bridgeport Sound Tigers",
               "Springfield Falcons", "0:1,0:0,0:1", "11:13,19:9,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Chicago Wolves",
               "Iowa Wild", "0:0,0:1,2:0", "7:4,16:3,19:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Rockford IceHogs",
               "Lake Erie Monsters", "1:0,0:0,2:1", "14:14,10:7,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "San Antonio Rampage",
               "Charlotte Checkers", "1:0,2:1,0:3", "6:10,7:9,5:10", 0, False)

print("Inserting " + leaguename + " Game Data From 11/24/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Charlotte Checkers",
               "San Jose Barracuda", "3:0,0:0,0:1", "9:7,5:16,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Milwaukee Admirals",
               "San Antonio Rampage", "2:1,2:2,2:0", "6:7,13:8,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Bakersfield Condors",
               "Texas Stars", "1:1,0:2,0:0", "10:10,14:13,7:7", 0, False)

print("Inserting " + leaguename + " Game Data From 11/25/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Albany Devils",
               "Bridgeport Sound Tigers", "2:0,0:1,1:0", "16:6,12:5,2:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Charlotte Checkers",
               "San Jose Barracuda", "0:2,1:0,0:1", "4:12,12:2,4:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Grand Rapids Griffins",
               "Iowa Wild", "1:0,3:0,1:1", "13:7,14:6,11:16", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Hershey Bears",
               "Providence Bruins",
               "1:1,0:0,0:0,1:0",
               "6:16,4:6,8:6,3:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Lake Erie Monsters",
               "Manitoba Moose", "1:0,2:1,1:1", "9:4,14:11,20:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Utica Comets",
               "Lehigh Valley Phantoms",
               "1:0,4:0,2:1",
               "9:12,13:7,11:9",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Binghamton Senators",
               "Wilkes-Barre/Scranton Penguins",
               "1:2,1:0,1:1,0:1",
               "12:8,3:20,3:9,3:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Rochester Americans",
               "Syracuse Crunch", "2:1,1:0,0:2,1:0", "10:14,10:8,8:9,1:2", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151125,
               "Rockford IceHogs",
               "San Antonio Rampage",
               "0:1,2:0,0:1,1:0",
               "10:15,17:5,8:7,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Ontario Reign",
               "Stockton Heat", "2:1,0:0,0:0", "12:4,7:9,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "San Diego Gulls",
               "Texas Stars", "0:2,0:2,3:1", "6:7,6:17,8:11", 0, False)

print("Inserting " + leaguename + " Game Data From 11/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Albany Devils",
               "Binghamton Senators", "2:0,2:0,0:0", "11:1,18:4,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Lake Erie Monsters",
               "Manitoba Moose", "0:1,3:0,1:0", "4:10,12:9,15:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Portland Pirates",
               "Utica Comets", "0:1,0:0,1:3", "7:6,8:4,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Syracuse Crunch",
               "Toronto Marlies", "0:1,0:2,1:0", "1:5,7:15,9:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151127,
               "Lehigh Valley Phantoms",
               "Hershey Bears",
               "2:2,2:1,1:2,0:0,1:0",
               "9:8,16:8,4:10,5:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151127,
               "Rochester Americans",
               "St. John's IceCaps",
               "1:0,1:3,1:0,0:0,1:0",
               "11:6,8:14,13:8,2:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Wilkes-Barre/Scranton Penguins",
               "Providence Bruins", "1:0,1:0,1:0", "12:5,12:10,6:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Hartford Wolf Pack",
               "Springfield Falcons", "0:1,0:0,0:1", "8:8,21:3,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Milwaukee Admirals",
               "Grand Rapids Griffins", "0:2,0:1,0:3", "4:10,11:14,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Rockford IceHogs",
               "Chicago Wolves", "1:0,2:1,0:0", "10:4,13:7,11:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "San Diego Gulls",
               "Ontario Reign", "1:0,2:1,0:1", "11:6,10:9,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Stockton Heat",
               "Bakersfield Condors", "2:4,2:2,1:0", "20:13,12:8,17:4", 0, False)

print("Inserting " + leaguename + " Game Data From 11/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Toronto Marlies",
               "St. John's IceCaps", "1:1,1:2,0:3", "8:7,8:16,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "San Jose Barracuda",
               "Texas Stars", "0:1,4:2,1:1", "10:9,12:10,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Bridgeport Sound Tigers",
               "Hartford Wolf Pack", "1:1,2:1,2:0", "14:5,14:14,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Charlotte Checkers",
               "Iowa Wild", "0:3,1:1,6:0", "5:15,12:2,8:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151128,
               "Grand Rapids Griffins",
               "Lake Erie Monsters",
               "1:1,1:1,0:0,1:0",
               "15:10,9:16,6:16,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Portland Pirates",
               "Utica Comets", "1:3,2:1,0:2", "11:15,14:10,9:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Springfield Falcons",
               "Albany Devils", "1:2,1:1,1:1", "9:16,7:15,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Binghamton Senators",
               "Rochester Americans", "0:3,1:3,4:0", "9:11,12:7,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Lehigh Valley Phantoms",
               "Providence Bruins", "0:0,0:1,0:2", "6:11,5:11,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Wilkes-Barre/Scranton Penguins",
               "Hershey Bears", "0:0,3:1,0:1", "8:9,14:4,11:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Chicago Wolves",
               "San Antonio Rampage", "1:1,0:0,0:3", "11:5,10:12,4:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Milwaukee Admirals",
               "Rockford IceHogs", "1:1,0:0,1:0", "4:15,9:2,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Ontario Reign",
               "San Diego Gulls", "0:1,0:2,1:0", "7:5,9:14,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Bakersfield Condors",
               "Stockton Heat", "1:2,0:1,1:0", "10:18,9:9,13:6", 0, False)

print("Inserting " + leaguename + " Game Data From 11/29/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151129,
               "Charlotte Checkers",
               "Iowa Wild",
               "0:0,1:0,0:1,0:0,1:0",
               "12:10,8:5,12:7,5:1,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Toronto Marlies",
               "St. John's IceCaps", "0:3,1:0,0:2", "7:13,18:13,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Chicago Wolves",
               "San Antonio Rampage", "0:0,0:1,1:2", "5:10,9:10,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Bridgeport Sound Tigers",
               "Syracuse Crunch", "0:1,0:2,0:1", "9:11,7:14,15:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Springfield Falcons",
               "Portland Pirates", "0:1,1:0,1:5", "7:15,11:11,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151129, "San Jose Barracuda",
               "Texas Stars", "0:1,2:2,0:0", "8:9,13:10,14:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/1/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Milwaukee Admirals",
               "Manitoba Moose", "1:2,1:1,0:0", "14:8,8:8,10:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/2/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151202,
               "Albany Devils",
               "St. John's IceCaps",
               "1:1,0:0,0:0,1:0",
               "10:7,10:5,13:4,5:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Utica Comets",
               "Lehigh Valley Phantoms", "0:1,0:0,1:2", "12:4,9:9,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Chicago Wolves",
               "Manitoba Moose", "3:0,1:1,4:1", "15:12,3:12,10:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151202,
               "Texas Stars",
               "Rockford IceHogs",
               "2:1,2:3,1:1,0:1",
               "14:12,8:18,13:11,2:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/3/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Lake Erie Monsters",
               "Iowa Wild", "1:0,1:2,0:2", "14:10,7:14,12:7", 0, False)

print("Inserting " + leaguename + " Game Data From 12/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Grand Rapids Griffins",
               "Chicago Wolves", "0:1,3:0,0:0", "11:7,11:13,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Lake Erie Monsters",
               "Iowa Wild", "0:1,0:0,3:0", "7:9,3:5,12:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Springfield Falcons",
               "Bridgeport Sound Tigers",
               "2:0,1:0,1:0",
               "13:10,10:14,13:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Syracuse Crunch",
               "Binghamton Senators", "2:0,0:0,3:1", "7:7,16:10,6:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Utica Comets",
               "St. John's IceCaps",
               "0:1,1:0,0:0,0:1",
               "12:4,13:6,5:3,1:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Providence Bruins",
               "Portland Pirates",
               "0:0,1:1,1:1,1:0",
               "4:11,10:16,14:6,3:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Rochester Americans",
               "Toronto Marlies", "0:0,0:3,0:1", "7:12,8:14,7:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Wilkes-Barre/Scranton Penguins",
               "Lehigh Valley Phantoms",
               "1:0,0:2,0:1",
               "10:9,16:8,10:5",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151204,
               "Hartford Wolf Pack",
               "Hershey Bears",
               "2:1,1:1,0:1,0:0,1:0",
               "11:10,2:9,9:14,3:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "San Antonio Rampage",
               "Rockford IceHogs", "1:0,1:3,0:1", "8:8,3:15,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Bakersfield Condors",
               "San Diego Gulls", "3:1,2:0,1:3", "10:14,14:11,8:20", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "San Jose Barracuda",
               "Stockton Heat", "3:1,1:1,1:1", "7:12,8:13,3:21", 0, False)

print("Inserting " + leaguename + " Game Data From 12/5/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151205,
               "San Jose Barracuda",
               "Bakersfield Condors",
               "4:1,1:3,1:2,1:0",
               "11:10,6:13,10:6,2:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Albany Devils",
               "Rochester Americans", "1:0,1:0,0:1", "12:6,12:7,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Toronto Marlies",
               "Manitoba Moose", "0:0,0:0,3:1", "13:9,12:6,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Bridgeport Sound Tigers",
               "Portland Pirates", "0:0,1:0,0:2", "6:13,14:9,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Charlotte Checkers",
               "Ontario Reign", "0:0,0:2,1:1", "8:16,3:20,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Grand Rapids Griffins",
               "Lake Erie Monsters", "1:0,1:0,2:1", "6:9,4:17,7:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Hershey Bears",
               "Lehigh Valley Phantoms", "0:1,0:0,2:0", "14:5,13:5,17:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Syracuse Crunch",
               "Utica Comets", "1:0,1:0,0:4", "6:15,8:6,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Binghamton Senators",
               "St. John's IceCaps", "1:1,1:0,2:0", "9:13,6:5,15:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Providence Bruins",
               "Springfield Falcons", "1:0,1:0,1:1", "17:10,15:9,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Wilkes-Barre/Scranton Penguins",
               "Hartford Wolf Pack", "1:1,0:1,0:1", "12:7,13:7,4:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151205,
               "Chicago Wolves",
               "Milwaukee Admirals",
               "0:1,0:1,2:0,0:0,0:1",
               "6:10,9:7,17:4,7:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Stockton Heat",
               "San Diego Gulls", "1:0,1:2,2:0", "16:12,13:5,15:8", 0, False)

print("Inserting " + leaguename + " Game Data From 12/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Toronto Marlies",
               "Manitoba Moose", "3:0,2:0,4:0", "12:7,16:8,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Providence Bruins",
               "Springfield Falcons", "1:0,4:1,1:0", "14:6,16:13,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Milwaukee Admirals",
               "Texas Stars", "1:1,2:1,2:0", "10:7,6:10,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Albany Devils",
               "Syracuse Crunch", "1:0,2:0,1:0", "10:7,7:9,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Bridgeport Sound Tigers",
               "Hartford Wolf Pack", "0:0,3:2,1:0", "12:10,9:12,3:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Charlotte Checkers",
               "Ontario Reign", "0:1,1:2,0:2", "15:9,7:12,12:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151206,
               "Hershey Bears",
               "Wilkes-Barre/Scranton Penguins",
               "1:0,1:0,2:1",
               "17:9,6:6,10:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "San Antonio Rampage",
               "Rockford IceHogs", "2:2,0:2,0:1", "13:17,11:9,11:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Iowa Wild",
               "Chicago Wolves", "1:1,0:2,2:2", "12:9,12:13,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Texas Stars",
               "Rockford IceHogs", "1:1,1:2,1:2", "19:9,19:9,14:14", 0, False)

print("Inserting " + leaguename + " Game Data From 12/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Grand Rapids Griffins",
               "Milwaukee Admirals", "1:1,0:0,3:0", "9:9,10:5,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Portland Pirates",
               "Springfield Falcons", "2:1,3:0,0:0", "9:8,9:13,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Lehigh Valley Phantoms",
               "Hershey Bears", "0:1,0:1,2:0,1:0", "11:7,4:8,12:4,4:2", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151209,
               "Rochester Americans",
               "Utica Comets",
               "0:1,3:2,0:0,0:0,0:1",
               "6:13,19:8,4:15,5:4,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Wilkes-Barre/Scranton Penguins",
               "Syracuse Crunch", "3:0,0:1,3:1", "12:7,13:13,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "San Antonio Rampage",
               "Charlotte Checkers", "0:2,0:0,2:1", "5:10,3:11,14:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151210, "San Antonio Rampage",
               "Stockton Heat", "2:1,0:1,0:1", "7:11,11:20,7:11", 0, False)

print("Inserting " + leaguename + " Game Data From 12/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151211, "St. John's IceCaps",
               "Rochester Americans", "1:0,0:1,0:2", "22:4,11:15,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Albany Devils",
               "Syracuse Crunch", "0:0,2:1,1:0", "11:6,11:9,5:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Lake Erie Monsters",
               "Chicago Wolves", "2:0,1:1,1:2", "11:10,12:10,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Portland Pirates",
               "Bridgeport Sound Tigers", "0:0,1:0,0:3", "13:7,6:10,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Springfield Falcons",
               "Binghamton Senators", "1:0,1:2,2:1", "11:7,7:13,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Utica Comets",
               "Toronto Marlies", "0:0,0:0,0:2", "8:9,9:13,10:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151211,
               "Lehigh Valley Phantoms",
               "Wilkes-Barre/Scranton Penguins",
               "0:2,0:1,0:1",
               "6:8,12:6,5:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Providence Bruins",
               "Hartford Wolf Pack", "1:1,1:0,1:0", "8:17,14:9,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Rockford IceHogs",
               "Iowa Wild", "1:0,0:0,1:1", "16:6,15:5,9:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151211,
               "Texas Stars",
               "Charlotte Checkers",
               "2:3,2:0,0:1,0:1",
               "12:10,19:4,14:12,0:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Bakersfield Condors",
               "San Diego Gulls", "1:0,1:0,1:0", "10:10,8:11,8:10", 0, False)

print("Inserting " + leaguename + " Game Data From 12/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151212, "San Jose Barracuda",
               "San Diego Gulls", "0:3,0:0,0:2", "10:12,14:7,8:7", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "St. John's IceCaps",
               "Rochester Americans",
               "0:0,2:1,0:1,0:1",
               "10:11,12:11,6:11,0:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Hartford Wolf Pack",
               "Bridgeport Sound Tigers", "0:0,2:1,2:1", "9:5,9:7,8:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Hershey Bears",
               "Binghamton Senators", "4:0,0:2,1:1", "16:13,6:14,10:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "Portland Pirates",
               "Providence Bruins",
               "1:0,1:1,0:1,1:0",
               "9:10,9:8,13:5,1:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Syracuse Crunch",
               "Toronto Marlies", "1:3,0:0,2:0,0:1", "8:18,8:8,17:9,2:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "Lehigh Valley Phantoms",
               "Springfield Falcons",
               "2:1,0:1,2:2,0:0,1:0",
               "11:9,8:14,18:10,1:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Wilkes-Barre/Scranton Penguins",
               "Albany Devils", "1:0,2:0,1:0", "7:9,14:6,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Lake Erie Monsters",
               "Chicago Wolves", "1:0,1:1,0:0", "13:6,5:9,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Manitoba Moose",
               "Milwaukee Admirals", "1:1,2:0,0:1", "8:8,9:10,4:14", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151212,
               "Rockford IceHogs",
               "Grand Rapids Griffins",
               "1:1,0:0,0:3",
               "15:11,10:13,14:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Texas Stars",
               "Stockton Heat", "2:0,2:1,1:1", "16:12,12:7,8:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Ontario Reign",
               "Bakersfield Condors", "1:0,2:1,0:0", "11:6,10:8,10:5", 0, False)

print("Inserting " + leaguename + " Game Data From 12/13/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151213,
               "Manitoba Moose",
               "Milwaukee Admirals",
               "1:1,1:1,1:1,0:0,0:1",
               "7:5,7:19,11:8,3:5,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Toronto Marlies",
               "Utica Comets", "1:1,2:2,1:1,0:1", "7:6,10:9,6:10,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Providence Bruins",
               "Hartford Wolf Pack", "2:0,0:1,2:1", "12:8,13:7,8:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151213,
               "Bridgeport Sound Tigers",
               "Hershey Bears",
               "0:0,1:0,0:1,0:0,0:1",
               "9:10,9:10,12:6,3:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151213,
               "Iowa Wild",
               "Grand Rapids Griffins",
               "1:0,2:1,0:2,0:1",
               "11:11,14:11,6:7,1:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "San Antonio Rampage",
               "Texas Stars", "1:1,1:1,0:1", "7:17,12:14,14:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151213,
               "Ontario Reign",
               "San Jose Barracuda",
               "0:1,0:0,1:0,1:0",
               "11:10,7:7,6:3,2:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151215, "St. John's IceCaps",
               "Albany Devils", "1:1,2:0,0:1", "10:11,10:14,11:21", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Charlotte Checkers",
               "Iowa Wild", "1:0,1:0,1:3,0:1", "7:11,5:10,11:7,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Milwaukee Admirals",
               "Chicago Wolves", "1:0,0:1,1:0", "8:6,4:10,10:8", 0, False)

print("Inserting " + leaguename + " Game Data From 12/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151216, "St. John's IceCaps",
               "Albany Devils", "3:0,1:1,1:0", "12:7,7:18,4:21", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Lake Erie Monsters",
               "Grand Rapids Griffins", "0:1,1:2,1:0", "14:15,18:6,17:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Portland Pirates",
               "Springfield Falcons", "3:0,0:0,2:2", "11:12,7:9,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Utica Comets",
               "Rochester Americans", "2:0,2:2,1:0", "12:10,14:6,12:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Binghamton Senators",
               "Toronto Marlies", "0:1,0:2,2:0", "5:9,7:12,10:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151216,
               "Lehigh Valley Phantoms",
               "Wilkes-Barre/Scranton Penguins",
               "0:1,0:1,0:1",
               "3:11,5:5,9:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Manitoba Moose",
               "San Antonio Rampage", "1:1,1:0,3:0", "13:10,13:11,10:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Stockton Heat",
               "Bakersfield Condors", "0:1,0:1,2:1", "13:8,18:7,15:8", 0, False)

print("Inserting " + leaguename + " Game Data From 12/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Chicago Wolves", "Texas Stars",
               "3:0,0:0,0:3,0:0,1:0", "12:11,8:12,12:13,5:4,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Charlotte Checkers",
               "Iowa Wild", "2:0,0:0,1:2", "9:4,13:8,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Manitoba Moose",
               "San Antonio Rampage", "0:1,1:1,2:0", "7:10,15:13,4:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Grand Rapids Griffins",
               "Texas Stars", "1:2,1:1,3:1", "15:8,12:13,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Springfield Falcons",
               "Utica Comets", "3:1,0:3,1:3", "11:8,12:17,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Syracuse Crunch",
               "Binghamton Senators", "1:0,1:0,2:0", "10:10,8:7,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Lehigh Valley Phantoms",
               "Hershey Bears", "2:3,2:0,2:1", "16:8,11:7,9:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151218,
               "Providence Bruins",
               "Bridgeport Sound Tigers",
               "0:0,2:1,0:1,1:0",
               "7:17,16:4,13:9,2:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Rochester Americans",
               "Hartford Wolf Pack", "1:0,2:0,4:1", "9:10,11:8,12:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151218,
               "Wilkes-Barre/Scranton Penguins",
               "Toronto Marlies",
               "2:0,0:0,1:3,0:0,0:1",
               "15:11,16:7,8:6,3:6,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Milwaukee Admirals",
               "Rockford IceHogs", "0:0,1:3,1:3", "8:7,10:14,15:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151218,
               "San Diego Gulls",
               "San Jose Barracuda",
               "0:0,2:1,0:1,1:0",
               "10:12,9:11,11:8,1:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 12/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Bridgeport Sound Tigers",
               "Portland Pirates", "1:2,0:0,0:0", "8:14,11:8,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Charlotte Checkers",
               "Lake Erie Monsters", "0:0,3:1,1:0", "11:5,15:13,7:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Grand Rapids Griffins",
               "Texas Stars", "1:0,2:0,3:1", "9:11,14:7,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Hershey Bears",
               "Toronto Marlies", "1:1,1:3,0:2", "8:7,9:12,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Springfield Falcons",
               "Providence Bruins", "0:0,2:1,2:1", "10:14,11:13,7:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151219,
               "Syracuse Crunch",
               "Wilkes-Barre/Scranton Penguins",
               "0:1,0:0,0:2",
               "17:3,6:10,7:10",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151219,
               "Utica Comets",
               "Hartford Wolf Pack",
               "1:1,0:0,0:0,0:0,0:1",
               "6:8,7:8,11:13,2:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Binghamton Senators",
               "Lehigh Valley Phantoms", "0:0,1:0,1:1", "12:9,11:5,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Stockton Heat",
               "Bakersfield Condors", "0:1,1:0,2:1", "18:11,12:8,8:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Rochester Americans",
               "Albany Devils", "4:0,0:0,0:1", "12:9,8:11,4:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151219,
               "Chicago Wolves",
               "Rockford IceHogs",
               "2:1,0:0,1:2,1:0",
               "14:13,4:9,15:13,6:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Milwaukee Admirals",
               "Manitoba Moose", "1:2,3:1,3:2", "8:7,16:11,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Ontario Reign", "San Diego Gulls",
               "1:1,0:1,1:0,0:0,0:1", "12:8,10:9,7:1,0:5,0:1", 0, False)

print("Inserting " + leaguename + " Game Data From 12/20/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151220,
               "Charlotte Checkers",
               "Lake Erie Monsters",
               "2:1,1:1,0:1,1:0",
               "12:6,12:6,6:12,3:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Iowa Wild",
               "San Antonio Rampage", "1:1,1:1,0:1", "13:8,7:15,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Bridgeport Sound Tigers",
               "Portland Pirates", "0:0,0:0,0:3", "4:16,6:7,13:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151220,
               "Hershey Bears",
               "Syracuse Crunch",
               "0:3,2:0,2:1,1:0",
               "6:8,21:5,16:3,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151220,
               "Ontario Reign",
               "Bakersfield Condors",
               "0:0,0:1,1:0,1:0",
               "5:4,10:11,10:5,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "San Jose Barracuda",
               "Stockton Heat", "0:2,4:1,1:1", "6:11,14:10,11:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Chicago Wolves",
               "Manitoba Moose", "2:0,1:1,1:0", "14:5,9:11,6:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Iowa Wild",
               "San Antonio Rampage", "1:0,0:1,0:1", "11:6,7:12,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Rockford IceHogs",
               "Milwaukee Admirals", "0:1,0:3,2:2", "12:8,8:8,19:11", 0, False)

print("Inserting " + leaguename + " Game Data From 12/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Portland Pirates",
               "Providence Bruins", "1:1,0:0,3:1", "12:7,14:3,9:9", 0, False)

print("Inserting " + leaguename + " Game Data From 12/26/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Toronto Marlies",
               "St. John's IceCaps", "0:0,2:0,3:2", "9:8,14:10,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Albany Devils",
               "Providence Bruins", "1:0,0:0,3:1", "9:8,8:9,10:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151226,
               "Hershey Bears",
               "Wilkes-Barre/Scranton Penguins",
               "3:0,2:0,0:0",
               "15:7,6:6,7:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Lake Erie Monsters",
               "Grand Rapids Griffins", "1:3,2:2,0:2", "12:8,11:5,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Syracuse Crunch",
               "Springfield Falcons", "0:1,2:0,1:0", "12:12,7:8,4:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Binghamton Senators",
               "Hartford Wolf Pack", "2:1,1:1,1:0", "9:11,10:10,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Lehigh Valley Phantoms",
               "Bridgeport Sound Tigers", "0:1,0:1,1:0", "9:11,5:13,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Rochester Americans",
               "Utica Comets", "1:1,0:1,0:1", "9:15,12:7,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Chicago Wolves",
               "Iowa Wild", "0:1,0:1,1:0", "8:15,10:9,9:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151226,
               "Rockford IceHogs",
               "Milwaukee Admirals",
               "0:0,1:1,0:0,0:0,0:1",
               "7:9,15:9,9:3,3:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Texas Stars",
               "San Antonio Rampage", "0:2,2:1,2:2", "11:10,19:4,18:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Bakersfield Condors",
               "Stockton Heat", "2:0,2:1,1:2", "10:13,17:4,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "San Diego Gulls",
               "Ontario Reign", "1:1,1:0,2:0", "9:11,6:13,6:6", 0, False)

print("Inserting " + leaguename + " Game Data From 12/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Toronto Marlies",
               "St. John's IceCaps", "1:1,2:1,1:3", "7:14,12:6,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Utica Comets",
               "Syracuse Crunch", "1:1,2:1,1:0", "13:7,10:4,8:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151227,
               "Wilkes-Barre/Scranton Penguins",
               "Lehigh Valley Phantoms",
               "0:1,0:1,0:1",
               "13:7,8:5,14:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Bridgeport Sound Tigers",
               "Providence Bruins", "0:1,4:1,0:1", "10:11,12:14,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Hershey Bears",
               "Binghamton Senators", "1:1,1:2,1:2", "9:12,9:3,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Lake Erie Monsters",
               "Grand Rapids Griffins", "2:0,0:1,1:1", "15:6,8:10,2:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "San Antonio Rampage",
               "Texas Stars", "0:2,1:1,1:0", "14:13,14:16,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Springfield Falcons",
               "Portland Pirates", "0:1,0:3,1:1", "7:10,13:17,16:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Rochester Americans",
               "Hartford Wolf Pack", "0:0,0:0,0:1", "8:7,7:8,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Iowa Wild",
               "Rockford IceHogs", "2:1,0:0,1:0", "9:9,3:9,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Bakersfield Condors",
               "San Diego Gulls", "0:0,2:0,2:1", "6:8,11:11,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "San Jose Barracuda",
               "Stockton Heat", "2:0,2:1,1:0", "14:10,15:10,6:12", 0, False)

print("Inserting " + leaguename + " Game Data From 12/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151228, "San Jose Barracuda",
               "Charlotte Checkers", "0:0,1:0,0:4", "6:12,4:11,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Milwaukee Admirals",
               "Chicago Wolves", "2:1,1:0,1:0", "9:11,8:7,12:18", 0, False)

print("Inserting " + leaguename + " Game Data From 12/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Hartford Wolf Pack",
               "Portland Pirates", "2:0,1:0,2:2", "13:8,14:10,12:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Hershey Bears",
               "Syracuse Crunch", "0:0,1:2,0:1", "12:1,14:8,4:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Lake Erie Monsters",
               "Toronto Marlies", "0:0,1:0,1:1", "8:7,9:8,13:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151229,
               "Binghamton Senators",
               "Lehigh Valley Phantoms",
               "0:1,0:0,1:0,0:0,1:0",
               "8:17,15:11,14:9,3:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Milwaukee Admirals",
               "Grand Rapids Griffins", "0:0,2:0,1:0", "8:11,10:8,7:11", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151229,
               "Texas Stars",
               "San Antonio Rampage",
               "2:1,1:1,1:2,1:0",
               "9:9,15:15,10:12,3:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Stockton Heat",
               "Ontario Reign", "0:0,0:2,1:0", "11:16,12:18,17:10", 0, False)

print("Inserting " + leaguename + " Game Data From 12/30/2015.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20151230,
               "San Jose Barracuda",
               "Charlotte Checkers",
               "1:1,0:0,1:1,0:0,1:0",
               "13:12,10:11,7:6,4:4,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Albany Devils",
               "Utica Comets", "1:1,1:0,0:1,1:0", "5:10,8:13,11:3,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Springfield Falcons",
               "Providence Bruins", "1:1,1:2,1:1", "14:9,8:8,18:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151230,
               "Rochester Americans",
               "St. John's IceCaps",
               "1:0,1:2,0:0,0:0,1:0",
               "10:6,7:15,11:4,2:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Rockford IceHogs",
               "Chicago Wolves", "2:0,1:1,2:1", "12:13,11:9,11:8", 0, False)

print("Inserting " + leaguename + " Game Data From 12/31/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Toronto Marlies",
               "Lake Erie Monsters", "2:2,1:0,0:0", "10:10,12:4,8:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20151231,
               "Hershey Bears",
               "Lehigh Valley Phantoms",
               "0:1,0:1,1:1",
               "12:18,10:5,6:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Manitoba Moose",
               "Iowa Wild", "0:1,4:2,0:0", "8:17,15:16,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Portland Pirates",
               "Providence Bruins", "0:0,1:2,3:1", "8:14,7:9,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Utica Comets",
               "Albany Devils", "1:1,0:1,0:2", "9:7,7:14,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Wilkes-Barre/Scranton Penguins",
               "Syracuse Crunch", "1:2,1:1,0:1", "9:7,5:5,16:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Grand Rapids Griffins",
               "Milwaukee Admirals", "0:0,1:0,2:0", "15:8,9:7,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Binghamton Senators",
               "St. John's IceCaps", "2:0,1:2,0:0", "12:13,13:5,9:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Texas Stars",
               "San Diego Gulls", "3:0,2:0,1:1", "17:9,14:10,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Ontario Reign",
               "Stockton Heat", "0:1,0:0,1:3", "6:4,6:6,15:9", 0, False)

print("Inserting " + leaguename + " Game Data From 1/1/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Springfield Falcons",
               "Bridgeport Sound Tigers", "2:0,0:0,0:1", "9:8,11:9,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Manitoba Moose", "Iowa Wild",
               "2:1,1:1,0:1,0:0,0:1", "12:12,5:12,7:13,4:1,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "San Antonio Rampage",
               "San Diego Gulls", "0:0,1:2,0:1", "9:15,8:11,8:9", 0, False)

print("Inserting " + leaguename + " Game Data From 1/2/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Toronto Marlies",
               "Syracuse Crunch", "0:1,2:1,1:0", "12:4,13:11,10:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Bridgeport Sound Tigers",
               "Rochester Americans",
               "0:0,3:2,0:1,1:0",
               "5:10,19:16,9:11,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Hartford Wolf Pack",
               "Albany Devils", "2:1,0:1,1:2", "19:6,6:17,8:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Hershey Bears",
               "Binghamton Senators",
               "1:2,2:3,2:0,1:0",
               "12:9,10:13,9:8,1:3",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Portland Pirates",
               "Lehigh Valley Phantoms",
               "2:1,1:2,0:0,1:0",
               "12:12,10:12,9:7,1:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Stockton Heat", "Texas Stars",
               "2:3,2:3,2:0,0:0,1:0", "12:15,10:11,15:7,7:2,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Utica Comets",
               "St. John's IceCaps", "1:2,0:0,0:1", "5:5,9:6,13:4", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Wilkes-Barre/Scranton Penguins",
               "Springfield Falcons",
               "1:1,3:0,0:0",
               "7:11,13:10,10:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Chicago Wolves",
               "Rockford IceHogs", "0:0,0:0,2:0", "8:11,7:12,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Milwaukee Admirals",
               "Lake Erie Monsters", "2:1,0:0,1:0", "10:11,8:8,6:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Ontario Reign",
               "Charlotte Checkers", "0:2,2:1,0:1", "16:7,9:4,12:3", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160102,
               "Bakersfield Condors",
               "San Jose Barracuda",
               "1:1,3:3,0:0,0:0,0:1",
               "4:11,11:11,3:12,3:8,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/3/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Hartford Wolf Pack",
               "Wilkes-Barre/Scranton Penguins",
               "0:1,1:2,1:0",
               "5:13,9:15,10:6",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Manitoba Moose",
               "Grand Rapids Griffins", "0:2,0:0,1:2", "6:21,12:7,8:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Toronto Marlies",
               "Syracuse Crunch",
               "1:1,0:0,1:1,1:0",
               "11:11,9:0,13:12,2:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Portland Pirates",
               "Lehigh Valley Phantoms",
               "0:1,0:1,1:0",
               "10:9,10:11,18:4",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Bridgeport Sound Tigers",
               "Hershey Bears", "0:1,0:2,0:2", "7:12,13:13,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Chicago Wolves",
               "Lake Erie Monsters", "2:0,1:1,2:1", "11:12,6:12,10:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160103,
               "Rockford IceHogs",
               "Milwaukee Admirals",
               "1:1,1:1,0:0,1:0",
               "16:11,11:9,8:6,3:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "San Antonio Rampage",
               "San Diego Gulls", "2:0,1:2,0:2", "13:8,7:10,3:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Providence Bruins",
               "Rochester Americans", "1:2,2:0,2:0", "11:11,12:11,16:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Ontario Reign",
               "Charlotte Checkers", "0:1,0:1,0:0", "4:10,8:6,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Stockton Heat",
               "Bakersfield Condors", "1:1,0:0,2:0", "11:8,19:10,18:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "San Jose Barracuda",
               "Texas Stars", "2:1,1:0,2:0", "11:7,6:7,7:8", 0, False)

print("Inserting " + leaguename + " Game Data From 1/5/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160105,
               "Wilkes-Barre/Scranton Penguins",
               "Binghamton Senators",
               "0:1,2:0,2:0",
               "5:11,12:13,11:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Manitoba Moose",
               "Grand Rapids Griffins", "1:0,0:1,1:0", "13:9,3:12,10:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Milwaukee Admirals",
               "Lake Erie Monsters", "0:0,0:2,0:2", "3:4,6:11,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Ontario Reign",
               "Texas Stars", "0:0,1:0,1:2,1:0", "10:12,5:9,8:10,3:1", 0, False)

print("Inserting " + leaguename + " Game Data From 1/6/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160106, "San Jose Barracuda",
               "Stockton Heat", "0:2,1:1,2:0,1:0", "10:12,7:14,16:9,3:0", 0, False)

print("Inserting " + leaguename + " Game Data From 1/8/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160108, "St. John's IceCaps",
               "Portland Pirates", "0:2,1:1,0:2", "6:20,10:12,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Albany Devils",
               "Syracuse Crunch", "2:2,1:1,3:1", "10:9,5:6,16:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Grand Rapids Griffins",
               "Milwaukee Admirals", "2:1,2:0,0:1", "11:9,8:9,9:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Binghamton Senators",
               "Utica Comets", "3:1,2:1,1:1", "8:9,8:8,9:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160108,
               "Lehigh Valley Phantoms",
               "Wilkes-Barre/Scranton Penguins",
               "3:4,0:0,0:0",
               "4:13,8:5,8:5",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Providence Bruins",
               "Bridgeport Sound Tigers", "2:1,1:1,2:2", "13:12,9:8,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Rochester Americans",
               "Hershey Bears", "1:3,3:1,1:0", "5:11,14:9,4:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Hartford Wolf Pack",
               "Springfield Falcons", "0:1,2:1,0:1", "12:6,9:14,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Manitoba Moose",
               "Toronto Marlies", "0:0,0:1,0:2", "13:5,6:11,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Texas Stars",
               "Chicago Wolves", "2:0,1:0,0:1", "15:8,9:4,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Bakersfield Condors",
               "San Antonio Rampage", "1:2,0:1,0:0", "8:9,3:11,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Ontario Reign",
               "Stockton Heat", "1:0,2:1,3:0", "8:8,18:11,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "San Diego Gulls",
               "Charlotte Checkers", "0:1,1:1,0:1", "14:8,6:13,10:8", 0, False)

print("Inserting " + leaguename + " Game Data From 1/9/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Albany Devils",
               "Lehigh Valley Phantoms", "1:0,2:1,1:1", "6:12,14:8,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "St. John's IceCaps",
               "Portland Pirates", "0:3,0:1,1:0", "11:11,15:11,15:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160109,
               "Grand Rapids Griffins",
               "Lake Erie Monsters",
               "2:1,1:2,0:0,0:0,1:0",
               "17:15,5:10,6:10,0:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160109,
               "Hartford Wolf Pack",
               "Bridgeport Sound Tigers",
               "1:1,2:1,2:2",
               "9:11,8:12,12:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Springfield Falcons",
               "Providence Bruins", "0:0,0:3,2:1", "5:10,11:10,9:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Syracuse Crunch",
               "Hershey Bears", "1:1,1:1,2:0", "6:10,13:8,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Binghamton Senators",
               "Rochester Americans", "0:2,0:0,1:0", "13:11,14:10,11:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Wilkes-Barre/Scranton Penguins",
               "Utica Comets", "2:0,0:1,2:1", "10:11,10:10,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Manitoba Moose",
               "Toronto Marlies", "0:0,1:1,0:3", "7:13,8:17,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Milwaukee Admirals",
               "Iowa Wild", "0:1,1:2,0:1", "11:14,7:9,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Texas Stars",
               "Chicago Wolves", "2:1,2:1,1:0", "6:16,12:18,9:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Bakersfield Condors",
               "Ontario Reign", "0:0,3:0,1:0", "9:9,18:6,6:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "San Diego Gulls",
               "Charlotte Checkers", "2:1,0:1,0:2", "17:9,10:11,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "San Jose Barracuda",
               "San Antonio Rampage", "3:1,2:1,1:2", "14:8,10:6,7:14", 0, False)

print("Inserting " + leaguename + " Game Data From 1/10/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Hartford Wolf Pack",
               "Albany Devils", "1:1,1:2,1:0,1:0", "8:14,8:12,2:8,1:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160110,
               "Providence Bruins",
               "Springfield Falcons",
               "0:0,1:1,0:0,0:0,1:0",
               "8:13,11:15,9:7,4:7,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Hershey Bears",
               "Utica Comets", "1:1,2:1,3:1", "12:9,13:10,15:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Lehigh Valley Phantoms",
               "Binghamton Senators", "0:1,0:0,1:1", "12:4,10:11,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Rochester Americans",
               "Syracuse Crunch", "0:1,0:0,1:1", "11:6,9:7,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Iowa Wild",
               "Rockford IceHogs", "1:1,0:2,0:0", "14:11,16:14,4:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160110,
               "San Jose Barracuda",
               "San Antonio Rampage",
               "0:0,0:0,0:0,0:1",
               "9:6,4:11,4:9,4:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/11/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160111, "Manitoba Moose",
               "Lake Erie Monsters", "1:1,0:2,2:4", "7:12,9:12,11:11", 0, False)

print("Inserting " + leaguename + " Game Data From 1/12/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160112,
               "St. John's IceCaps",
               "Wilkes-Barre/Scranton Penguins",
               "1:0,0:1,0:1",
               "13:8,5:8,16:7",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Charlotte Checkers",
               "Grand Rapids Griffins", "1:1,1:1,1:3", "8:17,13:11,15:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Rockford IceHogs",
               "Chicago Wolves", "2:1,1:0,2:1", "10:7,11:8,12:11", 0, False)

print("Inserting " + leaguename + " Game Data From 1/13/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160113,
               "St. John's IceCaps",
               "Wilkes-Barre/Scranton Penguins",
               "3:2,1:2,0:2",
               "17:7,10:7,13:5",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Albany Devils",
               "Rochester Americans", "1:0,1:0,2:0", "14:4,11:8,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Charlotte Checkers",
               "Grand Rapids Griffins", "0:2,1:1,3:0", "12:16,18:6,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Utica Comets", "Toronto Marlies",
               "1:1,0:1,1:0,0:0,0:1", "11:8,6:8,16:3,4:2,0:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160113,
               "Binghamton Senators",
               "Syracuse Crunch",
               "1:1,1:1,1:1,1:0",
               "14:10,10:15,9:6,2:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Manitoba Moose",
               "Lake Erie Monsters", "1:0,2:0,1:0", "10:10,8:4,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Stockton Heat",
               "San Antonio Rampage", "2:1,2:1,2:0", "15:6,14:15,4:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160113,
               "San Diego Gulls",
               "San Jose Barracuda",
               "0:0,0:0,1:1,0:1",
               "11:9,4:9,10:3,0:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/15/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160115,
               "Grand Rapids Griffins",
               "Lake Erie Monsters",
               "0:0,0:0,0:0,1:0",
               "12:10,14:10,12:8,1:2",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160115,
               "Portland Pirates",
               "Bridgeport Sound Tigers",
               "1:0,1:1,3:0",
               "10:9,11:12,6:9",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Springfield Falcons",
               "Hartford Wolf Pack", "0:1,0:0,0:0", "11:9,11:10,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Syracuse Crunch",
               "Utica Comets", "0:2,0:0,1:1", "6:17,11:8,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Lehigh Valley Phantoms",
               "Hershey Bears", "0:0,2:3,1:1", "8:10,10:10,27:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Providence Bruins",
               "Albany Devils", "0:1,1:0,4:1", "13:15,14:10,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Rochester Americans",
               "Binghamton Senators", "0:2,0:1,0:1", "12:8,13:12,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Chicago Wolves",
               "Iowa Wild", "0:0,0:0,3:0", "12:12,14:12,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Rockford IceHogs",
               "San Jose Barracuda", "1:2,1:1,0:2", "15:12,11:11,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "San Antonio Rampage",
               "Milwaukee Admirals", "0:0,0:1,0:2", "6:11,8:13,5:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Bakersfield Condors",
               "Texas Stars", "0:1,0:1,2:2", "2:14,8:20,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Ontario Reign",
               "San Diego Gulls", "1:0,2:0,2:0", "14:5,11:12,9:10", 0, False)

print("Inserting " + leaguename + " Game Data From 1/16/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Charlotte Checkers",
               "Manitoba Moose", "0:0,2:1,0:1,1:0", "11:9,8:12,7:8,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "St. John's IceCaps",
               "Toronto Marlies", "2:4,0:1,1:1", "9:9,10:8,14:4", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160116,
               "Hershey Bears",
               "Springfield Falcons",
               "1:1,1:2,1:0,0:0,1:0",
               "17:13,8:15,7:6,3:2,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Portland Pirates",
               "Bridgeport Sound Tigers", "1:0,1:0,1:1", "13:6,10:8,5:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160116,
               "Syracuse Crunch",
               "Wilkes-Barre/Scranton Penguins",
               "3:1,0:0,1:1",
               "8:7,6:10,8:10",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Utica Comets",
               "Albany Devils", "0:0,0:0,0:0,1:0", "17:1,10:6,13:6,4:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Binghamton Senators",
               "Rochester Americans", "1:0,0:2,0:0", "7:7,6:13,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Lehigh Valley Phantoms",
               "Hartford Wolf Pack", "0:0,1:1,0:1", "6:11,12:9,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Chicago Wolves",
               "Lake Erie Monsters", "0:2,1:2,1:0", "8:12,9:13,16:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Iowa Wild", "San Jose Barracuda",
               "0:0,0:1,1:0,1:0", "17:9,14:11,15:5,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Rockford IceHogs",
               "Stockton Heat", "1:0,0:0,2:0", "12:11,8:4,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "San Antonio Rampage",
               "Milwaukee Admirals", "0:4,1:1,2:1", "8:12,10:9,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Ontario Reign",
               "Bakersfield Condors", "0:2,1:0,1:2", "5:9,14:11,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "San Diego Gulls",
               "Texas Stars", "1:1,1:1,1:3", "8:5,6:5,6:9", 0, False)

print("Inserting " + leaguename + " Game Data From 1/17/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160117, "St. John's IceCaps",
               "Toronto Marlies", "0:0,2:2,4:2", "11:13,13:9,10:12", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160117,
               "Providence Bruins",
               "Portland Pirates",
               "0:0,0:1,1:0,0:1",
               "13:9,15:12,14:9,4:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Grand Rapids Griffins",
               "Chicago Wolves", "1:1,1:1,1:1,0:1", "6:9,10:14,9:9,0:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Bridgeport Sound Tigers",
               "Lehigh Valley Phantoms", "0:2,1:0,0:2", "18:9,15:9,10:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160117,
               "Hershey Bears",
               "Springfield Falcons",
               "1:1,0:1,1:0,0:1",
               "10:6,8:7,13:10,0:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Charlotte Checkers",
               "Manitoba Moose", "1:1,1:0,2:0", "13:10,10:5,5:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Iowa Wild",
               "Stockton Heat", "1:1,0:3,3:3", "7:13,9:12,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Ontario Reign",
               "Texas Stars", "0:0,0:1,2:0", "2:7,9:8,12:7", 0, False)

print("Inserting " + leaguename + " Game Data From 1/18/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Rockford IceHogs",
               "Lake Erie Monsters", "0:0,2:0,1:1", "10:7,10:11,6:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160118,
               "Providence Bruins",
               "Hartford Wolf Pack",
               "0:1,1:1,1:0,0:1",
               "12:9,7:8,12:7,0:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Rochester Americans",
               "Syracuse Crunch", "0:0,0:1,1:1", "7:13,13:5,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "San Jose Barracuda",
               "Bakersfield Condors", "0:3,1:1,2:1", "15:11,12:9,18:7", 0, False)

print("Inserting " + leaguename + " Game Data From 1/19/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160119, "San Antonio Rampage",
               "San Diego Gulls", "0:0,0:2,1:0", "11:3,18:9,12:10", 0, False)

print("Inserting " + leaguename + " Game Data From 1/20/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Albany Devils",
               "Hartford Wolf Pack",
               "0:0,2:2,0:0,0:1",
               "12:5,9:3,12:4,1:5",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Bridgeport Sound Tigers",
               "St. John's IceCaps",
               "1:1,1:1,0:0,1:0",
               "11:11,9:11,6:14,2:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Lake Erie Monsters",
               "Grand Rapids Griffins",
               "1:1,1:0,0:1,0:1",
               "12:12,11:17,8:13,1:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Toronto Marlies",
               "Syracuse Crunch",
               "1:1,0:1,3:2,1:0",
               "14:11,10:9,18:16,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Ontario Reign",
               "Manitoba Moose", "1:1,2:0,1:0", "10:11,13:7,8:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/20/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Albany Devils",
               "Hartford Wolf Pack",
               "0:0,2:2,0:0,0:1",
               "12:5,9:3,12:4,1:5",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Bridgeport Sound Tigers",
               "St. John's IceCaps",
               "1:1,1:1,0:0,1:0",
               "11:11,9:11,6:14,2:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Lake Erie Monsters",
               "Grand Rapids Griffins",
               "1:1,1:0,0:1,0:1",
               "12:12,11:17,8:13,1:4",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160120,
               "Toronto Marlies",
               "Syracuse Crunch",
               "1:1,0:1,3:2,1:0",
               "14:11,10:9,18:16,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Ontario Reign",
               "Manitoba Moose", "1:1,2:0,1:0", "10:11,13:7,8:6", 0, False)


print("Inserting " + leaguename + " Game Data From 1/22/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Albany Devils",
               "St. John's IceCaps", "1:0,1:3,0:1", "11:4,8:12,7:1", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Charlotte Checkers",
               "Chicago Wolves",
               "1:0,2:0,0:3,0:0,0:1",
               "9:7,11:6,6:11,5:3,0:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Grand Rapids Griffins",
               "Rochester Americans", "1:2,1:0,1:3", "12:20,13:16,19:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Lake Erie Monsters",
               "Milwaukee Admirals",
               "0:1,1:0,0:0,1:0",
               "4:6,11:6,7:11,1:0",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Portland Pirates",
               "Wilkes-Barre/Scranton Penguins",
               "2:0,0:1,0:0",
               "11:11,11:16,7:12",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Binghamton Senators",
               "Hershey Bears", "0:1,0:3,0:0", "12:14,4:15,14:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Providence Bruins",
               "Springfield Falcons", "2:0,1:0,1:1", "12:7,11:7,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Rockford IceHogs", "Iowa Wild",
               "2:1,1:1,0:1,0:0,0:1", "11:8,13:10,10:10,3:4,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "San Antonio Rampage",
               "Bakersfield Condors", "0:0,2:0,4:1", "14:7,5:12,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Texas Stars",
               "San Diego Gulls", "1:0,0:2,1:1", "8:9,6:11,7:6", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160122,
               "Ontario Reign",
               "San Jose Barracuda",
               "0:2,0:0,2:0,1:0",
               "8:11,11:5,14:6,1:0",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Stockton Heat", "Manitoba Moose",
               "0:0,1:0,0:1,0:0,1:0", "9:9,19:7,18:11,4:4,1:0", 0, False)

print("Inserting " + leaguename + " Game Data From 1/23/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Lake Erie Monsters",
               "Milwaukee Admirals", "0:0,0:1,0:0", "9:11,4:11,6:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Albany Devils",
               "St. John's IceCaps", "0:0,0:2,1:0", "9:11,11:5,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Toronto Marlies",
               "Utica Comets", "1:0,2:1,1:1", "6:15,9:7,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Charlotte Checkers",
               "Chicago Wolves", "2:2,2:2,2:1", "9:8,17:8,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Grand Rapids Griffins",
               "Rochester Americans", "0:1,0:0,0:1", "12:11,15:13,15:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160123,
               "Portland Pirates",
               "Wilkes-Barre/Scranton Penguins",
               "0:2,0:1,0:2",
               "13:16,11:9,10:8",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160123,
               "Springfield Falcons",
               "Providence Bruins",
               "3:1,1:1,0:2,1:0",
               "12:14,10:12,8:8,1:3",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Binghamton Senators",
               "Syracuse Crunch", "1:1,1:0,0:2", "4:7,5:12,14:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Rockford IceHogs",
               "Iowa Wild", "0:0,0:0,1:0", "5:10,6:12,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "San Antonio Rampage",
               "Bakersfield Condors", "0:1,2:0,3:1", "12:10,11:13,12:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Texas Stars",
               "San Diego Gulls", "2:1,1:0,2:1", "13:9,6:14,6:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "San Jose Barracuda",
               "Ontario Reign", "1:2,0:0,0:0", "11:8,6:7,2:10", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160123,
               "Stockton Heat",
               "Manitoba Moose",
               "0:1,2:0,0:1,1:0",
               "18:9,15:7,13:8,1:2",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/24/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Hartford Wolf Pack",
               "Portland Pirates", "1:0,3:1,0:0", "12:6,12:11,3:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Toronto Marlies",
               "Utica Comets", "4:0,2:1,1:0", "20:9,6:11,16:9", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160124,
               "Providence Bruins",
               "Wilkes-Barre/Scranton Penguins",
               "1:0,4:2,0:0",
               "11:6,13:12,6:8",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "San Antonio Rampage",
               "Texas Stars", "0:2,0:2,1:2", "18:13,6:9,7:12", 0, False)

print("Inserting " + leaguename + " Game Data From 1/25/2016.\n")
MakeHockeyGame((sqlcur,
                sqlcon),
               20160125,
               "Hershey Bears",
               "Lehigh Valley Phantoms",
               "0:1,3:3,2:1,0:0,0:1",
               "9:8,10:11,8:9,4:3,0:1",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/26/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Iowa Wild", "Chicago Wolves",
               "0:0,1:2,2:1,0:1", "10:8,11:18,13:15,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Bakersfield Condors",
               "Manitoba Moose", "2:1,3:1,1:1", "13:9,16:12,22:6", 0, False)

print("Inserting " + leaguename + " Game Data From 1/27/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Grand Rapids Griffins",
               "Toronto Marlies", "0:2,0:1,0:1", "7:13,14:7,18:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Albany Devils",
               "Hershey Bears", "1:0,0:1,1:1,1:0", "7:3,12:5,4:11,1:0", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160127,
               "Bridgeport Sound Tigers",
               "Springfield Falcons",
               "0:0,0:0,0:0,1:0",
               "17:6,10:11,12:8,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Portland Pirates",
               "St. John's IceCaps", "1:0,2:0,1:1", "13:6,13:12,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Lehigh Valley Phantoms",
               "Binghamton Senators", "1:1,1:1,4:1", "11:9,7:14,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Rochester Americans",
               "Syracuse Crunch", "1:1,2:3,2:1,1:0", "6:12,8:9,11:4,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Wilkes-Barre/Scranton Penguins",
               "Hartford Wolf Pack", "0:1,1:0,0:2", "4:8,12:8,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Rockford IceHogs",
               "Charlotte Checkers", "1:1,1:0,1:0", "12:9,20:8,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Texas Stars",
               "San Jose Barracuda", "2:0,0:0,1:0", "12:12,13:9,11:14", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160127,
               "Stockton Heat",
               "Ontario Reign",
               "1:0,0:1,0:0,1:0",
               "11:10,9:14,6:13,1:0",
               0,
               False)

print("Inserting " + leaguename + " Game Data From 1/29/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Albany Devils",
               "Utica Comets", "1:0,0:1,2:2,0:1", "7:9,7:11,11:7,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Grand Rapids Griffins",
               "Toronto Marlies", "1:0,0:1,1:3", "16:7,13:10,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Lake Erie Monsters",
               "Texas Stars", "0:0,2:1,1:1", "8:12,8:8,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Portland Pirates",
               "St. John's IceCaps", "1:0,0:1,3:1", "9:8,9:12,17:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Syracuse Crunch",
               "Hershey Bears", "2:1,1:3,0:1", "7:11,17:7,13:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Lehigh Valley Phantoms",
               "Wilkes-Barre/Scranton Penguins",
               "0:1,0:1,3:1,1:0",
               "6:14,8:6,17:8,3:2",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Providence Bruins",
               "Springfield Falcons", "2:0,4:1,2:0", "11:8,17:5,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Rochester Americans",
               "Binghamton Senators", "1:2,1:1,0:2", "13:8,10:12,11:8", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Hartford Wolf Pack",
               "Bridgeport Sound Tigers",
               "0:2,1:1,0:1",
               "12:12,13:6,7:10",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160129,
               "Iowa Wild",
               "Charlotte Checkers",
               "0:1,3:2,1:1,1:0",
               "8:14,20:9,13:8,3:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Rockford IceHogs",
               "Chicago Wolves", "4:0,1:0,1:0", "7:9,9:3,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "San Antonio Rampage",
               "San Jose Barracuda", "2:1,0:0,0:0", "15:10,15:9,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "Bakersfield Condors",
               "Manitoba Moose", "1:0,0:2,5:0", "6:4,14:21,17:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160129, "San Diego Gulls",
               "Ontario Reign", "0:1,0:1,0:0", "6:10,9:12,6:8", 0, False)

print("Inserting " + leaguename + " Game Data From 1/30/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Lake Erie Monsters",
               "Texas Stars", "0:1,1:1,1:1", "13:13,10:10,16:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Iowa Wild",
               "Charlotte Checkers", "3:1,2:0,0:0", "13:11,11:9,10:13", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Toronto Marlies",
               "Binghamton Senators",
               "1:1,2:1,2:3,0:1",
               "14:9,14:9,6:10,3:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Bridgeport Sound Tigers",
               "Albany Devils", "2:0,1:0,1:1", "10:11,6:8,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Hartford Wolf Pack",
               "St. John's IceCaps", "1:0,2:0,1:1", "8:8,12:7,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Hershey Bears",
               "Syracuse Crunch", "1:1,2:0,2:0", "7:8,11:6,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Springfield Falcons",
               "Portland Pirates", "2:0,2:1,2:1", "8:13,8:10,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Utica Comets",
               "Rochester Americans", "1:2,1:0,2:0", "10:10,13:7,9:5", 0, False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Wilkes-Barre/Scranton Penguins",
               "Lehigh Valley Phantoms",
               "1:0,1:4,1:1",
               "11:12,8:15,8:8",
               0,
               False)
MakeHockeyGame((sqlcur,
                sqlcon),
               20160130,
               "Chicago Wolves",
               "Rockford IceHogs",
               "1:0,0:1,1:1,1:0",
               "10:6,10:8,5:12,2:1",
               0,
               False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Milwaukee Admirals",
               "Grand Rapids Griffins", "1:0,5:3,1:0", "17:7,12:9,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "San Antonio Rampage",
               "San Jose Barracuda", "2:1,0:1,1:2", "10:12,7:17,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Ontario Reign",
               "Manitoba Moose", "1:0,2:0,1:0", "7:7,14:8,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160130, "Stockton Heat",
               "Bakersfield Condors", "1:1,2:0,1:1", "12:8,17:13,15:9", 0, False)

print("Database Check Return: " +
      str(sqlcon.execute("PRAGMA integrity_check(100);").fetchone()[0]) + "\n")

sqlcon.close()

print("DONE! All Game Data Inserted.")

print("DONE! " + leaguename + " Database Created.")
