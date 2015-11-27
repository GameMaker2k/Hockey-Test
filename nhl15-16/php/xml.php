<?php
if(!ob_start("ob_gzhandler")) { ob_start(); }
date_default_timezone_set("UTC");
if(stristr($_SERVER["HTTP_ACCEPT"],"application/xml+xslt") ) {
header("Content-Type: application/xml+xslt; charset=UTF-8"); }
elseif(stristr($_SERVER["HTTP_ACCEPT"],"application/xml") ) {
header("Content-Type: application/xml; charset=UTF-8"); }
else { header("Content-Type: text/xml; charset=UTF-8"); }
header("Content-Language: en");
header("Vary: Accept-Encoding,Cookie");
header("X-Content-Type-Options: nosniff");
header("X-UA-Compatible: IE=Edge");
header("Cache-Control: private, no-cache, no-store, must-revalidate, pre-check=0, post-check=0, max-age=0");
header("Pragma: private, no-cache, no-store, must-revalidate, pre-check=0, post-check=0, max-age=0");
header("Date: ".gmdate("D, d M Y H:i:s")." GMT");
header("Last-Modified: ".gmdate("D, d M Y H:i:s")." GMT");
header("Expires: ".gmdate("D, d M Y H:i:s")." GMT");
$leaguename = "NHL";
$fullurl = "http://localhost/hockey/nhl/";
if(isset($_SERVER['HTTPS'])) {
 $fullurl = "https://".$_SERVER["SERVER_NAME"].str_replace("//", "/", dirname($_SERVER["SCRIPT_NAME"])."/"); } 
if(!isset($_SERVER['HTTPS'])) {
 $fullurl = "http://".$_SERVER["SERVER_NAME"].str_replace("//", "/", dirname($_SERVER["SCRIPT_NAME"])."/"); }
if(isset($_GET['xslt']) || (isset($_GET['act']) && $_GET['act']=="xslt")) {
header("Content-Type: application/xslt+xml; charset=UTF-8");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
 <xsl:template match="/">
  <html xsl:version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xml:lang="en" xmlns="http://www.w3.org/1999/xhtml" lang="en">
   <head>
    <meta charset="UTF-8" />
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
        <th>&#xA0;</th>
        <th>&#xA0;</th>
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
        <th>&#xA0;</th>
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
       <xsl:if test="home/@goals &gt; away/@goals">
        <td style="text-align: center; font-weight: bold;"><xsl:value-of select="home/@team"/></td>
       </xsl:if>
       <xsl:if test="home/@goals &lt; away/@goals">
        <td style="text-align: center;"><xsl:value-of select="home/@team"/></td>
       </xsl:if>
       <xsl:for-each select="home/score">
        <td style="text-align: center;"><xsl:value-of select="@goals"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#xA0;</td>
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
      <td style="text-align: center;"><xsl:value-of select="home/@goals"/></td>
      </tr>
      <tr>
       <td style="text-align: center;">Shots on Goal</td>
       <xsl:for-each select="home/score">
        <td style="text-align: center;"><xsl:value-of select="@sog"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#xA0;</td>
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <td style="text-align: center;"><xsl:value-of select="home/@sog"/></td>
      </tr>
      <xsl:if test="count(home/score) = 3">
       <tr>
        <th>Teams</th>
        <th>1st</th>
        <th>2nd</th>
        <th>3rd</th>
        <th>&#xA0;</th>
        <th>&#xA0;</th>
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
        <th>&#xA0;</th>
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
       <xsl:if test="away/@goals &gt; home/@goals">
        <td style="text-align: center; font-weight: bold;"><xsl:value-of select="away/@team"/></td>
       </xsl:if>
       <xsl:if test="away/@goals &lt; home/@goals">
        <td style="text-align: center;"><xsl:value-of select="away/@team"/></td>
       </xsl:if>
       <xsl:for-each select="away/score">
        <td style="text-align: center;"><xsl:value-of select="@goals"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#xA0;</td>
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
      <td style="text-align: center;"><xsl:value-of select="away/@goals"/></td>
      </tr>
      <tr>
       <td style="text-align: center;">Shots on Goal</td>
       <xsl:for-each select="away/score">
        <td style="text-align: center;"><xsl:value-of select="@sog"/></td>
       </xsl:for-each>
       <xsl:if test="count(home/score) = 3">
        <td style="text-align: center;">&#xA0;</td>
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <xsl:if test="count(home/score) = 4">
        <td style="text-align: center;">&#xA0;</td>
       </xsl:if>
       <td style="text-align: center;"><xsl:value-of select="away/@sog"/></td>
      </tr>
      <tr>
       <td colspan="7" style="text-align: center;">&#xA0;</td>
      </tr>
      <tr>
       <td colspan="7" style="text-align: center;">&#xA0;</td>
      </tr>
     </xsl:for-each>
    </table>
   </body>
  </html>
 </xsl:template>
</xsl:stylesheet>
<?php exit(); }
if(isset($_GET['dtd']) || (isset($_GET['act']) && $_GET['act']=="dtd")) {
header("Content-Type: application/xml-dtd; charset=UTF-8");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<!ELEMENT hockey (game)*>
<!ATTLIST hockey league CDATA #IMPLIED>
<!ELEMENT away (score)*>
<!ATTLIST away team CDATA #REQUIRED>
<!ATTLIST away goals CDATA #REQUIRED>
<!ATTLIST away sog CDATA #IMPLIED>
<!ELEMENT home (score)*>
<!ATTLIST home team CDATA #REQUIRED>
<!ATTLIST home goals CDATA #REQUIRED>
<!ATTLIST home sog CDATA #IMPLIED>
<!ELEMENT score  EMPTY >
<!ATTLIST score period CDATA #REQUIRED>
<!ATTLIST score goals CDATA #REQUIRED>
<!ATTLIST score sog CDATA #IMPLIED>
<!ELEMENT game (home,away)*>
<!ATTLIST game date CDATA #REQUIRED>
<!ATTLIST game arena CDATA #REQUIRED>
<?php exit(); }
if(isset($_GET['xsd']) || (isset($_GET['act']) && $_GET['act']=="xsd")) {
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
  <xs:element name="hockey">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" maxOccurs="unbounded" ref="game"/>
      </xs:sequence>
      <xs:attribute name="league"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="away">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" maxOccurs="unbounded" ref="score"/>
      </xs:sequence>
      <xs:attribute name="team" use="required"/>
      <xs:attribute name="goals" use="required"/>
      <xs:attribute name="sog"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="home">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" maxOccurs="unbounded" ref="score"/>
      </xs:sequence>
      <xs:attribute name="team" use="required"/>
      <xs:attribute name="goals" use="required"/>
      <xs:attribute name="sog"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="score">
    <xs:complexType>
      <xs:attribute name="period" use="required"/>
      <xs:attribute name="goals" use="required"/>
      <xs:attribute name="sog"/>
    </xs:complexType>
  </xs:element>
  <xs:element name="game">
    <xs:complexType>
      <xs:sequence minOccurs="0" maxOccurs="unbounded">
        <xs:element ref="home"/>
        <xs:element ref="away"/>
      </xs:sequence>
      <xs:attribute name="date" use="required"/>
      <xs:attribute name="arena" use="required"/>
    </xs:complexType>
  </xs:element>
</xs:schema>
<?php exit(); }
if(isset($_GET['rnc']) || (isset($_GET['act']) && $_GET['act']=="rnc")) {
header("Content-Type: text/plain; charset=UTF-8");
?>
hockey = element hockey { attlist.hockey, game* }
attlist.hockey &= attribute league { text }?
away = element away { attlist.away, score* }
attlist.away &= attribute team { text }
attlist.away &= attribute goals { text }
attlist.away &= attribute sog { text }?
home = element home { attlist.home, score* }
attlist.home &= attribute team { text }
attlist.home &= attribute goals { text }
attlist.home &= attribute sog { text }?
score = element score { attlist.score, empty }
attlist.score &= attribute period { text }
attlist.score &= attribute goals { text }
attlist.score &= attribute sog { text }?
game = element game { attlist.game, (home, away)* }
attlist.game &= attribute date { text }
attlist.game &= attribute arena { text }
start = hockey
<?php exit(); }
if(isset($_GET['rng']) || (isset($_GET['act']) && $_GET['act']=="rng")) {
header("Content-Type: pplication/relaxng+xml; charset=UTF-8");
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
?>
<grammar xmlns="http://relaxng.org/ns/structure/1.0">
  <define name="hockey">
    <element name="hockey">
      <ref name="attlist.hockey"/>
      <zeroOrMore>
        <ref name="game"/>
      </zeroOrMore>
    </element>
  </define>
  <define name="attlist.hockey" combine="interleave">
    <optional>
      <attribute name="league"/>
    </optional>
  </define>
  <define name="away">
    <element name="away">
      <ref name="attlist.away"/>
      <zeroOrMore>
        <ref name="score"/>
      </zeroOrMore>
    </element>
  </define>
  <define name="attlist.away" combine="interleave">
    <attribute name="team"/>
  </define>
  <define name="attlist.away" combine="interleave">
    <attribute name="goals"/>
  </define>
  <define name="attlist.away" combine="interleave">
    <optional>
      <attribute name="sog"/>
    </optional>
  </define>
  <define name="home">
    <element name="home">
      <ref name="attlist.home"/>
      <zeroOrMore>
        <ref name="score"/>
      </zeroOrMore>
    </element>
  </define>
  <define name="attlist.home" combine="interleave">
    <attribute name="team"/>
  </define>
  <define name="attlist.home" combine="interleave">
    <attribute name="goals"/>
  </define>
  <define name="attlist.home" combine="interleave">
    <optional>
      <attribute name="sog"/>
    </optional>
  </define>
  <define name="score">
    <element name="score">
      <ref name="attlist.score"/>
      <empty/>
    </element>
  </define>
  <define name="attlist.score" combine="interleave">
    <attribute name="period"/>
  </define>
  <define name="attlist.score" combine="interleave">
    <attribute name="goals"/>
  </define>
  <define name="attlist.score" combine="interleave">
    <optional>
      <attribute name="sog"/>
    </optional>
  </define>
  <define name="game">
    <element name="game">
      <ref name="attlist.game"/>
      <zeroOrMore>
        <ref name="home"/>
        <ref name="away"/>
      </zeroOrMore>
    </element>
  </define>
  <define name="attlist.game" combine="interleave">
    <attribute name="date"/>
  </define>
  <define name="attlist.game" combine="interleave">
    <attribute name="arena"/>
  </define>
  <start>
    <choice>
      <ref name="hockey"/>
    </choice>
  </start>
</grammar>
<?php exit(); }
echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n";
echo "<?xml-stylesheet type=\"text/xsl\" href=\"".$fullurl."xml.php?xslt\"?>\n";
echo "<!DOCTYPE hockey SYSTEM \"".$fullurl."xml.php?dtd\">\n";
echo "<hockey league=\"".$leaguename."\">\n\n";
if(!isset($_GET['act'])&&isset($_GET['view'])) { $_GET['act'] = "view"; }
if(!isset($_GET['act'])&&isset($_GET['games'])) { $_GET['act'] = "view"; }
if(!isset($_GET['act'])&&isset($_GET['stats'])) { $_GET['act'] = "stats"; }
if(!isset($_GET['act'])&&isset($_GET['calendar'])) { $_GET['act'] = "calendar"; }
if(isset($_GET['month']) && strlen($_GET['month'])==1) {
 $_GET['month'] = "0".$_GET['month']; }
if(isset($_GET['day']) && strlen($_GET['day'])==1) {
 $_GET['day'] = "0".$_GET['day']; }
if(isset($_GET['date']) && strlen($_GET['date'])==8) {
 $chckyear = substr($_GET['date'], 0, 4);
 $chckmonth = substr($_GET['date'], 4, 2);
 if($chckmonth>12) { $chckmonth = $chckmonth = "12"; }
 if($chckmonth<1) { $chckmonth = $chckmonth = "01"; }
 $chckday = substr($_GET['date'], 6, 2);
 if($chckday>gmdate("t", gmmktime(0, 0, 0, $chckmonth, 1, $chckyear))) { $chckday = gmdate("t", gmmktime(0, 0, 0, $chckmonth, 1, $chckyear)); }
 if($chckday<1) { $chckday = "01"; } 
 $_GET['date'] = $chckyear.$chckmonth.$chckday; }
if(isset($_GET['date']) && strlen($_GET['date'])==6) {
 $chckyear = substr($_GET['date'], 0, 4);
 if($chckmonth>12) { $chckmonth = $chckmonth = "12"; }
 if($chckmonth<1) { $chckmonth = $chckmonth = "01"; }
 $chckmonth = substr($_GET['date'], 4, 2);
 $_GET['date'] = $chckyear.$chckmonth; }
if((isset($_GET['day']) && strlen($_GET['day'])==2)) {
 if((isset($_GET['year']) && strlen($_GET['year'])==4)) {
  if((isset($_GET['month']) && strlen($_GET['month'])==2)) {
   if($_GET['month']>12) { $_GET['month'] = 12; }
   if($_GET['month']<1) { $_GET['month'] = "01"; }
   if($_GET['day']<1) { $_GET['day'] = "01"; }
   if($_GET['day']>gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year']))) { $_GET['day'] = gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year'])); } }
  if((!isset($_GET['month']) || strlen($_GET['month'])!=2)) {
   $_GET['month'] = gmdate("m");
   if($_GET['day']<1) { $_GET['day'] = "01"; }
   if($_GET['day']>gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year']))) { $_GET['day'] = gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year'])); } } }
 if((!isset($_GET['year']) || strlen($_GET['year'])!=4)) {
  if((isset($_GET['month']) && strlen($_GET['month'])==2)) {
   if($_GET['month']>12) { $_GET['month'] = 12; }
   if($_GET['month']<1) { $_GET['month'] = "01"; }
   $_GET['year'] = gmdate("Y");
   if($_GET['day']<1) { $_GET['day'] = "01"; }
   if($_GET['day']>gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year']))) { $_GET['day'] = gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year'])); } }
  if((!isset($_GET['month']) || strlen($_GET['month'])!=2)) {
   if($_GET['month']>12) { $_GET['month'] = 12; }
   if($_GET['month']<1) { $_GET['month'] = "01"; }
   $_GET['year'] = gmdate("Y");
   $_GET['month'] = gmdate("m");
   if($_GET['day']<1) { $_GET['day'] = "01"; }
   if($_GET['day']>gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year']))) { $_GET['day'] = gmdate("t", gmmktime(0, 0, 0, $_GET['month'], 1, $_GET['year'])); } } } }
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
if($_GET['act']!="view" && $_GET['act']!="games" && $_GET['act']!="stats" && $_GET['act']!="calendar") { $_GET['act'] = "view"; }
$sqldb = new SQLite3("../hockey15-16.db3");
$sqldb->exec("PRAGMA encoding = \"UTF-8\";");
$sqldb->exec("PRAGMA auto_vacuum = 1;");
$sqldb->exec("PRAGMA foreign_keys = 1;");
$sqlite_games_string = "";
$firstgamedate = $sqldb->querySingle("SELECT Date FROM ".$leaguename."Games WHERE id=1");
$lastgamedate = $sqldb->querySingle("SELECT Date FROM ".$leaguename."Games WHERE id=(SELECT MAX(id) FROM ".$leaguename."Games)");
if($_GET['act']=="calendar") {
echo "</".strtolower($leaguename).">";
die(1);
if(isset($_GET['date']) && strlen($_GET['date'])==8) {
 if(!isset($_GET['month']) || !is_numeric($_GET['month'])) {
  $_GET['month'] = substr($_GET['date'], 4, 2); }
 if(!isset($_GET['year']) || !is_numeric($_GET['year'])) {
  $_GET['year'] = substr($_GET['date'], 0, 4); } }
if(isset($_GET['date']) && strlen($_GET['date'])==6) {
 if(!isset($_GET['month']) || !is_numeric($_GET['month'])) {
  $_GET['month'] = substr($_GET['date'], 4, 2); }
 if(!isset($_GET['year']) || !is_numeric($_GET['year'])) {
  $_GET['year'] = substr($_GET['date'], 0, 4); } }
if(!isset($_GET['month']) || !is_numeric($_GET['month']) or !strlen($_GET['month'])==2) {
 $_GET['month'] = gmdate("m"); }
if(!isset($_GET['date']) && is_numeric($_GET['month']) && strlen($_GET['month'])==2) {
 if(!isset($_GET['year']) || !is_numeric($_GET['year']) || strlen($_GET['year'])<4) {
  $_GET['year'] = gmdate("Y"); }
 $startday = $_GET['year'].$_GET['month']."01";
 $endday = $_GET['year'].$_GET['month']."31"; }
$curtimestamp = gmmktime(12, 30, 0, intval($_GET['month']), 1, intval($_GET['year']));
$weekdaystart = intval(date("w", $curtimestamp));
$numofdays = intval(date("t", $curtimestamp));
$endtimestamp = gmmktime(12, 30, 0, intval($_GET['month']), $numofdays, intval($_GET['year']));
$weekdayend = intval(date("w", $endtimestamp));
$monthonly = date("F", $curtimestamp);
$yearonly = date("Y", $curtimestamp);
$monthyear = $monthonly." ".$yearonly;
$daycount = 1;
$daynextcount = 1;
echo "  <table style=\"width: 100%;\">\n";
echo "   <tr>\n    <th colspan=\"7\"><a href=\"html.php?games&amp;date=".urlencode(date("Y", $curtimestamp).date("m", $curtimestamp))."\">".$monthyear."</a></th>\n   </tr>\n";
echo "   <tr>\n    <td style=\"width: 14%; font-weight: bold;\">Sunday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Monday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Tuesday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Wednesday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Thursday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Friday</td>\n    <td style=\"width: 14%; font-weight: bold;\">Saturday</td>\n   </tr>\n";
while($daynextcount <= $weekdaystart) {
 if($daynextcount==1) { echo "   <tr>\n"; }
 echo "    <td style=\"width: 14%; height: 100px; vertical-align: top;\">&#xA0;</td>\n";
 $daynextcount += 1; }
while($daycount <= $numofdays) {
 $daycheck = $daycount;
 if(strlen($daycount)==1) { $daycheck = "0".$daycount; }
 $numofgames = 0;
 if($_GET['year'].$_GET['month'].$daycheck>=$firstgamedate && $_GET['year'].$_GET['month'].$daycheck<=$lastgamedate) {
 $prenumofgames = $sqldb->query("SELECT COUNT(*) as count FROM ".$leaguename."Games WHERE Date=".$_GET['year'].$_GET['month'].$daycheck." ORDER BY Date DESC, id DESC");
 $numofgamesarray = $prenumofgames->fetchArray();
 $numofgames = intval($numofgamesarray['count']);
 $gamedaystr = $daycount;
 $numgamesstr = "No Games"; }
 if($_GET['year'].$_GET['month'].$daycheck<$firstgamedate || $_GET['year'].$_GET['month'].$daycheck>$lastgamedate) {
  $gamedaystr = $daycount;
  $numgamesstr = "&#xA0;"; }
 if($_GET['year'].$_GET['month'].$daycheck>=$firstgamedate && $_GET['year'].$_GET['month'].$daycheck<=$lastgamedate) {
 $gamedaystr = "<a href=\"html.php?games&amp;date=".urlencode(date("Y", $curtimestamp).date("m", $curtimestamp).$daycheck)."\">".$daycount."</a>";
 if($numofgames==1) { $numgamesstr = "1 Game"; }
 if($numofgames>1) { $numgamesstr = $numofgames." Games"; } }
 if($daynextcount==1) { echo "   <tr>\n"; }
 echo "    <td style=\"width: 14%; height: 100px; vertical-align: top;\">".$gamedaystr."<br /><br /><div style=\"text-align: center;\">".$numgamesstr."</div></td>\n"; 
 if($daynextcount==7) { echo "   </tr>\n"; $daynextcount = 0; }
 $daynextcount += 1; $daycount += 1; }
if($daynextcount>1) {
while($daynextcount <= 7) {
 if($daynextcount==1) { echo "   <tr>\n"; }
 echo "\n    <td style=\"width: 14%; height: 100px; vertical-align: top;\">&#xA0;</td>";
 if($daynextcount==7) { echo "   </tr>\n"; }
 $daynextcount += 1; } }
echo "  </table>\n"; }
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
  $SelectWhere .= " AND (HomeTeam='".$sqldb->escapeString($_GET['team'])."' OR AwayTeam='".$sqldb->escapeString($_GET['team'])."') "; }
 if($SelectWhereNext==false) {
  $SelectWhere = "WHERE (HomeTeam='".$sqldb->escapeString($_GET['team'])."' OR AwayTeam='".$sqldb->escapeString($_GET['team'])."') ";
  $SelectWhereNext = true; } }
$results = $sqldb->query("SELECT * FROM ".$leaguename."Games ".$SelectWhere."ORDER BY Date DESC, id DESC");
while ($row = $results->fetchArray()) {
    $toneres = $sqldb->querySingle("SELECT CityName, TeamName, FullName FROM ".$leaguename."Teams WHERE FullName='".$sqldb->escapeString($row['HomeTeam'])."'", true);
    $ttwores = $sqldb->querySingle("SELECT CityName, TeamName, FullName FROM ".$leaguename."Teams WHERE FullName='".$sqldb->escapeString($row['AwayTeam'])."'", true);
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlspecialchars($tarenares['ArenaName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\">\n  <home team=\"".htmlspecialchars($toneres['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n  </home>\n  <away team=\"".htmlspecialchars($ttwores['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n  </away>\n </game>\n"; }
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlspecialchars($tarenares['ArenaName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\">\n  <home team=\"".htmlspecialchars($toneres['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[0]."\" sog=\"".$PerTeamSOGFour[0]."\" />\n  </home>\n  <away team=\"".htmlspecialchars($ttwores['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[1]."\" sog=\"".$PerTeamSOGFour[1]."\" />\n  </away>\n </game>\n"; }
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
       $LineOne = " <game date=\"".substr($row['Date'], 4, 2)."/".substr($row['Date'], 6, 2)."/".substr($row['Date'], 0, 4)."\" arena=\"".htmlspecialchars($tarenares['ArenaName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\">\n  <home team=\"".htmlspecialchars($toneres['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[0]."\" sog=\"".$PerTeamSOGTotal[0]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[0]."\" sog=\"".$PerTeamSOGOne[0]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[0]."\" sog=\"".$PerTeamSOGTwo[0]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[0]."\" sog=\"".$PerTeamSOGThree[0]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[0]."\" sog=\"".$PerTeamSOGFour[0]."\" />\n   <score period=\"so\" goals=\"".$PerTeamScoreFive[0]."\" />\n  </home>\n  <away team=\"".htmlspecialchars($ttwores['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."\" goals=\"".$PerTeamScoreTotal[1]."\" sog=\"".$PerTeamSOGTotal[1]."\">\n   <score period=\"1\" goals=\"".$PerTeamScoreOne[1]."\" sog=\"".$PerTeamSOGOne[1]."\" />\n   <score period=\"2\" goals=\"".$PerTeamScoreTwo[1]."\" sog=\"".$PerTeamSOGTwo[1]."\" />\n   <score period=\"3\" goals=\"".$PerTeamScoreThree[1]."\" sog=\"".$PerTeamSOGThree[1]."\" />\n   <score period=\"ot\" goals=\"".$PerTeamScoreFour[1]."\" sog=\"".$PerTeamSOGFour[1]."\" />\n   <score period=\"so\" goals=\"".$PerTeamScoreFive[1]."\" />\n  </away>\n </game>\n"; }
    echo $LineOne."\n"; } }
if($_GET['act']=="stats") {
echo "</".strtolower($leaguename).">";
die(1);
$SelectWhere = "";
$SelectWhereNext = false;
if(isset($_GET['date']) && is_numeric($_GET['date']) && strlen($_GET['date'])==8) {
 $SelectWhere = "WHERE Date<=".$sqldb->escapeString($_GET['date'])." ";
 $SelectWhereNext = true; }
$sqldb->exec("CREATE TEMP TABLE ".$leaguename."Standings AS SELECT * FROM ".$leaguename."Stats ".$SelectWhere." GROUP BY TeamID ORDER BY TeamID ASC, Date DESC");
echo "<table style=\"width: 100%;\">";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#OverallStats\" id=\"OverallStats\">".$leaguename." Team Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlspecialchars($trow['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; }
$conresults = $sqldb->query("SELECT * FROM ".$leaguename."Conferences");
while ($conrow = $conresults->fetchArray()) {
if($_GET['conference']=="All" || $_GET['conference']==$conrow['Conference']) {
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Conference='".$sqldb->escapeString($conrow['Conference'])."' ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#".$conrow['Conference']."ConferenceStats\" id=\"".$conrow['Conference']."ConferenceStats\">".$leaguename." ".$conrow['Conference']." Conference Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlspecialchars($trow['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; } } }
$divresults = $sqldb->query("SELECT * FROM ".$leaguename."Divisions");
while ($divrow = $divresults->fetchArray()) {
if($_GET['division']=="All" || $_GET['division']==$divrow['Division']) {
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n";
$tresults = $sqldb->query("SELECT * FROM ".$leaguename."Standings WHERE Division='".$sqldb->escapeString($divrow['Division'])."' ORDER BY Points DESC, GamesPlayed ASC, Losses ASC, Wins DESC, GoalsDifference DESC");
echo "\n <tr>\n   <th colspan=\"18\"><a href=\"index.php?stats&amp;#".$divrow['Division']."DivisionStats\" id=\"".$divrow['Division']."DivisionStats\">".$leaguename." ".$divrow['Division']." Division Team Stats &amp; Standings</a></th>\n </tr>";
echo "\n <tr>\n   <th colspan=\"2\">Team</th>\n   <th>GP</th>\n   <th>W</th>\n   <th>L</th>\n   <th>OTL</th>\n   <th>SOL</th>\n   <th>P</th>\n   <th>PCT</th>\n   <th>ROW</th>\n   <th>GF</th>\n   <th>GA</th>\n   <th>DIFF</th>\n   <th>Home</th>\n   <th>Away</th>\n   <th>S/O</th>\n   <th>L10</th>\n   <th>Streak</th>\n </tr>";
$teamplace = 1;
while ($trow = $tresults->fetchArray()) {
    if($trow['Shootouts']=="0:0") { $trow['Shootouts'] = "-"; }
    if($trow['GoalsDifference']=="0") { $trow['GoalsDifference'] = "E"; }
    echo "\n <tr>\n   <td style=\"text-align: center;\">".$teamplace."</td>\n   <td style=\"text-align: center;\"><a href=\"?games&amp;date=".urlencode($trow['Date'])."&amp;team=".urlencode($trow['FullName'])."\">".htmlspecialchars($trow['FullName'], ENT_COMPAT | ENT_XML1, "UTF-8")."</a></td>\n   <td style=\"text-align: center;\">".$trow['GamesPlayed']."</td>\n   <td style=\"text-align: center;\">".$trow['TWins']."</td>\n   <td style=\"text-align: center;\">".$trow['Losses']."</td>\n   <td style=\"text-align: center;\">".$trow['OTLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['SOLosses']."</td>\n   <td style=\"text-align: center;\">".$trow['Points']."</td>\n   <td style=\"text-align: center;\">".number_format($trow['PCT'], 3)."</td>\n   <td style=\"text-align: center;\">".$trow['ROW']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsFor']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsAgainst']."</td>\n   <td style=\"text-align: center;\">".$trow['GoalsDifference']."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['HomeRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['AwayRecord'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['Shootouts'])."</td>\n   <td style=\"text-align: center;\">".str_replace(":", "-", $trow['LastTen'])."</td>\n   <td style=\"text-align: center;\">".$trow['Streak']."</td>\n </tr>"; $teamplace += 1; } } }
echo " <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n <tr>\n   <td colspan=\"18\" style=\"text-align: center;\">&#xA0;</td>\n </tr>\n";
echo "\n</table>\n<div>&#xA0;<br />&#xA0;</div>\n\n"; }
echo "</hockey>";
?>
