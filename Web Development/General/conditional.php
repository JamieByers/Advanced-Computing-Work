<html>

    <head>
        <title>Variables</title>
    </head>

    <body>
        
        <?php 

            $hour = date("H");
            if ($hour < 12) {
                echo "Good morning";
            } else if ($hour <= 17 ) {
                echo "Good Afternoon";
            } else {
                echo "Good evening";
            } 

        ?>

    </body>

</html>