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

    $sql = "DELETE FROM Fridge WHERE id = $id";

    if (mysqli_query($conn, $sql)) {
        echo "Item removed";
    } else {
        echo "error";
    }
    
    mysqli_close($conn);
?> 