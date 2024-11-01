<?php

    session_start();

    session_destroy();

    echo"session ended";

    echo "click <a href='session_message.php'>Session message</a>";
    echo "Click <a href='session.php'>Session</a>";

?>