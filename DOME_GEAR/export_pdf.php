	<h2 class = 'ResultsHeading' align = 'center'>Results</h2>
	<div>Pitch Line Velocity: 
		<?php if(isset($_POST['submit'])){
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
		<?php if(isset($_POST['submit'])){
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
		Dynamic Factor Kv: <?php if(isset($_POST['submit']) && isset($_POST['Units']))echo $result->Kv ?>
	</div>
	
	<div>
		Overload Factor Ko: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Ko ?>
	</div>
	
	<div>
		Size Factor Ks: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Ks ?>
	</div>

	<div>
		Load distribution Factor Kh: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Kh ?>
	</div>

	<div>
		Geometry Factor for Bending J: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->J ?>
	</div>

	<div>
		Geometry Factor for PittingI: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->I ?>
	</div>

	<div>
		Relaibility Factor Kr: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Kr ?>
	</div>

	<div>
		Stress Cycle Factor for Bending Yn: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Yn ?>
	</div>

	<div>
		Stress Cycle Factor for Pitting Zn: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Zn ?>
	</div>

	<div>Bending Stress: 
		<?php if(isset($_POST['submit'])){
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
		Bending Factor of Safety: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Sf; ?>
	</div>

	<div>Pitting Stress: 
		<?php if(isset($_POST['submit'])){
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
		Pitting Factor of Safety: <?php if(isset($_POST['submit']) && isset($_POST['Units'])) echo $result->Sh; ?>
	</div>
	<!-- Export PDF Code !-->

	</form>