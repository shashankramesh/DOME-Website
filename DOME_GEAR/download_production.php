<?php 
	sleep(1);
	$servername = "localhost";
	$username = "root";
	$password = "";
	$dbname = "mydatabase";
	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
	    die("Connection failed: " . $conn->connect_error);
	}

	$sql = "SELECT id, variable2, variable3, variable17, backlash, hole_dia, hub_height, hub_dia, variable9, scale, projection, title, Company_Name, Name FROM drawing";
	$result = $conn->query($sql);

	if ($result->num_rows > 0) {
	    $row = $result->fetch_assoc();
	    $variable3 = $row["variable3"];
	    $variable2 = $row["variable2"];
	    $variable17 = $row["variable17"];
	    $backlash = $row["backlash"];
	    $hole_dia = $row["hole_dia"];
	    $hub_dia = $row["hub_dia"];
	    $hub_height = $row["hub_height"];
	    $Projection = $row["projection"];
	    $scale = $row["scale"];
	    $variable9 = $row["variable9"];
	    $title = $row["title"];
	    $CompanyName = $row["Company_Name"];
	    $Name = $row["Name"];
	    $command = escapeshellcmd("python Gear_Production_Drawing.py --teeth-count=$variable3 --tooth-module=$variable2 --pressure-angle=$variable17 --backlash=$backlash --hole-diameter=$hole_dia --scale=$scale --hub-diameter=$hub_dia --face-width=$variable9 --hub-height=$hub_height --Projection=$Projection --title=$title --Name=$Name --Company-Name='"."$CompanyName"."'");
		    
		$output = shell_exec($command);
	} else {
	    echo "0 results";
	}
	$conn->close();
	header("Content-type: application/pdf");
	//header("Content-Disposition: attachment; filename=download.pdf");
	echo $output;
 ?>