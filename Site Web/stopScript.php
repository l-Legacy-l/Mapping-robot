<?php
session_start();

ini_set('display_errors','on');
error_reporting(E_ALL);

if($_SESSION['password'])
{
	$command=escapeshellcmd('/usr/bin/python /var/www/html/stop.py && /usr/bin/sudo /usr/bin/killall python && /usr/bin/python /var/www/html/stop.py');
	$output=shell_exec($command);
	echo $output;
	
}

echo "<script type='text/javascript'>document.location.replace('Cartographie.php');</script>";

?>

