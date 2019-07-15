<div>
	<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm'>
		<tbody>
			<h2 align = 'center'>Parameters for Gear</h2>
			<div>
				<div>
				<!-- Applied Torque !-->
				<tr>
					<td>
						Applied Torque
					</td>
					<td>
						<input name="variable4" type="number" value = "<?php echo $variable4 ?>" min="0" >
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
						<input name="variable1" type="number" value = "<?php echo $variable1 ?>" min="0" >
					</td>
				</tr>
				</div>
				<tr>
					<td>
						Gear Type
					</td>
					<td>
						<select name="variable16">
							<option selected>External</option>
							<option>Internal</option>	
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
						<input name="variable9" type="number" min="0" value="15">
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
							<option selected>Uncrowned</option>
							<option>Crowned</option>	
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
						<input name="variable23" type="number" min="0" value="100000000">
					</td>
				</tr>
				</div>
				<div>
				<!-- Number of teeth!-->
				<tr>
					<td>
						Number of teeth
					</td>
					<td>
						<input name="variable3" type="number" min="0" value="16">
					</td>
				</tr>
				</div>
				<div>
				<!-- Gear Material !-->
				<tr>
					<td>
						Material
					</td>
					<td>
						<select name="variable25">
							<option selected>HS</option>
							<option>NTHS</option>	
							<option>NS</option>
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
							<option selected>Steel</option>
							<option>Malleable Iron</option>	
							<option>Nodular Iron</option>
							<option>Cast Iron</option>
							<option>Aluminium Bronze</option>
							<option>Tin Bronze</option>
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
							<option selected>Steel</option>
							<option>Malleable Iron</option>	
							<option>Nodular Iron</option>
							<option>Cast Iron</option>
							<option>Aluminium Bronze</option>
							<option>Tin Bronze</option>
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
							<option selected>g1</option>
							<option>g2</option>	
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
						<input name="variable24" type="number" min="0" value="200">
					</td>
				</tr>
				</div>

			</div>
			<!-- /form -->
		</tbody>

		</table>
</div>