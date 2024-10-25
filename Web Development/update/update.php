<?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $database = "phpDatabase";

    $conn = mysqli_connect($server, $username, $password, $database);

	if ($conn == false) {
		die("conn failed");
	}

    $id = $_POST['id'];
    $newPrice = $_POST['newPrice'];

    $sql = "UPDATE Product
            SET price='$newPrice'
            WHERE id='$id'";

    $result = mysqli_query($conn, $sql);

    if (mysqli_affected_rows($conn) > 0) {
        echo "update the price of product $id is now £$newPrice. <br>";
    } else {
        echo "failed";
    }
?>