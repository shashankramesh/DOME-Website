<?php 

/* Form validation */
$variable1 = 100;
$variable2 = 1;
$variable3 = 16;
$variable4 = 1;
$variable5 = 8;
$variable7 = '';
$variable8 = '';
$variable9 = 15;
$variable10 = 17;
$variable11 = '';
$variable12 = $variable13 = 1;
$variable14 = '';
$variable15 = 1;
$variable16 = '';
$variable17 = 20;
$variable18 = '';
$variable19 = '';
$variable20 = 0.9;
$variable21 = $variable22 = 200;
$variable23 = 100000000;
$variable24 = 200;
$variable25 = $variable26 = '';

	
$error_log = '';
$error = ['variable1' =>'','variable2'=>'','variable3'=>''];
$result = '';
$show_result = 0;
$Units = 'SI';
$US_Units = ["Velocity"=>"ft/min", "Force"=>"lbf", "stress"=>"kpsi", "length"=>"inch", "Torque"=>"lb-inch", "Omega"=>"rpm", "angle"=>"deg"];
$SI_Units = ["Velocity"=>"m/s", "Force"=>"N", "stress"=>"MPa", "length"=>"mm", "Torque"=>"Nm", "Omega"=>"rpm", "angle"=>"deg"];

if($_SERVER["REQUEST_METHOD"] == "POST"){
	if(empty($_POST['Units'])){
		$error['Units'] = "Enter units";
	}
	else{
		$Units = $_POST['Units'];
	}
}

if(isset($_POST['submit'])){

	if(empty($_POST['variable1'])){
		$error['variable1'] =  "A variable is required";
	}
	else{
		$variable1 = $_POST['variable1'];
	}

	if(empty($_POST['variable2'])){
		$error['variable2'] =  "A variable is required";
	}
	else{
		$variable2 = $_POST['variable2'];
	}

	if(empty($_POST['variable3'])){
		$error['variable3'] =  "A variable is required";
	}
	else{
		$variable3 = $_POST['variable3'];
	}

	if(empty($_POST['variable4'])){
		$error['variable4'] =  "A variable is required";
	}
	else{
		$variable4 = $_POST['variable4'];
	}

	if(empty($_POST['variable5'])){
		$error['variable5'] =  "A variable is required";
	}
	else{
		$variable5 = $_POST['variable5'];
	}

	if(empty($_POST['variable6'])){
		$error['variable6'] =  "A variable is required";
	}
	else{
		$variable6 = $_POST['variable6'];
	}

	if(empty($_POST['variable7'])){
		$error['variable7'] =  "A variable is required";
	}
	else{
		$variable7 = $_POST['variable7'];
	}

	if(empty($_POST['variable8'])){
		$error['variable8'] =  "A variable is required";
	}
	else{
		$variable8 = $_POST['variable8'];
	}

	if(empty($_POST['variable9'])){
		$error['variable9'] =  "A variable is required";
	}
	else{
		$variable9 = $_POST['variable9'];
	}

	if(empty($_POST['variable10'])){
		$error['variable10'] =  "A variable is required";
	}
	else{
		$variable10 = $_POST['variable10'];
	}

	if(empty($_POST['variable11'])){
		$error['variable11'] =  "A variable is required";
	}
	else{
		$variable11 = $_POST['variable11'];
	}

	if(empty($_POST['variable12'])){
		$error['variable12'] =  "A variable is required";
	}
	else{
		$variable12 = $_POST['variable12'];
	}

	if(empty($_POST['variable13'])){
		$error['variable13'] =  "A variable is required";
	}
	else{
		$variable13 = $_POST['variable13'];
	}

	if(empty($_POST['variable14'])){
		$error['variable14'] =  "A variable is required";
	}
	else{
		$variable14 = $_POST['variable14'];
	}

	if(empty($_POST['variable15'])){
		$error['variable15'] =  "A variable is required";
	}
	else{
		$variable15 = $_POST['variable15'];
	}

	if(empty($_POST['variable16'])){
		$error['variable16'] =  "A variable is required";
	}
	else{
		$variable16 = $_POST['variable16'];
	}

	if(empty($_POST['variable17'])){
		$error['variable17'] =  "A variable is required";
	}
	else{
		$variable17 = $_POST['variable17'];
	}

	if(empty($_POST['variable18'])){
		$error['variable18'] =  "A variable is required";
	}
	else{
		$variable18 = $_POST['variable18'];
	}

	if(empty($_POST['variable19'])){
		$error['variable19'] =  "A variable is required";
	}
	else{
		$variable19 = $_POST['variable19'];
	}

	if(empty($_POST['variable20'])){
		$error['variable20'] =  "A variable is required";
	}
	else{
		$variable20 = $_POST['variable20'];
	}

	if(empty($_POST['variable21'])){
		$error['variable21'] =  "A variable is required";
	}
	else{
		$variable21 = $_POST['variable21'];
	}

	if(empty($_POST['variable22'])){
		$error['variable22'] =  "A variable is required";
	}
	else{
		$variable22 = $_POST['variable22'];
	}

	if(empty($_POST['variable23'])){
		$error['variable23'] =  "A variable is required";
	}
	else{
		$variable23 = $_POST['variable23'];
	}

	if(empty($_POST['variable24'])){
		$error['variable24'] =  "A variable is required";
	}
	else{
		$variable24 = $_POST['variable24'];
	}

	if(empty($_POST['variable25'])){
		$error['variable25'] =  "A variable is required";
	}
	else{
		$variable25 = $_POST['variable25'];
	}

	if(empty($_POST['variable26'])){
		$error['variable26'] =  "A variable is required";
	}
	else{
		$variable26 = $_POST['variable26'];
	}
}
?>

<?php
	if(isset($_POST['submit']))
	{
		if($_POST['submit'] == 'submit' && $_POST['Units'])
		{
			if($_POST['Units'] == "US")
			{
				$variable4 = $variable4/8.85;
				$variable9 = $variable9*25.4;
			}
			$variable6 = 'SI';
		    $command = escapeshellcmd("python Main.py $variable1 $variable2 $variable3 $variable4 $variable5 $variable6 $variable7 $variable8 $variable9 $variable10 $variable11 $variable12 $variable13 $variable14 $variable15 $variable16 $variable17 $variable18 $variable19 $variable20 $variable21 $variable22 $variable23 $variable24 $variable25 $variable26");
		    $output = exec($command, $err);
		    $result = json_decode($output);
		    $show_result = 1;

		    if($_POST['Units'] == "US")
		    {
		    	$result->PLVel *= 196.85;
		    	$result->Force *= 0.224809;
		    	$result->sigB *= 0.000145038;
		    	$result->sigC *= 0.145038;
		    }
		}

		if($_POST['submit'] == 'Export PDF')
		{
			// shell_exec("python3 /home/abhishek/Desktop/mycode.py $variable1 $variable2 $variable3");
		    $command = escapeshellcmd("python exportPDF.py $variable1 $variable2 $variable3 $variable4 $variable5 $variable6 $variable7 $variable8 $variable9 $variable10 $variable11 $variable12 $variable13 $variable14 $variable15 $variable16 $variable17 $variable18 $variable19 $variable20 $variable21 $variable22 $variable23 $variable24 $variable25 $variable26");
		    $output = exec($command, $err);
		    echo 'Exported';
		}

		if($_POST['submit'] == 'Update Units')
		{
			$show_result = 0;
		}
	}

?>



<!DOCTYPE html>
<html>
<head>
	<title>GEAR GUI</title>
	<link rel="stylesheet" href="styles.css">
</head>
<body>
	<div>
		<h1 class = 'Heading' align = 'center'>GEAR DESIGN</h1>
	</div>
	<section class = 'GUISection'>
		<div class = 'GUI InputTable'>
			<?php include 'content.php' ?>
			<?php include 'content_gear_params.php' ?>
			<?php include 'content_mount_params.php' ?>
		</div>
		<div class = 'GUI Results'>
			<?php include 'export_pdf.php' ?>
		</div>
	</section>
</body>
</html>