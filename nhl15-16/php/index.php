<?php
if(!ob_start("ob_gzhandler")) { ob_start(); }
header("Content-Language: en");
header("Vary: Accept-Encoding");
header("Date: ".gmdate("D, d M Y H:i:s")." GMT");
header("Last-Modified: ".gmdate("D, d M Y H:i:s")." GMT");
header("Expires: ".gmdate("D, d M Y H:i:s")." GMT");
$fullurl = "http://localhost/hockey/nhl/";
if(isset($_SERVER['HTTPS'])) {
 $fullurl = "https://".$_SERVER["SERVER_NAME"].str_replace("//", "/", dirname($_SERVER["SCRIPT_NAME"])."/"); } 
if(!isset($_SERVER['HTTPS'])) {
 $fullurl = "http://".$_SERVER["SERVER_NAME"].str_replace("//", "/", dirname($_SERVER["SCRIPT_NAME"])."/"); }
if(!isset($_GET['output'])) { 
 if(isset($_GET['html'])) { 
    $_GET['output'] = "html"; }
 if(!isset($_GET['html']) && isset($_GET['xhtml'])) { 
    $_GET['output'] = "xhtml"; }
 if(isset($_GET['html'])) { 
    $_GET['output'] = "html"; }
 if(!isset($_GET['html']) && !isset($_GET['xhtml']) && isset($_GET['xml'])) { 
    $_GET['output'] = "xml"; } }
if(!isset($_GET['output'])) { 
    $_GET['output'] = "html"; }
if($_GET['output']!="html" && $_GET['output']!="xhtml" && $_GET['output']!="xml") { 
   $_GET['output'] = "html"; }
if($_GET['output']=="html") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 if(isset($_GET['xhtml'])) { unset($_GET['xhtml']); }
 $qstring = http_build_query($_GET);
 if(strlen($qstring)==0) {
  header("Location: ".$fullurl."html.php", true, 303); }
 if(strlen($qstring)>0) {
  header("Location: ".$fullurl."html.php?".$qstring, true, 303); } }
if($_GET['output']=="xhtml") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 if(isset($_GET['xhtml'])) { unset($_GET['xhtml']); }
 $qstring = http_build_query($_GET);
 if(strlen($qstring)==0) {
  header("Location: ".$fullurl."xhtml.php", true, 303); }
 if(strlen($qstring)>0) {
  header("Location: ".$fullurl."xhtml.php?".$qstring, true, 303); } }
if($_GET['output']=="xml") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 if(isset($_GET['xhtml'])) { unset($_GET['xhtml']); }
 $qstring = http_build_query($_GET);
 if(strlen($qstring)==0) {
  header("Location: ".$fullurl."xml.php", true, 303); }
 if(strlen($qstring)>0) {
  header("Location: ".$fullurl."xml.php?".$qstring, true, 303); } }
?>