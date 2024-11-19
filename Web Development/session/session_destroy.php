<?php

    session_start();

    session_destroy();

    echo"session ended";

    echo "click <a href='session_message.php'>Session message</a> to check if your session variables are still loadaed";
    echo "Click <a href='session.php'>Session</a> to go back and create a new session";

?>