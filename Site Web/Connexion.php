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
                //On enregistre la session
                $_SESSION['login'] = $_POST['login'];
                //Chiffrement du mdp
                $mdp = sha1($_POST['password']);
                setcookie('pseudo', $_SESSION['login'], time() + 365*24*3600, null, null, false, true);
            
                try
                {
                    //On se connecte à la BDD et on check si les données entrées dans le formulaire sont conforment à ceux de la BDD           
                    $bdd = new PDO('mysql:host=localhost;dbname=raspberrypi;charset=utf8', 'root', 'rasp789456');
                    $req= $bdd ->prepare('SELECT login,password FROM users WHERE login = :login && password = :password');
                    $req->execute(array('login' => $_SESSION['login'], 'password' => $mdp));
                    $donnees = $req->fetch();
                    
                    //Si la requête a bien retourné une correspondance alors on est connecté
                    if(!empty($donnees))
                    {
                        echo 'Vous êtes connecté !';
                        $_SESSION['password']=$mdp;

                        //On est connecté, ont peut donc accéder à l'interface de la cartographie, on fait une redirection
                        echo "<script type='text/javascript'>document.location.replace('Cartographie.php');</script>";
                    ?>
                                
                    <?php
                    }
                    
                    //Aucune correspondance, mauvais login/mot de passe
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
       
            
        </div>
