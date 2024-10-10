#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime
import gzip
import os
import re
import sqlite3
import sys
import time
import unicodedata
import urllib

import cookielib
import StringIO
import urllib2
import urlparse

sqlcon = sqlite3.connect("../hockey15-16.db3")
sqlcur = sqlcon.cursor()

leaguename = "NHL"
getforday = "7"
getformonth = "10"
getforyear = "2015"
getendyear = "2016"
useragent = "Mozilla/5.0 (Windows NT 6.1; rv:41.0) Gecko/20100101 Firefox/41.0"

if (len(sys.argv) > 1):
    getforday = sys.argv[1]
if (len(sys.argv) > 2):
    getformonth = sys.argv[2]
if (len(sys.argv) > 3):
    getforyear = sys.argv[3]
if (len(sys.argv) > 4):
    getendyear = sys.argv[4]

if (int(getformonth) >= 10):
    getforcuryear = getforyear
if (int(getformonth) <= 9):
    getforcuryear = getendyear


def GetFull2Team(sqldatacon, TeamName):
    global leaguename
    return str(
        sqldatacon[0].execute(
            "SELECT TeamName FROM " +
            leaguename +
            "Teams WHERE FullName=\"" +
            str(TeamName) +
            "\"").fetchone()[0])


def GetTeam2Full(sqldatacon, TeamName):
    global leaguename
    return str(
        sqldatacon[0].execute(
            "SELECT FullName FROM " +
            leaguename +
            "Teams WHERE TeamName=\"" +
            str(TeamName) +
            "\"").fetchone()[0])


geturls_cj = cookielib.CookieJar()
geturls_opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(geturls_cj))
geturls_opener.addheaders = [
    ("Referer",
     "http://www.nhl.com/"),
    ("User-Agent",
     useragent),
    ("Accept-Encoding",
     "gzip, deflate"),
    ("Accept-Language",
     "en-US,en;q=0.8,en-CA,en-GB;q=0.6"),
    ("Accept-Charset",
     "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"),
    ("Accept",
     "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("Connection",
     "close")]
urllib2.install_opener(geturls_opener)
geturls_text = geturls_opener.open(
    "http://www.nhl.com/ice/schedulebyday.htm?date=" +
    getformonth +
    "/" +
    getforday +
    "/" +
    getforcuryear +
    "&season=" +
    getforyear +
    getendyear)
if (geturls_text.info().get("Content-Encoding") ==
        "gzip" or geturls_text.info().get("Content-Encoding") == "deflate"):
    strbuf = StringIO.StringIO(geturls_text.read())
    gzstrbuf = gzip.GzipFile(fileobj=strbuf)
    prehockey_text = gzstrbuf.read()[:]
if (geturls_text.info().get("Content-Encoding") !=
        "gzip" and geturls_text.info().get("Content-Encoding") != "deflate"):
    prehockey_text = geturls_text.read()[:]
pre_get_todays_games = re.escape("<a class=\"btn\" shape=\"rect\" href=\"http://www.nhl.com/gamecenter/en/recap?id=") + \
    "([0-9]+)" + re.escape("\"><span>RECAP›</span></a>")
get_todays_games = re.findall(pre_get_todays_games, prehockey_text)
num_todays_games = len(get_todays_games)
cur_todays_games = 0
if (num_todays_games > 0):
    print(
        "print(\"Inserting \"+leaguename+\" Game Data From " +
        getformonth.lstrip('0') +
        "/" +
        getforday.lstrip('0') +
        "/" +
        getforcuryear +
        ".\\n\");")
while (cur_todays_games < num_todays_games):
    newgetforday = getforday
    if (len(getforday) == 1):
        newgetforday = "0" + getforday
    newgetformonth = getformonth
    if (len(getformonth) == 1):
        newgetformonth = "0" + getformonth
    geturls_opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(geturls_cj))
    geturls_opener.addheaders = [
        ("Referer",
         "http://www.nhl.com/ice/schedulebyday.htm?date=" +
         getformonth +
         "/" +
         getforday +
         "/" +
         getforcuryear +
         "&season=" +
         getforyear +
         getendyear),
        ("User-Agent",
         useragent),
        ("Accept-Encoding",
         "gzip, deflate"),
        ("Accept-Language",
         "en-US,en;q=0.8,en-CA,en-GB;q=0.6"),
        ("Accept-Charset",
         "ISO-8859-1,ISO-8859-15,utf-8;q=0.7,*;q=0.7"),
        ("Accept",
         "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
        ("Connection",
         "close")]
    urllib2.install_opener(geturls_opener)
    geturls_text = geturls_opener.open(
        "http://www.nhl.com/gamecenter/en/boxscore?id=" +
        get_todays_games[cur_todays_games])
    if (geturls_text.info().get("Content-Encoding") ==
            "gzip" or geturls_text.info().get("Content-Encoding") == "deflate"):
        strbuf = StringIO.StringIO(geturls_text.read())
        gzstrbuf = gzip.GzipFile(fileobj=strbuf)
        curgame_text = gzstrbuf.read()[:]
    if (geturls_text.info().get("Content-Encoding") !=
            "gzip" and geturls_text.info().get("Content-Encoding") != "deflate"):
        curgame_text = geturls_text.read()[:]
    numpers = 3
    pre_curgame_score_text = re.escape("<span style=\"display: none;\" class=\"prd") + \
        "([0-9]+)" + re.escape("\">") + "([0-9]+)" + re.escape("</span>")
    curgame_score_text = re.findall(pre_curgame_score_text, curgame_text)
    pre_curgame_otscore_text = re.escape(
        "<span style=\"display: none;\" class=\"ot\">") + "([0-9]+)" + re.escape("</span>")
    curgame_otscore_text = re.findall(pre_curgame_otscore_text, curgame_text)
    if (len(curgame_otscore_text) == 2):
        numpers = 4
    pre_curgame_soscore_text = re.escape("<span style=\"display: none;\" class=\"details\">") + \
        "([0-9]+)" + re.escape(" - ") + "([0-9]+)" + re.escape("</span>")
    curgame_soscore_text = re.findall(pre_curgame_soscore_text, curgame_text)
    if (len(curgame_soscore_text) == 2 and (
            int(curgame_soscore_text[0][0]) > 0 or int(curgame_soscore_text[1][0]) > 0)):
        numpers = 5
    pre_team_text = re.escape("<img title=\"") + "([a-zA-Z\\. ]+)" + re.escape(
        "\" alt=\"") + "([a-zA-Z\\. ]+)" + re.escape("\" class=\"team-logo  \" src=\"")
    team_text = re.findall(pre_team_text, unicodedata.normalize(
        'NFKD', curgame_text.decode("utf-8")).encode('ASCII', 'ignore'))
    pre_team_shots = re.escape(
        "colspan=\"1\" rowspan=\"1\" class=\"aShots\">") + "([0-9]+)" + re.escape("</td>")
    away_team_shots = re.findall(pre_team_shots, curgame_text)
    pre_team_shots = re.escape(
        "colspan=\"1\" rowspan=\"1\" class=\"hShots\">") + "([0-9]+)" + re.escape("</td>")
    home_team_shots = re.findall(pre_team_shots, curgame_text)
    pre_team_stats = re.escape("colspan=\"1\" rowspan=\"1\" class=\"") + \
        "((a|h)[a-zA-Z]+)" + re.escape("\">") + \
        "([0-9\\/]+)" + re.escape("</td>")
    get_team_stats = re.findall(pre_team_stats, curgame_text)
    if (numpers == 3):
        print(
            "MakeHockeyGame((sqlcur, sqlcon), " +
            getforcuryear +
            newgetformonth +
            newgetforday +
            ", \"" +
            team_text[1][0] +
            "\", \"" +
            team_text[0][0] +
            "\", \"" +
            curgame_score_text[3][1] +
            ":" +
            curgame_score_text[0][1] +
            "," +
            curgame_score_text[4][1] +
            ":" +
            curgame_score_text[1][1] +
            "," +
            curgame_score_text[5][1] +
            ":" +
            curgame_score_text[2][1] +
            "\", \"" +
            home_team_shots[0] +
            ":" +
            away_team_shots[0] +
            "," +
            home_team_shots[1] +
            ":" +
            away_team_shots[1] +
            "," +
            home_team_shots[2] +
            ":" +
            away_team_shots[2] +
            "\", 0, False);")
    if (numpers == 4):
        print(
            "MakeHockeyGame((sqlcur, sqlcon), " +
            getforcuryear +
            newgetformonth +
            newgetforday +
            ", \"" +
            team_text[1][0] +
            "\", \"" +
            team_text[0][0] +
            "\", \"" +
            curgame_score_text[3][1] +
            ":" +
            curgame_score_text[0][1] +
            "," +
            curgame_score_text[4][1] +
            ":" +
            curgame_score_text[1][1] +
            "," +
            curgame_score_text[5][1] +
            ":" +
            curgame_score_text[2][1] +
            "," +
            curgame_otscore_text[1] +
            ":" +
            curgame_otscore_text[0] +
            "\", \"" +
            home_team_shots[0] +
            ":" +
            away_team_shots[0] +
            "," +
            home_team_shots[1] +
            ":" +
            away_team_shots[1] +
            "," +
            home_team_shots[2] +
            ":" +
            away_team_shots[2] +
            "," +
            home_team_shots[3] +
            ":" +
            away_team_shots[3] +
            "\", 0, False);")
    if (numpers == 5):
        print(
            "MakeHockeyGame((sqlcur, sqlcon), " +
            getforcuryear +
            newgetformonth +
            newgetforday +
            ", \"" +
            team_text[1][0] +
            "\", \"" +
            team_text[0][0] +
            "\", \"" +
            curgame_score_text[3][1] +
            ":" +
            curgame_score_text[0][1] +
            "," +
            curgame_score_text[4][1] +
            ":" +
            curgame_score_text[1][1] +
            "," +
            curgame_score_text[5][1] +
            ":" +
            curgame_score_text[2][1] +
            "," +
            curgame_otscore_text[1] +
            ":" +
            curgame_otscore_text[0] +
            "," +
            curgame_soscore_text[1][0] +
            ":" +
            curgame_soscore_text[0][0] +
            "\", \"" +
            home_team_shots[0] +
            ":" +
            away_team_shots[0] +
            "," +
            home_team_shots[1] +
            ":" +
            away_team_shots[1] +
            "," +
            home_team_shots[2] +
            ":" +
            away_team_shots[2] +
            "," +
            home_team_shots[3] +
            ":" +
            away_team_shots[3] +
            "\", 0, False);")
    cur_todays_games = cur_todays_games + 1

sqlcon.close()
