<?php

    $server = "localhost";
    $username = "root";
    $password = "";
    $database = "phpDatabase";

    $conn = mysqli_connect($server, $username, $password, $database);

	if ($conn == false) {
		die("conn failed");
	}
	
    $month = $_POST['month'];

    $sql = "SELECT * FROM birthday WHERE birthday LIKE '____-$month-__'";

    $result = mysqli_query($conn, $sql);
	
    $rows = mysqli_num_rows($result);

    if ($rows > 0) {
        echo"number of results: $rows";

        echo"<table border=1> <tr> <th>Name</th> <th>Birthday</th> </tr>";
        
        while ($row = mysqli_fetch_array($result)) {
            echo"<tr><td>" . $row['name'] . "</td> <td> " . $row['birthday'] . "</td></tr>";
        }
        
        echo "</table>";
    } else {
        echo "No results";
    }

?>