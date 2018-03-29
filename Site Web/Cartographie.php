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
            <?php

            session_start();

            $_SESSION['login'] = $_POST['login'];
            $mdp = sha1($_POST['password']);
            setcookie('pseudo', $_SESSION['login'], time() + 365*24*3600, null, null, false, true);
           
            try
            {
            
                $bdd = new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8', 'root', 'rasp789456');

                $req= $bdd ->prepare('SELECT login,password FROM users WHERE login = :login && password = :password');
                $req->execute(array('login' => $_SESSION['login'], 'password' => $mdp));
                $donnees = $req->fetch();

                if(!empty($donnees))
                {
			echo 'Vous êtes connecté !';
			$_SESSION['password'] = $mdp;
                ?>
                
                
                <?php
                }

                else
                {
                    session_destroy();
                    echo "<script type='text/javascript'>document.location.replace('index.php');</script>";                 
                }
            }

            catch (Exception $e) 
            {
                echo 'Erreur de connexion à la BD '.$e;
            }
             ?>
       
            </p>
        </div>
        <h1>Connexion au Raspberry Pi</h1>
        <div id="img">
            <img src="Images/logo.gif" >
	</div>
	<a href="script.php">Cliquer pour lancer le script</a>
    </body>
</html>
