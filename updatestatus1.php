<?php

$servername = "localhost" ;
$username = "id6317479_kshama_singh" ;
$password1 = "Kshama@321" ;
$database = "id6317479_iot" ;


$NAME = $_REQUEST["NAME"];
$PASSWORD = $_REQUEST["PASSWORD"];
$PHONE_NUMBER = $_REQUEST["PHONE_NUMBER"];
$address = $_REQUEST["ADDRESS"];
$amount = $_REQUEST["Amount"];
$rfid = $_REQUEST["RFID"];

if(isset($NAME)&&isset($PASSWORD)&&isset($PHONE_NUMBER)&&isset($address)&&isset($amount)&&isset($rfid))
{

// create connection

$con =new mysqli($servername,$username,$password1,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "insert into REGISTER (NAME,PASSWORD,PHONE_NUMBER,ADDRESS,Amount,RFID) values('$NAME','$PASSWORD','$PHONE_NUMBER','$address','$amount','$rfid')";
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
die("something is not set");	
}
?>