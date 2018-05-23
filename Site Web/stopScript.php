<?php
session_start();
//Pour voir les erreurs 
ini_set('display_errors','on');
error_reporting(E_ALL);

//Si on est connecté
if($_SESSION['password'])
{
	//Execution de commande pour arrêter le robot
	$command=escapeshellcmd('/usr/bin/python /var/www/html/stop.py && /usr/bin/sudo /usr/bin/killall python && /usr/bin/python /var/www/html/stop.py');
	$output=shell_exec($command);
	echo $output;	
}

//Redirection pour afficher sa/ses cartographies
echo "<script type='text/javascript'>document.location.replace('Cartographie.php');</script>";

?>

