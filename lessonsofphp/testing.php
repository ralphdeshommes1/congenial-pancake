<!doctype html>

<title> Home Page</title>
<html>
<form action="testing.php" method="post">
    <input type="text" name="username" value="username">
    <input type="text" name="password" value="password">
</form>

<body>
    <h1> this is the best website in the world</h1>
</body>

</html>

<?php 

if(isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    
    echo $username;
    echo $password;}