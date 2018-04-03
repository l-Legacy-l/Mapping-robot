<?php
session_start();


if(!empty($_SESSION["piece"]))
{
    try
    {
	    /*$GLOBALS['img'] = '/var/www/html/'.$_SESSION['login'].'/'.$_SESSION['pièce'];*/
	$GLOBALS['image'] = $_SESSION['login'].'/'.$_SESSION['piece'].'.svg' ;
        $bd=new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8','root','rasp789456');
        $req = $bd -> prepare('INSERT INTO data VALUES (:login,:piece,:image)');
    	$req -> execute(array('login' => $_SESSION['login'],'piece' => $_SESSION['piece'],'image' => $GLOBALS['image']));
	
	$_SESSION['image'] = $GLOBALS['image'];	
	
    }	

    catch(Exception $e)
    {
        echo "erreur connexion a a DB";
    }
}

?>
