	<div>Pitch Line Velocity: <?php echo $result->PLVel ?></div>
	<div>Force on Gear Teeth: <?php echo $result->Force ?></div>
	<div>Velocity Factor Kv: <?php echo $result->Kv ?></div>
	<div>Ko: <?php echo $result->Ko ?></div>
	<div>Ks: <?php echo $result->Ks ?></div>
	<div>Kh: <?php echo $result->Kh ?></div>
	<div>Geometry Factor J: <?php echo $result->J ?></div>
	<div>I: <?php echo $result->I ?></div>
	<div>Cp: <?php echo $result->Cp ?></div>
	<div>Kr: <?php echo $result->Kr ?></div>
	<div>Yn: <?php echo $result->Yn ?></div>
	<div>Zn: <?php echo $result->Zn ?></div>
	<div>Bending Stress: <?php echo $result->sigB ?></div>
	<div>Bending Factor of Safety: <?php echo $result->Sf; ?></div>
	<div>Pitting Stress: <?php echo $result->sigC ?></div>
	<div>Pitting Factor of Safety: <?php echo $result->Sh; ?></div>

	<!-- Export PDF Code !-->
<button type="submit" onclick="window.open('file.doc')">Download!</button>

	</form>