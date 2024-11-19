<?php 

    session_start();

    if ($_SESSION['animal'] == 'dog') {
        echo'great choice';
    } elseif ($_SESSION['animal'] == 'cat') {
        echo 'bad choice';
    } else {
        echo 'i dont know that animal';
    }

    echo'Click to <a href="session_destroy.php"> End session </a>';
?>