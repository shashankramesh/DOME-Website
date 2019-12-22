<div>
	<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm'>
		<tbody>
			<h2 align = 'center'>Parameters for Gear</h2>
			<div>
				<div>
				<!-- Design !-->
				<tr>
					<td>
						Design for
					</td>
					<td>
						<select name="design">
							<option <?php if($design == 'Pinion') echo "selected" ?>>Pinion</option>
							<option <?php if($design == 'Gear') echo "selected" ?>>Gear</option>	
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- Applied Torque !-->
				<tr>
					<td>
						Applied Torque
					</td>
					<td>
						<input name="variable4" type="number" value = "<?php echo $variable4 ?>" min="0" step = '0.001'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['Torque'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['Torque'];
						 ?>
					</td>
				</tr>
				</div>
				<div>
				<!-- Speed!-->
				<tr>
					<td>
						Speed
					</td>
					<td>
						<input name="variable1" type="number" value = "<?php echo $variable1 ?>" min="0" step = '0.001'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['Omega'];
						if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['Omega'];
						 ?>
					</td>
				</tr>
				</div>
				<tr>
					<td>
						Gear Type
					</td>
					<td>
						<select name="variable16">
							<option <?php if($variable16 == 'External') echo "selected" ?>>External</option>
							<option <?php if($variable16 == 'Internal') echo "selected" ?>>Internal</option>
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- Face width !-->
				<tr>
					<td>
						Face width
					</td>
					<td>
						<input name="variable9" type="number" min="0" value="<?php echo $variable9 ?>" step = '0.001'>
					</td>
					<td>
						<?php 
						if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['length'];
						if(isset($_POST['Units']) && $_POST['Units']== 'US') echo $US_Units['length'];
						 ?>
					</td>
				</tr>
				</div>
				<div>
				<!-- Teeth Type !-->
				<tr>
					<td>
						Teeth type
					</td>
					<td>
						<select name="variable14">
							<option <?php if($variable14 == 'Uncrowned') echo "selected" ?>>Uncrowned</option>
							<option <?php if($variable14 == 'Crowned') echo "selected" ?>>Crowned</option>	
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- Number of cycles!-->
				<tr>
					<td>
						Number of cycles
					</td>
					<td>
						<input name="variable23" type="number" min="0" value="<?php echo $variable23 ?>">
					</td>
				</tr>
				</div>
				<!-- Gear Material !-->
				<tr>
					<td>
						Material
					</td>
					<td>
						<select name="variable25">
							<option <?php if($variable25 == 'HS') echo "selected" ?>>HS</option>
							<option <?php if($variable25 == 'NTHS') echo "selected" ?>>NTHS</option>	
							<option <?php if($variable25 == 'NS') echo "selected" ?>>NS</option>
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- Pinion Material !-->
				<tr>
					<td>
						Pinion Material
					</td>
					<td>
						<select name="variable18">
							<option <?php if($variable18 == 'Steel') echo "selected" ?>>Steel</option>
							<option <?php if($variable18 == 'Malleable Iron') echo "selected" ?>>Malleable Iron</option>
							<option <?php if($variable18 == 'Nodular Iron') echo "selected" ?>>Nodular Iron</option>
							<option <?php if($variable18 == 'Cast Iron') echo "selected" ?>>Cast Iron</option>
							<option <?php if($variable18 == 'Aluminium Bronze') echo "selected" ?>>Aluminium Bronze</option>
							<option <?php if($variable18 == 'Tin Bronze') echo "selected" ?>>Tin Bronze</option>
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- Material !-->
				<tr>
					<td>
						Gear Material
					</td>
					<td>
						<select name="variable19">
							<option <?php if($variable19 == 'Steel') echo "selected" ?>>Steel</option>
							<option <?php if($variable19 == 'Malleable Iron') echo "selected" ?>>Malleable Iron</option>
							<option <?php if($variable19 == 'Nodular Iron') echo "selected" ?>>Nodular Iron</option>
							<option <?php if($variable19 == 'Cast Iron') echo "selected" ?>>Cast Iron</option>
							<option <?php if($variable19 == 'Aluminium Bronze') echo "selected" ?>>Aluminium Bronze</option>
							<option <?php if($variable19 == 'Tin Bronze') echo "selected" ?>>Tin Bronze</option>
						</select>
					</td>
				</tr>
				</div>
				<div>
				<!-- grade !-->
				<tr>
					<td>
						grade
					</td>
					<td>
						<select name="variable26">
							<option <?php if($variable26 == 'g1') echo "selected" ?>>g1</option>
							<option <?php if($variable26 == 'g2') echo "selected" ?>>g2</option>	
						</select>
					</td>
				</tr>
				</div>
				<!--Brinell hardness !-->					
				<div>
				<tr>
					<td>
						Brinell hardness
					</td>
					<td>
						<input name="variable24" type="number" min="0" value="<?php echo $variable24 ?>">
					</td>
				</tr>
				</div>

			</div>
			<!-- /form -->
		</tbody>

		</table>
</div>