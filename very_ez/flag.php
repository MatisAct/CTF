<html>
<head>
    <title>check flag! ! !</title>
    <meta charset="utf-8">
</head>
<body>
<h2>éc éc éc tôi get get bạn</h2>

<?php
    require('ketnoi.php');

    if (isset($_GET['flag']))
        $code = $_GET['flag'];
    else
        die('looking for now ! !');

    $sql = "SELECT * FROM `member` where username = '$flag'";

$result = mysqli_query($conn, $sql);

if(!$result) {
    die('Query error: [' . $link->error . ']');
}
$row = mysqli_fetch_array($result, MYSQLI_ASSOC);

if (!$row)
    die('điều quan trọng là anh kia cặp với chị này  ! !  nghĩa là 1 cộng 1 ');
else
    echo $row['fullname'];
?>

</body>
</html>
