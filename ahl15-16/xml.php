<?php
ob_start("ob_gzhandler");
if(stristr($_SERVER["HTTP_ACCEPT"],"application/xml") ) {
header("Content-Type: application/xml; charset=UTF-8"); }
else { header("Content-Type: text/xml; charset=UTF-8"); }
header("Content-Style-Type: text/css");
header("Content-Script-Type: text/javascript");
header("Content-Language: en");
header("Vary: Accept-Encoding");
header("Date: ".gmdate("D, d M Y H:i:s")." GMT");
header("Last-Modified: ".gmdate("D, d M Y H:i:s")." GMT");
header("Expires: ".gmdate("D, d M Y H:i:s")." GMT");
$leaguename = "AHL";
if(isset($_GET['xslt']) || (isset($_GET['act']) && $_GET['act']=="xslt")) {
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:template match="/">
  <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
   <head>
    <meta charset="UTF-8" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title><?php echo $leaguename; ?> Games &amp; Team Stats</title>
   </head>
   <body>
    <table style="width: 100%;">
     <xsl:for-each select="/hockey/game">
      <tr>
       <th colspan="7"><xsl:value-of select="home/@team"/> vs <xsl:value-of select="away/@team"/> at <xsl:value-of select="@arena"/> on <xsl:value-of select="@date"/></th>
      </tr>
      <xsl:if test="count(home/score) = 3">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>&#160;</th>
        <th>&#160;</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <xsl:if test="count(home/score) = 4">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>OT</th>
        <th>&#160;</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <xsl:if test="count(home/score) = 5">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>OT</th>
        <th>SO</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <tr>
       <td style="text-align: center;"><xsl:value-of select="home/@team"/></td>
       <xsl:for-each select="home/score">
        <td style="text-align: center;"><xsl:value-of select="@goals"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#160;</td>
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
      <td style="text-align: center;"><xsl:value-of select="home/@goals"/></td>
      </tr>
      <tr>
       <td style="text-align: center;">Shots on Goal</td>
       <xsl:for-each select="home/score">
        <td style="text-align: center;"><xsl:value-of select="@sog"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#160;</td>
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <td style="text-align: center;"><xsl:value-of select="home/@sog"/></td>
      </tr>
      <xsl:if test="count(home/score) = 3">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>&#160;</th>
        <th>&#160;</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <xsl:if test="count(home/score) = 4">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>OT</th>
        <th>&#160;</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <xsl:if test="count(home/score) = 5">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>OT</th>
        <th>SO</th>
        <th>Total</th>
       </tr>
      </xsl:if>
      <tr>
       <td style="text-align: center;"><xsl:value-of select="away/@team"/></td>
       <xsl:for-each select="away/score">
        <td style="text-align: center;"><xsl:value-of select="@goals"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#160;</td>
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
      <td style="text-align: center;"><xsl:value-of select="away/@goals"/></td>
      </tr>
      <tr>
       <td style="text-align: center;">Shots on Goal</td>
       <xsl:for-each select="away/score">
        <td style="text-align: center;"><xsl:value-of select="@sog"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#160;</td>
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#160;</td>
       </xsl:if>
       <td style="text-align: center;"><xsl:value-of select="away/@sog"/></td>
      </tr>
      <tr>
       <td colspan="7" style="text-align: center;">&#160;</td>
      </tr>
      <tr>
       <td colspan="7" style="text-align: center;">&#160;</td>
      </tr>
     </xsl:for-each>
    </table>
   </body>
  </html>
 </xsl:template>
</xsl:stylesheet>
<?php exit(); }
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
echo "<?xml-stylesheet type=\"text/xsl\" href=\"xml.php?xslt\"?>\n";
?>
<!DOCTYPE hockey [
<!ELEMENT hockey (game)* >
<!ATTLIST hockey league CDATA #IMPLIED >
<!ELEMENT away (score)* >
<!ATTLIST away team CDATA #REQUIRED >
<!ATTLIST away goals CDATA #REQUIRED >
<!ATTLIST away sog CDATA #IMPLIED >
<!ELEMENT home (score)* >
<!ATTLIST home team CDATA #REQUIRED >
<!ATTLIST home goals CDATA #REQUIRED >
<!ATTLIST home sog CDATA #IMPLIED >
<!ELEMENT score  EMPTY >
<!ATTLIST score period CDATA #REQUIRED >
<!ATTLIST score goals CDATA #REQUIRED >
<!ATTLIST score sog CDATA #IMPLIED >
<!ELEMENT game (home,away)* >
<!ATTLIST game date CDATA #REQUIRED >
<!ATTLIST game arena CDATA #REQUIRED >
]>

<?php
echo "<hockey league=\"".$leaguename."\">\n\n";
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")."\">\n  <home team=\"".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n  </home>\n  <away team=\"".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n  </away>\n </game>\n"; }
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")."\">\n  <home team=\"".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[0]."\" sog=\"".$PerTeamSOGFour[0]."\" />\n  </home>\n  <away team=\"".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[1]."\" sog=\"".$PerTeamSOGFour[1]."\" />\n  </away>\n </game>\n"; }
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlentities($tarenares['ArenaName'], ENT_QUOTES, "UTF-8")."\">\n  <home team=\"".htmlentities($toneres['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[0]."\" sog=\"".$PerTeamSOGFour[0]."\" />\n   <score period=\"so\" goals=\"".$PerTeamScoreFive[0]."\" />\n  </home>\n  <away team=\"".htmlentities($ttwores['FullName'], ENT_QUOTES, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[1]."\" sog=\"".$PerTeamSOGFour[1]."\" />\n   <score period=\"so\" goals=\"".$PerTeamScoreFive[1]."\" />\n  </away>\n </game>\n"; }
    echo $LineOne."\n"; } }
if($_GET['act']=="stats") {
echo "</".strtolower($leaguename).">";
die(1);
$SelectWhere = "";
$SelectWhereNext = false;
if(isset($_GET['date']) && is_numeric($_GET['date']) && strlen($_GET['date'])==8) {
 $SelectWhere = "WHERE Date<=".$sqldb->escapeString($_GET['date'])." ";
 $SelectWhereNext = true; }
$sqldb->exec("CREATE TEMP TABLE ".$leaguename."Standings AS SELECT * FROM ".$leaguename."Stats ".$SelectWhere." GROUP BY FullName ORDER BY Date DESC");
echo "<table style=\"width: 100%;\">";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings ORDER BY PCT DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
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
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Conference='".$sqldb->escapeString($conrow['Conference'])."' ORDER BY PCT DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
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
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Division='".$sqldb->escapeString($divrow['Division'])."' ORDER BY PCT DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#".$divrow['Division']."DivisionStats\" id=\"".$divrow['Division']."DivisionStats\">".$leaguename." ".$divrow['Division']." Division Team Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlentities($trow['FullName'], ENT_QUOTES, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; } } }
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&nbsp;</td>\n </tr>\n";
echo "\n</table>\n<div>&nbsp;<br />&nbsp;</div>\n\n"; }
echo "</hockey>";
?>
