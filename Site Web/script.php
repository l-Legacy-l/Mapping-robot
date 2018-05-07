<?php
error_reporting(E_ALL);
ini_set('display_errors','on');

session_start();

/*
ini_set("display_errors", 1);
ini_set("track_errors", 1);
ini_set("html_errors", 1);
error_reporting(E_ALL);
*
exec("/usr/bin/python -c 'print test'", $mavar);


echo"jepasse";

echo "<script type ='text/javascript'>document.location.replace('Cartographie.php');</script>"

 */
if($_SESSION['password'])
{
$command=escapeshellcmd('/usr/bin/python /var/www/html/mapper.py'.' '.$_SESSION['login'].' '.$_POST['piece']);
$output=shell_exec($command);
echo $output;
$_SESSION['piece'] = $_POST['piece'];

require('insereCartographie.php');
/*require('lireCartographie.php');*/
/*echo "<script type='text/javascript'>document.location.replace('insereCartographie.php');</script>";*/
/*echo "<script type='text/javascript'>document.location.replace('Cartographie.php');</script>";*/
/*echo "<script type='text/javascript'>document.location.replace('lireCartographie.php');</script>";*/
header('Location:Cartographie.php');


}

else
{
	echo "<script type='text/javascript'>document.location.replace('index.php');</script>";
}

/*
$result=exec("/usr/bin/python /home/testPython/test.py /tmp");
$result_array=json_decode($result);
foreach($result_array as $row){
	echo $row."<br>";i
*/

?>

