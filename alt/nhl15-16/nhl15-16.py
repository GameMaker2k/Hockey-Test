#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import sys
import os
import re

leaguename = "NHL"
getforday = "23"
getformonth = "10"
getforyear = "2015"
getendyear = "2016"

print("Creating "+leaguename+" Database.")

if (len(sys.argv) == 0):
    sqlcon = sqlite3.connect("./nhl15-16.db3")
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
    getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(
        teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT 10").fetchall()
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
    return str(wins)+":"+str(losses)+":"+str(otlosses)


def UpdateTeamData(sqldatacon, teamid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET " +
                          dataname+"="+str(TMPData)+" WHERE id="+str(teamid))
    return int(TMPData)


def UpdateTeamDataString(sqldatacon, teamid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET " +
                          dataname+"=\""+str(newdata)+"\" WHERE id="+str(teamid))
    return True


def GetTeamData(sqldatacon, teamid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0])
    return TMPData


def UpdateGameData(sqldatacon, gameid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute("UPDATE "+leaguename+"Games SET " +
                          dataname+"="+str(TMPData)+" WHERE id="+str(gameid))
    return int(TMPData)


def UpdateGameDataString(sqldatacon, gameid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute("UPDATE "+leaguename+"Games SET " +
                          dataname+"=\""+str(newdata)+"\" WHERE id="+str(gameid))
    return True


def GetGameData(sqldatacon, gameid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0])
    return TMPData


def UpdateArenaData(sqldatacon, arenaid, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM " +
                      leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) - addtodata
    sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET " +
                          dataname+"="+str(TMPData)+" WHERE id="+str(arenaid))
    return int(TMPData)


def UpdateArenaDataString(sqldatacon, arenaid, dataname, newdata):
    global leaguename
    sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET " +
                          dataname+"=\""+str(newdata)+"\" WHERE id="+str(arenaid))
    return True


def GetArenaData(sqldatacon, arenaid, dataname, datatype):
    global leaguename
    if (datatype == "float"):
        TMPData = float(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0])
    if (datatype == "int"):
        TMPData = int(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0])
    if (datatype == "str"):
        TMPData = str(sqldatacon[0].execute(
            "SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0])
    return TMPData


def UpdateConferenceData(sqldatacon, conference, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename +
                      "Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename +
                      "Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) - addtodata
    sqldatacon[0].execute("UPDATE "+leaguename+"Conferences SET "+dataname +
                          "="+str(TMPData)+" WHERE Conference=\""+str(conference)+"\"")
    return int(TMPData)


def UpdateDivisionData(sqldatacon, division, dataname, addtodata, addtype):
    global leaguename
    if (addtype == "="):
        TMPData = addtodata
    if (addtype == "+"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename +
                      "Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) + addtodata
    if (addtype == "-"):
        TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename +
                      "Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) - addtodata
    sqldatacon[0].execute("UPDATE "+leaguename+"Divisions SET " +
                          dataname+"="+str(TMPData)+" WHERE Division=\""+str(division)+"\"")
    return int(TMPData)


print("Creating "+leaguename+" Conference Table.")
print("Inserting "+leaguename+" Conference Data.")

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Conferences")
sqlcur.execute("CREATE TABLE "+leaguename +
               "Conferences(id INTEGER PRIMARY KEY, Conference TEXT, NumberOfTeams INTEGER)")
sqlcon.commit()


def MakeHockeyConferences(sqldatacon, conference):
    global leaguename
    print("Conference Name: "+conference)
    print(" ")
    sqldatacon[0].execute("INSERT INTO "+leaguename +
                          "Conferences(Conference, NumberOfTeams) VALUES(\""+str(conference)+"\", 0)")
    return True


MakeHockeyConferences((sqlcur, sqlcon), "Eastern")
MakeHockeyConferences((sqlcur, sqlcon), "Western")
sqlcon.commit()

print("Creating "+leaguename+" Division Table.")
print("Inserting "+leaguename+" Division Data.")

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Divisions")
sqlcur.execute("CREATE TABLE "+leaguename +
               "Divisions(id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, NumberOfTeams INTEGER)")
sqlcon.commit()


def MakeHockeyDivisions(sqldatacon, division, conference):
    global leaguename
    print("Conference Name: "+conference)
    print("Division Name: "+division)
    print(" ")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions(Division, Conference, NumberOfTeams) VALUES(\"" +
                          str(division)+"\", \""+str(conference)+"\", 0)")
    return True


MakeHockeyDivisions((sqlcur, sqlcon), "Atlantic", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "Metropolitan", "Eastern")
MakeHockeyDivisions((sqlcur, sqlcon), "Central", "Western")
MakeHockeyDivisions((sqlcur, sqlcon), "Pacific", "Western")

print("Creating "+leaguename+" Team Table.")
print("Inserting "+leaguename+" Team Data.")

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Arenas")
sqlcur.execute("CREATE TABLE "+leaguename +
               "Arenas(id INTEGER PRIMARY KEY, CityName TEXT, AreaName TEXT, FullCityName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER)")
sqlcon.commit()

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Teams")
sqlcur.execute("CREATE TABLE "+leaguename+"Teams(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, Affiliates TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)")
sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Stats")
sqlcur.execute("CREATE TABLE "+leaguename+"Stats(id INTEGER PRIMARY KEY, TeamID  INTEGER, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, Affiliates TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, ShutoutWins INTEGER, ShutoutLosses INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, ShotsBlockedFor INTEGER, ShotsBlockedAgainst INTEGER, ShotsBlockedDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)")
sqlcon.commit()


def MakeHockeyTeams(sqldatacon, cityname, areaname, teamname, conference, division, arenaname, teamnameprefix, teamaffiliates):
    global leaguename
    print("Team Name: "+teamname)
    print("Arena Name: "+arenaname)
    print("City Name: "+cityname)
    print("Full City Name: "+cityname+", "+areaname)
    print("Full Name: "+teamnameprefix+" "+teamname)
    print("Conference: "+conference)
    print("Division: "+division)
    print(" ")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams(Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) VALUES(\"20151001\", \"" +
                          str(teamnameprefix+" "+teamname)+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", \""+str(teamaffiliates)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"None\")")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+teamnameprefix+" "+teamname+"\";")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(
        cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)")
    UpdateConferenceData((sqlcur, sqlcon), conference, "NumberOfTeams", 1, "+")
    UpdateDivisionData((sqlcur, sqlcon), division, "NumberOfTeams", 1, "+")
    return True


def MakeHockeyArena(sqldatacon, cityname, areaname, arenaname, teamnameprefix):
    global leaguename
    print("Arena Name: "+arenaname)
    print("City Name: "+cityname)
    print("Full City Name: "+cityname+", "+areaname)
    print(" ")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(
        cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)")
    return True


print("Inserting "+leaguename+" Teams From Eastern Conference.")
print("Inserting "+leaguename+" Teams From Atlantic Division.\n")
MakeHockeyTeams((sqlcur, sqlcon), "Boston", "MA", "Bruins", "Eastern", "Atlantic",
                "TD Garden", "Boston", "ECHL:Atlanta Gladiators,AHL:Providence Bruins")
MakeHockeyTeams((sqlcur, sqlcon), "Buffalo", "NY", "Sabres", "Eastern", "Atlantic",
                "First Niagara Center", "Buffalo", "ECHL:Elmira Jackals,AHL:Rochester Americans ")
MakeHockeyTeams((sqlcur, sqlcon), "Detroit", "MI", "Red Wings", "Eastern", "Atlantic",
                "Joe Louis Arena", "Detroit", "ECHL:Toledo Walleye,AHL:Grand Rapids Griffins ")
MakeHockeyTeams((sqlcur, sqlcon), "Sunrise", "FL", "Panthers", "Eastern",
                "Atlantic", "BB&T Center", "Florida", "ECHL:None,AHL:Portland Pirates")
MakeHockeyTeams((sqlcur, sqlcon), "Montreal", "QC", "Canadiens", "Eastern", "Atlantic",
                "Bell Centre", "Montreal", "ECHL:Brampton Beast,AHL:St. John's Icecaps")
MakeHockeyTeams((sqlcur, sqlcon), "Ottawa", "ON", "Senators", "Eastern", "Atlantic",
                "Canadian Tire Centre", "Ottawa", "ECHL:Evansville IceMen,AHL:Binghamton Senators")
MakeHockeyTeams((sqlcur, sqlcon), "Tampa Bay", "FL", "Lightning", "Eastern",
                "Atlantic", "Amalie Arena", "Tampa Bay", "ECHL:None,AHL:Syracuse Crunch")
MakeHockeyTeams((sqlcur, sqlcon), "Toronto", "ON", "Maple Leafs", "Eastern", "Atlantic",
                "Air Canada Centre", "Toronto", "ECHL:Orlando Solar Bears,AHL:Toronto Marlies")

print("Inserting "+leaguename+" Teams From Metropolitan Division.\n")
MakeHockeyTeams((sqlcur, sqlcon), "Carolina", "NC", "Hurricanes", "Eastern", "Metropolitan",
                "PNC Arena", "Carolina", "ECHL:Florida Everblades,AHL:Charlotte Checkers")
MakeHockeyTeams((sqlcur, sqlcon), "Columbus", "OH", "Blue Jackets", "Eastern", "Metropolitan",
                "Nationwide Arena", "Columbus", "ECHL:Kalamazoo Wings,AHL:Lake Erie Monsters")
MakeHockeyTeams((sqlcur, sqlcon), "New Jersey", "NJ", "Devils", "Eastern",
                "Metropolitan", "Prudential Center", "New Jersey", "ECHL:None,AHL:Albany Devils")
MakeHockeyTeams((sqlcur, sqlcon), "New York City", "NY", "Islanders", "Eastern", "Metropolitan",
                "Barclays Center", "New York", "ECHL:Missouri Mavericks,AHL:Bridgeport Sound Tigers")
MakeHockeyTeams((sqlcur, sqlcon), "New York City", "NY", "Rangers", "Eastern", "Metropolitan",
                "Madison Square Garden", "New York", "ECHL:Greenville Swamp Rabbits,AHL:Hartford Wolf Pack")
MakeHockeyTeams((sqlcur, sqlcon), "Philadelphia", "PA", "Flyers", "Eastern", "Metropolitan",
                "Wells Fargo Center", "Philadelphia", "ECHL:Reading Royals,AHL:Lehigh Valley Phantoms")
MakeHockeyTeams((sqlcur, sqlcon), "Pittsburgh", "PA", "Penguins", "Eastern", "Metropolitan",
                "Consol Energy Center", "Pittsburgh", "ECHL:Wheeling Nailers,AHL:Wilkes-Barre/Scranton Penguins")
MakeHockeyTeams((sqlcur, sqlcon), "Washington", "D.C.", "Capitals", "Eastern", "Metropolitan",
                "Verizon Center", "Washington", "ECHL:South Carolina Stingrays,AHL:Hershey Bears")

print("Inserting "+leaguename+" Teams From Western Conference.")
print("Inserting "+leaguename+" Teams From Central Division.\n")
MakeHockeyTeams((sqlcur, sqlcon), "Chicago", "IL", "Blackhawks", "Western",
                "Central", "United Center", "Chicago", "ECHL:Indy Fuel,AHL:Rockford IceHogs")
MakeHockeyTeams((sqlcur, sqlcon), "Denver", "CO", "Avalanche", "Western", "Central",
                "Pepsi Center", "Colorado", "ECHL:Fort Wayne Komets,AHL:San Antonio Rampage")
MakeHockeyTeams((sqlcur, sqlcon), "Dallas", "TX", "Stars", "Western", "Central",
                "American Airlines Center", "Dallas", "ECHL:Idaho Steelheads,AHL:Texas Stars")
MakeHockeyTeams((sqlcur, sqlcon), "St. Paul", "MN", "Wild", "Western", "Central",
                "Xcel Energy Center", "Minnesota", "ECHL:Quad City Mallards,AHL:Iowa Wild")
MakeHockeyTeams((sqlcur, sqlcon), "Nashville", "TN", "Predators", "Western", "Central",
                "Bridgestone Arena", "Nashville", "ECHL:Cincinnati Cyclones,AHL:Milwaukee Admirals")
MakeHockeyTeams((sqlcur, sqlcon), "St. Louis", "MO", "Blues", "Western",
                "Central", "Scottrade Center", "St. Louis", "ECHL:None,AHL:Chicago Wolves")
MakeHockeyTeams((sqlcur, sqlcon), "Winnipeg", "MB", "Jets", "Western", "Central",
                "MTS Centre", "Winnipeg", "ECHL:Tulsa Oilers,AHL:Manitoba Moose")

print("Inserting "+leaguename+" Teams From Pacific Division.\n")
MakeHockeyTeams((sqlcur, sqlcon), "Anaheim", "CA", "Ducks", "Western", "Pacific",
                "Honda Center", "Anaheim", "ECHL:Utah Grizzlies,AHL:San Diego Gulls")
MakeHockeyTeams((sqlcur, sqlcon), "Glendale", "AZ", "Coyotes", "Western", "Pacific",
                "Gila River Arena", "Arizona", "ECHL:Rapid City Rush,AHL:Springfield Falcons")
MakeHockeyTeams((sqlcur, sqlcon), "Calgary", "AB", "Flames", "Western", "Pacific",
                "Scotiabank Saddledome", "Calgary", "ECHL:Adirondack Thunder,AHL:Stockton Heat")
MakeHockeyTeams((sqlcur, sqlcon), "Edmonton", "AB", "Oilers", "Western", "Pacific",
                "Rexall Place", "Edmonton", "ECHL:Norfolk Admirals,AHL:Bakersfield Condors")
MakeHockeyTeams((sqlcur, sqlcon), "Los Angeles", "CA", "Kings", "Western", "Pacific",
                "Staples Center", "Los Angeles", "ECHL:Manchester Monarchs,AHL:Ontario Reign")
MakeHockeyTeams((sqlcur, sqlcon), "San Jose", "CA", "Sharks", "Western", "Pacific",
                "SAP Center", "San Jose", "ECHL:Allen Americans,AHL:San Jose Barracuda")
MakeHockeyTeams((sqlcur, sqlcon), "Vancouver", "BC", "Canucks", "Western",
                "Pacific", "Rogers Arena", "Vancouver", "ECHL:None,AHL:Utica Comets")

MakeHockeyArena((sqlcur, sqlcon), "Foxborough", "MA",
                "Gillette Stadium", "Foxborough")
MakeHockeyArena((sqlcur, sqlcon), "Minneapolis", "MN",
                "TCF Bank Stadium", "Minneapolis")
MakeHockeyArena((sqlcur, sqlcon), "Denver", "CO", "Coors Field", "Denver")
sqlcon.commit()


def GetNum2Team(sqldatacon, TeamNum, ReturnVar):
    global leaguename
    return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Teams WHERE id="+str(TeamNum)).fetchone()[0])


def GetTeam2Num(sqldatacon, TeamName):
    global leaguename
    return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Teams WHERE FullName=\""+str(TeamName)+"\"").fetchone()[0])


def GetNum2Arena(sqldatacon, ArenaNum, ReturnVar):
    global leaguename
    return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Arenas WHERE id="+str(ArenaNum)).fetchone()[0])


def GetArena2Num(sqldatacon, ArenaName):
    global leaguename
    return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Arenas WHERE FullArenaName=\""+str(ArenaName)+"\"").fetchone()[0])


print("DONE! All Team Data Inserted.")

print("Creating "+leaguename+" Game Table.")

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Games")
sqlcur.execute("CREATE TABLE "+leaguename+"Games(id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam Text, AwayTeam Text, AtArena Text, TeamScorePeriods TEXT, TeamFullScore Text, ShotsOnGoal TEXT, FullShotsOnGoal TEXT, ShotsBlocked TEXT, FullShotsBlocked TEXT, NumberPeriods INTEGER, TeamWin Text, IsPlayOffGame INTEGER)")
sqlcon.commit()


def MakeHockeyGame(sqldatacon, date, hometeam, awayteam, periodsscore, shotsongoal, atarena, isplayoffgame):
    global leaguename
    isplayoffgsql = "0"
    if (isplayoffgame == True):
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
        homeperiodscore = homeperiodscore+" "+str(periodscoresplit[0])
        awayperiodscore = awayperiodscore+" "+str(periodscoresplit[1])
        if (periodcounting <= 3):
            homescore = homescore + int(periodscoresplit[0])
            awayscore = awayscore + int(periodscoresplit[1])
        if (isplayoffgame == True and periodcounting > 3):
            homescore = homescore + int(periodscoresplit[0])
            awayscore = awayscore + int(periodscoresplit[1])
        if (isplayoffgame == False and periodcounting > 3):
            if (periodscoresplit[0] > periodscoresplit[1]):
                homescore = homescore + 1
            if (periodscoresplit[0] < periodscoresplit[1]):
                awayscore = awayscore + 1
        periodcounting = periodcounting + 1
    totalscore = str(homescore)+":"+str(awayscore)
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
        sbstr = sbstr+str(homesb)+":"+str(awaysb)+" "
        periodsogcounting = periodsogcounting + 1
    sbstr = sbstr.rstrip()
    sbstr = sbstr.replace(" ", ",")
    tsbstr = str(hometsb)+":"+str(awaytsb)
    totalsog = str(homesog)+":"+str(awaysog)
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
    print("Home Arena: "+str(atarenaname))
    print("Home Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"))
    print("Home Period Scores:"+homeperiodscore)
    print("Home Score: "+str(teamscores[0]))
    print("Away Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"))
    print("Away Period Scores:"+awayperiodscore)
    print("Away Score: "+str(teamscores[1]))
    print("Number Of Periods: "+str(numberofperiods))
    if (teamscores[0] > teamscores[1]):
        print("Winning Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"))
        print("Losing Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"))
        losingteam = awayteam
        winningteam = hometeam
        winningteamname = hometeamname
        losingteamname = awayteamname
    if (teamscores[0] < teamscores[1]):
        print("Winning Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"))
        print("Losing Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"))
        losingteam = hometeam
        winningteam = awayteam
        winningteamname = awayteamname
        losingteamname = hometeamname
    print(" ")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Games(Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, ShotsBlocked, FullShotsBlocked, NumberPeriods, TeamWin, IsPlayOffGame) VALUES("+str(date)+", \""+str(hometeamname)+"\", \""+str(
        awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", \""+str(sbstr)+"\", \""+str(tsbstr)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", "+str(isplayoffgsql)+")")
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
    if ((isplayoffgame == False and numberofperiods < 5) or (isplayoffgame == True)):
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
            NewHTR = str(HTRSpit[0] + 1)+":" + \
                str(HTRSpit[1])+":"+str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "AwayRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0])+":" + \
                str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])
            UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR)
        if (losingteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "AwayRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1)+":" + \
                str(HTRSpit[1])+":"+str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "HomeRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0])+":" + \
                str(ATRSpit[1] + 1)+":"+str(ATRSpit[2])
            UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR)
    if (numberofperiods > 3):
        if ((numberofperiods == 4 and isplayoffgame == False) or (numberofperiods > 4 and isplayoffgame == True)):
            UpdateTeamData(sqldatacon, winningteam, "OTWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "OTSOWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "TWins", 1, "+")
        UpdateTeamData(sqldatacon, winningteam, "Points", 2, "+")
        if ((numberofperiods == 4 and isplayoffgame == False) or (numberofperiods > 4 and isplayoffgame == True)):
            UpdateTeamData(sqldatacon, losingteam, "OTLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "OTSOLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "TLosses", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "Points", 1, "+")
        if (winningteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "HomeRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1)+":" + \
                str(HTRSpit[1])+":"+str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "AwayRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1]) + \
                ":"+str(ATRSpit[2] + 1)
            UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR)
        if (losingteam == hometeam):
            HomeTeamRecord = GetTeamData(
                sqldatacon, winningteam, "AwayRecord", "str")
            HTRSpit = [int(n) for n in HomeTeamRecord.split(":")]
            NewHTR = str(HTRSpit[0] + 1)+":" + \
                str(HTRSpit[1])+":"+str(HTRSpit[2])
            UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR)
            AwayTeamRecord = GetTeamData(
                sqldatacon, losingteam, "HomeRecord", "str")
            ATRSpit = [int(n) for n in AwayTeamRecord.split(":")]
            NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1]) + \
                ":"+str(ATRSpit[2] + 1)
            UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR)
    if (isplayoffgame == False and numberofperiods > 4):
        UpdateTeamData(sqldatacon, winningteam, "SOWins", 1, "+")
        UpdateTeamData(sqldatacon, losingteam, "SOLosses", 1, "+")
        WinningTeamShootouts = GetTeamData(
            sqldatacon, winningteam, "Shootouts", "str")
        WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")]
        NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1])
        UpdateTeamDataString(sqldatacon, winningteam, "Shootouts", NewWTSo)
        LosingTeamShootouts = GetTeamData(
            sqldatacon, losingteam, "Shootouts", "str")
        LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")]
        NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1)
        UpdateTeamDataString(sqldatacon, losingteam, "Shootouts", NewLTSo)
    HomeOTLossesPCT = float("%.2f" % float(float(
        0.5) * float(GetTeamData((sqlcur, sqlcon), hometeam, "OTSOLosses", "float"))))
    HomeWinsPCT = float("%.3f" % float(float(GetTeamData((sqlcur, sqlcon), hometeam, "TWins", "float") +
                        HomeOTLossesPCT) / float(GetTeamData((sqlcur, sqlcon), hometeam, "GamesPlayed", "float"))))
    AwayOTLossesPCT = float("%.2f" % float(float(
        0.5) * float(GetTeamData((sqlcur, sqlcon), awayteam, "OTSOLosses", "float"))))
    AwayWinsPCT = float("%.3f" % float(float(GetTeamData((sqlcur, sqlcon), awayteam, "TWins", "float") +
                        AwayOTLossesPCT) / float(GetTeamData((sqlcur, sqlcon), awayteam, "GamesPlayed", "float"))))
    UpdateTeamData(sqldatacon, hometeam, "PCT", HomeWinsPCT, "=")
    UpdateTeamData(sqldatacon, awayteam, "PCT", AwayWinsPCT, "=")
    sqldatacon[1].commit()
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";")
    sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (TeamID, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak) SELECT id, Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, Affiliates, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, ShutoutWins, ShutoutLosses, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, ShotsBlockedFor, ShotsBlockedAgainst, ShotsBlockedDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";")
    sqldatacon[1].commit()
    return True


print("Inserting "+leaguename+" Game Data From 10/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Toronto Maple Leafs",
               "Montreal Canadiens", "0:1,1:0,0:2", "11:7,16:15,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Chicago Blackhawks",
               "New York Rangers", "1:3,1:0,0:0", "12:11,8:9,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Calgary Flames",
               "Vancouver Canucks", "0:2,1:1,0:2", "9:15,5:11,16:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151007, "Los Angeles Kings",
               "San Jose Sharks", "1:2,0:2,0:1", "8:14,6:6,6:12", 0, False)

print("Inserting "+leaguename+" Game Data From 10/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Boston Bruins",
               "Winnipeg Jets", "1:0,0:3,1:3", "14:6,10:11,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Buffalo Sabres",
               "Ottawa Senators", "0:1,0:1,1:1", "6:7,7:11,14:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Tampa Bay Lightning",
               "Philadelphia Flyers", "0:0,2:2,0:0,1:0", "10:13,13:3,4:6,5:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "St. Louis Blues",
               "Edmonton Oilers", "0:1,1:0,2:0", "8:10,14:7,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Nashville Predators",
               "Carolina Hurricanes", "2:0,0:0,0:1", "14:5,8:9,3:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Dallas Stars",
               "Pittsburgh Penguins", "1:0,1:0,1:0", "4:10,11:13,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151008, "Colorado Avalanche",
               "Minnesota Wild", "3:0,1:1,0:4", "11:9,7:11,5:10", 0, False)

print("Inserting "+leaguename+" Game Data From 10/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151009, "New Jersey Devils",
               "Winnipeg Jets", "0:0,1:3,0:0", "4:12,7:11,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Columbus Blue Jackets",
               "New York Rangers", "0:1,1:0,1:3", "9:6,14:10,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Detroit Red Wings",
               "Toronto Maple Leafs", "2:0,2:0,0:0", "8:9,8:7,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "New York Islanders",
               "Chicago Blackhawks", "0:1,1:1,1:0,0:1", "12:12,11:10,12:10,1:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151009, "Los Angeles Kings",
               "Arizona Coyotes", "0:2,1:2,0:0", "13:8,14:6,14:8", 0, False)

print("Inserting "+leaguename+" Game Data From 10/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Buffalo Sabres",
               "Tampa Bay Lightning", "0:0,1:2,0:2", "11:8,5:14,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Boston Bruins",
               "Montreal Canadiens", "0:1,1:2,1:1", "8:10,7:18,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Toronto Maple Leafs",
               "Ottawa Senators", "0:0,2:3,2:1,0:0,1:2", "16:10,5:10,13:11,7:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Florida Panthers",
               "Philadelphia Flyers", "4:0,1:1,2:0", "12:11,6:13,12:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "New York Rangers",
               "Columbus Blue Jackets", "3:0,1:0,1:2", "15:14,7:12,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Washington Capitals",
               "New Jersey Devils", "2:2,0:0,3:1", "6:11,11:5,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Carolina Hurricanes",
               "Detroit Red Wings", "0:0,2:1,1:3", "18:2,16:6,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Nashville Predators",
               "Edmonton Oilers", "0:0,1:0,1:0", "14:8,9:14,3:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Minnesota Wild",
               "St. Louis Blues", "1:0,2:1,0:1", "10:7,8:12,1:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Chicago Blackhawks",
               "New York Islanders", "1:0,2:0,1:1", "11:12,11:13,12:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Colorado Avalanche",
               "Dallas Stars", "1:2,2:1,3:0", "7:11,9:12,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Vancouver Canucks",
               "Calgary Flames", "0:1,2:0,0:1,0:1", "9:15,11:10,8:12,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "Arizona Coyotes",
               "Pittsburgh Penguins", "0:0,2:1,0:0", "13:11,13:6,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151010, "San Jose Sharks",
               "Anaheim Ducks", "0:0,1:0,1:0", "13:9,14:15,17:3", 0, False)

print("Inserting "+leaguename+" Game Data From 10/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151011, "Ottawa Senators",
               "Montreal Canadiens", "0:2,1:0,0:1", "6:15,6:9,9:10", 0, False)

print("Inserting "+leaguename+" Game Data From 10/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151012, "Boston Bruins",
               "Tampa Bay Lightning", "2:2,1:2,0:2", "13:9,10:8,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151012, "New York Islanders",
               "Winnipeg Jets", "1:0,2:1,1:1", "16:6,20:9,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151012, "Buffalo Sabres",
               "Columbus Blue Jackets", "0:0,1:0,3:2", "7:7,16:8,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151012, "Philadelphia Flyers",
               "Florida Panthers", "1:0,0:0,0:0", "10:10,14:7,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151012, "Anaheim Ducks",
               "Vancouver Canucks", "0:0,1:1,0:0,0:0,1:2", "9:6,9:8,9:7,2:4", 0, False)

print("Inserting "+leaguename+" Game Data From 10/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151013, "New Jersey Devils",
               "Nashville Predators", "0:1,0:0,1:2", "10:8,6:4,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "New York Rangers",
               "Winnipeg Jets", "1:1,0:1,0:2", "13:11,20:8,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Pittsburgh Penguins",
               "Montreal Canadiens", "0:1,2:1,0:1", "4:7,15:12,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Washington Capitals",
               "San Jose Sharks", "0:1,0:2,0:2", "8:17,12:10,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Carolina Hurricanes",
               "Florida Panthers", "0:1,1:0,0:3", "7:14,8:5,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Detroit Red Wings",
               "Tampa Bay Lightning", "0:0,1:0,2:1", "8:7,8:4,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Dallas Stars",
               "Edmonton Oilers", "1:0,1:2,2:0", "18:9,14:13,20:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Calgary Flames",
               "St. Louis Blues", "2:1,0:3,1:0", "7:14,3:9,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151013, "Los Angeles Kings",
               "Vancouver Canucks", "0:0,0:2,0:1", "5:7,4:14,6:5", 0, False)

print("Inserting "+leaguename+" Game Data From 10/14/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151014, "Columbus Blue Jackets",
               "Ottawa Senators", "2:1,1:3,0:3", "15:7,14:8,12:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151014, "Philadelphia Flyers",
               "Chicago Blackhawks", "0:0,2:0,1:0", "8:6,15:9,6:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151014, "Colorado Avalanche",
               "Boston Bruins", "0:2,1:3,1:1", "5:9,7:11,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151014, "Anaheim Ducks",
               "Arizona Coyotes", "0:3,0:1,0:0", "11:10,15:7,11:12", 0, False)

print("Inserting "+leaguename+" Game Data From 10/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151015, "New York Islanders",
               "Nashville Predators", "0:1,2:1,2:1", "7:17,13:17,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Pittsburgh Penguins",
               "Ottawa Senators", "0:0,2:0,0:0", "16:6,10:11,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Washington Capitals",
               "Chicago Blackhawks", "1:0,1:0,2:1", "9:5,7:17,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Montreal Canadiens",
               "New York Rangers", "0:0,1:0,2:0", "9:7,10:11,13:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Tampa Bay Lightning",
               "Dallas Stars", "1:2,0:2,2:1", "6:9,15:8,12:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Florida Panthers",
               "Buffalo Sabres", "2:0,0:1,1:1", "14:7,6:12,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Edmonton Oilers",
               "St. Louis Blues", "1:1,0:1,1:2", "10:7,7:10,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151015, "Arizona Coyotes",
               "Minnesota Wild", "0:2,2:2,1:0", "6:12,11:9,13:3", 0, False)

print("Inserting "+leaguename+" Game Data From 10/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151016, "New Jersey Devils",
               "San Jose Sharks", "0:1,0:0,1:0,0:0,1:2", "5:10,12:13,11:9,4:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Columbus Blue Jackets",
               "Toronto Maple Leafs", "1:0,1:3,1:3", "6:11,12:15,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Detroit Red Wings",
               "Carolina Hurricanes", "0:1,2:2,1:2", "5:13,11:13,4:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Winnipeg Jets",
               "Calgary Flames", "0:1,1:0,2:0", "8:11,9:4,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Vancouver Canucks",
               "St. Louis Blues", "0:1,1:2,2:1", "9:13,9:8,16:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Anaheim Ducks",
               "Colorado Avalanche", "0:1,0:1,0:1", "15:7,9:10,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151016, "Los Angeles Kings",
               "Minnesota Wild", "0:0,1:0,0:1,1:0", "16:5,16:9,4:10,1:2", 0, False)

print("Inserting "+leaguename+" Game Data From 10/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Montreal Canadiens",
               "Detroit Red Wings", "0:0,1:1,3:0", "12:8,9:9,20:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Ottawa Senators",
               "Nashville Predators", "0:1,2:1,1:1,0:0,1:2", "13:9,13:7,12:8,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Tampa Bay Lightning",
               "Buffalo Sabres", "0:1,1:0,1:0", "3:16,12:7,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Florida Panthers",
               "Dallas Stars", "0:0,2:1,0:3", "8:5,8:16,10:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Pittsburgh Penguins",
               "Toronto Maple Leafs", "2:1,0:0,0:0", "8:13,9:8,16:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Washington Capitals",
               "Carolina Hurricanes", "1:0,0:0,3:1", "17:5,10:7,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "New York Islanders",
               "San Jose Sharks", "0:1,3:2,3:0", "10:10,12:8,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Chicago Blackhawks",
               "Columbus Blue Jackets", "0:0,2:0,2:1", "6:9,15:3,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Calgary Flames",
               "Edmonton Oilers", "0:1,1:1,1:3", "8:5,5:14,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151017, "Arizona Coyotes",
               "Boston Bruins", "1:0,0:2,2:3", "7:14,4:19,13:10", 0, False)

print("Inserting "+leaguename+" Game Data From 10/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151018, "New York Rangers",
               "New Jersey Devils", "1:0,0:1,0:0,0:1", "9:6,8:11,8:5,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Winnipeg Jets",
               "St. Louis Blues", "0:0,2:2,0:2", "12:10,11:14,6:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Anaheim Ducks",
               "Minnesota Wild", "2:1,0:0,2:0", "9:6,3:13,10:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Vancouver Canucks",
               "Edmonton Oilers", "1:1,0:0,0:0,0:1", "13:5,10:8,10:9,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151018, "Los Angeles Kings",
               "Colorado Avalanche", "1:0,1:1,0:0", "14:10,12:7,14:6", 0, False)

print("Inserting "+leaguename+" Game Data From 10/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151019, "New York Rangers",
               "San Jose Sharks", "1:0,1:0,2:0", "13:9,10:4,5:9", 0, False)

print("Inserting "+leaguename+" Game Data From 10/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151020, "New Jersey Devils",
               "Arizona Coyotes", "0:0,1:0,1:2,1:0", "5:2,12:10,7:7,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Pittsburgh Penguins",
               "Florida Panthers", "1:0,0:0,1:2,1:0", "16:5,12:16,5:11,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Columbus Blue Jackets",
               "New York Islanders", "0:1,0:0,0:3", "12:14,13:10,12:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Philadelphia Flyers",
               "Dallas Stars", "0:1,0:1,1:0", "7:14,13:12,15:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Montreal Canadiens",
               "St. Louis Blues", "1:0,1:0,1:0", "11:17,13:11,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Nashville Predators",
               "Tampa Bay Lightning", "1:0,2:3,1:1,0:0,1:0", "12:10,9:8,11:10,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151020, "Calgary Flames",
               "Washington Capitals", "1:1,0:3,1:2", "7:7,4:13,8:10", 0, False)

print("Inserting "+leaguename+" Game Data From 10/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Buffalo Sabres",
               "Toronto Maple Leafs", "0:1,0:0,1:0,0:0,2:1", "12:6,12:11,10:4,1:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Boston Bruins",
               "Philadelphia Flyers", "2:2,2:0,0:2,0:1", "12:15,11:10,6:11,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Edmonton Oilers",
               "Detroit Red Wings", "1:0,2:0,0:1", "11:5,11:11,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151021, "Colorado Avalanche",
               "Carolina Hurricanes", "0:0,0:0,0:0,0:1", "9:5,7:5,9:8,1:1", 0, False)

print("Inserting "+leaguename+" Game Data From 10/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151022, "New York Rangers",
               "Arizona Coyotes", "0:1,1:0,3:0", "6:5,10:14,12:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Pittsburgh Penguins",
               "Dallas Stars", "0:2,1:2,0:0", "11:9,9:12,14:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Ottawa Senators",
               "New Jersey Devils", "1:2,1:0,2:2,0:0,1:2", "14:11,14:9,9:8,2:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Nashville Predators",
               "Anaheim Ducks", "0:0,3:0,2:1", "6:10,13:6,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Minnesota Wild",
               "Columbus Blue Jackets", "1:2,2:0,0:0", "6:13,13:9,4:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Chicago Blackhawks",
               "Florida Panthers", "1:1,1:0,1:1", "12:5,9:5,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "Vancouver Canucks",
               "Washington Capitals", "0:1,2:0,0:2", "8:11,10:12,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151022, "San Jose Sharks",
               "Los Angeles Kings", "0:2,1:1,0:1", "18:8,12:11,10:10", 0, False)

print("Inserting "+leaguename+" Game Data From 10/23/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Buffalo Sabres",
               "Montreal Canadiens", "0:1,2:3,0:3", "11:11,11:7,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "New York Islanders",
               "Boston Bruins", "2:1,0:2,1:2", "18:8,5:11,3:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Winnipeg Jets",
               "Tampa Bay Lightning", "1:1,1:2,1:0,0:1", "11:6,8:16,16:7,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Calgary Flames",
               "Detroit Red Wings", "1:2,0:0,1:0,1:0", "8:13,16:4,13:9,3:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Edmonton Oilers",
               "Washington Capitals", "2:3,2:3,0:1", "9:10,9:9,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151023, "Los Angeles Kings",
               "Carolina Hurricanes", "1:0,0:0,2:0", "9:15,9:13,10:12", 0, False)

print("Inserting "+leaguename+" Game Data From 10/24/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Minnesota Wild",
               "Anaheim Ducks", "1:0,2:0,0:0", "15:3,11:6,4:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Buffalo Sabres",
               "New Jersey Devils", "1:1,1:2,1:1", "6:7,12:13,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Montreal Canadiens",
               "Toronto Maple Leafs", "1:0,4:2,0:1", "11:14,11:23,5:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Ottawa Senators",
               "Arizona Coyotes", "0:1,1:0,0:3", "8:8,18:7,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Philadelphia Flyers",
               "New York Rangers", "1:1,1:1,0:0,0:0,2:1", "12:13,13:14,18:9,5:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "St. Louis Blues",
               "New York Islanders", "0:1,0:1,2:0,0:1", "8:9,14:7,15:2,3:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Nashville Predators",
               "Pittsburgh Penguins", "0:0,0:1,1:0,0:1", "5:7,17:11,17:5,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Dallas Stars",
               "Florida Panthers", "1:2,0:2,1:2", "10:9,16:13,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Chicago Blackhawks",
               "Tampa Bay Lightning", "0:0,0:0,0:0,1:0", "9:9,10:4,11:8,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Colorado Avalanche",
               "Columbus Blue Jackets", "1:2,2:0,0:2", "10:11,13:9,11:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "Vancouver Canucks",
               "Detroit Red Wings", "1:0,1:0,0:2,0:1", "10:7,13:4,7:12,2:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151024, "San Jose Sharks",
               "Carolina Hurricanes", "2:0,2:2,1:0", "6:7,8:12,7:15", 0, False)

print("Inserting "+leaguename+" Game Data From 10/25/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Winnipeg Jets",
               "Minnesota Wild", "3:1,2:2,0:1", "17:9,10:9,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "New York Rangers",
               "Calgary Flames", "0:1,2:0,2:0", "8:8,5:10,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151025, "Edmonton Oilers",
               "Los Angeles Kings", "1:1,0:1,1:1", "8:10,5:13,15:11", 0, False)

print("Inserting "+leaguename+" Game Data From 10/26/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151026, "New York Islanders",
               "Calgary Flames", "0:0,1:0,3:0", "14:8,10:10,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151026, "Toronto Maple Leafs",
               "Arizona Coyotes", "1:2,0:1,2:1", "8:8,5:11,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151026, "Chicago Blackhawks",
               "Anaheim Ducks", "0:0,0:0,0:0,1:0", "6:9,11:9,6:19,1:2", 0, False)

print("Inserting "+leaguename+" Game Data From 10/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Boston Bruins",
               "Arizona Coyotes", "1:0,2:0,3:0", "9:7,11:12,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "New Jersey Devils",
               "Columbus Blue Jackets", "0:0,0:0,1:3", "8:2,7:6,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Philadelphia Flyers",
               "Buffalo Sabres", "1:2,0:0,2:1,0:1", "7:11,13:14,10:13,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Detroit Red Wings",
               "Carolina Hurricanes", "0:0,1:1,0:2", "9:8,10:9,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Florida Panthers",
               "Colorado Avalanche", "1:0,0:0,3:1", "10:12,9:12,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "St. Louis Blues",
               "Tampa Bay Lightning", "1:0,0:0,1:0", "8:12,7:8,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Minnesota Wild",
               "Edmonton Oilers", "2:1,0:1,2:1", "8:5,11:9,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Winnipeg Jets",
               "Los Angeles Kings", "0:0,1:1,0:3", "9:8,11:10,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Dallas Stars",
               "Anaheim Ducks", "0:3,3:0,1:0", "6:9,11:9,17:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151027, "Vancouver Canucks",
               "Montreal Canadiens", "3:0,0:0,2:1", "11:12,9:11,8:3", 0, False)

print("Inserting "+leaguename+" Game Data From 10/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Ottawa Senators",
               "Calgary Flames", "0:0,2:1,2:3,0:0,2:1", "4:10,6:10,12:16,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "Washington Capitals",
               "Pittsburgh Penguins", "0:0,0:0,1:3", "13:14,14:4,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151028, "San Jose Sharks",
               "Nashville Predators", "0:1,0:0,1:1", "9:7,4:9,8:8", 0, False)

print("Inserting "+leaguename+" Game Data From 10/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151029, "New York Islanders",
               "Carolina Hurricanes", "1:1,1:0,0:1,0:1", "8:4,6:8,4:13,1:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Philadelphia Flyers",
               "New Jersey Devils", "0:0,1:1,0:3", "7:13,12:10,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Pittsburgh Penguins",
               "Buffalo Sabres", "2:2,2:0,0:1", "11:11,14:18,4:24", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Tampa Bay Lightning",
               "Colorado Avalanche", "0:1,1:1,0:0", "9:10,13:11,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "St. Louis Blues",
               "Anaheim Ducks", "0:0,1:1,1:0", "10:12,9:7,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Winnipeg Jets",
               "Chicago Blackhawks", "1:1,1:0,1:0", "9:14,13:18,9:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Dallas Stars",
               "Vancouver Canucks", "1:1,0:1,2:1,1:0", "13:10,5:12,9:10,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151029, "Edmonton Oilers",
               "Montreal Canadiens", "0:3,1:0,3:0", "5:11,11:5,11:5", 0, False)

print("Inserting "+leaguename+" Game Data From 10/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Buffalo Sabres",
               "Philadelphia Flyers", "1:0,1:0,1:1", "15:7,16:7,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "New York Rangers",
               "Toronto Maple Leafs", "1:0,0:0,2:1", "9:6,7:9,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Washington Capitals",
               "Columbus Blue Jackets", "0:0,1:0,1:1", "9:10,9:10,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Carolina Hurricanes",
               "Colorado Avalanche", "0:0,2:1,1:1", "7:11,13:7,6:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Detroit Red Wings",
               "Ottawa Senators", "0:1,1:1,0:1", "10:12,11:8,9:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Florida Panthers",
               "Boston Bruins", "0:1,1:2,0:0", "7:7,7:9,18:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Minnesota Wild",
               "Chicago Blackhawks", "3:2,1:2,1:0", "16:10,6:9,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Calgary Flames",
               "Montreal Canadiens", "0:1,2:3,0:2", "15:13,11:7,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151030, "Arizona Coyotes",
               "Vancouver Canucks", "0:3,2:1,1:0", "10:10,13:6,8:6", 0, False)

print("Inserting "+leaguename+" Game Data From 10/31/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151031, "New Jersey Devils",
               "New York Islanders", "2:0,0:2,0:0,0:0,2:1", "7:7,6:9,2:6,2:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Dallas Stars",
               "San Jose Sharks", "1:0,2:3,2:0", "10:9,6:9,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Los Angeles Kings",
               "Nashville Predators", "0:0,1:2,2:1,1:0", "7:8,12:12,8:11,2:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Toronto Maple Leafs",
               "Pittsburgh Penguins", "0:1,0:2,0:1", "5:9,9:14,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Ottawa Senators",
               "Detroit Red Wings", "0:1,1:2,2:2", "13:9,7:12,16:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Tampa Bay Lightning",
               "Boston Bruins", "1:1,0:0,0:2", "7:13,10:10,5:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Florida Panthers",
               "Washington Capitals", "0:0,1:0,0:1,0:1", "10:6,6:10,10:9,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Columbus Blue Jackets",
               "Winnipeg Jets", "1:3,0:0,1:0", "4:11,10:12,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "St. Louis Blues",
               "Minnesota Wild", "2:2,0:0,0:0,1:0", "7:7,8:9,8:10,3:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151031, "Edmonton Oilers",
               "Calgary Flames", "1:3,1:1,2:1", "8:12,11:10,4:10", 0, False)

print("Inserting "+leaguename+" Game Data From 11/1/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Colorado Avalanche",
               "San Jose Sharks", "1:1,1:1,1:2", "10:12,7:13,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Carolina Hurricanes",
               "Tampa Bay Lightning", "1:0,0:2,2:2", "6:10,11:14,18:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Montreal Canadiens",
               "Winnipeg Jets", "2:0,3:0,0:1", "6:6,12:9,8:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "New York Islanders",
               "Buffalo Sabres", "0:0,1:0,0:2", "10:6,13:6,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151101, "Anaheim Ducks",
               "Nashville Predators", "3:0,1:2,0:0", "13:17,12:17,3:8", 0, False)

print("Inserting "+leaguename+" Game Data From 11/2/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151102, "Toronto Maple Leafs",
               "Dallas Stars", "1:1,2:0,1:0", "8:12,12:19,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151102, "Chicago Blackhawks",
               "Los Angeles Kings", "1:2,0:0,3:0", "6:10,8:6,12:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151102, "Vancouver Canucks",
               "Philadelphia Flyers", "1:0,1:1,2:0", "10:11,13:10,11:7", 0, False)

print("Inserting "+leaguename+" Game Data From 11/3/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Boston Bruins",
               "Dallas Stars", "2:1,0:2,1:2", "15:6,9:9,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "New York Islanders",
               "New Jersey Devils", "1:0,0:0,1:1", "12:8,11:11,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "New York Rangers",
               "Washington Capitals", "2:1,2:1,1:0", "9:8,3:14,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Montreal Canadiens",
               "Ottawa Senators", "0:0,1:1,0:0,0:1", "10:7,12:8,15:11,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Detroit Red Wings",
               "Tampa Bay Lightning", "0:0,1:1,1:0", "9:8,10:9,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "St. Louis Blues",
               "Los Angeles Kings", "0:0,0:1,0:2", "5:12,11:17,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Colorado Avalanche",
               "Calgary Flames", "1:0,2:2,3:1", "17:11,13:7,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "Edmonton Oilers",
               "Philadelphia Flyers", "1:0,0:2,3:0", "19:2,17:13,13:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151103, "San Jose Sharks",
               "Columbus Blue Jackets", "1:1,1:3,0:1", "10:13,15:8,18:3", 0, False)

print("Inserting "+leaguename+" Game Data From 11/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Toronto Maple Leafs",
               "Winnipeg Jets", "1:2,1:0,0:2", "13:10,8:10,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Chicago Blackhawks",
               "St. Louis Blues", "5:2,0:3,0:0,0:1", "18:8,8:12,14:7,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Vancouver Canucks",
               "Pittsburgh Penguins", "0:1,0:0,2:2", "6:7,7:7,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151104, "Anaheim Ducks",
               "Florida Panthers", "0:0,1:2,1:0,0:0,2:1", "14:6,13:9,10:5,2:5", 0, False)

print("Inserting "+leaguename+" Game Data From 11/5/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Buffalo Sabres",
               "Tampa Bay Lightning", "0:3,1:0,0:1", "8:11,21:8,2:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Washington Capitals",
               "Boston Bruins", "1:1,2:0,1:0", "14:9,9:13,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Montreal Canadiens",
               "New York Islanders", "1:0,0:1,3:0", "8:5,7:8,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Ottawa Senators",
               "Winnipeg Jets", "1:0,1:1,0:1,0:0,3:1", "11:9,10:10,7:14,3:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Minnesota Wild",
               "Nashville Predators", "0:0,1:1,1:2", "6:7,14:9,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Calgary Flames",
               "Philadelphia Flyers", "1:0,0:1,0:0,1:0", "8:8,10:9,10:8,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Arizona Coyotes",
               "Colorado Avalanche", "1:0,2:1,1:1", "9:7,13:12,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "Los Angeles Kings",
               "Columbus Blue Jackets", "1:2,0:0,1:1", "15:8,8:0,10:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151105, "San Jose Sharks",
               "Florida Panthers", "2:1,2:1,1:0", "11:11,11:11,10:11", 0, False)

print("Inserting "+leaguename+" Game Data From 11/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Toronto Maple Leafs",
               "Detroit Red Wings", "0:1,0:0,1:0,0:1", "12:9,8:3,13:9,0:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "New Jersey Devils",
               "Chicago Blackhawks", "3:0,1:1,0:1", "13:8,8:7,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Carolina Hurricanes",
               "Dallas Stars", "0:0,1:1,0:3", "6:13,13:8,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Colorado Avalanche",
               "New York Rangers", "1:0,0:2,0:0", "7:11,9:10,14:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Edmonton Oilers",
               "Pittsburgh Penguins", "0:0,1:1,0:1", "5:15,14:11,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151106, "Anaheim Ducks",
               "Columbus Blue Jackets", "1:0,1:1,2:1", "11:10,11:10,12:16", 0, False)

print("Inserting "+leaguename+" Game Data From 11/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Buffalo Sabres",
               "Vancouver Canucks", "0:0,2:1,1:1", "4:15,8:12,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Los Angeles Kings",
               "Florida Panthers", "0:1,3:0,1:0", "10:5,20:4,5:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Montreal Canadiens",
               "Boston Bruins", "0:1,1:1,3:0", "6:12,14:8,13:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Washington Capitals",
               "Toronto Maple Leafs", "0:1,1:0,1:1,0:0,1:0", "11:10,6:8,11:3,3:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Carolina Hurricanes",
               "Ottawa Senators", "0:0,1:2,1:0,1:0", "14:7,11:9,18:5,3:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Winnipeg Jets",
               "Philadelphia Flyers", "0:1,0:0,0:2", "12:8,6:8,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Nashville Predators",
               "St. Louis Blues", "0:1,0:0,0:3", "12:9,19:9,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Minnesota Wild",
               "Tampa Bay Lightning", "0:0,1:0,0:0", "7:13,11:7,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Arizona Coyotes",
               "New York Rangers", "0:1,0:3,1:0", "13:14,9:10,18:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "Calgary Flames",
               "Pittsburgh Penguins", "3:1,1:1,1:0", "16:8,11:10,4:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151107, "San Jose Sharks",
               "Anaheim Ducks", "0:1,0:0,0:0", "11:11,7:4,13:2", 0, False)

print("Inserting "+leaguename+" Game Data From 11/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Detroit Red Wings",
               "Dallas Stars", "1:2,0:0,0:2", "8:15,3:3,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "New Jersey Devils",
               "Vancouver Canucks", "2:1,1:2,0:0,1:0", "6:13,17:10,3:7,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "New York Islanders",
               "Boston Bruins", "0:1,0:1,1:0", "11:11,13:10,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151108, "Chicago Blackhawks",
               "Edmonton Oilers", "2:0,0:0,2:2", "9:5,6:22,13:9", 0, False)

print("Inserting "+leaguename+" Game Data From 11/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151109, "Anaheim Ducks",
               "Arizona Coyotes", "2:0,0:3,1:0,0:1", "6:6,11:12,18:9,1:1", 0, False)

print("Inserting "+leaguename+" Game Data From 11/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151110, "New Jersey Devils",
               "St. Louis Blues", "0:0,0:1,0:1", "11:6,4:14,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "New York Rangers",
               "Carolina Hurricanes", "2:0,0:0,1:0", "3:8,14:14,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Philadelphia Flyers",
               "Colorado Avalanche", "0:1,0:2,0:1", "7:15,7:14,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Columbus Blue Jackets",
               "Vancouver Canucks", "2:2,0:0,1:3", "11:13,22:7,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Detroit Red Wings",
               "Washington Capitals", "0:0,0:0,1:0", "9:14,9:7,9:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Tampa Bay Lightning",
               "Buffalo Sabres", "0:1,1:1,0:2", "5:11,13:8,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Florida Panthers",
               "Calgary Flames", "2:1,1:2,1:0", "11:9,11:12,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Nashville Predators",
               "Ottawa Senators", "1:3,3:2,3:0", "12:10,12:3,14:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Minnesota Wild",
               "Winnipeg Jets", "1:1,4:0,0:2", "7:8,11:7,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Dallas Stars",
               "Toronto Maple Leafs", "0:1,1:0,1:2", "12:8,16:10,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "Los Angeles Kings",
               "Arizona Coyotes", "1:1,1:1,0:1", "10:4,11:15,14:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151110, "San Jose Sharks",
               "New York Islanders", "0:2,1:0,1:2", "11:11,14:6,11:8", 0, False)

print("Inserting "+leaguename+" Game Data From 11/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Pittsburgh Penguins",
               "Montreal Canadiens", "2:1,0:2,1:0,0:0,2:0", "14:13,1:13,17:10,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151111, "Anaheim Ducks",
               "Edmonton Oilers", "1:0,0:1,2:2,0:1", "15:8,6:10,16:6,0:3", 0, False)

print("Inserting "+leaguename+" Game Data From 11/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Boston Bruins",
               "Colorado Avalanche", "2:2,0:0,0:1", "7:7,13:13,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "New York Rangers",
               "St. Louis Blues", "3:1,1:2,2:0", "7:16,8:10,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Philadelphia Flyers",
               "Washington Capitals", "1:1,1:3,0:1", "4:11,7:12,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Carolina Hurricanes",
               "Minnesota Wild", "2:1,0:1,0:0,0:1", "19:5,3:8,14:6,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Ottawa Senators",
               "Vancouver Canucks", "1:1,1:0,1:1", "7:7,8:19,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Tampa Bay Lightning",
               "Calgary Flames", "0:0,1:1,2:0", "11:8,7:15,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Florida Panthers",
               "Buffalo Sabres", "0:1,1:1,1:1", "8:6,17:7,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Nashville Predators",
               "Toronto Maple Leafs", "0:0,0:0,1:1,0:0,0:1", "4:6,8:8,9:7,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Chicago Blackhawks",
               "New Jersey Devils", "1:0,0:2,1:1", "10:7,10:6,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Dallas Stars",
               "Winnipeg Jets", "2:2,1:0,3:1", "16:12,6:15,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Arizona Coyotes",
               "Edmonton Oilers", "1:1,2:0,1:0", "7:7,10:14,4:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151112, "Los Angeles Kings",
               "New York Islanders", "1:1,1:0,0:0", "8:13,10:7,4:12", 0, False)

print("Inserting "+leaguename+" Game Data From 11/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Pittsburgh Penguins",
               "Columbus Blue Jackets", "0:0,0:2,1:0", "5:10,10:10,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Washington Capitals",
               "Calgary Flames", "0:0,0:1,2:1,0:1", "9:11,10:9,15:7,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Detroit Red Wings",
               "San Jose Sharks", "1:2,0:1,1:0", "10:7,12:4,6:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151113, "Anaheim Ducks",
               "New York Islanders", "0:1,1:1,0:2", "7:14,9:5,9:10", 0, False)

print("Inserting "+leaguename+" Game Data From 11/14/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Ottawa Senators",
               "New York Rangers", "1:1,0:0,0:0,0:0,1:2", "10:11,7:10,5:9,1:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Boston Bruins",
               "Detroit Red Wings", "0:0,3:0,0:1", "12:5,12:8,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Buffalo Sabres",
               "San Jose Sharks", "0:1,0:0,1:0,0:1", "8:9,9:9,13:9,1:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Toronto Maple Leafs",
               "Vancouver Canucks", "1:0,1:1,2:1", "10:6,15:14,15:25", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Montreal Canadiens",
               "Colorado Avalanche", "0:3,1:1,0:2", "18:8,14:3,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Tampa Bay Lightning",
               "Florida Panthers", "1:1,2:2,1:1,0:0,0:1", "6:7,11:6,10:9,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "New Jersey Devils",
               "Pittsburgh Penguins", "1:0,1:0,2:0", "10:8,12:5,15:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Carolina Hurricanes",
               "Philadelphia Flyers", "1:0,1:1,0:1,0:1", "9:3,9:4,3:11,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Columbus Blue Jackets",
               "Arizona Coyotes", "2:1,1:1,2:0", "8:11,7:12,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Nashville Predators",
               "Winnipeg Jets", "4:0,1:0,2:0", "9:4,11:10,14:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "St. Louis Blues",
               "Chicago Blackhawks", "0:1,2:2,0:1", "9:10,12:13,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Dallas Stars",
               "Minnesota Wild", "1:0,0:1,1:1,1:0", "10:7,11:11,10:6,5:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151114, "Los Angeles Kings",
               "Edmonton Oilers", "2:0,1:2,1:1", "14:7,7:11,7:7", 0, False)

print("Inserting "+leaguename+" Game Data From 11/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151115, "New York Rangers",
               "Toronto Maple Leafs", "0:1,2:1,2:1", "8:12,11:9,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151115, "Chicago Blackhawks",
               "Calgary Flames", "0:0,3:1,1:0", "10:4,15:12,16:10", 0, False)

print("Inserting "+leaguename+" Game Data From 11/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151116, "New York Islanders",
               "Arizona Coyotes", "1:0,0:0,4:2", "9:7,14:7,9:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151116, "Carolina Hurricanes",
               "Anaheim Ducks", "0:1,1:1,0:2", "4:5,10:4,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151116, "Montreal Canadiens",
               "Vancouver Canucks", "0:2,2:1,1:0,1:0", "9:11,15:7,8:6,4:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151116, "Ottawa Senators",
               "Detroit Red Wings", "1:2,0:1,2:0,0:1", "8:8,7:13,10:15,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151116, "Florida Panthers",
               "Tampa Bay Lightning", "0:0,0:0,1:0", "4:13,9:11,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151116, "St. Louis Blues",
               "Winnipeg Jets", "2:0,1:2,0:0", "11:3,9:9,8:6", 0, False)

print("Inserting "+leaguename+" Game Data From 11/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Boston Bruins",
               "San Jose Sharks", "2:2,1:3,1:0", "9:9,9:14,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Buffalo Sabres",
               "Dallas Stars", "0:1,0:0,1:2", "6:9,11:12,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Philadelphia Flyers",
               "Los Angeles Kings", "1:1,0:0,1:1,0:0,0:1", "14:11,11:10,8:14,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Columbus Blue Jackets",
               "St. Louis Blues", "1:1,1:0,1:0", "10:11,21:3,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Pittsburgh Penguins",
               "Minnesota Wild", "2:1,2:1,0:1", "12:8,11:8,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Toronto Maple Leafs",
               "Colorado Avalanche", "2:0,1:1,2:0", "10:13,11:12,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Nashville Predators",
               "Anaheim Ducks", "2:1,1:0,0:1", "8:10,9:19,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151117, "Calgary Flames",
               "New Jersey Devils", "2:0,1:2,0:0", "7:6,11:9,12:5", 0, False)

print("Inserting "+leaguename+" Game Data From 11/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Winnipeg Jets",
               "Vancouver Canucks", "1:0,1:1,2:0", "11:14,6:10,17:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Detroit Red Wings",
               "Washington Capitals", "1:1,0:0,0:0,0:1", "7:10,13:8,6:8,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151118, "Edmonton Oilers",
               "Chicago Blackhawks", "0:0,1:2,2:1,0:1", "11:3,9:12,16:10,1:2", 0, False)

print("Inserting "+leaguename+" Game Data From 11/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Boston Bruins",
               "Minnesota Wild", "1:0,2:2,1:0", "10:10,18:8,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Philadelphia Flyers",
               "San Jose Sharks", "0:0,0:0,0:0,0:1", "6:10,15:5,9:4,4:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Pittsburgh Penguins",
               "Colorado Avalanche", "0:1,3:0,1:2", "10:13,10:8,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Washington Capitals",
               "Dallas Stars", "1:1,0:0,1:2", "12:12,8:11,15:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Montreal Canadiens",
               "Arizona Coyotes", "0:2,1:1,1:0", "13:5,6:8,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Ottawa Senators",
               "Columbus Blue Jackets", "0:0,2:0,1:0", "8:6,11:6,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Tampa Bay Lightning",
               "New York Rangers", "1:0,0:0,1:1", "10:7,7:7,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "Florida Panthers",
               "Anaheim Ducks", "0:0,0:1,1:2", "7:16,7:17,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151119, "St. Louis Blues",
               "Buffalo Sabres", "1:0,1:2,0:0,0:0,1:0", "9:6,7:11,10:13,3:4", 0, False)

print("Inserting "+leaguename+" Game Data From 11/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Carolina Hurricanes",
               "Toronto Maple Leafs", "0:0,0:0,1:1,0:0,1:2", "12:8,10:4,9:8,3:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Columbus Blue Jackets",
               "Nashville Predators", "2:0,1:0,1:0", "5:10,7:17,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Detroit Red Wings",
               "Los Angeles Kings", "1:1,2:1,0:0", "10:14,9:15,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "New York Islanders",
               "Montreal Canadiens", "1:3,1:1,1:1", "10:11,15:11,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Calgary Flames",
               "Chicago Blackhawks", "1:1,0:0,0:0,1:0", "13:7,4:8,14:4,6:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151120, "Edmonton Oilers",
               "New Jersey Devils", "1:0,1:1,3:0", "9:4,6:12,12:4", 0, False)

print("Inserting "+leaguename+" Game Data From 11/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Boston Bruins",
               "Toronto Maple Leafs", "0:0,0:0,2:0", "14:7,10:9,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Ottawa Senators",
               "Philadelphia Flyers", "1:0,2:0,1:0", "7:10,16:13,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Tampa Bay Lightning",
               "Anaheim Ducks", "0:0,3:0,2:0", "6:8,9:13,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Florida Panthers",
               "New York Rangers", "0:1,2:1,2:2,0:1", "13:13,15:9,15:8,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Pittsburgh Penguins",
               "San Jose Sharks", "0:1,1:1,0:1", "12:9,15:9,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Washington Capitals",
               "Colorado Avalanche", "4:0,0:2,3:1", "11:10,11:10,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Winnipeg Jets",
               "Arizona Coyotes", "1:2,1:0,1:0", "9:10,5:12,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "St. Louis Blues",
               "Detroit Red Wings", "2:2,0:1,1:0,0:1", "13:13,11:6,7:9,2:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Dallas Stars",
               "Buffalo Sabres", "1:0,0:0,2:0", "10:8,5:5,17:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Minnesota Wild",
               "Nashville Predators", "1:0,2:0,1:0", "8:10,14:8,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151121, "Vancouver Canucks",
               "Chicago Blackhawks", "2:2,1:0,3:1", "7:7,6:11,7:11", 0, False)

print("Inserting "+leaguename+" Game Data From 11/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Carolina Hurricanes",
               "Los Angeles Kings", "1:0,3:2,0:1", "10:7,11:14,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Columbus Blue Jackets",
               "San Jose Sharks", "0:1,2:0,1:4", "5:10,19:7,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Montreal Canadiens",
               "New York Islanders", "0:1,2:0,2:1", "10:9,9:10,8:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151122, "Vancouver Canucks",
               "New Jersey Devils", "0:0,0:1,2:2", "6:9,13:6,19:7", 0, False)

print("Inserting "+leaguename+" Game Data From 11/23/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Buffalo Sabres",
               "St. Louis Blues", "0:0,1:0,0:2", "8:8,10:7,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "New York Rangers",
               "Nashville Predators", "0:0,1:0,2:0", "3:14,4:11,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Philadelphia Flyers",
               "Carolina Hurricanes", "0:0,2:0,0:2,1:0", "11:10,18:6,6:17,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Washington Capitals",
               "Edmonton Oilers", "0:0,0:0,1:0", "7:13,8:10,15:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Toronto Maple Leafs",
               "Boston Bruins", "0:2,3:1,0:0,0:0,0:1", "12:9,16:8,10:11,4:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Florida Panthers",
               "Los Angeles Kings", "0:1,1:1,0:1", "4:18,15:7,15:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151123, "Winnipeg Jets",
               "Colorado Avalanche", "1:0,0:1,0:3", "9:9,7:7,5:13", 0, False)

print("Inserting "+leaguename+" Game Data From 11/24/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Dallas Stars",
               "Ottawa Senators", "0:2,1:2,3:3", "11:6,12:6,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151124, "Anaheim Ducks",
               "Calgary Flames", "2:2,0:1,3:0", "9:10,13:4,10:11", 0, False)

print("Inserting "+leaguename+" Game Data From 11/25/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Buffalo Sabres",
               "Nashville Predators", "0:1,1:2,1:0", "11:4,14:7,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "New Jersey Devils",
               "Columbus Blue Jackets", "0:1,1:1,0:0", "4:14,14:6,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "New York Rangers",
               "Montreal Canadiens", "0:1,1:1,0:3", "11:10,12:8,11:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Pittsburgh Penguins",
               "St. Louis Blues", "1:1,1:0,1:2,1:0", "11:11,12:9,10:11,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Washington Capitals",
               "Winnipeg Jets", "2:2,2:1,1:0", "15:6,11:13,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Carolina Hurricanes",
               "Edmonton Oilers", "1:1,2:0,1:0", "7:8,12:10,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Minnesota Wild",
               "Vancouver Canucks", "1:1,0:1,1:1", "13:9,5:10,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "New York Islanders",
               "Philadelphia Flyers", "1:1,1:0,1:0", "9:8,12:6,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Detroit Red Wings",
               "Boston Bruins", "0:1,2:0,0:1,0:1", "13:9,11:4,10:8,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Tampa Bay Lightning",
               "Los Angeles Kings", "0:0,0:0,1:1,0:0,2:1", "11:8,8:13,9:13,2:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Arizona Coyotes",
               "Anaheim Ducks", "1:0,1:0,2:2", "6:10,14:10,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "Colorado Avalanche",
               "Ottawa Senators", "1:2,0:2,2:1", "11:14,10:11,22:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151125, "San Jose Sharks",
               "Chicago Blackhawks", "1:2,0:1,1:2", "5:11,12:6,12:9", 0, False)

print("Inserting "+leaguename+" Game Data From 11/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Boston Bruins",
               "New York Rangers", "1:0,1:2,2:1", "12:7,11:10,11:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Philadelphia Flyers",
               "Nashville Predators", "1:1,0:0,1:1,1:0", "10:12,10:10,10:12,6:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Minnesota Wild",
               "Winnipeg Jets", "0:0,0:1,1:2", "3:11,7:6,5:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Anaheim Ducks",
               "Chicago Blackhawks", "1:0,1:0,0:2,0:1", "8:9,8:14,9:7,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Washington Capitals",
               "Tampa Bay Lightning", "1:0,2:0,1:2", "18:9,13:5,6:20", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Buffalo Sabres",
               "Carolina Hurricanes", "1:0,2:1,1:0", "3:11,11:12,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "New Jersey Devils",
               "Montreal Canadiens", "0:0,2:1,0:1,0:0,1:2", "9:5,13:9,4:8,1:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Columbus Blue Jackets",
               "Pittsburgh Penguins", "0:0,0:0,1:1,1:0", "15:7,9:8,13:9,6:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Detroit Red Wings",
               "Edmonton Oilers", "0:0,3:2,0:1,1:0", "9:4,16:11,6:9,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Florida Panthers",
               "New York Islanders", "1:0,1:0,0:2,0:0,5:4", "11:9,7:6,5:9,4:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Dallas Stars",
               "Vancouver Canucks", "1:0,1:1,0:1,0:0,1:0", "8:14,6:7,5:13,6:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151127, "Arizona Coyotes",
               "Calgary Flames", "0:0,1:1,0:0,1:0", "8:12,5:9,5:4,3:1", 0, False)

print("Inserting "+leaguename+" Game Data From 11/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151128, "New York Rangers",
               "Philadelphia Flyers", "0:0,0:1,0:2", "10:4,7:18,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Toronto Maple Leafs",
               "Washington Capitals", "1:1,1:3,0:0", "16:4,4:11,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Montreal Canadiens",
               "New Jersey Devils", "0:0,1:0,1:2,0:1", "10:5,8:12,12:12,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Tampa Bay Lightning",
               "New York Islanders", "1:0,1:2,0:1", "9:6,17:7,5:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Pittsburgh Penguins",
               "Edmonton Oilers", "0:2,2:0,0:0,0:0,0:2", "14:13,11:9,11:11,5:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "St. Louis Blues",
               "Columbus Blue Jackets", "0:1,1:0,2:0", "6:6,18:8,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Nashville Predators",
               "Buffalo Sabres", "1:0,0:2,0:2", "13:9,7:10,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Minnesota Wild",
               "Dallas Stars", "2:0,1:0,0:3,0:1", "9:7,8:19,7:16,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Colorado Avalanche",
               "Winnipeg Jets", "2:0,1:2,2:1", "11:11,9:11,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Arizona Coyotes",
               "Ottawa Senators", "1:1,2:1,1:1", "4:18,10:8,5:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "San Jose Sharks",
               "Calgary Flames", "2:0,2:0,1:2", "11:10,12:7,6:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151128, "Los Angeles Kings",
               "Chicago Blackhawks", "0:1,0:1,2:0,1:0", "8:6,12:8,11:5,5:3", 0, False)

print("Inserting "+leaguename+" Game Data From 11/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151129, "Detroit Red Wings",
               "Florida Panthers", "0:0,1:0,0:1,0:1", "10:9,7:13,11:9,1:1", 0, False)

print("Inserting "+leaguename+" Game Data From 11/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151130, "New York Islanders",
               "Colorado Avalanche", "1:1,1:1,3:1", "7:10,14:4,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151130, "New York Rangers",
               "Carolina Hurricanes", "2:0,2:2,0:1", "6:10,8:14,8:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151130, "Toronto Maple Leafs",
               "Edmonton Oilers", "1:0,0:0,2:0", "3:8,13:8,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151130, "Anaheim Ducks",
               "Vancouver Canucks", "2:0,0:0,2:0", "14:8,9:8,7:9", 0, False)

print("Inserting "+leaguename+" Game Data From 12/1/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151201, "New Jersey Devils",
               "Colorado Avalanche", "0:0,0:2,1:0", "10:10,9:9,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Montreal Canadiens",
               "Columbus Blue Jackets", "1:1,0:0,1:0", "10:11,8:6,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Ottawa Senators",
               "Philadelphia Flyers", "1:1,1:2,0:1", "8:7,5:18,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Detroit Red Wings",
               "Buffalo Sabres", "2:1,1:1,1:2,0:0,1:0", "13:16,20:9,12:5,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "St. Louis Blues",
               "Florida Panthers", "0:0,1:3,0:0", "3:4,10:11,17:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Nashville Predators",
               "Arizona Coyotes", "0:1,1:1,4:0", "13:4,14:6,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Chicago Blackhawks",
               "Minnesota Wild", "0:1,1:0,0:1", "8:14,11:11,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Calgary Flames",
               "Dallas Stars", "0:2,0:1,3:0,0:0,3:1", "4:14,12:7,16:4,0:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "Los Angeles Kings",
               "Vancouver Canucks", "0:1,0:0,1:0,1:0", "12:6,10:9,15:1,3:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151201, "San Jose Sharks",
               "Pittsburgh Penguins", "0:1,1:2,0:2", "12:13,8:7,14:9", 0, False)

print("Inserting "+leaguename+" Game Data From 12/2/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Winnipeg Jets",
               "Toronto Maple Leafs", "2:1,0:0,4:0", "11:9,12:8,12:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "New York Islanders",
               "New York Rangers", "0:0,1:1,0:0,0:0,1:0", "6:13,16:9,12:6,3:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Edmonton Oilers",
               "Boston Bruins", "0:0,1:1,1:1,0:0,1:0", "10:8,13:15,10:13,3:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151202, "Anaheim Ducks",
               "Tampa Bay Lightning", "0:0,1:2,0:0", "5:8,16:9,12:5", 0, False)

print("Inserting "+leaguename+" Game Data From 12/3/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151203, "New York Rangers",
               "Colorado Avalanche", "0:0,0:2,1:0", "4:3,13:9,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Carolina Hurricanes",
               "New Jersey Devils", "0:1,1:3,0:1", "8:9,14:11,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Montreal Canadiens",
               "Washington Capitals", "0:1,1:1,1:1", "10:6,17:7,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Ottawa Senators",
               "Chicago Blackhawks", "2:0,0:2,1:1,1:0", "8:11,6:16,12:11,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Detroit Red Wings",
               "Arizona Coyotes", "3:0,1:1,1:0", "16:9,14:9,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Nashville Predators",
               "Florida Panthers", "0:1,1:1,0:0", "5:7,17:6,11:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Minnesota Wild",
               "Toronto Maple Leafs", "0:0,1:0,0:0", "12:8,5:10,11:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151203, "Vancouver Canucks",
               "Dallas Stars", "1:1,0:1,1:2", "4:6,6:18,6:10", 0, False)

print("Inserting "+leaguename+" Game Data From 12/4/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Buffalo Sabres",
               "Arizona Coyotes", "0:1,2:0,3:1", "7:7,10:7,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "New Jersey Devils",
               "Philadelphia Flyers", "1:1,0:1,2:1,0:1", "5:9,7:8,6:6,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Columbus Blue Jackets",
               "Florida Panthers", "0:0,1:1,0:0,0:0,1:2", "8:15,8:10,7:5,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "New York Islanders",
               "St. Louis Blues", "0:1,0:0,1:0,0:0,2:0", "6:11,9:7,7:9,3:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Calgary Flames",
               "Boston Bruins", "2:1,1:2,1:1,1:0", "9:15,12:7,14:11,2:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Edmonton Oilers",
               "Dallas Stars", "1:0,0:1,0:0,1:0", "8:14,10:13,4:15,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151204, "Anaheim Ducks",
               "San Jose Sharks", "0:0,0:0,1:0", "10:10,6:11,10:2", 0, False)

print("Inserting "+leaguename+" Game Data From 12/5/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Winnipeg Jets",
               "Washington Capitals", "1:0,0:1,0:0,1:0", "17:6,8:14,9:12,2:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Los Angeles Kings",
               "Pittsburgh Penguins", "0:0,4:2,1:1", "10:3,18:8,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Ottawa Senators",
               "New York Islanders", "0:1,0:0,2:1,1:0", "9:7,9:14,7:9,4:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Detroit Red Wings",
               "Nashville Predators", "1:0,1:3,2:1,1:0", "6:13,17:13,11:5,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Carolina Hurricanes",
               "Montreal Canadiens", "1:1,1:1,1:0", "10:9,10:16,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "St. Louis Blues",
               "Toronto Maple Leafs", "1:1,0:2,0:1", "15:15,2:9,11:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Philadelphia Flyers",
               "Columbus Blue Jackets", "0:2,1:2,0:0", "4:13,13:15,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Minnesota Wild",
               "Colorado Avalanche", "0:0,1:0,2:0", "17:6,12:10,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "Vancouver Canucks",
               "Boston Bruins", "0:2,0:1,0:1", "5:5,7:9,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151205, "San Jose Sharks",
               "Tampa Bay Lightning", "0:2,1:1,2:1", "4:6,14:8,16:6", 0, False)

print("Inserting "+leaguename+" Game Data From 12/6/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Carolina Hurricanes",
               "Arizona Coyotes", "2:2,1:0,2:2", "6:6,5:10,7:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Chicago Blackhawks",
               "Winnipeg Jets", "1:0,0:1,2:0", "11:11,9:12,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "New Jersey Devils",
               "Florida Panthers", "2:0,1:2,1:0", "11:7,4:12,3:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "New York Rangers",
               "Ottawa Senators", "2:0,0:1,2:0", "10:8,9:13,12:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Edmonton Oilers",
               "Buffalo Sabres", "3:1,1:1,0:0", "9:7,13:11,6:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Anaheim Ducks",
               "Pittsburgh Penguins", "0:1,2:0,0:0", "9:6,7:9,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151206, "Los Angeles Kings",
               "Tampa Bay Lightning", "1:0,2:1,0:0", "8:6,11:11,9:8", 0, False)

print("Inserting "+leaguename+" Game Data From 12/7/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151207, "Boston Bruins",
               "Nashville Predators", "1:1,1:1,0:1", "7:12,4:12,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151207, "Colorado Avalanche",
               "Minnesota Wild", "0:0,1:0,0:1,1:0", "6:4,4:9,6:4,4:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151207, "Vancouver Canucks",
               "Buffalo Sabres", "2:1,2:0,1:1", "11:9,10:12,10:13", 0, False)

print("Inserting "+leaguename+" Game Data From 12/8/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Philadelphia Flyers",
               "New York Islanders", "1:2,1:1,1:0,0:0,0:1", "15:9,17:5,13:11,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Columbus Blue Jackets",
               "Los Angeles Kings", "0:0,2:1,0:1,0:1", "5:8,6:15,10:16,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Washington Capitals",
               "Detroit Red Wings", "1:1,0:1,1:0,0:0,2:0", "11:8,17:7,11:6,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Toronto Maple Leafs",
               "New Jersey Devils", "1:1,1:1,0:0,0:0,2:1", "16:7,8:10,9:8,4:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Florida Panthers",
               "Ottawa Senators", "1:0,1:1,0:3", "11:7,8:6,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "St. Louis Blues",
               "Arizona Coyotes", "0:1,2:0,2:0", "3:9,9:7,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Chicago Blackhawks",
               "Nashville Predators", "1:0,1:1,2:0", "9:12,6:14,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Dallas Stars",
               "Carolina Hurricanes", "4:0,1:1,1:4", "8:10,7:11,5:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151208, "Calgary Flames",
               "San Jose Sharks", "2:2,2:0,0:0", "9:14,16:10,8:9", 0, False)

print("Inserting "+leaguename+" Game Data From 12/9/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Montreal Canadiens",
               "Boston Bruins", "1:0,0:0,0:3", "14:7,12:7,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Edmonton Oilers",
               "San Jose Sharks", "0:0,1:0,2:3,1:0", "6:9,8:10,5:8,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Colorado Avalanche",
               "Pittsburgh Penguins", "2:1,0:0,0:3", "10:10,4:13,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151209, "Vancouver Canucks",
               "New York Rangers", "0:0,0:0,2:1", "7:15,7:8,11:10", 0, False)

print("Inserting "+leaguename+" Game Data From 12/10/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Detroit Red Wings",
               "Montreal Canadiens", "0:0,1:1,2:1", "10:7,7:10,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Tampa Bay Lightning",
               "Ottawa Senators", "1:0,0:0,3:1", "6:8,11:13,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Florida Panthers",
               "Washington Capitals", "1:0,1:0,2:1", "9:7,10:10,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "St. Louis Blues",
               "Philadelphia Flyers", "0:0,1:3,1:1", "10:10,13:12,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Nashville Predators",
               "Chicago Blackhawks", "3:0,0:0,2:1", "18:7,8:13,8:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Winnipeg Jets",
               "Columbus Blue Jackets", "3:1,0:1,3:2", "11:5,15:7,9:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151210, "Calgary Flames",
               "Buffalo Sabres", "0:0,2:0,2:3", "10:6,12:8,10:16", 0, False)

print("Inserting "+leaguename+" Game Data From 12/11/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151211, "New Jersey Devils",
               "Detroit Red Wings", "0:0,0:2,2:0,1:0", "10:10,17:10,9:5,2:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Pittsburgh Penguins",
               "Los Angeles Kings", "0:1,1:0,1:1,0:0,1:2", "10:13,18:12,11:13,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Chicago Blackhawks",
               "Winnipeg Jets", "1:0,1:0,0:0", "13:7,8:5,10:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Dallas Stars",
               "Philadelphia Flyers", "0:0,2:1,1:0", "18:9,16:6,10:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Arizona Coyotes",
               "Minnesota Wild", "0:0,1:1,0:0,1:0", "5:10,6:10,9:8,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Edmonton Oilers",
               "New York Rangers", "3:1,0:2,4:2", "15:9,15:9,7:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151211, "Anaheim Ducks",
               "Carolina Hurricanes", "0:1,0:2,1:2", "9:8,7:9,16:7", 0, False)

print("Inserting "+leaguename+" Game Data From 12/12/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Boston Bruins",
               "Florida Panthers", "1:0,1:0,1:1", "10:6,10:7,5:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Buffalo Sabres",
               "Los Angeles Kings", "1:1,0:0,0:0,1:0", "12:3,9:7,8:8,1:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Montreal Canadiens",
               "Ottawa Senators", "2:0,1:1,0:0", "27:8,9:10,6:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Tampa Bay Lightning",
               "Washington Capitals", "0:1,0:1,1:0", "11:9,10:10,15:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Columbus Blue Jackets",
               "New York Islanders", "0:1,1:1,1:0,0:1", "9:4,13:7,6:7,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "St. Louis Blues",
               "Dallas Stars", "1:0,0:0,2:0", "17:5,2:11,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Nashville Predators",
               "Colorado Avalanche", "1:2,0:0,1:1", "12:13,10:1,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Arizona Coyotes",
               "Carolina Hurricanes", "0:2,1:1,3:1,0:1", "7:11,8:13,13:8,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "Calgary Flames",
               "New York Rangers", "0:1,2:0,2:3,1:0", "9:9,10:5,6:15,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151212, "San Jose Sharks",
               "Minnesota Wild", "0:0,0:0,0:2", "6:8,9:8,10:14", 0, False)

print("Inserting "+leaguename+" Game Data From 12/13/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151213, "New York Islanders",
               "New Jersey Devils", "2:0,2:0,0:0", "11:9,12:7,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "St. Louis Blues",
               "Colorado Avalanche", "0:2,0:0,1:1", "8:6,17:6,18:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151213, "Chicago Blackhawks",
               "Vancouver Canucks", "1:0,0:0,3:0", "8:8,11:13,11:9", 0, False)

print("Inserting "+leaguename+" Game Data From 12/14/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151214, "Boston Bruins",
               "Edmonton Oilers", "0:2,1:0,1:0,0:1", "11:12,18:3,20:7,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151214, "Pittsburgh Penguins",
               "Washington Capitals", "1:2,0:0,0:2", "15:10,16:14,14:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151214, "Columbus Blue Jackets",
               "Tampa Bay Lightning", "0:0,1:1,0:1", "7:10,7:13,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151214, "Ottawa Senators",
               "Los Angeles Kings", "0:1,4:1,1:1", "6:10,8:12,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151214, "Detroit Red Wings",
               "Buffalo Sabres", "0:0,1:0,0:2", "6:9,13:9,14:12", 0, False)

print("Inserting "+leaguename+" Game Data From 12/15/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Buffalo Sabres",
               "New Jersey Devils", "0:0,0:1,0:1", "6:9,7:8,12:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "New York Islanders",
               "Florida Panthers", "0:0,1:3,0:2", "19:2,9:10,6:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "New York Rangers",
               "Edmonton Oilers", "1:0,2:2,1:0", "9:6,6:7,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Philadelphia Flyers",
               "Carolina Hurricanes", "0:1,3:1,0:1,1:0", "6:9,13:13,10:9,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Toronto Maple Leafs",
               "Tampa Bay Lightning", "2:1,1:1,1:2,0:1", "16:4,8:10,12:12,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Montreal Canadiens",
               "San Jose Sharks", "0:1,1:2,0:0", "10:3,8:13,9:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Nashville Predators",
               "Calgary Flames", "1:0,0:1,0:0,0:1", "12:5,4:6,5:8,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Minnesota Wild",
               "Vancouver Canucks", "2:0,4:1,0:1", "17:12,19:9,5:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Winnipeg Jets",
               "St. Louis Blues", "1:0,2:2,0:2", "10:10,13:12,13:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Chicago Blackhawks",
               "Colorado Avalanche", "0:1,0:1,0:1", "9:12,13:9,7:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151215, "Dallas Stars",
               "Columbus Blue Jackets", "1:0,3:1,1:0", "8:16,19:12,7:7", 0, False)

print("Inserting "+leaguename+" Game Data From 12/16/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Washington Capitals",
               "Ottawa Senators", "1:0,1:0,0:1", "14:8,4:9,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151216, "Boston Bruins",
               "Pittsburgh Penguins", "1:0,1:0,1:0", "10:6,4:18,15:10", 0, False)

print("Inserting "+leaguename+" Game Data From 12/17/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Buffalo Sabres",
               "Anaheim Ducks", "0:0,2:0,1:0", "8:14,8:11,6:19", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "New Jersey Devils",
               "Florida Panthers", "0:2,0:1,1:2", "6:6,7:14,3:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Philadelphia Flyers",
               "Vancouver Canucks", "1:0,0:0,1:0", "12:12,12:16,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Toronto Maple Leafs",
               "San Jose Sharks", "1:2,2:0,1:2,0:1", "9:21,14:7,8:14,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Montreal Canadiens",
               "Los Angeles Kings", "0:0,0:2,0:1", "18:7,12:9,15:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "St. Louis Blues",
               "Nashville Predators", "0:1,0:0,2:0", "11:11,12:6,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Minnesota Wild",
               "New York Rangers", "1:0,1:1,3:1", "5:5,15:9,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Chicago Blackhawks",
               "Edmonton Oilers", "1:0,1:0,2:0", "14:9,16:15,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Dallas Stars",
               "Calgary Flames", "1:2,0:1,0:0", "11:8,8:13,17:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Colorado Avalanche",
               "New York Islanders", "1:0,0:1,1:0", "7:14,11:11,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151217, "Arizona Coyotes",
               "Columbus Blue Jackets", "1:2,3:3,1:2", "6:7,12:7,14:7", 0, False)

print("Inserting "+leaguename+" Game Data From 12/18/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Pittsburgh Penguins",
               "Boston Bruins", "1:1,1:2,0:3", "7:8,11:11,14:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Washington Capitals",
               "Tampa Bay Lightning", "0:1,1:2,4:0", "10:4,7:11,6:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Carolina Hurricanes",
               "Florida Panthers", "0:0,0:0,0:2", "6:5,9:7,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Ottawa Senators",
               "San Jose Sharks", "0:0,1:1,3:1", "12:13,13:8,10:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Detroit Red Wings",
               "Vancouver Canucks", "0:1,1:1,2:1,0:0,1:2", "5:17,5:10,14:12,4:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151218, "Winnipeg Jets",
               "New York Rangers", "3:1,1:1,1:0", "13:9,17:10,6:9", 0, False)

print("Inserting "+leaguename+" Game Data From 12/19/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Buffalo Sabres",
               "Chicago Blackhawks", "0:1,1:0,1:1,0:0,0:1", "5:6,14:9,7:11,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "St. Louis Blues",
               "Calgary Flames", "2:0,1:0,0:2", "7:8,6:15,9:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Toronto Maple Leafs",
               "Los Angeles Kings", "1:0,0:0,4:0", "7:9,12:8,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "New Jersey Devils",
               "Anaheim Ducks", "0:2,0:0,1:0", "7:8,10:5,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Pittsburgh Penguins",
               "Carolina Hurricanes", "0:2,1:0,0:0", "13:9,13:12,12:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Columbus Blue Jackets",
               "Philadelphia Flyers", "1:0,1:0,0:2,0:0,2:1", "16:9,10:10,8:12,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Dallas Stars",
               "Montreal Canadiens", "1:0,3:1,2:1", "8:11,13:6,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Nashville Predators",
               "Minnesota Wild", "2:0,1:1,0:1", "13:7,14:6,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Arizona Coyotes",
               "New York Islanders", "1:0,0:0,0:0", "7:8,7:10,15:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151219, "Colorado Avalanche",
               "Edmonton Oilers", "2:0,1:0,2:1", "9:13,12:14,8:13", 0, False)

print("Inserting "+leaguename+" Game Data From 12/20/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Florida Panthers",
               "Vancouver Canucks", "2:2,2:2,0:0,0:0,2:1", "13:8,13:14,8:11,8:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Boston Bruins",
               "New Jersey Devils", "1:0,0:1,0:0,0:0,1:0", "4:8,15:13,11:7,9:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Tampa Bay Lightning",
               "Ottawa Senators", "2:1,1:1,2:0", "11:8,14:10,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Detroit Red Wings",
               "Calgary Flames", "0:0,3:1,1:1", "13:15,14:5,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "New York Rangers",
               "Washington Capitals", "3:1,0:4,0:2", "15:7,9:17,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151220, "Chicago Blackhawks",
               "San Jose Sharks", "2:2,0:1,1:0,1:0", "11:13,13:12,5:11,3:0", 0, False)

print("Inserting "+leaguename+" Game Data From 12/21/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151221, "New York Islanders",
               "Anaheim Ducks", "3:1,0:0,2:1", "11:7,8:12,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Philadelphia Flyers",
               "St. Louis Blues", "0:2,2:1,2:0", "8:15,14:9,9:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Pittsburgh Penguins",
               "Columbus Blue Jackets", "0:1,4:0,1:1", "12:9,10:7,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Carolina Hurricanes",
               "Washington Capitals", "0:1,0:1,1:0", "12:7,7:8,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Nashville Predators",
               "Montreal Canadiens", "1:0,1:0,3:1", "8:14,4:9,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Minnesota Wild",
               "Dallas Stars", "2:0,0:3,1:3", "11:11,10:15,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Colorado Avalanche",
               "Toronto Maple Leafs", "1:2,2:1,1:4", "7:8,7:3,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151221, "Edmonton Oilers",
               "Winnipeg Jets", "2:0,1:1,0:0", "11:12,7:17,3:16", 0, False)

print("Inserting "+leaguename+" Game Data From 12/22/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Boston Bruins",
               "St. Louis Blues", "0:0,0:0,0:2", "14:10,12:11,6:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "New York Rangers",
               "Anaheim Ducks", "1:1,0:0,1:1,1:0", "5:8,5:5,10:6,2:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Detroit Red Wings",
               "New Jersey Devils", "1:3,1:0,1:1", "13:7,5:6,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Tampa Bay Lightning",
               "Vancouver Canucks", "0:1,1:0,0:1", "4:7,13:9,10:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Florida Panthers",
               "Ottawa Senators", "0:0,1:0,0:1,0:0,3:0", "13:8,19:4,6:2,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Minnesota Wild",
               "Montreal Canadiens", "1:0,0:0,1:1", "8:7,7:8,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Dallas Stars",
               "Chicago Blackhawks", "0:0,1:0,3:0", "7:3,8:14,17:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Calgary Flames",
               "Winnipeg Jets", "2:1,0:0,2:0", "14:6,9:7,10:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Arizona Coyotes",
               "Toronto Maple Leafs", "2:1,0:1,1:0", "9:12,10:15,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151222, "Los Angeles Kings",
               "San Jose Sharks", "2:1,1:1,0:3", "21:6,5:9,10:8", 0, False)

print("Inserting "+leaguename+" Game Data From 12/26/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Boston Bruins",
               "Buffalo Sabres", "0:0,2:1,1:5", "11:8,13:11,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Tampa Bay Lightning",
               "Columbus Blue Jackets", "1:1,3:1,1:0", "9:15,9:9,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Washington Capitals",
               "Montreal Canadiens", "1:0,1:1,1:0", "10:5,18:16,5:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Carolina Hurricanes",
               "New Jersey Devils", "0:0,1:0,2:1", "7:6,12:8,6:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "St. Louis Blues",
               "Dallas Stars", "0:0,1:2,1:0,0:0,5:4", "6:7,18:11,11:5,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Nashville Predators",
               "Detroit Red Wings", "1:1,1:1,0:1", "6:4,9:13,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Minnesota Wild",
               "Pittsburgh Penguins", "0:0,1:3,0:0", "4:11,8:16,14:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Arizona Coyotes",
               "Los Angeles Kings", "1:0,0:0,2:3,0:1", "9:8,7:10,11:14,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151226, "Vancouver Canucks",
               "Edmonton Oilers", "0:1,1:0,0:0,1:0", "6:13,11:9,5:8,2:3", 0, False)

print("Inserting "+leaguename+" Game Data From 12/27/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Ottawa Senators",
               "Boston Bruins", "1:0,1:1,1:0", "10:16,7:15,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Florida Panthers",
               "Columbus Blue Jackets", "2:0,0:1,1:1", "19:1,8:9,5:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "New York Islanders",
               "Toronto Maple Leafs", "0:0,0:2,1:1", "8:12,6:16,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Dallas Stars",
               "St. Louis Blues", "1:0,0:0,2:0", "16:5,13:7,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Chicago Blackhawks",
               "Carolina Hurricanes", "0:0,0:1,1:1", "11:12,6:6,19:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Winnipeg Jets",
               "Pittsburgh Penguins", "1:0,0:0,0:0", "11:9,5:14,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Colorado Avalanche",
               "Arizona Coyotes", "1:0,0:0,0:1,0:1", "14:8,9:12,13:6,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Anaheim Ducks",
               "Philadelphia Flyers", "1:1,1:1,2:0", "15:11,14:10,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151227, "Calgary Flames",
               "Edmonton Oilers", "0:2,4:1,1:0", "10:8,20:12,7:11", 0, False)

print("Inserting "+leaguename+" Game Data From 12/28/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Buffalo Sabres",
               "Washington Capitals", "0:0,0:2,0:0", "10:9,12:7,9:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Tampa Bay Lightning",
               "Montreal Canadiens", "0:1,1:1,2:1,0:0,1:2", "11:14,16:8,11:10,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Nashville Predators",
               "New York Rangers", "1:0,1:1,3:2", "15:6,11:14,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Minnesota Wild",
               "Detroit Red Wings", "1:0,0:0,2:1", "9:11,10:7,16:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "Vancouver Canucks",
               "Los Angeles Kings", "0:1,0:2,0:2", "9:16,9:10,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151228, "San Jose Sharks",
               "Colorado Avalanche", "1:2,1:1,1:3", "8:9,17:9,13:8", 0, False)

print("Inserting "+leaguename+" Game Data From 12/29/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Boston Bruins",
               "Ottawa Senators", "2:1,1:1,4:1", "13:6,15:13,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Toronto Maple Leafs",
               "New York Islanders", "1:3,1:3,1:0", "12:7,13:8,8:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "New Jersey Devils",
               "Carolina Hurricanes", "0:0,1:2,2:0", "11:8,9:13,4:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Columbus Blue Jackets",
               "Dallas Stars", "3:1,1:1,2:1", "14:17,13:9,6:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Florida Panthers",
               "Montreal Canadiens", "1:1,1:0,1:0", "13:12,9:8,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "St. Louis Blues",
               "Nashville Predators", "1:1,1:0,1:2,1:0", "7:7,7:17,5:9,6:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Winnipeg Jets",
               "Detroit Red Wings", "2:0,2:0,0:1", "7:12,10:12,8:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Calgary Flames",
               "Anaheim Ducks", "0:0,0:1,0:0", "4:6,3:11,7:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Edmonton Oilers",
               "Los Angeles Kings", "0:0,1:4,1:1", "13:10,17:14,14:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151229, "Arizona Coyotes",
               "Chicago Blackhawks", "2:3,0:2,3:2", "12:5,14:17,11:7", 0, False)

print("Inserting "+leaguename+" Game Data From 12/30/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Pittsburgh Penguins",
               "Toronto Maple Leafs", "1:1,1:1,0:0,0:0,1:2", "7:12,20:10,10:11,4:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Washington Capitals",
               "Buffalo Sabres", "0:1,1:1,4:0", "14:11,14:8,15:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Ottawa Senators",
               "New Jersey Devils", "0:2,0:0,0:1", "8:10,15:6,13:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "Tampa Bay Lightning",
               "New York Rangers", "1:1,1:1,0:3", "5:8,10:5,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151230, "San Jose Sharks",
               "Philadelphia Flyers", "0:0,1:1,3:1", "9:3,11:10,13:6", 0, False)

print("Inserting "+leaguename+" Game Data From 12/31/2015.\n")
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Buffalo Sabres",
               "New York Islanders", "0:0,0:1,1:1", "17:5,10:18,16:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Detroit Red Wings",
               "Pittsburgh Penguins", "2:0,0:2,0:3", "10:11,13:17,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Carolina Hurricanes",
               "Washington Capitals", "0:0,1:1,3:1", "11:8,15:13,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "St. Louis Blues",
               "Minnesota Wild", "0:0,1:1,0:2", "10:10,13:10,11:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Colorado Avalanche",
               "Chicago Blackhawks", "1:1,1:2,1:0,0:1", "9:11,5:17,13:11,3:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Dallas Stars",
               "Nashville Predators", "0:0,2:1,3:0", "12:12,10:11,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Calgary Flames",
               "Los Angeles Kings", "0:1,0:2,1:1", "10:10,4:11,10:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Edmonton Oilers",
               "Anaheim Ducks", "0:1,0:0,0:0", "9:11,5:14,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20151231, "Arizona Coyotes",
               "Winnipeg Jets", "1:1,0:0,3:1", "6:14,5:15,10:8", 0, False)

print("Inserting "+leaguename+" Game Data From 1/1/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Boston Bruins", "Montreal Canadiens",
               "0:1,0:2,1:2", "3:14,14:11,11:5", "Gillette Stadium, Foxborough", False)
MakeHockeyGame((sqlcur, sqlcon), 20160101, "Vancouver Canucks",
               "Anaheim Ducks", "0:0,0:1,1:0,0:0,1:0", "6:9,9:9,8:10,2:0", 0, False)

print("Inserting "+leaguename+" Game Data From 1/2/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Buffalo Sabres",
               "Detroit Red Wings", "0:1,2:1,1:2", "11:7,13:8,11:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Edmonton Oilers",
               "Arizona Coyotes", "2:1,0:1,1:1,0:0,2:1", "10:12,12:10,16:9,3:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Los Angeles Kings",
               "Philadelphia Flyers", "2:0,0:0,0:1", "15:7,9:7,8:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Toronto Maple Leafs",
               "St. Louis Blues", "0:0,1:1,3:0", "11:11,8:11,14:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Tampa Bay Lightning",
               "Minnesota Wild", "1:1,1:0,0:1,0:0,1:0", "12:4,13:11,3:15,2:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Florida Panthers",
               "New York Rangers", "1:0,2:0,0:0", "7:10,6:15,7:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "New Jersey Devils",
               "Dallas Stars", "0:0,2:0,0:2,1:0", "9:8,9:11,8:12,4:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Pittsburgh Penguins",
               "New York Islanders", "2:0,3:1,0:1", "20:12,10:14,13:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Carolina Hurricanes",
               "Nashville Predators", "1:0,0:1,0:0,0:1", "9:9,6:8,11:3,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Columbus Blue Jackets",
               "Washington Capitals", "2:2,0:1,2:1,0:0,2:1", "13:8,7:7,8:12,1:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "Colorado Avalanche",
               "Calgary Flames", "0:1,0:3,0:0", "12:10,13:12,1:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160102, "San Jose Sharks",
               "Winnipeg Jets", "0:1,1:2,0:1", "8:7,9:13,11:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/3/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160103, "New York Islanders",
               "Dallas Stars", "2:2,3:0,1:3", "14:12,20:12,10:17", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Florida Panthers",
               "Minnesota Wild", "1:0,0:1,1:0", "8:10,10:18,11:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Chicago Blackhawks",
               "Ottawa Senators", "0:0,1:0,2:0", "7:6,11:9,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160103, "Anaheim Ducks",
               "Winnipeg Jets", "2:0,2:1,0:0", "14:8,9:7,12:5", 0, False)

print("Inserting "+leaguename+" Game Data From 1/4/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160104, "New Jersey Devils",
               "Detroit Red Wings", "0:1,0:0,0:0", "12:9,5:6,5:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160104, "St. Louis Blues",
               "Ottawa Senators", "1:0,1:1,0:1,0:1", "11:13,14:7,13:11,0:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160104, "Colorado Avalanche",
               "Los Angeles Kings", "0:0,2:1,2:0", "10:7,13:8,10:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160104, "Edmonton Oilers",
               "Carolina Hurricanes", "0:0,0:0,0:0,1:0", "6:9,8:9,8:9,5:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160104, "Vancouver Canucks",
               "Arizona Coyotes", "0:0,1:2,1:1", "12:10,15:12,10:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/5/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Boston Bruins",
               "Washington Capitals", "0:1,1:1,1:1", "7:10,7:13,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Buffalo Sabres",
               "Florida Panthers", "0:1,1:1,0:3", "12:10,12:8,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "New York Rangers",
               "Dallas Stars", "2:1,1:0,3:1", "14:6,6:8,9:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Pittsburgh Penguins",
               "Chicago Blackhawks", "0:0,0:2,2:0,0:1", "7:7,14:9,10:9,5:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Columbus Blue Jackets",
               "Minnesota Wild", "0:1,1:1,1:2", "9:10,11:13,11:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Philadelphia Flyers",
               "Montreal Canadiens", "1:1,2:1,1:1", "12:4,10:9,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Nashville Predators",
               "Winnipeg Jets", "0:1,0:1,1:2", "17:4,12:6,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160105, "Calgary Flames",
               "Tampa Bay Lightning", "1:0,1:0,1:1", "13:8,7:14,4:9", 0, False)

print("Inserting "+leaguename+" Game Data From 1/6/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Montreal Canadiens",
               "New Jersey Devils", "1:0,1:0,0:1", "8:9,10:6,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Chicago Blackhawks",
               "Pittsburgh Penguins", "1:0,0:1,2:0", "15:3,10:8,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Colorado Avalanche",
               "St. Louis Blues", "1:2,1:1,1:0,1:0", "9:17,10:7,10:10,4:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Vancouver Canucks",
               "Carolina Hurricanes", "0:0,1:1,2:1", "8:2,7:13,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160106, "Anaheim Ducks",
               "Toronto Maple Leafs", "0:1,0:2,0:1", "18:8,14:16,7:14", 0, False)

print("Inserting "+leaguename+" Game Data From 1/7/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160107, "New York Islanders",
               "Washington Capitals", "0:2,1:1,0:1", "10:10,14:14,11:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Ottawa Senators",
               "Florida Panthers", "0:2,1:0,1:1", "9:4,11:6,12:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Minnesota Wild",
               "Philadelphia Flyers", "1:1,1:2,1:0,0:1", "10:15,6:11,13:6,5:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Dallas Stars",
               "Winnipeg Jets", "1:0,0:1,0:0,0:0,2:1", "10:8,4:12,8:8,2:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Calgary Flames",
               "Arizona Coyotes", "1:1,0:0,0:1", "6:14,12:12,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "Los Angeles Kings",
               "Toronto Maple Leafs", "0:0,0:0,2:1", "16:6,11:9,14:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160107, "San Jose Sharks",
               "Detroit Red Wings", "1:1,0:0,0:1", "16:12,10:6,10:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/8/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160108, "New Jersey Devils",
               "Boston Bruins", "0:1,1:2,0:1", "7:11,9:6,4:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Carolina Hurricanes",
               "Columbus Blue Jackets", "1:0,1:1,2:0", "9:6,10:14,10:16", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Chicago Blackhawks",
               "Buffalo Sabres", "1:0,0:0,2:1", "11:11,19:12,15:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Colorado Avalanche",
               "Nashville Predators", "2:1,1:2,2:0", "14:8,5:9,8:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Edmonton Oilers",
               "Tampa Bay Lightning", "1:0,1:0,0:3", "5:9,14:8,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160108, "Anaheim Ducks",
               "St. Louis Blues", "1:0,1:3,1:0,0:0,2:1", "12:8,5:17,19:2,3:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/9/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160109, "New York Rangers",
               "Washington Capitals", "0:1,0:1,3:1,0:1", "8:8,10:8,7:14,1:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Philadelphia Flyers",
               "New York Islanders", "0:0,2:0,2:0", "11:2,10:8,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Montreal Canadiens",
               "Pittsburgh Penguins", "0:0,1:2,0:1", "5:12,12:12,17:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Ottawa Senators",
               "Boston Bruins", "1:0,0:1,0:0,1:0", "16:10,9:11,9:11,6:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Columbus Blue Jackets",
               "Carolina Hurricanes", "0:1,1:2,2:0,0:1", "5:10,10:10,8:7,1:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "San Jose Sharks",
               "Toronto Maple Leafs", "0:0,4:0,3:0", "7:12,12:9,12:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Dallas Stars",
               "Minnesota Wild", "0:0,0:2,1:0", "11:6,8:15,16:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Arizona Coyotes",
               "Nashville Predators", "0:0,1:0,3:0", "11:14,9:5,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Vancouver Canucks",
               "Tampa Bay Lightning", "1:1,0:0,1:1,0:1", "8:6,7:9,5:17,3:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160109, "Los Angeles Kings",
               "St. Louis Blues", "0:0,1:1,0:0,0:0,1:2", "7:3,9:4,9:6,2:3", 0, False)

print("Inserting "+leaguename+" Game Data From 1/10/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Winnipeg Jets",
               "Buffalo Sabres", "1:2,1:0,0:2", "11:8,18:12,15:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Washington Capitals",
               "Ottawa Senators", "2:0,3:1,2:0", "12:7,17:18,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Chicago Blackhawks",
               "Colorado Avalanche", "2:0,4:2,0:1", "15:11,9:12,11:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Minnesota Wild",
               "New Jersey Devils", "0:0,0:0,1:2", "3:7,4:6,11:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Anaheim Ducks",
               "Detroit Red Wings", "1:1,0:0,0:1", "7:7,11:8,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160110, "Edmonton Oilers",
               "Florida Panthers", "1:2,0:0,0:0", "4:5,14:2,7:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/11/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160111, "New York Rangers",
               "Boston Bruins", "0:0,0:1,2:0", "10:11,12:11,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160111, "Calgary Flames",
               "San Jose Sharks", "1:2,2:1,1:2", "12:8,8:5,15:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160111, "Vancouver Canucks",
               "Florida Panthers", "0:2,1:0,1:0,1:0", "13:7,8:8,8:11,1:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160111, "Los Angeles Kings",
               "Detroit Red Wings", "1:2,1:0,2:0", "12:10,10:4,9:13", 0, False)

print("Inserting "+leaguename+" Game Data From 1/12/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160112, "New York Islanders",
               "Columbus Blue Jackets", "2:1,1:1,2:0", "17:5,7:9,9:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Carolina Hurricanes",
               "Pittsburgh Penguins", "0:0,2:1,0:1,1:0", "5:5,5:7,8:13,3:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "St. Louis Blues",
               "New Jersey Devils", "1:2,2:0,2:0", "9:10,15:8,13:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Minnesota Wild",
               "Buffalo Sabres", "0:3,1:0,1:0", "10:11,14:5,6:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Winnipeg Jets",
               "San Jose Sharks", "1:2,0:0,0:2", "7:11,8:6,7:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Chicago Blackhawks",
               "Nashville Predators", "1:0,2:1,0:1", "11:10,6:20,6:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Colorado Avalanche",
               "Tampa Bay Lightning", "0:1,0:2,0:1", "9:15,8:12,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160112, "Arizona Coyotes",
               "Edmonton Oilers", "0:1,1:1,2:1,1:0", "6:7,9:12,13:8,3:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/13/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Toronto Maple Leafs",
               "Columbus Blue Jackets", "0:1,0:1,1:1", "10:8,15:9,17:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Philadelphia Flyers",
               "Boston Bruins", "1:0,0:2,2:0", "5:8,9:12,7:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Calgary Flames",
               "Florida Panthers", "4:0,1:0,1:0", "15:5,10:4,11:6", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160113, "Anaheim Ducks",
               "Ottawa Senators", "0:0,1:1,3:0", "12:9,12:9,14:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/14/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160114, "New York Islanders",
               "New York Rangers", "0:0,0:1,3:0", "10:14,12:13,10:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Washington Capitals",
               "Vancouver Canucks", "0:0,2:0,2:1", "13:8,15:14,12:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Montreal Canadiens",
               "Chicago Blackhawks", "1:2,0:0,0:0", "11:12,12:11,17:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "St. Louis Blues",
               "Carolina Hurricanes", "0:0,0:1,1:3", "6:5,5:15,13:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Winnipeg Jets",
               "Nashville Predators", "0:1,3:0,1:3,1:0", "9:9,8:12,6:14,1:0", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Colorado Avalanche",
               "New Jersey Devils", "1:0,1:0,1:0", "8:5,11:8,7:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "Arizona Coyotes",
               "Detroit Red Wings", "0:0,2:0,0:2,0:1", "12:5,8:11,7:8,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160114, "San Jose Sharks",
               "Edmonton Oilers", "1:0,0:1,0:0,0:0,2:0", "7:6,15:7,11:8,4:4", 0, False)

print("Inserting "+leaguename+" Game Data From 1/15/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Buffalo Sabres",
               "Boston Bruins", "1:0,0:1,0:3", "10:9,16:9,8:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Toronto Maple Leafs",
               "Chicago Blackhawks", "0:0,0:2,1:2", "10:7,8:11,11:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Carolina Hurricanes",
               "Vancouver Canucks", "1:1,0:1,1:0,0:1", "9:6,19:5,11:7,1:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Tampa Bay Lightning",
               "Pittsburgh Penguins", "1:1,2:1,1:2,1:0", "7:8,6:11,10:18,2:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Minnesota Wild",
               "Winnipeg Jets", "0:1,0:0,0:0", "13:9,4:12,7:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160115, "Anaheim Ducks",
               "Dallas Stars", "4:0,0:1,0:1", "19:7,7:6,9:11", 0, False)

print("Inserting "+leaguename+" Game Data From 1/16/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Philadelphia Flyers",
               "New York Rangers", "1:1,0:1,1:0,0:0,0:1", "12:16,11:4,10:9,3:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Arizona Coyotes",
               "New Jersey Devils", "0:1,0:0,0:1", "10:8,15:5,13:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Los Angeles Kings",
               "Ottawa Senators", "1:0,1:1,1:4", "8:7,18:5,7:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Boston Bruins",
               "Toronto Maple Leafs", "1:1,1:1,1:0", "18:13,13:8,14:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Buffalo Sabres",
               "Washington Capitals", "2:0,2:0,0:1", "8:7,15:15,6:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Columbus Blue Jackets",
               "Colorado Avalanche", "1:0,0:1,1:0", "5:6,6:13,10:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "St. Louis Blues",
               "Montreal Canadiens", "1:0,1:2,1:1,1:0", "9:17,7:22,4:9,2:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Nashville Predators",
               "Minnesota Wild", "1:0,0:0,2:0", "11:12,5:13,9:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "Edmonton Oilers",
               "Calgary Flames", "0:1,0:0,1:0,0:0,1:0", "8:14,14:5,15:8,0:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160116, "San Jose Sharks",
               "Dallas Stars", "0:1,2:0,1:2,1:0", "16:13,14:8,6:13,3:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/17/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Pittsburgh Penguins",
               "Carolina Hurricanes", "2:0,1:0,2:0", "15:9,9:6,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "New York Islanders",
               "Vancouver Canucks", "0:0,0:1,1:0,0:0,0:1", "11:5,13:12,22:4,2:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Tampa Bay Lightning",
               "Florida Panthers", "0:0,2:0,1:1", "5:3,15:10,12:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Washington Capitals",
               "New York Rangers", "1:1,2:1,2:0", "8:13,10:11,6:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Chicago Blackhawks",
               "Montreal Canadiens", "1:1,2:0,2:1", "10:6,14:10,9:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Detroit Red Wings",
               "Philadelphia Flyers", "0:0,1:0,0:1,0:0,1:2", "10:11,13:5,4:14,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160117, "Anaheim Ducks",
               "Los Angeles Kings", "0:0,1:3,1:0", "5:7,11:12,16:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/18/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Florida Panthers",
               "Edmonton Oilers", "0:2,0:1,2:1", "9:6,14:9,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "St. Louis Blues",
               "Pittsburgh Penguins", "1:1,1:1,3:0", "9:14,8:17,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Winnipeg Jets",
               "Colorado Avalanche", "0:0,0:2,1:0", "12:10,9:16,16:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "Arizona Coyotes",
               "Buffalo Sabres", "0:0,0:2,1:0", "11:9,7:15,9:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160118, "San Jose Sharks",
               "Ottawa Senators", "0:1,1:1,2:1,0:0,0:1", "11:5,9:8,9:3,6:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/19/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160119, "New Jersey Devils",
               "Calgary Flames", "1:1,2:1,1:0", "10:9,12:8,4:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "New York Rangers",
               "Vancouver Canucks", "0:1,1:1,1:0,1:0", "17:11,13:6,16:2,3:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Philadelphia Flyers",
               "Toronto Maple Leafs", "1:1,0:1,1:1", "13:12,8:14,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Columbus Blue Jackets",
               "Washington Capitals", "1:2,1:3,1:1", "12:5,11:14,12:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Montreal Canadiens",
               "Boston Bruins", "0:1,1:1,0:2", "9:10,16:7,14:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Tampa Bay Lightning",
               "Edmonton Oilers", "2:2,2:0,2:2", "10:11,11:5,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Nashville Predators",
               "Chicago Blackhawks", "0:1,1:2,0:1", "12:10,11:12,16:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160119, "Los Angeles Kings",
               "Dallas Stars", "2:2,0:0,1:0", "13:9,7:9,9:11", 0, False)

print("Inserting "+leaguename+" Game Data From 1/20/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Detroit Red Wings",
               "St. Louis Blues", "0:1,0:0,1:1", "11:7,9:9,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Colorado Avalanche",
               "Buffalo Sabres", "0:0,0:1,2:0", "9:10,8:13,18:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Anaheim Ducks",
               "Minnesota Wild", "1:1,0:0,2:0", "9:5,11:14,7:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/20/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Detroit Red Wings",
               "St. Louis Blues", "0:1,0:0,1:1", "11:7,9:9,10:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Colorado Avalanche",
               "Buffalo Sabres", "0:0,0:1,2:0", "9:10,8:13,18:5", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160120, "Anaheim Ducks",
               "Minnesota Wild", "1:1,0:0,2:0", "9:5,11:14,7:7", 0, False)

print("Inserting "+leaguename+" Game Data From 1/21/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Boston Bruins",
               "Vancouver Canucks", "0:1,1:0,1:3", "11:4,11:12,8:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "New Jersey Devils",
               "Ottawa Senators", "5:0,0:1,1:2", "10:6,3:13,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Pittsburgh Penguins",
               "Philadelphia Flyers", "0:2,3:0,1:1", "9:11,17:9,19:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Columbus Blue Jackets",
               "Calgary Flames", "0:1,2:1,0:2", "7:7,15:12,7:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Toronto Maple Leafs",
               "Carolina Hurricanes", "0:0,0:0,0:0,0:1", "12:10,13:13,3:15,4:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Tampa Bay Lightning",
               "Chicago Blackhawks", "1:1,1:0,0:0", "13:4,10:5,10:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Winnipeg Jets",
               "Nashville Predators", "1:1,0:1,0:2", "7:12,11:5,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Dallas Stars",
               "Edmonton Oilers", "1:0,2:1,0:1", "11:7,11:8,13:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Arizona Coyotes",
               "San Jose Sharks", "0:2,0:0,1:1", "7:8,8:8,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160121, "Los Angeles Kings",
               "Minnesota Wild", "0:0,0:2,0:1", "12:8,7:12,13:8", 0, False)

print("Inserting "+leaguename+" Game Data From 1/22/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Buffalo Sabres",
               "Detroit Red Wings", "0:0,0:0,0:3", "8:12,9:15,2:18", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Carolina Hurricanes",
               "New York Rangers", "0:2,1:2,0:0", "9:17,10:14,12:1", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Ottawa Senators",
               "New York Islanders", "0:1,2:1,0:3", "8:10,18:10,4:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Florida Panthers",
               "Chicago Blackhawks", "3:0,1:0,0:0", "13:8,10:7,9:12", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160122, "Colorado Avalanche",
               "St. Louis Blues", "0:0,0:1,1:0,0:0,1:0", "8:10,13:12,16:11,4:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/23/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Pittsburgh Penguins",
               "Vancouver Canucks", "0:2,1:0,4:2", "9:10,9:9,12:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "San Jose Sharks",
               "Minnesota Wild", "1:2,2:0,1:1", "9:10,14:8,10:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Boston Bruins",
               "Columbus Blue Jackets", "0:0,2:2,0:0,0:0,2:0", "11:13,9:10,8:6,6:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Toronto Maple Leafs",
               "Montreal Canadiens", "0:2,1:0,1:0,0:0,1:2", "3:14,8:5,4:7,4:3", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Detroit Red Wings",
               "Anaheim Ducks", "1:2,1:0,1:2", "9:13,10:13,8:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Florida Panthers",
               "Tampa Bay Lightning", "0:0,4:0,1:2", "11:13,19:5,5:22", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Winnipeg Jets",
               "New Jersey Devils", "0:1,0:1,1:1", "4:10,10:2,9:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Dallas Stars",
               "Colorado Avalanche", "0:1,1:1,0:1", "10:7,19:4,14:4", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Arizona Coyotes",
               "Los Angeles Kings", "1:0,1:2,1:0", "13:5,6:12,5:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160123, "Edmonton Oilers",
               "Nashville Predators", "1:1,0:1,0:2", "9:9,9:6,6:10", 0, False)

print("Inserting "+leaguename+" Game Data From 1/24/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Ottawa Senators",
               "New York Rangers", "0:0,1:0,2:0", "12:13,11:8,10:14", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Carolina Hurricanes",
               "Calgary Flames", "2:0,1:1,2:1", "14:8,12:12,10:15", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "Chicago Blackhawks",
               "St. Louis Blues", "0:0,1:0,1:0", "6:12,11:6,8:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160124, "San Jose Sharks",
               "Los Angeles Kings", "0:0,1:0,1:2,0:1", "5:10,13:11,12:10,2:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/25/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160125, "New York Islanders",
               "Detroit Red Wings", "1:1,0:2,1:1", "11:7,9:11,9:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160125, "Philadelphia Flyers",
               "Boston Bruins", "0:2,1:0,1:1", "8:16,15:6,13:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160125, "Columbus Blue Jackets",
               "Montreal Canadiens", "1:1,1:1,3:0", "8:12,11:11,6:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160125, "New York Rangers",
               "Buffalo Sabres", "1:1,1:0,4:2", "9:7,12:8,12:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160125, "Dallas Stars",
               "Calgary Flames", "0:0,2:0,0:1", "10:3,13:12,7:9", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160125, "Minnesota Wild",
               "Arizona Coyotes", "0:0,0:0,1:1,0:0,0:1", "13:4,11:2,11:17,0:1", 0, False)

print("Inserting "+leaguename+" Game Data From 1/26/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Boston Bruins",
               "Anaheim Ducks", "1:2,0:2,1:2", "13:16,12:12,9:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Pittsburgh Penguins",
               "New Jersey Devils", "1:0,1:0,0:0", "7:11,16:6,8:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Carolina Hurricanes",
               "Chicago Blackhawks", "3:0,2:0,0:0", "16:6,9:9,15:11", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Montreal Canadiens",
               "Columbus Blue Jackets", "0:2,1:1,1:2", "9:11,12:8,9:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Ottawa Senators",
               "Buffalo Sabres", "1:1,1:1,0:1", "7:13,7:7,22:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Florida Panthers",
               "Toronto Maple Leafs", "0:1,3:0,2:0", "7:5,15:10,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Winnipeg Jets",
               "Arizona Coyotes", "2:0,3:1,0:1", "11:10,14:14,12:10", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "Vancouver Canucks",
               "Nashville Predators", "1:1,0:0,0:1", "12:6,12:5,5:8", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160126, "San Jose Sharks",
               "Colorado Avalanche", "2:0,2:0,2:1", "9:6,11:5,4:11", 0, False)

print("Inserting "+leaguename+" Game Data From 1/27/2016.\n")
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Tampa Bay Lightning",
               "Toronto Maple Leafs", "1:0,0:0,0:0", "17:6,5:11,7:13", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Washington Capitals",
               "Philadelphia Flyers", "0:2,2:1,1:0,0:1", "6:12,11:6,13:12,0:2", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Calgary Flames",
               "Nashville Predators", "0:1,0:1,1:0", "4:11,7:6,16:7", 0, False)
MakeHockeyGame((sqlcur, sqlcon), 20160127, "Los Angeles Kings",
               "Colorado Avalanche", "2:0,1:2,0:2", "18:5,9:7,11:7", 0, False)

'''
print("Inserting "+leaguename+" Game Data From 1/31/2016.\n");
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Team Atlantic", "Team Metropolitan", "2:2,2:1,0:0", "10:10,12:12,0:0", "Bridgestone Arena, Nashville", False);
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Team Central", "Team Pacific", "3:3,3:6,0:0", "7:8,10:14,0:0", "Bridgestone Arena, Nashville", False);
MakeHockeyGame((sqlcur, sqlcon), 20160131, "Team Pacific", "Team Atlantic", "0:0,1:0,0:0", "12:10,4:7,0:0", "Bridgestone Arena, Nashville", False);
'''

print("Database Check Return: " +
      str(sqlcon.execute("PRAGMA integrity_check(100);").fetchone()[0])+"\n")

sqlcon.close()

print("DONE! All Game Data Inserted.")

print("DONE! "+leaguename+" Database Created.")
