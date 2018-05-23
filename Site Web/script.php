<?php
//Pour afficher les éventuelles erreurs php
error_reporting(E_ALL);
ini_set('display_errors','on');

session_start();
//Si on est connecté
if($_SESSION['password'])
{
	//Exécution du script Python pour démarrer une cartographie
	$command=escapeshellcmd('/usr/bin/python /var/www/html/mapper.py'.' '.$_SESSION['login'].' '.$_POST['piece']);
	$output=shell_exec($command);
	echo $output;
	$_SESSION['piece'] = $_POST['piece'];
	//A cette instruction, la cartographie est terminé --> ajoute les infos de la cartograpie dans la BDD
	require('insereCartographie.php');
	//Redirection pour visualiser la cartographie
	header('Location:Cartographie.php');
}

//On est pas connecté, redirection
else
{
	echo "<script type='text/javascript'>document.location.replace('index.php');</script>";
}

?>

