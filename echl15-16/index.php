<?php
ob_start("ob_gzhandler");
if(!isset($_GET['output'])) { 
 if(isset($_GET['html'])) { 
    $_GET['output'] = "html"; }
 if(!isset($_GET['html']) && isset($_GET['xml'])) { 
    $_GET['output'] = "xml"; } }
if(!isset($_GET['output'])) { 
    $_GET['output'] = "html"; }
if($_GET['output']!="html" && $_GET['output']!="xml") { 
   $_GET['output'] = "html"; }
if($_GET['output']=="html") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 header("Location: ./html.php?".http_build_query($_GET)); }
if($_GET['output']=="xml") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 header("Location: ./xml.php?".http_build_query($_GET)); }
?>