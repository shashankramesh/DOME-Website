<?php 
	
	$variable1 = 200;
	$variable2 = 1;
	$variable3 = 30;
	$variable4 = 4;
	$variable5 = 8;
	$variable6 = "SI";
	$variable7 = "Uniform";
	$variable8 = "Uniform";
	$variable9 = 10;
	$variable10 = 30;
	$variable11 = "CommercialEnclosed"; #See
	$variable12 = 1;
	$variable13 = 1;
	$variable14 = "Uncrowned";
	$variable15 = 3;
	$variable16 = "External";
	$variable17 = 20;
	$variable18 = "Steel";
	$variable19 = "Steel";
	$variable20 = 0.9;
	$variable21 = 200;
	$variable22 = 200;
	$variable23 = 100000000;
	$variable24 = 200;
	$variable25 = "HS";
	$variable26 = "g1";
		

	$command = escapeshellcmd("python /home/shashankr/Shashank/python/dome_code/Main.py $variable1 $variable2 $variable3 $variable4 $variable5 $variable6 $variable7 $variable8 $variable9 $variable10 $variable11 $variable12 $variable13 $variable14 $variable15 $variable16 $variable17 $variable18 $variable19 $variable20 $variable21 $variable22 $variable23 $variable24 $variable25 $variable26");
    $output = exec($command, $err);
    $json_arr = json_decode($output, true);
    var_dump($output);
    var_dump($err);
 ?>