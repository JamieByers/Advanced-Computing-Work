<html>

    <head>
        <title>Form</title>
    </head>

    <body>
        
        <form action="form.php">

            Forename: <br>
            <input type="text" name="forename" id=""> <br> <br>
            Surname: <br>
            <input type="text" name="surname" id=""> <br> <br>
            Comment: <br>
            <textarea name="comment" id=""></textarea>

            <input type="submit" value="Submit Form">
        </form>


        <?php 

            $forename = $_GET['forename'];
            $surname = $_GET['surname'];
            $comment = $_GET['comment'];

            echo "$forename, $surname, $comment";

        ?>

    </body>

</html>