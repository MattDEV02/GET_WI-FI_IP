<?php 

$ip = 
	getenv('HTTP_CLIENT_IP') ?:
	getenv('HTTP_X_FORWARDED_FOR') ?:
	getenv('HTTP_X_FORWARDED') ?:
	getenv('HTTP_FORWARDED_FOR') ?:
	getenv('HTTP_FORWARDED') ?:
	getenv('REMOTE_ADDR');
    
$base = "http://ip-api.com/json/";
$url = "$base/$ip";

$str = file_get_contents($url) or die('Unable to make Request');
$arr = json_decode($str);
$json = json_encode($arr,JSON_PRETTY_PRINT);
$body = ('<pre>'.$json.'</pre>');

$file = fopen('ip.html', 'w') or die('Unable to open file!');
fwrite($file, $body) or die('Unable to write file!');
fclose($file) or die('Unable to close file!');

?>
