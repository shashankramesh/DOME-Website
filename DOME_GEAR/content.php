<form action="index.php" method="POST">
<div>
	<h2 align = 'center'>Units</h2>
	<ul class = 'Units_List'>
		<li><input type="radio" name="Units" value = "SI">SI</li>
		<li><input type="radio" name="Units" value = "US">US</li>
	</ul>
</div>
<div>
		<table cellpadding="5" cellspacing="5" border="0" class = 'TableForm'>
			<tbody>
				<h2 align = 'center'>Parameters for Gear Assembly</h2>
				<div>
					<div>
					<!-- Module !-->
					<tr>
						<td>
							Module
						</td>
						<td>
							<input name="variable2" value="2" type="number" min="0" >
						</td>
					</tr>
					</div>
					<!--Gear-ratio !-->
					<div>
					<tr>
						<td>
							Gear-ratio
						</td>
						<td>
							<input name="variable15" value="2" type="number" min="1" >
						</td>
					</tr>
					</div>
					<!--Pinion teeth !-->					
					<div>
					<tr>
						<td>
							Pinion teeth
						</td>
						<td>
							<input name="variable10" value="16" type="number" min="1" step="1">
						</td>
					</tr>
					</div>
					<!--Quality factor !-->					
					<div>
					<tr>
						<td>
							Quality Factor
						</td>
						<td>
							<input name="variable5" type="number" min="6" max="12" value="8">
						</td>
					</tr>
					</div>
					<div>
					<!-- Power Shock condition !-->
					<tr>
						<td>
							Power Shock Condition
						</td>
						<td>
							<select name="variable7">
								<option selected>Uniform</option>
								<option>LightShock</option>	
								<option>MediumShock</option>			
							</select>
						</td>
					</tr>
					</div>
					<div>
					<!-- Load Shock condition !-->
					<tr>
						<td>
							Load Shock Condition
						</td>
						<td>
							<select name="variable8">
								<option selected>Uniform</option>
								<option>ModerateShock</option>	
								<option>HeavyShock</option>			
							</select>
						</td>
					</tr>
					</div>
					<div>
					<!-- Enclosure !-->
					<tr>
						<td>
							Enclosure
						</td>
						<td>
							<select name="variable11">
								<option selected>CommercialEnclosed</option>
								<option>PrecisionEnclosed</option>	
								<option>OpenGearing</option>	
								<option>ExtraPrecisionEnclosed</option>			
							</select>
						</td>
					</tr>
					</div>
					<!--Reliability !-->					
					<div>
					<tr>
						<td>
							Reliability
						</td>
						<td>
							<input name="variable20"  type="number" min="0" max="1" step="0.01"  value="0.95">
						</td>
					</tr>
					</div>
					<!--Pinion Brinell hardness !-->					
					<div>
					<tr>
						<td>
							Pinion Brinell hardness
						</td>
						<td>
							<input name="variable22" type="number" min="0" value="200">
						</td>
					</tr>
					</div>
					<!--Gear Brinell hardness !-->					
					<div>
					<tr>
						<td>
							Gear Brinell hardness
						</td>
						<td>
							<input name="variable21" type="number" min="0" value="200">
						</td>
					</tr>
					</div>

				</div>
				<!--/form -->
			</tbody>
		</table>
</div>