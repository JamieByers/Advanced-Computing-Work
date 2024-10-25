<?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $database = "phpDatabase";

    $conn = mysqli_connect($server, $username, $password, $database);

	if ($conn == false) {
		die("conn failed");
	}
	
    $sql = "";

    $result = mysqli_query($conn, $sql);
?>