<?php 

    session_start();

    $_SESSION['forename'] = $_POST['forename'];
    $_SESSION['surname'] = $_POST['surname'];
    $_SESSION['animal'] = $_POST['animal'];

    echo "Hi " . $_SESSION['forename'] . ''. $_SESSION['surname'] .'your favourite animal is '. $_SESSION['animal'];
    
?>