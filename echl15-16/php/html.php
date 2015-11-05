<?php
ob_start("ob_gzhandler");
header("Content-Type: text/html; charset=UTF-8");
header("Content-Style-Type: text/css");
header("Content-Script-Type: text/javascript");
header("Content-Language: en");
header("Vary: Accept-Encoding");
header("Date: ".gmdate("D, d M Y H:i:s")." GMT");
header("Last-Modified: ".gmdate("D, d M Y H:i:s")." GMT");
header("Expires: ".gmdate("D, d M Y H:i:s")." GMT");
$leaguename = "ECHL";
?>
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title><?php echo $leaguename; ?> Games &amp; Team Stats</title>
 </head>
 <body>
<?php
if(!isset($_GET['act'])&&isset($_GET['view'])) { $_GET['act'] = "view"; }
if(!isset($_GET['act'])&&isset($_GET['games'])) { $_GET['act'] = "view"; }
if(!isset($_GET['act'])&&isset($_GET['stats'])) { $_GET['act'] = "stats"; }
if(isset($_GET['month']) && strlen($_GET['month'])==1) {
 $_GET['month'] = "0".$_GET['month']; }
if(isset($_GET['day']) && strlen($_GET['day'])==1) {
 $_GET['day'] = "0".$_GET['day']; }
if(!isset($_GET['year']) && isset($_GET['month']) && isset($_GET['day']) &&
   is_numeric($_GET['month']) && is_numeric($_GET['day']) &&
   strlen($_GET['month'])==2 && strlen($_GET['day'])==2) {
   $_GET['date'] = gmdate("Y").$_GET['month'].$_GET['day']; }
if(isset($_GET['year']) && isset($_GET['month']) && isset($_GET['day']) &&
   is_numeric($_GET['year']) && is_numeric($_GET['month']) && is_numeric($_GET['day']) &&
   strlen($_GET['year'])>=4 && strlen($_GET['month'])==2 && strlen($_GET['day'])==2) {
   $_GET['date'] = $_GET['year'].$_GET['month'].$_GET['day']; }
if($_GET['act']=="stats") {
 if(!isset($_GET['conference'])) { $_GET['conference'] = "All"; }
 if(!isset($_GET['division'])) { $_GET['division'] = "All"; } }
if(!isset($_GET['act'])) { $_GET['act'] = "view"; }
if($_GET['act']!="view" && $_GET['act']!="games" && $_GET['act']!="stats") { $_GET['act'] = "view"; }
$sqldb = new SQLite3("../hockey15-16.db3");
$sqldb->exec("PRAGMA encoding = \"UTF-8\";");
$sqldb->exec("PRAGMA auto_vacuum = 1;");
$sqldb->exec("PRAGMA foreign_keys = 1;");
$sqlite_games_string = "";
function get_last_ten_games($teamid, $sqlink) {
 global $leaguename;
 $ltresults = $sqlink->query("SELECT * FROM ".$leaguename."Games WHERE (TeamOne=".$teamid." OR TeamTwo=".$teamid.") ORDER BY id DESC LIMIT 10");
 $teamwins = 0;
 $teamlosses = 0;
 $teamotlosses = 0;
 while ($ltrow = $ltresults->fetchArray()) {
  if($teamid==$ltrow['TeamWin']) {
   $teamwins += 1; }
  if($teamid!=$ltrow['TeamWin']) {
   if($ltrow['NumberPeriods']==3) {
    $teamlosses += 1; }
   if($ltrow['NumberPeriods']>3) {
    $teamotlosses += 1; } } }
 return $teamwins."-".$teamlosses."-".$teamotlosses; }
function get_streak_num($teamid, $sqlink) {
 global $leaguename;
 $ltresults = $sqlink->query("SELECT * FROM ".$leaguename."Games WHERE (TeamOne=".$teamid." OR TeamTwo=".$teamid.") ORDER BY id DESC");
 $streak = "";
 $teamwins = 0;
 $teamlosses = 0;
 $teamotlosses = 0;
 while ($ltrow = $ltresults->fetchArray()) {
  if($teamid==$ltrow['TeamWin']) {
   if($teamlosses>0 || $teamotlosses>0) { break; }
   $teamwins += 1; }
  if($teamid!=$ltrow['TeamWin']) {
   if($ltrow['NumberPeriods']==3) {
    if($teamwins>0 || $teamotlosses>0) { break; }
    $teamlosses += 1; }
   if($ltrow['NumberPeriods']>3) {
    if($teamwins>0 || $teamlosses>0) { break; }
    $teamotlosses += 1; } } }
 if($streak=="" && $teamwins>0) { $streak = "Won ".$teamwins; }
 if($streak=="" && $teamlosses>0) { $streak = "Lost ".$teamlosses; }
 if($streak=="" && $teamotlosses>0) { $streak = "OT ".$teamotlosses; }
 return $streak; }
if($_GET['act']=="view") {
$SelectWhere = "";
$SelectWhereNext = false;
if(isset($_GET['date']) && is_numeric($_GET['date']) && strlen($_GET['date'])==8) {
 $SelectWhere = "WHERE Date=".$sqldb->escapeString($_GET['date'])." ";
 $SelectWhereNext = true; }
if(!isset($_GET['month']) || !is_numeric($_GET['month']) or !strlen($_GET['month'])==2) {
 $_GET['month'] = gmdate("m"); }
if(!isset($_GET['date']) && is_numeric($_GET['month']) && strlen($_GET['month'])==2) {
 if(!isset($_GET['year']) || !is_numeric($_GET['year']) || strlen($_GET['year'])<4) {
  $_GET['year'] = gmdate("Y"); }
 $startday = $_GET['year'].$_GET['month']."01";
 $endday = $_GET['year'].$_GET['month']."31";
 $SelectWhere = "WHERE (Date>=".$sqldb->escapeString($startday)." AND Date<=".$sqldb->escapeString($endday).") ";
 $SelectWhereNext = true; }
if(isset($_GET['team'])) {
 if($SelectWhereNext==true) {
  $SelectWhere .= " AND (TeamOne='".$sqldb->escapeString($_GET['team'])."' OR TeamTwo='".$sqldb->escapeString($_GET['team'])."') "; }
 if($SelectWhereNext==false) {
  $SelectWhere = "WHERE (TeamOne='".$sqldb->escapeString($_GET['team'])."' OR TeamTwo='".$sqldb->escapeString($_GET['team'])."') ";
  $SelectWhereNext = true; } }
$results = $sqldb->query("SELECT * FROM ".$leaguename."Games ".$SelectWhere."ORDER BY id DESC");
echo "<table style=\"width: 100%;\">\n";
while ($row = $results->fetchArray()) {
    $toneres = $sqldb->querySingle("SELECT CityName, TeamName, FullName FROM ".$leaguename."Teams WHERE FullName='".$sqldb->escapeString($row['TeamOne'])."'", true);
    $ttwores = $sqldb->querySingle("SELECT CityName, TeamName, FullName FROM ".$leaguename."Teams WHERE FullName='".$sqldb->escapeString($row['TeamTwo'])."'", true);
    $tarenares = $sqldb->querySingle("SELECT CityName, ArenaName, FullArenaName FROM ".$leaguename."Arenas WHERE FullArenaName='".$sqldb->escapeString($row['AtArena'])."'", true);
    if($row['NumberPeriods']==3) {
       $PerPeriodScore = explode(",", $row['TeamScorePeriods']);
       $PerTeamScoreOne = explode(":", $PerPeriodScore[0]);
       $PerTeamScoreTwo = explode(":", $PerPeriodScore[1]);
       $PerTeamScoreThree = explode(":", $PerPeriodScore[2]);
       $PerTeamScoreTotal = explode(":", $row['TeamFullScore']);
       $PerPeriodSOG = explode(",", $row['ShotsOnGoal']);
       $PerTeamSOGOne = explode(":", $PerPeriodSOG[0]);
       $PerTeamSOGTwo = explode(":", $PerPeriodSOG[1]);
       $PerTeamSOGThree = explode(":", $PerPeriodSOG[2]);
       $PerTeamSOGTotal = explode(":", $row['FullShotsOnGoal']);
       $tonebold = "";
       if($PerTeamScoreTotal[0]>$PerTeamScoreTotal[1]) { $tonebold = " font-weight: bold;"; }
       $ttwobold = "";
       if($PerTeamScoreTotal[0]<$PerTeamScoreTotal[1]) { $ttwobold = " font-weight: bold;"; }
       $LineOne = " <tr>\n   <th colspan=\"7\"><a href=\"index.php?games&amp;date=".urlencode($row['Date'])."&amp;team=".urlencode($toneres['FullName'])."&amp;#".$leaguename."Game-".urlencode($row['Date'])."-".urlencode(preg_replace('/\s+/', '', $toneres['FullName']))."-vs-".urlencode(preg_replace('/\s+/', '', $ttwores['FullName']))."\" id=\"".$leaguename."Game-".$row['Date']."-".preg_replace('/\s+/', '', htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8"))."-vs-".preg_replace('/\s+/', '', htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8"))."\">".htmlentities($toneres['TeamName'], ENT_QUOTES, "UTF-8")." vs ".htmlentities($ttwores['TeamName'], ENT_QUOTES, "UTF-8")." at ".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")." on ".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."</a></th>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>&#160;</th>\n   <th>&#160;</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$tonebold."\"><a href=\"?games&amp;team=".urlencode($toneres['FullName'])."\">".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[0]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[0]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[0]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[0]."</td>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>&#160;</th>\n   <th>&#160;</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$ttwobold."\"><a href=\"?games&amp;team=".urlencode($ttwores['FullName'])."\">".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[1]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[1]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[1]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[1]."</td>\n </tr>\n"; }
    if($row['NumberPeriods']==4) {
       $PerPeriodScore = explode(",", $row['TeamScorePeriods']);
       $PerTeamScoreOne = explode(":", $PerPeriodScore[0]);
       $PerTeamScoreTwo = explode(":", $PerPeriodScore[1]);
       $PerTeamScoreThree = explode(":", $PerPeriodScore[2]);
       $PerTeamScoreFour = explode(":", $PerPeriodScore[3]);
       $PerTeamScoreTotal = explode(":", $row['TeamFullScore']);
       $PerPeriodSOG = explode(",", $row['ShotsOnGoal']);
       $PerTeamSOGOne = explode(":", $PerPeriodSOG[0]);
       $PerTeamSOGTwo = explode(":", $PerPeriodSOG[1]);
       $PerTeamSOGThree = explode(":", $PerPeriodSOG[2]);
       $PerTeamSOGFour = explode(":", $PerPeriodSOG[3]);
       $PerTeamSOGTotal = explode(":", $row['FullShotsOnGoal']);
       $tonebold = "";
       if($PerTeamScoreTotal[0]>$PerTeamScoreTotal[1]) { $tonebold = " font-weight: bold;"; }
       $ttwobold = "";
       if($PerTeamScoreTotal[0]<$PerTeamScoreTotal[1]) { $ttwobold = " font-weight: bold;"; }
       $LineOne = " <tr>\n   <th colspan=\"7\"><a href=\"index.php?games&amp;date=".urlencode($row['Date'])."&amp;team=".urlencode($toneres['FullName'])."&amp;#".$leaguename."Game-".$row['Date']."-".urlencode(preg_replace('/\s+/', '', $toneres['FullName']))."-vs-".urlencode(preg_replace('/\s+/', '', $ttwores['FullName']))."\" id=\"".$leaguename."Game-".urlencode($row['Date'])."-".preg_replace('/\s+/', '', htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8"))."-vs-".preg_replace('/\s+/', '', htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8"))."\">".htmlentities($toneres['TeamName'], ENT_QUOTES, "UTF-8")." vs ".htmlentities($ttwores['TeamName'], ENT_QUOTES, "UTF-8")." at ".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")." on ".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."</a></th>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>OT</th>\n   <th>&#160;</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$tonebold."\"><a href=\"?games&amp;team=".urlencode($toneres['FullName'])."\">".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFour[0]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[0]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGFour[0]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[0]."</td>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>OT</th>\n   <th>&#160;</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$ttwobold."\"><a href=\"?games&amp;team=".urlencode($ttwores['FullName'])."\">".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFour[1]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[1]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGFour[1]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[1]."</td>\n </tr>\n"; }
    if($row['NumberPeriods']==5) {
       $PerPeriodScore = explode(",", $row['TeamScorePeriods']);
       $PerTeamScoreOne = explode(":", $PerPeriodScore[0]);
       $PerTeamScoreTwo = explode(":", $PerPeriodScore[1]);
       $PerTeamScoreThree = explode(":", $PerPeriodScore[2]);
       $PerTeamScoreFour = explode(":", $PerPeriodScore[3]);
       $PerTeamScoreFive = explode(":", $PerPeriodScore[4]);
       $PerTeamScoreTotal = explode(":", $row['TeamFullScore']);
       $PerPeriodSOG = explode(",", $row['ShotsOnGoal']);
       $PerTeamSOGOne = explode(":", $PerPeriodSOG[0]);
       $PerTeamSOGTwo = explode(":", $PerPeriodSOG[1]);
       $PerTeamSOGThree = explode(":", $PerPeriodSOG[2]);
       $PerTeamSOGFour = explode(":", $PerPeriodSOG[3]);
       $PerTeamSOGTotal = explode(":", $row['FullShotsOnGoal']);
       $tonebold = "";
       if($PerTeamScoreTotal[0]>$PerTeamScoreTotal[1]) { $tonebold = " font-weight: bold;"; }
       $ttwobold = "";
       if($PerTeamScoreTotal[0]<$PerTeamScoreTotal[1]) { $ttwobold = " font-weight: bold;"; }
       $LineOne = " <tr>\n   <th colspan=\"7\"><a href=\"index.php?games&amp;date=".urlencode($row['Date'])."&amp;team=".urlencode($toneres['FullName'])."&amp;#".$leaguename."Game-".$row['Date']."-".urlencode(preg_replace('/\s+/', '', $toneres['FullName']))."-vs-".urlencode(preg_replace('/\s+/', '', $ttwores['FullName']))."\" id=\"".$leaguename."Game-".urlencode($row['Date'])."-".preg_replace('/\s+/', '', htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8"))."-vs-".preg_replace('/\s+/', '', htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8"))."\">".htmlentities($toneres['TeamName'], ENT_QUOTES, "UTF-8")." vs ".htmlentities($ttwores['TeamName'], ENT_QUOTES, "UTF-8")." at ".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")." on ".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."</a></th>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>OT</th>\n   <th>SO</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$tonebold."\"><a href=\"?games&amp;team=".urlencode($toneres['FullName'])."\">".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFour[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFive[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[0]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[0]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGFour[0]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[0]."</td>\n </tr>\n <tr>\n   <th>Teams</th>\n   <th>1st</th>\n   <th>2nd</th>\n   <th>3rd</th>\n   <th>OT</th>\n   <th>SO</th>\n   <th>Total</th>\n </tr>\n <tr>\n   <td style=\"text-align: center;".$ttwobold."\"><a href=\"?games&amp;team=".urlencode($ttwores['FullName'])."\">".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$PerTeamScoreOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreThree[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFour[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreFive[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamScoreTotal[1]."</td>\n </tr>\n <tr>\n   <td style=\"text-align: center;\">Shots on Goal</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGOne[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTwo[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGThree[1]."</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGFour[1]."</td>\n   <td style=\"text-align: center;\">&#160;</td>\n   <td style=\"text-align: center;\">".$PerTeamSOGTotal[1]."</td>\n </tr>\n"; }
    echo $LineOne."\n <tr>\n   <td colspan=\"7\" style=\"text-align: center;\">&#160;</td>\n </tr>\n <tr>\n   <td colspan=\"7\" style=\"text-align: center;\">&#160;</td>\n </tr>\n"; }
echo "</table>\n<div>&#160;<br />&#160;</div>\n\n"; }
if($_GET['act']=="stats") {
$SelectWhere = "";
$SelectWhereNext = false;
if(isset($_GET['date']) && is_numeric($_GET['date']) && strlen($_GET['date'])==8) {
 $SelectWhere = "WHERE Date<=".$sqldb->escapeString($_GET['date'])." ";
 $SelectWhereNext = true; }
$sqldb->exec("CREATE TEMP TABLE ".$leaguename."Standings AS SELECT * FROM ".$leaguename."Stats ".$SelectWhere." GROUP BY FullName ORDER BY Date DESC");
echo "<table style=\"width: 100%;\">";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#OverallStats\" id=\"OverallStats\">".$leaguename." Team Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlentities($trow['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; }
$conresults = $sqldb->query("SELECT * FROM ".$leaguename."Conferences");
while ($conrow = $conresults->fetchArray()) {
if($_GET['conference']=="All" || $_GET['conference']==$conrow['Conference']) {
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Conference='".$sqldb->escapeString($conrow['Conference'])."' ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#".$conrow['Conference']."ConferenceStats\" id=\"".$conrow['Conference']."ConferenceStats\">".$leaguename." ".$conrow['Conference']." Conference Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlentities($trow['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; } } }
$divresults = $sqldb->query("SELECT * FROM ".$leaguename."Divisions");
while ($divrow = $divresults->fetchArray()) {
if($_GET['division']=="All" || $_GET['division']==$divrow['Division']) {
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Division='".$sqldb->escapeString($divrow['Division'])."' ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#".$divrow['Division']."DivisionStats\" id=\"".$divrow['Division']."DivisionStats\">".$leaguename." ".$divrow['Division']." Division Team Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlentities($trow['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; } } }
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#160;</td>\n </tr>\n";
echo "\n</table>\n<div>&#160;<br />&#160;</div>\n\n"; }
?>
 </body>
</html>
