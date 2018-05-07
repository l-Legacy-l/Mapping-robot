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
    <form method='POST' action = "script.php"> Votre pièce: <input  type = "text" name="piece" required />
</br>
	<input type="submit" id="submit" value="Lancer le script">
</form>
	<form action="stopScript.php" method="POST">
		<input type="submit" id="submit1" value="Arrêter le robot">
	</form> 
	</div>
    </body>

<?php
session_start();

if(!empty($_SESSION['password']))
{
	
	 require("lireCartographie.php"); 

	 /*if($_SESSION['count'] >=1)*/
	{
			
	$nbLigne = $_SESSION['count'];
	$i=0;
	$j = 0;

	
		
		for ($i = 0; $i < $nbLigne; $i++)
		{
			for($j = 0; $j < 3 ; $j++)
			{
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
		

}

?>

</html>




