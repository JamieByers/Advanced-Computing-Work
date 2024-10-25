<?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $database = "phpDatabase";

    $conn = mysqli_connect($server, $username, $password, $database);

	if ($conn == false) {
		die("conn failed");
	}
	
    $sql = "SELECT * FROM Fridge";

    $result = mysqli_query($conn, $sql);

    $rows = mysqli_num_rows($result);

    if ($rows > 0) {
        echo"Number of fridge items: $rows";

        echo"<form action='delete_confirm.php' method='post'>";
        echo"<select name='id'>";
        while ($row = mysqli_fetch_array($result)) {
            echo"<option value=" . $row['id'] . ">" . $row['item'] . "</option>";
        }

        echo "</select> <br>";
        echo "<input type='submit' value='Remove Item'> ";
        echo "</form>";
    }
    else {
        echo "The fridge is empty";
    }

    mysqli_close($conn);
?>