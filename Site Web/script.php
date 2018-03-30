<?php
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
$command=escapeshellcmd('/usr/bin/python /home/pi/piconzero/test.py');
$output=shell_exec($command);
echo $output;
/*echo "<script type='text/javascript'>document.location.replace('Cartographie.php');</script>";*/
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

