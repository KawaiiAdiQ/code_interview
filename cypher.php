<?php

function print_help(){
    echo "Usage:\n";
    echo "a) php cypher.php YOUR_INT [OPTION] < YOUR_FILE_TO_ENCRYPT\n";
    echo "b) php cypher.php YOUR_SOURCE_CHAR YOUR_DESTINATION_CHAR [OPTION] < YOUR_FILE_TO_ENCRYPT\n";
    echo "[OPTION]:\n";
    echo "-h --help\n";
    echo "   prints usage (this).\n\n";
    echo "-f --force-overwrite\n";
    echo "   if destination file exists, overwrites it.\n";
    die();
}

function recommend_help(){
    echo "Bad arguments.\n";
    echo "Type: \"php cypher.php -h\" for help.\n";
    die();
}

function c_cypher($n, $overwrite){
    $n %= 26;
    if(file_exists("zasifrovana(". $n .").txt") && !$overwrite){
        echo "File already exists. If you want to overwrite, run the command with --force-overwrite or -f\n";
        die();
    }
    try{
        $out_file = fopen("zasifrovana(". $n .").txt", "w");
        if(! $out_file){
            throw new Exception();
        }
        $input = fopen('php://stdin', 'r');
        while($line = fgets($input)){
            $result = "";
            $chars = str_split($line);
            foreach($chars as $char){
                if (ord($char) >= ord('a') && ord($char) <= ord('z')){
                    $result .= chr((ord($char) + $n - ord('a')) % 26 + ord('a'));
                }
                else if(ord($char) >= ord('A') && ord($char) <= ord('Z')){
                    $result .= chr((ord($char) + $n - ord('A')) % 26 + ord('A'));
                }
                else{
                    $result .= $char;
                }
            }
            echo $result;
            fwrite($out_file, $result);
        }
    }
    catch(Exception $e){
        echo "Error has occured.\n";
        die();
    }
    finally{
        fclose($out_file);
    }
}
//echo count($argv);
if(count($argv) < 2 || count($argv) > 4){
    recommend_help();
}

$overwrite = false;
foreach($argv as $arg){
    //echo $arg;
    //echo "\n";
    if($arg == "-h" || $arg == "--help"){
        print_help();
    }
    if($arg == "-f" || $arg == "--force-overwrite"){
        $overwrite = true;
    }
}

$n = 0;
if(is_numeric($argv[1])){
    $n = intval($argv[1]);
}
else if(count($argv) > 2){
    if(strlen($argv[1]) != 1 || strlen($argv[2]) != 1){
        recommend_help();
    }
    if(!ctype_alpha($argv[1]) || !ctype_alpha($argv[2])){
        recommend_help();
    }
    $n = ord(strtolower($argv[2])) - ord(strtolower($argv[1]));
}
else{
    recommend_help();
}

c_cypher($n, $overwrite);

?>