<?php 
    $server = "localhost";
    $user = "root";
    $password = "";
    $database = "phpDatabase";

    $conn = mysqli_connect($server, $user, $password, $database);

    if ($conn == false) {
        die("Connection failed");
    }

    $forename = $_POST['forename'];	
    $surname = $_POST['surname'];
    $comment = $_POST['comment'];

    $sql = "INSERT INTO Comment (forename, surname, comment) VALUES ('$forename', '$surname', '$comment')";

    if (mysqli_query($conn, $sql)) {
        echo "comment posted";
    } else {
        echo "comment not posted";
    }
    mysqli_close($conn);
?>

