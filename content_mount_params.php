<div>
		<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm'>
			<tbody>
				<div>
					<h2 align = 'center'>Mounting Parameters</h2>
				</div>
				<div>
					<img src='Gearmounting.png' alt='Gear mounting Parameters' style="width:500px;height:350px;">
				</div>
					<div>
						<!-- S -->
					<tr>
						<td>
							S
						</td>
						<td>
							<input name="variable12" value="<?php echo $variable12 ?>" type="number" min="0" >
						</td>
					</tr>
					</div>
					<div>
						<!-- S1 -->
					<tr>
						<td>
							S1
						</td>
						<td>
							<input name="variable13" value="<?php echo $variable13 ?>" type="number" min="0" >
						</td>
					</tr>
					</div>
					<div>
						<!-- Helix angle -->
					<tr>
						<td>
							Helix angle
						</td>
						<td>
							<input name="Helix_angle" value="0" type="number" min="0" max="90">
						</td>
						<td>
							<?php 
							if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['angle'];
							if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['angle'];
							 ?>
						</td>
					</tr>
					</div>
					<div>
						<!-- pressure angle -->
					<tr>
						<td>
							pressure angle
						</td>
						<td>
							<input name="variable17" value="<?php echo $variable17 ?>" type="number" min="0" max="90" step="0.01">
						</td>
						<td>
							<?php 
							if(isset($_POST['Units']) && $_POST['Units'] == 'SI') echo $SI_Units['angle'];
							if(isset($_POST['Units']) && $_POST['Units'] == 'US') echo $US_Units['angle'];
							 ?>
						</td>
					</tr>
					</div>
					<div>

					<tr>
						<td>
							<input type = 'submit' name = 'submit' value = 'submit' align ="centre"></input>
						</td>
					</tr>
					</div>
			</tbody>
		</table>
</div>