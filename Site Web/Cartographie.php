<!DOCTYPE html>
<html>
    <head>
        <title>Raspberry Pi</title>
        <link rel="stylesheet" href="Style.css"/>
    </head>
    <body>
        <div id="header">
            <a href="Logout.php">Se déconnecter</a>
            </br>
        </div>
        <h1>Connexion au Raspberry Pi</h1>
        <div id="img">
            <img src="Images/logo.gif" >
		</div>

		<div id="div_script">
		<!--Formulaire pour le lancement du script pour cartographier-->
		<form method='POST' action = "script.php"> Votre pièce: <input  type = "text" name="piece" required />
		</br>
		<input type="submit" id="submit" value="Lancer le script">
		</form>

		<!--Formulaire pour le lancement du script pour arrêter la cartographie-->
		<form action="stopScript.php" method="POST">
			<input type="submit" id="submit1" value="Arrêter le robot">
		</form> 
		</div>
    </body>

<?php
	session_start();
		//Si on est connecté
		if(!empty($_SESSION['password']))
		{	
			//On vérifie si on a une cartographie
			require("lireCartographie.php"); 			
			$nbLigne = $_SESSION['count'];
			$i=0;
			$j = 0;	
				for ($i = 0; $i < $nbLigne; $i++)
				{
					for($j = 0; $j < 3 ; $j++)
					{
						//Tout les 3 èmes ligne on affiche le svg
						if($j != 2)
						{
							echo "<p>".$_SESSION[resultat][$i][$j]."</p>" ;
						}
						else
						{
							echo "<div id='svg'> <img src='".$_SESSION[resultat][$i][$j]."' > </div>";	
						}
					}

					echo '<br>';
				}
		}

		else
		{
			//Redirection vers la page de connexion si est sur cette page dans être connecté
			header('Location: Connexion.php');
		}
?>

</html>




