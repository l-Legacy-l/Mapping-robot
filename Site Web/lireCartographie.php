<?php
session_start();
try
{
    $bdd = new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8', 'root', 'rasp789456');
    $req= $bdd ->prepare('SELECT * FROM data WHERE login = :login');
    $req->execute(array('login' => $_SESSION['login']));

    $donnees = $req -> fetchAll();
 
    $_SESSION['resultat'] = $donnees;
    $_SESSION['count'] = $req -> rowCount();
    
   
}

catch(Exception $e)
{
	echo "erreur connection BD";
}
?>
