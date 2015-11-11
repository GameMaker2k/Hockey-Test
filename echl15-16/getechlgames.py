#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re, os, sys, urllib, urllib2, cookielib, StringIO, gzip, time, datetime, argparse, urlparse, sqlite3, unicodedata;

sqlcon = sqlite3.connect("../hockey15-16.db3");
sqlcur = sqlcon.cursor();

leaguename = "ECHL";
getforday = "7";
getformonth = "10";
getforyear = "2015";
useragent = "Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0";

if(len(sys.argv) > 1):
 getforday = sys.argv[1];
if(len(sys.argv) > 2):
 getformonth = sys.argv[2];
if(len(sys.argv) > 3):
 getforyear = sys.argv[3];

def GetFull2Team(sqldatacon, TeamName):
 global leaguename;
 return str(sqldatacon[0].execute("SELECT TeamName FROM "+leaguename+"Teams WHERE FullName=\""+str(TeamName)+"\"").fetchone()[0]);

def GetTeam2Full(sqldatacon, TeamName):
 global leaguename;
 return str(sqldatacon[0].execute("SELECT FullName FROM "+leaguename+"Teams WHERE TeamName=\""+str(TeamName)+"\"").fetchone()[0]);

geturls_cj = cookielib.CookieJar();
geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(geturls_cj));
geturls_opener.addheaders = [("Referer", "http://echl.com/"), ("User-Agent", useragent), ("Accept-Encoding", "gzip, deflate"), ("Accept-Language", "en-US,en;q=0.8,en-CA,en-GB;q=0.6"), ("Accept-Charset", "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"), ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"), ("Connection", "close")];
urllib2.install_opener(geturls_opener);
geturls_text = geturls_opener.open("http://echl.com/stats/schedule.php?date="+getforyear+"-"+getformonth+"-"+getforday);
if(geturls_text.info().get("Content-Encoding")=="gzip" or geturls_text.info().get("Content-Encoding")=="deflate"):
 strbuf = StringIO.StringIO(geturls_text.read());
 gzstrbuf = gzip.GzipFile(fileobj=strbuf);
 prehockey_text = gzstrbuf.read()[:];
if(geturls_text.info().get("Content-Encoding")!="gzip" and geturls_text.info().get("Content-Encoding")!="deflate"):
 prehockey_text = geturls_text.read()[:];
pre_get_todays_games = re.escape("<a href=\"game-summary.php?game_id=")+"([0-9]+).*"+re.escape("title=\"Game Summary\">");
get_todays_games = re.findall(pre_get_todays_games, prehockey_text);
num_todays_games = len(get_todays_games);
cur_todays_games = 0;
if(num_todays_games>0):
 print("print(\"Inserting \"+leaguename+\" Game Data From "+getformonth+"/"+getforday+"/"+getforyear+".\\n\");");
while(cur_todays_games<num_todays_games):
 newgetforday = getforday;
 if(len(getforday)==1):
  newgetforday = "0"+getforday;
 newgetformonth = getformonth;
 if(len(getformonth)==1):
  newgetformonth = "0"+getformonth;
 geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(geturls_cj));
 geturls_opener.addheaders = [("Referer", "http://echl.com/stats/schedule.php?date="+getforyear+"-"+getformonth+"-"+getforday), ("User-Agent", useragent), ("Accept-Encoding", "gzip, deflate"), ("Accept-Language", "en-US,en;q=0.8,en-CA,en-GB;q=0.6"), ("Accept-Charset", "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"), ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"), ("Connection", "close")];
 urllib2.install_opener(geturls_opener);
 geturls_text = geturls_opener.open("http://echl.com/stats/game-summary.php?game_id="+get_todays_games[cur_todays_games]);
 if(geturls_text.info().get("Content-Encoding")=="gzip" or geturls_text.info().get("Content-Encoding")=="deflate"):
  strbuf = StringIO.StringIO(geturls_text.read());
  gzstrbuf = gzip.GzipFile(fileobj=strbuf);
  curgame_text = gzstrbuf.read()[:];
 if(geturls_text.info().get("Content-Encoding")!="gzip" and geturls_text.info().get("Content-Encoding")!="deflate"):
  curgame_text = geturls_text.read()[:];
 numpers = 5;
 pre_curgame_score_text = re.escape("<td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\"><b>")+"([0-9]+)"+re.escape("</b></td>");
 curgame_score_text = re.findall(pre_curgame_score_text, curgame_text);
 if(len(curgame_score_text)==0):
  numpers = 4;
  pre_curgame_score_text = re.escape("<td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\"><b>")+"([0-9]+)"+re.escape("</b></td>");
  curgame_score_text = re.findall(pre_curgame_score_text, curgame_text);
 if(len(curgame_score_text)==0):
  numpers = 3;
  pre_curgame_score_text = re.escape("<td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\">")+"([0-9]+)"+re.escape("</td><td align=\"center\" class=\"content\"><b>")+"([0-9]+)"+re.escape("</b></td>");
  curgame_score_text = re.findall(pre_curgame_score_text, curgame_text);
 pre_team_text = re.escape("<tr class=\"light\"><td class=\"content\" nowrap>")+"(.*)"+re.escape("</td>");
 team_text  = re.findall(pre_team_text, unicodedata.normalize('NFKD', curgame_text.decode("utf-8")).encode('ASCII', 'ignore'));
 pre_team_stats = re.escape("<td class=\"light\" align=\"center\">")+"(.*)"+re.escape("</td>");
 get_team_stats = re.findall(pre_team_stats, curgame_text);
 if(numpers==3):
  print("MakeHockeyGame((sqlcur, sqlcon), "+getforyear+newgetformonth+newgetforday+", \""+team_text[3]+"\", \""+team_text[2]+"\", \""+curgame_score_text[1][0]+":"+curgame_score_text[0][0]+","+curgame_score_text[1][1]+":"+curgame_score_text[0][1]+","+curgame_score_text[1][2]+":"+curgame_score_text[0][2]+"\", \""+curgame_score_text[3][0]+":"+curgame_score_text[2][0]+","+curgame_score_text[3][1]+":"+curgame_score_text[2][1]+","+curgame_score_text[3][2]+":"+curgame_score_text[2][2]+"\", 0, False);");
 if(numpers==4):
  print("MakeHockeyGame((sqlcur, sqlcon), "+getforyear+newgetformonth+newgetforday+", \""+team_text[3]+"\", \""+team_text[2]+"\", \""+curgame_score_text[1][0]+":"+curgame_score_text[0][0]+","+curgame_score_text[1][1]+":"+curgame_score_text[0][1]+","+curgame_score_text[1][2]+":"+curgame_score_text[0][2]+","+curgame_score_text[1][3]+":"+curgame_score_text[0][3]+"\", \""+curgame_score_text[3][0]+":"+curgame_score_text[2][0]+","+curgame_score_text[3][1]+":"+curgame_score_text[2][1]+","+curgame_score_text[3][2]+":"+curgame_score_text[2][2]+","+curgame_score_text[3][3]+":"+curgame_score_text[2][3]+"\", 0, False);");
 if(numpers==5):
  print("MakeHockeyGame((sqlcur, sqlcon), "+getforyear+newgetformonth+newgetforday+", \""+team_text[3]+"\", \""+team_text[2]+"\", \""+curgame_score_text[1][0]+":"+curgame_score_text[0][0]+","+curgame_score_text[1][1]+":"+curgame_score_text[0][1]+","+curgame_score_text[1][2]+":"+curgame_score_text[0][2]+","+curgame_score_text[1][3]+":"+curgame_score_text[0][3]+","+curgame_score_text[1][4]+":"+curgame_score_text[0][4]+"\", \""+curgame_score_text[3][0]+":"+curgame_score_text[2][0]+","+curgame_score_text[3][1]+":"+curgame_score_text[2][1]+","+curgame_score_text[3][2]+":"+curgame_score_text[2][2]+","+curgame_score_text[3][3]+":"+curgame_score_text[2][3]+","+curgame_score_text[3][4]+":"+curgame_score_text[2][4]+"\", 0, False);");
 cur_todays_games = cur_todays_games + 1;

sqlcon.close();
