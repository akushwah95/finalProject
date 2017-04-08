<?php

$command = escapeshellcmd('/home/lohit/Documents/projectwork-master/src/files/examples/example_search.py');
$output = shell_exec($command);
echo $output;

?>
