<?php

$servername = "localhost" ;
$username = "id6317479_kshama_singh" ;
$password1 = "Kshama@321" ;
$database = "id6317479_iot" ;

$rfid = $_REQUEST["RFID"];
// create connection

$con =new mysqli($servername,$username,$password1,$database);

if($con->connect_error)
{
	die("Connection Error");
}

$query = "select * from REGISTER where RFID='$rfid'";
	
$result = $con->query($query);

if($result->num_rows>0)
{
	
	 while($row = $result->fetch_assoc()) {
        
	 $temp = ($row["PASSWORD"]);
			 
    }
	
	die($temp);
}
else
{
	die("failed");
}


?>