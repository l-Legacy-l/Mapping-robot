<?php
session_start();

//Si on bien indiqué une pièce dans le formulaire
if(!empty($_SESSION["piece"]))
{
    try
    {
        //Chemin pour aller stocker le svg de la cartograpie
        $GLOBALS['image'] = $_SESSION['login'].'/'.$_SESSION['piece'].'.svg' ;
        //Connexion à la BDD + ajout des informations dans celle-ci
        $bd=new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8','root','rasp789456');
        $req = $bd -> prepare('INSERT INTO data VALUES (:login,:piece,:image)');
    	$req -> execute(array('login' => $_SESSION['login'],'piece' => $_SESSION['piece'],'image' => $GLOBALS['image']));
    
        //On stocke l'image pour pouvoir l'afficher dans cartographie.php
	    $_SESSION['image'] = $GLOBALS['image'];	
	
    }	

    catch(Exception $e)
    {
        echo "erreur connexion a a DB";
    }
}

?>
