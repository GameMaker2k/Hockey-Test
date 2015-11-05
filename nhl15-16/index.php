<?php
ob_start("ob_gzhandler");
if(!isset($_GET['output'])) { 
    $_GET['output'] = "html"; }
if($_GET['output']!="html" && $_GET['output']!="xml") { 
   $_GET['output'] = "html"; }
if($_GET['output']=="html") {
 $tmpquery = str_replace("?output=html", "?", $_SERVER['QUERY_STRING']);
 $tmpquery = str_replace("&output=html", "", $tmpquery);
 header("Location: ./html.php?".$tmpquery); }
if($_GET['output']=="xml") {
 $tmpquery = str_replace("?output=xml", "?", $_SERVER['QUERY_STRING']);
 $tmpquery = str_replace("&output=xml", "", $tmpquery);
 header("Location: ./xml.php?".$tmpquery); }
?>