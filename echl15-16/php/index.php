<?php
if(!ob_start("ob_gzhandler")) { ob_start(); }
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
 header("Location: ./html.php?".http_build_query($_GET), true, 303); }
if($_GET['output']=="xhtml") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 if(isset($_GET['xhtml'])) { unset($_GET['xhtml']); }
 header("Location: ./xhtml.php?".http_build_query($_GET), true, 303); }
if($_GET['output']=="xml") {
 if(isset($_GET['output'])) { unset($_GET['output']); }
 if(isset($_GET['xml'])) { unset($_GET['xml']); }
 if(isset($_GET['html'])) { unset($_GET['html']); }
 if(isset($_GET['xhtml'])) { unset($_GET['xhtml']); }
 header("Location: ./xml.php?".http_build_query($_GET), true, 303); }
?>