<?php
//Déconnexion + redirection vers la page de connexion
session_start();
session_destroy();
echo "<script type='text/javascript'>document.location.replace('Connexion.php');</script>";
?>