<?php
session_start();
try
{
    //On va récupérer les cartographie faites par l'utilisateur connecté
    $bdd = new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8', 'root', 'rasp789456');
    $req= $bdd ->prepare('SELECT * FROM data WHERE login = :login');
    $req->execute(array('login' => $_SESSION['login']));

    $donnees = $req -> fetchAll();
    $_SESSION['resultat'] = $donnees;
    /*On enregistre les nombres de lignes retourné par la requêtes pour déterminer le nombre de cartographie
    qu'on a réalisé*/
    $_SESSION['count'] = $req -> rowCount();
    
   
}

catch(Exception $e)
{
	echo "erreur connection BD";
}
?>
