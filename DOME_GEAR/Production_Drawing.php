<!-- Module - variable2
	 teeth - variable3
	 face width - variable9
	 pressure_angle - variable17
 !-->
<?php 
$backlash = 0;
$face_width = 8.5;
$hub_dia = 15;
$hole_dia = 10;
$fillet_rad = 0;
$scale = 3.0;
$projection = 'first_angle';
$title = "Title";
$Company_Name = "Company Name";
$Name = "Name";
$hub_height = 6.5;
 ?>
<?php 
if(isset($_POST['submit'])){

	if(empty($_POST['backlash'])){
		$error['backlash'] =  "A variable is required";
	}
	else{
		$backlash = $_POST['backlash'];
	}

	if(empty($_POST['hub_dia'])){
		$error['hub_dia'] =  "A variable is required";
	}
	else{
		$hub_dia = $_POST['hub_dia'];
	}

	if(empty($_POST['hole_dia'])){
		$error['hole_dia'] =  "A variable is required";
	}
	else{
		$hole_dia = $_POST['hole_dia'];
	}

	if(empty($_POST['fillet_rad'])){
		$error['fillet_rad'] =  "A variable is required";
	}
	else{
		$fillet_rad = $_POST['fillet_rad'];
	}

	if(empty($_POST['scale'])){
		$error['scale'] =  "A variable is required";
	}
	else{
		$scale = $_POST['scale'];
	}

	if(empty($_POST['title'])){
		$error['title'] =  "A variable is required";
	}
	else{
		$title = $_POST['title'];
	}

	if(empty($_POST['Company_Name'])){
		$error['Company_Name'] =  "A variable is required";
	}
	else{
		$Company_Name = $_POST['Company_Name'];
	}

	if(empty($_POST['Name'])){
		$error['Name'] =  "A variable is required";
	}
	else{
		$Name = $_POST['Name'];
	}

	if(empty($_POST['projection'])){
		$error['projection'] =  "A variable is required";
	}
	else{
		$projection = $_POST['projection'];
	}

	if(empty($_POST['hub_height'])){
		$error['hub_height'] =  "A variable is required";
	}
	else{
		$hub_height = $_POST['hub_height'];
	}
}
?>
<h2 class = 'ResultsHeading' align = 'center'>Production Drawing</h2>
	<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm' align="center">
		<tbody>
			<div>
				<!-- Backlash !-->
				<tr>
					<td>
						Backlash
					</td>
					<td>
						<input name="backlash" value = "<?php echo $backlash ?>" type="number" min="0" step = '0.01'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['angle'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['angle'];
						 ?>
					</td>
				</tr>
				</div>
				<!-- Hub Dia !-->
				<tr>
					<td>
						Hub Diameter
					</td>
					<td>
						<input name="hub_dia" value = "<?php echo $hub_dia ?>" type="number" min="0" step = '0.01'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['length'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['length'];
						 ?>
					</td>
				</tr>
				</div>
				<div>
				<!-- Hub Height !-->
				<tr>
					<td>
						Hub Height
					</td>
					<td>
						<input name="hub_height" value = "<?php echo $hub_height ?>" type="number" min="0" step = '0.01'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['length'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['length'];
						 ?>
					</td>
				</tr>
				</div>
				<div>
				<!-- Hole Dia !-->
				<tr>
					<td>
						Shaft Diameter
					</td>
					<td>
						<input name="hole_dia" value = "<?php echo $hole_dia ?>" type="number" min="0" step = '0.01'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['length'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['length'];
						 ?>
					</td>
				</tr>
				</div>
				<div>
				<!-- Fillet Radius !-->
				<tr>
					<td>
						Root Fillet Radius
					</td>
					<td>
						<input name="fillet_rad" value = "<?php echo $fillet_rad ?>" type="number" min="0" step = '0.01'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['length'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['length'];
						 ?>
					</td>
				</tr>
				</div>
			</div>
		</tbody>
	</table>
	<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm' align="center">
		<tbody>
			<div>
				<div>
					<tr>
						<td>
							Scale
						</td>
						<td>
							<input name="scale" value = "<?php echo $scale ?>" type="number" min="0" step = '0.01'>
						</td>
						<td>
							
						</td>
					</tr>
				</div>
				<div>
					<tr>
						<td>
							Projection
						</td>
						<td>
							<select name="projection">
							<option selected>FirstAngle</option>
							<option>ThirdAngle</option>	
						</select>
						</td>
						<td>
							
						</td>
					</tr>
				</div>
				<div>
					<tr>
						<td>
							Title
						</td>
						<td>
							<input name="title" value = "<?php echo $title ?>" type="text">
						</td>
						<td>
							
						</td>
					</tr>
				</div>
				<div>
					<tr>
						<td>
							Company Name
						</td>
						<td>
							<input name="Company_Name" value = "<?php echo $Company_Name ?>" type="text">
						</td>
						<td>
							
						</td>
					</tr>
				</div>
				<div>
					<tr>
						<td>
							Name
						</td>
						<td>
							<input name="Name" value = "<?php echo $Name ?>" type="text">
						</td>
						<td>
							
						</td>
					</tr>
				</div>
			</div>
			<div>
				<tr>
					<td>
						<input type = 'submit' name = 'submit' value = 'drawing' align ="centre" onclick="window.open('download_production.php')"></input>
					</td>
				</tr>
			</div>
		</tbody>
	</table>
</form>

<?php 
if(isset($_POST['submit']))
	{
		if($_POST['submit'] == 'drawing' && $_POST['Units'])
		{
			if($_POST['Units'] == "US")
			{
				$face_width = $face_width*25.4;
				$hole_dia = $hole_dia*25.4;
				$hub_dia = $hub_dia*25.4;
				$fillet_rad = $fillet_rad*25.4;
			}
			$variable6 = 'SI';
			//var_dump(headers_list());
			//echo $output;

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

			// sql to create table
			$conn->query("DROP TABLE IF EXISTS drawing");
			$sql = "CREATE TABLE drawing (
			id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, 
			variable2 FLOAT,
			variable3 FLOAT,
			variable17 FLOAT,
			backlash FLOAT,
			hole_dia FLOAT,
			hub_dia FLOAT,
			hub_height FLOAT,
			scale FLOAT,
			variable9 FLOAT,
			projection VARCHAR(125),
			title VARCHAR(125),
			Company_Name VARCHAR(125),
			Name VARCHAR(125))";

			if ($conn->query($sql) === TRUE) {
			    echo "Table MyGuests created successfully";
			} else {
			    echo "Error creating table: " . $conn->error;
			}
			$sql = "INSERT INTO drawing (id, variable2, variable3, variable17, backlash, hole_dia, hub_height, hub_dia, variable9, scale, projection, title, Company_Name, Name) VALUES (1, $variable2, $variable3, $variable17, $backlash, $hole_dia, $hub_height, $hub_dia, $variable9, $scale, '".$projection."', '".$title."', '".$Company_Name."', '".$Name."')";

			if ($conn->query($sql) === TRUE) {
			    echo "New record created successfully";
			} else {
			    echo "Error: " . "<br>" . $conn->error;
			}

			$conn->close();
		}
	}
 ?>