	<h2 class = 'ResultsHeading' align = 'center'>Results</h2>
	<div>Pitch Line Velocity: 
		<?php if(isset($_POST['submit']) && $show_result == 1){
			echo $result->PLVel; echo " ";
			if(isset($_POST['Units']) && $_POST['Units']=="US"){
				echo $US_Units["Velocity"];
			}
			if(isset($_POST['Units']) && $_POST['Units']=="SI"){
				echo $SI_Units["Velocity"];
			}
		} ?>
	</div>
	
	<div>Force on Gear Teeth:
		<?php if(isset($_POST['submit']) && $show_result == 1){
			echo $result->Force; echo " ";
			if(isset($_POST['Units']) && $_POST['Units']=="US"){
				echo $US_Units["Force"];
			}
			if(isset($_POST['Units']) && $_POST['Units']=="SI"){
				echo $SI_Units["Force"];
			}
		} ?>
	</div>

	<div>
		Dynamic Factor Kv: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1)echo $result->Kv ?>
	</div>
	
	<div>
		Overload Factor Ko: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Ko ?>
	</div>
	
	<div>
		Size Factor Ks: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Ks ?>
	</div>

	<div>
		Load distribution Factor Kh: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Kh ?>
	</div>

	<div>
		Geometry Factor for Bending J: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->J ?>
	</div>

	<div>
		Geometry Factor for PittingI: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->I ?>
	</div>

	<div>
		Relaibility Factor Kr: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Kr ?>
	</div>

	<div>
		Stress Cycle Factor for Bending Yn: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Yn ?>
	</div>

	<div>
		Stress Cycle Factor for Pitting Zn: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Zn ?>
	</div>

	<div>Bending Stress: 
		<?php if(isset($_POST['submit']) && $show_result == 1){
			echo $result->sigB; echo " ";
			if(isset($_POST['Units']) && $_POST['Units']=="US"){
				echo $US_Units["stress"];
			}
			if(isset($_POST['Units']) && $_POST['Units']=="SI"){
				echo $SI_Units["stress"];
			}
		} ?>
	</div>

	<div>
		Bending Factor of Safety: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Sf; ?>
	</div>

	<div>Pitting Stress: 
		<?php if(isset($_POST['submit']) && $show_result == 1){
			echo $result->sigC; echo " ";
			if(isset($_POST['Units']) && $_POST['Units']=="US"){
				echo $US_Units["stress"];
			}
			if(isset($_POST['Units']) && $_POST['Units']=="SI"){
				echo $SI_Units["stress"];
			}
		} ?>
	</div>

	<div>
		Pitting Factor of Safety: <?php if(isset($_POST['submit']) && isset($_POST['Units']) && $show_result == 1) echo $result->Sh; ?>
	</div>
	<!-- Export PDF Code !-->
	<?php 
			// shell_exec("python3 /home/abhishek/Desktop/mycode.py $variable1 $variable2 $variable3");
		    $command = escapeshellcmd("python3 exportPDF.py $variable1 $variable2 $variable3 $variable4 $variable5 $variable6 $variable7 $variable8 $variable9 $variable10 $variable11 $variable12 $variable13 $variable14 $variable15 $variable16 $variable17 $variable18 $variable19 $variable20 $variable21 $variable22 $variable23 $variable24 $variable25 $variable26");
		    $output = exec($command, $err);
		    echo 'Exported';
	?>
	<button type="submit" onclick="window.open('simple_table.pdf')">Download!</button>
	</form>