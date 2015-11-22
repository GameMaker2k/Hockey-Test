#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3, sys, os, re;

leaguename = "ECHL";
getforday = "7";
getformonth = "10";
getforyear = "2015";

print("Creating "+leaguename+" Database.");

if(len(sys.argv) == 0):
 sqlcon = sqlite3.connect("./echl15-16.db3");
if(len(sys.argv) > 0):
 sqlcon = sqlite3.connect(sys.argv[1]);
sqlcur = sqlcon.cursor();

sqlcon.execute("PRAGMA encoding = \"UTF-8\";");
sqlcon.execute("PRAGMA auto_vacuum = 1;");
sqlcon.execute("PRAGMA foreign_keys = 1;");

def GetLastTenGames(sqldatacon, teamname):
 global leaguename;
 wins = 0;
 losses = 0;
 otlosses = 0;
 getlastninegames = sqldatacon[0].execute("SELECT NumberPeriods, TeamWin FROM "+leaguename+"Games WHERE (HomeTeam=\""+str(teamname)+"\" OR AwayTeam=\""+str(teamname)+"\") ORDER BY id DESC LIMIT 10").fetchall();
 nmax = len(getlastninegames);
 nmin = 0;
 while(nmin<nmax):
  if(teamname==str(getlastninegames[nmin][1])):
   wins = wins + 1;
  if(teamname!=str(getlastninegames[nmin][1])):
   if(int(getlastninegames[nmin][0])==3):
    losses = losses + 1;
   if(int(getlastninegames[nmin][0])>3):
    otlosses = otlosses + 1;
  nmin = nmin + 1;
 return str(wins)+":"+str(losses)+":"+str(otlosses);

def UpdateTeamData(sqldatacon, teamid, dataname, addtodata, addtype):
 global leaguename;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"="+str(TMPData)+" WHERE id="+str(teamid));
 return int(TMPData);
def UpdateTeamDataString(sqldatacon, teamid, dataname, newdata):
 global leaguename;
 sqldatacon[0].execute("UPDATE "+leaguename+"Teams SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(teamid));
 return True;
def GetTeamData(sqldatacon, teamid, dataname, datatype):
 global leaguename;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Teams WHERE id="+str(teamid)).fetchone()[0]);
 return TMPData;

def UpdateGameData(sqldatacon, gameid, dataname, addtodata, addtype):
 global leaguename;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"="+str(TMPData)+" WHERE id="+str(gameid));
 return int(TMPData);
def UpdateGameDataString(sqldatacon, gameid, dataname, newdata):
 global leaguename;
 sqldatacon[0].execute("UPDATE "+leaguename+"Games SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(gameid));
 return True;
def GetGameData(sqldatacon, gameid, dataname, datatype):
 global leaguename;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Games WHERE id="+str(gameid)).fetchone()[0]);
 return TMPData;

def UpdateArenaData(sqldatacon, arenaid, dataname, addtodata, addtype):
 global leaguename;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"="+str(TMPData)+" WHERE id="+str(arenaid));
 return int(TMPData);
def UpdateArenaDataString(sqldatacon, arenaid, dataname, newdata):
 global leaguename;
 sqldatacon[0].execute("UPDATE "+leaguename+"Arenas SET "+dataname+"=\""+str(newdata)+"\" WHERE id="+str(arenaid));
 return True;
def GetArenaData(sqldatacon, arenaid, dataname, datatype):
 global leaguename;
 if(datatype=="float"):
  TMPData = float(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="int"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 if(datatype=="str"):
  TMPData = str(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Arenas WHERE id="+str(arenaid)).fetchone()[0]);
 return TMPData;

def UpdateConferenceData(sqldatacon, conference, dataname, addtodata, addtype):
 global leaguename;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Conferences WHERE Conference=\""+str(conference)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Conferences SET "+dataname+"="+str(TMPData)+" WHERE Conference=\""+str(conference)+"\"");
 return int(TMPData);

def UpdateDivisionData(sqldatacon, division, dataname, addtodata, addtype):
 global leaguename;
 if(addtype=="="):
  TMPData = addtodata;
 if(addtype=="+"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) + addtodata;
 if(addtype=="-"):
  TMPData = int(sqldatacon[0].execute("SELECT "+dataname+" FROM "+leaguename+"Divisions WHERE Division=\""+str(division)+"\"").fetchone()[0]) - addtodata;
 sqldatacon[0].execute("UPDATE "+leaguename+"Divisions SET "+dataname+"="+str(TMPData)+" WHERE Division=\""+str(division)+"\"");
 return int(TMPData);

print("Creating "+leaguename+" Conference Table.");
print("Inserting "+leaguename+" Conference Data.");

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Conferences");
sqlcur.execute("CREATE TABLE "+leaguename+"Conferences(id INTEGER PRIMARY KEY, Conference TEXT, NumberOfTeams INTEGER)");
sqlcon.commit();

def MakeHockeyConferences(sqldatacon, conference):
 global leaguename;
 print("Conference Name: "+conference);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Conferences(Conference, NumberOfTeams) VALUES(\""+str(conference)+"\", 0)");
 return True;

MakeHockeyConferences((sqlcur, sqlcon), "Eastern");
MakeHockeyConferences((sqlcur, sqlcon), "Western");
sqlcon.commit();

print("Creating "+leaguename+" Division Table.");
print("Inserting "+leaguename+" Division Data.");

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Divisions");
sqlcur.execute("CREATE TABLE "+leaguename+"Divisions(id INTEGER PRIMARY KEY, Division TEXT, Conference TEXT, NumberOfTeams INTEGER)");
sqlcon.commit();

def MakeHockeyDivisions(sqldatacon, division, conference):
 global leaguename;
 print("Conference Name: "+conference);
 print("Division Name: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Divisions(Division, Conference, NumberOfTeams) VALUES(\""+str(division)+"\", \""+str(conference)+"\", 0)");
 return True;

MakeHockeyDivisions((sqlcur, sqlcon), "East", "Eastern");
MakeHockeyDivisions((sqlcur, sqlcon), "North", "Eastern");
MakeHockeyDivisions((sqlcur, sqlcon), "South", "Eastern");
MakeHockeyDivisions((sqlcur, sqlcon), "Midwest", "Western");
MakeHockeyDivisions((sqlcur, sqlcon), "Central", "Western");
MakeHockeyDivisions((sqlcur, sqlcon), "West", "Western");

print("Creating "+leaguename+" Team Table.");
print("Inserting "+leaguename+" Team Data.");

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Arenas");
sqlcur.execute("CREATE TABLE "+leaguename+"Arenas(id INTEGER PRIMARY KEY, CityName TEXT, AreaName TEXT, FullCityName TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER)");
sqlcon.commit();

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Teams");
sqlcur.execute("CREATE TABLE "+leaguename+"Teams(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Stats");
sqlcur.execute("CREATE TABLE "+leaguename+"Stats(id INTEGER PRIMARY KEY, Date INTEGER, FullName TEXT, CityName TEXT, TeamPrefix TEXT, AreaName TEXT, FullCityName TEXT, TeamName TEXT, Conference TEXT, Division TEXT, ArenaName TEXT, FullArenaName TEXT, GamesPlayed INTEGER, GamesPlayedHome INTEGER, GamesPlayedAway INTEGER, Wins INTEGER, OTWins INTEGER, SOWins INTEGER, OTSOWins INTEGER, TWins INTEGER, Losses INTEGER, OTLosses INTEGER, SOLosses INTEGER, OTSOLosses INTEGER, TLosses INTEGER, ROW INTEGER, ROT INTEGER, HomeRecord TEXT, AwayRecord TEXT, Shootouts TEXT, GoalsFor INTEGER, GoalsAgainst INTEGER, GoalsDifference INTEGER, SOGFor INTEGER, SOGAgainst INTEGER, SOGDifference INTEGER, Points INTEGER, PCT REAL, LastTen TEXT, Streak TEXT)");
sqlcon.commit();

def MakeHockeyTeams(sqldatacon, cityname, areaname, teamname, conference, division, arenaname, teamnameprefix):
 global leaguename;
 print("Team Name: "+teamname);
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print("Full Name: "+teamnameprefix+" "+teamname);
 print("Conference: "+conference);
 print("Division: "+division);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Teams(Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak) VALUES(\"20151001\", \""+str(teamnameprefix+" "+teamname)+"\", \""+str(cityname)+"\", \""+str(teamnameprefix)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(teamname)+"\", \""+str(conference)+"\", \""+str(division)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"0:0:0\", \"0:0\", 0, 0, 0, 0, 0, 0, 0, 0, \"0:0:0\", \"None\")");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak) SELECT Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+teamnameprefix+" "+teamname+"\";");
 UpdateConferenceData((sqlcur, sqlcon), conference, "NumberOfTeams", 1, "+");
 UpdateDivisionData((sqlcur, sqlcon), division, "NumberOfTeams", 1, "+");
 return True;

def MakeHockeyArena(sqldatacon, cityname, areaname, arenaname, teamnameprefix):
 global leaguename;
 print("Arena Name: "+arenaname);
 print("City Name: "+cityname);
 print("Full City Name: "+cityname+", "+areaname);
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Arenas(CityName, AreaName, FullCityName, ArenaName, FullArenaName, GamesPlayed) VALUES(\""+str(cityname)+"\", \""+str(areaname)+"\", \""+str(cityname+", "+areaname)+"\", \""+str(arenaname)+"\", \""+str(arenaname+", "+cityname)+"\", 0)");
 return True;

print("Inserting "+leaguename+" Teams From Eastern Conference.");
print("Inserting "+leaguename+" Teams From East Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Elmira", "NY", "Jackals", "Eastern", "East", "First Arena", "Elmira");
MakeHockeyTeams((sqlcur, sqlcon), "Reading", "PA", "Royals", "Eastern", "East", "Santander Arena", "Reading");
MakeHockeyTeams((sqlcur, sqlcon), "Norfolk", "VA", "Admirals", "Eastern", "East", "Norfolk Scope", "Norfolk");
MakeHockeyTeams((sqlcur, sqlcon), "Glens Falls", "NY", "Thunder", "Eastern", "East", "Glens Falls Civic Center", "Adirondack");
MakeHockeyTeams((sqlcur, sqlcon), "Manchester", "NH", "Monarchs", "Eastern", "East", "Verizon Wireless Arena", "Manchester");

print("Inserting "+leaguename+" Teams From North Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Kalamazoo", "MI", "Wings", "Eastern", "North", "Wings Event Center", "Kalamazoo");
MakeHockeyTeams((sqlcur, sqlcon), "Toledo", "OH", "Walleye", "Eastern", "North", "Huntington Center", "Toledo");
MakeHockeyTeams((sqlcur, sqlcon), "Wheeling", "WV", "Nailers", "Eastern", "North", "WesBanco Arena", "Wheeling");
MakeHockeyTeams((sqlcur, sqlcon), "Brampton", "ON", "Beast", "Eastern", "North", "Powerade Centre", "Brampton");

print("Inserting "+leaguename+" Teams From South Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Duluth", "GA", "Gladiators", "Eastern", "South", "Infinite Energy Arena", "Atlanta");
MakeHockeyTeams((sqlcur, sqlcon), "Greenville", "SC", "Swamp Rabbits", "Eastern", "South", "Bon Secours Wellness Arena", "Greenville");
MakeHockeyTeams((sqlcur, sqlcon), "Estero", "FL", "Everblades", "Eastern", "South", "Germain Arena", "Florida");
MakeHockeyTeams((sqlcur, sqlcon), "Orlando", "FL", "Solar Bears", "Eastern", "South", "Amway Center", "Orlando");
MakeHockeyTeams((sqlcur, sqlcon), "North Charleston", "SC", "Stingrays", "Eastern", "South", "North Charleston Coliseum", "South Carolina");

print("Inserting "+leaguename+" Teams From Western Conference.");
print("Inserting "+leaguename+" Teams From Midwest Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Moline", "IL", "Mallards", "Western", "Midwest", "iWireless Center", "Quad City");
MakeHockeyTeams((sqlcur, sqlcon), "Evansville", "IN", "IceMen", "Western", "Midwest", "Ford Center", "Evansville");
MakeHockeyTeams((sqlcur, sqlcon), "Indianapolis", "IN", "Fuel", "Western", "Midwest", "Indiana Farmers Coliseum", "Indy");
MakeHockeyTeams((sqlcur, sqlcon), "Fort Wayne", "IN", "Komets", "Western", "Midwest", "Allen County War Memorial Coliseum", "Fort Wayne");
MakeHockeyTeams((sqlcur, sqlcon), "Cincinnati", "OH", "Cyclones", "Western", "Midwest", "US Bank Arena", "Cincinnati");

print("Inserting "+leaguename+" Teams From Central Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Wichita", "KS", "Thunder", "Western", "Central", "Intrust Bank Arena", "Wichita");
MakeHockeyTeams((sqlcur, sqlcon), "Allen", "TX", "Americans", "Western", "Central", "Allen Event Center", "Allen");
MakeHockeyTeams((sqlcur, sqlcon), "Tulsa", "OK", "Oilers", "Western", "Central", "BOK Center", "Tulsa");
MakeHockeyTeams((sqlcur, sqlcon), "Independence", "MO", "Mavericks", "Western", "Central", "Silverstein Eye Centers Arena", "Missouri");

print("Inserting "+leaguename+" Teams From West Division.\n");
MakeHockeyTeams((sqlcur, sqlcon), "Anchorage", "AK", "Aces", "Western", "West", "Sullivan Arena", "Alaska");
MakeHockeyTeams((sqlcur, sqlcon), "Boise", "ID", "Steelheads", "Western", "West", "CenturyLink Arena", "Idaho");
MakeHockeyTeams((sqlcur, sqlcon), "West Valley City", "UT", "Grizzlies", "Western", "West", "Maverik Center", "Utah");
MakeHockeyTeams((sqlcur, sqlcon), "Loveland", "CO", "Eagles", "Western", "West", "Budweiser Events Center", "Colorado");
MakeHockeyTeams((sqlcur, sqlcon), "Rapid City", "SD", "Rush", "Western", "West", "Rushmore Plaza Civic Center", "Rapid City");

sqlcon.commit();

def GetNum2Team(sqldatacon, TeamNum, ReturnVar):
 global leaguename;
 return str(sqldatacon[0].execute("SELECT "+ReturnVar+" FROM "+leaguename+"Teams WHERE id="+str(TeamNum)).fetchone()[0]);

def GetTeam2Num(sqldatacon, TeamName):
 global leaguename;
 return int(sqldatacon[0].execute("SELECT id FROM "+leaguename+"Teams WHERE FullName=\""+str(TeamName)+"\"").fetchone()[0]);

print("DONE! All Team Data Inserted.");

print("Creating "+leaguename+" Game Table.");

sqlcon.execute("DROP TABLE IF EXISTS "+leaguename+"Games");
sqlcur.execute("CREATE TABLE "+leaguename+"Games(id INTEGER PRIMARY KEY, Date INTEGER, HomeTeam Text, AwayTeam Text, AtArena Text, TeamScorePeriods TEXT, TeamFullScore Text, ShotsOnGoal INTEGER, FullShotsOnGoal INTEGER, NumberPeriods INTEGER, TeamWin Text, IsPlayOffGame INTEGER)");
sqlcon.commit();

def MakeHockeyGame(sqldatacon, date, hometeam, awayteam, periodsscore, shotsongoal, atarena, isplayoffgame):
 global leaguename;
 isplayoffgsql = "0";
 if(isplayoffgame==True):
  isplayoffgsql = "1";
 if(isplayoffgame==False):
  isplayoffsql = "0";
 periodssplit = periodsscore.split(",");
 periodcounting = 0;
 numberofperiods=int(len(periodssplit));
 homescore = 0;
 awayscore = 0;
 homeperiodscore = "";
 awayperiodscore = "";
 while(periodcounting<numberofperiods):
  periodscoresplit = periodssplit[periodcounting].split(":");
  homeperiodscore = homeperiodscore+" "+str(periodscoresplit[0]);
  awayperiodscore = awayperiodscore+" "+str(periodscoresplit[1]);
  if(periodcounting <= 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==True and periodcounting > 3):
   homescore = homescore + int(periodscoresplit[0]);
   awayscore = awayscore + int(periodscoresplit[1]);
  if(isplayoffgame==False and periodcounting > 3):
   if(periodscoresplit[0] > periodscoresplit[1]):
    homescore = homescore + 1;
   if(periodscoresplit[0] < periodscoresplit[1]):
    awayscore = awayscore + 1;
  periodcounting = periodcounting + 1;
 totalscore = str(homescore)+":"+str(awayscore);
 teamscores=totalscore.split(":");
 shotsongoalsplit = shotsongoal.split(",");
 numberofsogperiods=int(len(shotsongoalsplit));
 periodsogcounting = 0;
 homesog = 0;
 awaysog = 0;
 homeperiodsog = "";
 awayperiodsog = "";
 while(periodsogcounting<numberofsogperiods):
  periodsogsplit = shotsongoalsplit[periodsogcounting].split(":");
  homesog = homesog + int(periodsogsplit[0]);
  awaysog = awaysog + int(periodsogsplit[1]);
  periodsogcounting = periodsogcounting + 1;
 totalsog = str(homesog)+":"+str(awaysog);
 teamssog=totalsog.split(":");
 hometeamname = hometeam;
 hometeam = GetTeam2Num(sqldatacon, hometeam);
 awayteamname = awayteam;
 awayteam = GetTeam2Num(sqldatacon, awayteam);
 if(atarena==0):
  atarena = hometeam;
  atarenaname = GetTeamData(sqldatacon, hometeam, "FullArenaName", "str");
 print("Home Arena: "+str(atarenaname));
 print("Home Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"));
 print("Home Period Scores:"+homeperiodscore);
 print("Home Score: "+str(teamscores[0]));
 print("Away Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"));
 print("Away Period Scores:"+awayperiodscore);
 print("Away Score: "+str(teamscores[1]));
 print("Number Of Periods: "+str(numberofperiods));
 if(teamscores[0] > teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"));
  losingteam = awayteam;
  winningteam = hometeam;
  winningteamname = hometeamname;
  losingteamname = awayteamname;
 if(teamscores[0] < teamscores[1]):
  print("Winning Team: "+GetNum2Team(sqldatacon, int(awayteam), "FullName"));
  print("Losing Team: "+GetNum2Team(sqldatacon, int(hometeam), "FullName"));
  losingteam = hometeam;
  winningteam = awayteam;
  winningteamname = awayteamname;
  losingteamname = hometeamname;
 print(" ");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Games(Date, HomeTeam, AwayTeam, AtArena, TeamScorePeriods, TeamFullScore, ShotsOnGoal, FullShotsOnGoal, NumberPeriods, TeamWin, IsPlayOffGame) VALUES("+str(date)+", \""+str(hometeamname)+"\", \""+str(awayteamname)+"\", \""+str(atarenaname)+"\", \""+str(periodsscore)+"\", \""+str(totalscore)+"\", \""+str(shotsongoal)+"\", \""+str(totalsog)+"\", "+str(numberofperiods)+", \""+str(winningteamname)+"\", "+str(isplayoffgsql)+")");
 UpdateArenaData(sqldatacon, atarena, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, hometeam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, hometeam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, hometeam, "GamesPlayedHome", 1, "+");
 UpdateTeamData(sqldatacon, hometeam, "GoalsFor", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, hometeam, "GoalsAgainst", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, hometeam, "GoalsDifference", int(int(teamscores[0]) - int(teamscores[1])), "+");
 UpdateTeamData(sqldatacon, hometeam, "SOGFor", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, hometeam, "SOGAgainst", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, hometeam, "SOGDifference", int(int(teamssog[0]) - int(teamssog[1])), "+");
 UpdateTeamData(sqldatacon, awayteam, "Date", int(date), "=");
 UpdateTeamData(sqldatacon, awayteam, "GamesPlayed", 1, "+");
 UpdateTeamData(sqldatacon, awayteam, "GamesPlayedAway", 1, "+");
 UpdateTeamData(sqldatacon, awayteam, "GoalsFor", int(teamscores[1]), "+");
 UpdateTeamData(sqldatacon, awayteam, "GoalsAgainst", int(teamscores[0]), "+");
 UpdateTeamData(sqldatacon, awayteam, "GoalsDifference", int(int(teamscores[1]) - int(teamscores[0])), "+");
 UpdateTeamData(sqldatacon, awayteam, "SOGFor", int(teamssog[1]), "+");
 UpdateTeamData(sqldatacon, awayteam, "SOGAgainst", int(teamssog[0]), "+");
 UpdateTeamData(sqldatacon, awayteam, "SOGDifference", int(int(teamssog[1]) - int(teamssog[0])), "+");
 UpdateTeamDataString(sqldatacon, winningteam, "LastTen", GetLastTenGames(sqldatacon, winningteamname));
 UpdateTeamDataString(sqldatacon, losingteam, "LastTen", GetLastTenGames(sqldatacon, losingteamname));
 GetWinningStreak = GetTeamData(sqldatacon, winningteam, "Streak", "str");
 GetWinningStreakNext = "Won 1";
 if(GetWinningStreak!="None"):
  GetWinningStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetWinningStreak);
  if(GetWinningStreakSplit[0][0]=="Won"):
   GetWinningStreakNext = "Won "+str(int(GetWinningStreakSplit[0][1]) + 1);
  if(GetWinningStreakSplit[0][0]=="Lost"):
   GetWinningStreakNext = "Won 1";
  if(GetWinningStreakSplit[0][0]=="OT"):
   GetWinningStreakNext = "Won 1";
 UpdateTeamDataString(sqldatacon, winningteam, "Streak", GetWinningStreakNext);
 GetLosingStreak = GetTeamData(sqldatacon, losingteam, "Streak", "str");
 if(numberofperiods==3):
  GetLosingStreakNext = "Lost 1";
 if(numberofperiods>3):
  GetLosingStreakNext = "OT 1";
 if(GetLosingStreak!="None"):
  GetLosingStreakSplit = re.findall("([a-zA-Z]+) ([0-9]+)", GetLosingStreak);
  if(GetLosingStreakSplit[0][0]=="Won"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="Lost"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost "+str(int(GetLosingStreakSplit[0][1]) + 1);
   if(numberofperiods>3):
    GetLosingStreakNext = "OT 1";
  if(GetLosingStreakSplit[0][0]=="OS"):
   if(numberofperiods==3):
    GetLosingStreakNext = "Lost 1";
   if(numberofperiods>3):
    GetLosingStreakNext = "OT "+str(int(GetLosingStreakSplit[0][1]) + 1);
 UpdateTeamDataString(sqldatacon, losingteam, "Streak", GetLosingStreakNext);
 if((isplayoffgame==False and numberofperiods<5) or (isplayoffgame==True)):
  UpdateTeamData(sqldatacon, winningteam, "ROW", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "ROT", 1, "+");
 if(numberofperiods==3):
  UpdateTeamData(sqldatacon, winningteam, "Wins", 1, "+");
  UpdateTeamData(sqldatacon, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, winningteam, "Points", 2, "+");
  UpdateTeamData(sqldatacon, losingteam, "Losses", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "Points", 0, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1] + 1)+":"+str(ATRSpit[2]);
   UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR);
 if(numberofperiods>3):
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, winningteam, "OTWins", 1, "+");
  UpdateTeamData(sqldatacon, winningteam, "OTSOWins", 1, "+");
  UpdateTeamData(sqldatacon, winningteam, "TWins", 1, "+");
  UpdateTeamData(sqldatacon, winningteam, "Points", 2, "+");
  if((numberofperiods==4 and isplayoffgame==False) or (numberofperiods>4 and isplayoffgame==True)):
   UpdateTeamData(sqldatacon, losingteam, "OTLosses", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "OTSOLosses", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "TLosses", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "Points", 1, "+");
  if(winningteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, winningteam, "HomeRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, winningteam, "HomeRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, losingteam, "AwayRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, losingteam, "AwayRecord", NewATR);
  if(losingteam==hometeam):
   HomeTeamRecord = GetTeamData(sqldatacon, winningteam, "AwayRecord", "str");
   HTRSpit = [int(n) for n in HomeTeamRecord.split(":")];
   NewHTR = str(HTRSpit[0] + 1)+":"+str(HTRSpit[1])+":"+str(HTRSpit[2]);
   UpdateTeamDataString(sqldatacon, winningteam, "AwayRecord", NewHTR);
   AwayTeamRecord = GetTeamData(sqldatacon, losingteam, "HomeRecord", "str");
   ATRSpit = [int(n) for n in AwayTeamRecord.split(":")];
   NewATR = str(ATRSpit[0])+":"+str(ATRSpit[1])+":"+str(ATRSpit[2] + 1);
   UpdateTeamDataString(sqldatacon, losingteam, "HomeRecord", NewATR);
 if(isplayoffgame==False and numberofperiods>4):
  UpdateTeamData(sqldatacon, winningteam, "SOWins", 1, "+");
  UpdateTeamData(sqldatacon, losingteam, "SOLosses", 1, "+");
  WinningTeamShootouts = GetTeamData(sqldatacon, winningteam, "Shootouts", "str");
  WTSoSplit = [int(n) for n in WinningTeamShootouts.split(":")];
  NewWTSo = str(WTSoSplit[0] + 1)+":"+str(WTSoSplit[1]);
  UpdateTeamDataString(sqldatacon, winningteam, "Shootouts", NewWTSo);
  LosingTeamShootouts = GetTeamData(sqldatacon, losingteam, "Shootouts", "str");
  LTSoSplit = [int(n) for n in LosingTeamShootouts.split(":")];
  NewLTSo = str(LTSoSplit[0])+":"+str(LTSoSplit[1] + 1);
  UpdateTeamDataString(sqldatacon, losingteam, "Shootouts", NewLTSo);
 HomeOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData((sqlcur, sqlcon), hometeam, "OTSOLosses", "float"))));
 HomeWinsPCT = float("%.3f" % float(float(GetTeamData((sqlcur, sqlcon), hometeam, "TWins", "float") + HomeOTLossesPCT) / float(GetTeamData((sqlcur, sqlcon), hometeam, "GamesPlayed", "float"))));
 AwayOTLossesPCT = float("%.2f" % float(float(0.5) * float(GetTeamData((sqlcur, sqlcon), awayteam, "OTSOLosses", "float"))));
 AwayWinsPCT = float("%.3f" % float(float(GetTeamData((sqlcur, sqlcon), awayteam, "TWins", "float") + AwayOTLossesPCT) / float(GetTeamData((sqlcur, sqlcon), awayteam, "GamesPlayed", "float"))));
 UpdateTeamData(sqldatacon, hometeam, "PCT", HomeWinsPCT, "=");
 UpdateTeamData(sqldatacon, awayteam, "PCT", AwayWinsPCT, "=");
 sqldatacon[1].commit();
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak) SELECT Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+hometeamname+"\";");
 sqldatacon[0].execute("INSERT INTO "+leaguename+"Stats (Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak) SELECT Date, FullName, CityName, TeamPrefix, AreaName, FullCityName, TeamName, Conference, Division, ArenaName, FullArenaName, GamesPlayed, GamesPlayedHome, GamesPlayedAway, Wins, OTWins, SOWins, OTSOWins, TWins, Losses, OTLosses, SOLosses, OTSOLosses, TLosses, ROW, ROT, HomeRecord, AwayRecord, Shootouts, GoalsFor, GoalsAgainst, GoalsDifference, SOGFor, SOGAgainst, SOGDifference, Points, PCT, LastTen, Streak FROM "+leaguename+"Teams WHERE FullName=\""+awayteamname+"\";");
 sqldatacon[1].commit();
 return True;

print("Database Check Return: "+str(sqlcon.execute("PRAGMA integrity_check(100);").fetchone()[0])+"\n");

sqlcon.close();

print("DONE! All Game Data Inserted.");

print("DONE! "+leaguename+" Database Created.");

