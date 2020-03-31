<?php

$servername = "localhost" ;
$username = "id6317479_kshama_singh" ;
$password1 = "Kshama@321" ;
$database = "id6317479_iot" ;


$rfid = $_REQUEST["RFID"];
$amount=$_REQUEST["Amount"];
if(isset($rfid)&&isset($amount))
{

// create connection

$con =new mysqli($servername,$username,$password1,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "update REGISTER  set Amount='$amount' where RFID='$rfid'";
if($con->query($query)==TRUE)
{
	die("success");
}
else
{
	die("failed");
}
}
else
{
die("status or id is not set");	
}
?>