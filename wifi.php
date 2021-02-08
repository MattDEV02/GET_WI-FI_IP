<?php 

$key = 'wifi';
$cond = ((!empty($_POST)) && (isset($_POST[$key])));
if($cond) {
   $data = $_POST[$key];
   $arr = json_decode($data);
   $str = json_encode($arr,JSON_PRETTY_PRINT);
   $json = ('<pre>'.$str.'</pre>');
   $file = fopen('wifi.html', 'w') or die('Unable to open file!');
   fwrite($file, $json) or die('Unable to write file!');
   fclose($file) or die('Unable to close file!');
} else echo 'No WLAN checked.';

?>
