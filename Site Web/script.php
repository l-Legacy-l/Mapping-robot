<?php
session_start();
/*
ini_set('display_errors','on');
error_reporting(E_ALL);

exec('sudo -S python /home/pi/testPython/test.py 2>/dev/null >/dev/null &');
die("ok");
 */
if ($_SESSION['password'])
{

	$command = escapeshellcmd('/home/pi/testPython/test.py');
	$output = shell_exec($command);
	echo $output;
}

else
{
	echo "<script type='text/javascript'>document.location.replace('index.php');</script>";	
}

?>
