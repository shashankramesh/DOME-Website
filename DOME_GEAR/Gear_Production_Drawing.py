#!/usr/bin/env python

import sys
import numpy
import argparse
import itertools

from shapely.ops import cascaded_union
from shapely.geometry import Point, MultiPoint, Polygon, box
from shapely.affinity import rotate, scale, translate

from fpdf import FPDF

def Scale(x, y, scale):
	return numpy.multiply(x, scale), numpy.multiply(y, scale)

def Translate(x, y, xTo, yTo):
	return numpy.add(x, xTo), numpy.add(y, yTo)

def FindCircleCorner(xCenter, yCenter, radius):
	return xCenter-radius, yCenter-radius, 2*radius, 2*radius

def DrawasCenterLine(pdwg, x, y, specs_array):
	count = 1
	which_section = 1
	for i in range(0, len(x)-1):
		count += 1
		if which_section == 1 or which_section == 3:
			pdwg.line(x[i], y[i], x[i+1], y[i+1])
		
		if count == specs_array[0] and which_section == 1:
			count = 1
			which_section = 2
		if count == specs_array[1] and which_section == 2:
			count = 1
			which_section = 3
		if count == specs_array[2] and which_section == 3:
			count = 1
			which_section = 4
		if count == specs_array[3] and which_section == 4:
			count = 1
			which_section = 1
		

def rot_matrix(x):
	c, s = numpy.cos(x), numpy.sin(x)
	return numpy.array([[c, -s], [s, c]])

def rotation(X, angle, center = None):
	if center is None:
		return numpy.dot(X, rot_matrix(angle))
	else:
		return numpy.dot(X - center, rot_matrix(angle)) + center

def deg2rad(x):
	return (numpy.pi / 180) * x

def generate(teeth_count = 8,
             tooth_module = 1.,
             pressure_angle = deg2rad(20.),
             backlash = 0.,
             frame_count = 16):
        
	pitch_radius = teeth_count*tooth_module/2.
	pitch_circumference = pitch_radius*2.*numpy.pi
	tooth_width = pitch_circumference/(2.*teeth_count)
	tooth_width += backlash
	addendum = tooth_width * (2 / numpy.pi)
	dedendum = addendum
	outer_radius = pitch_radius + addendum
	inner_radius = pitch_radius - dedendum
	# Tooth profile
	profile = numpy.array([
  	[-(.5 * tooth_width + addendum * numpy.tan(pressure_angle)),  addendum],
  	[-(.5 * tooth_width - dedendum * numpy.tan(pressure_angle)), -dedendum],
  	[ (.5 * tooth_width - dedendum * numpy.tan(pressure_angle)), -dedendum],
  	[ (.5 * tooth_width + addendum * numpy.tan(pressure_angle)) , addendum]
	])

	outer_circle = Point(0., 0.).buffer(outer_radius)

	poly_list = []
	prev_X = None
	l = 2 * tooth_width / pitch_radius
	for theta in numpy.linspace(0, l, frame_count):
		X = rotation(profile + numpy.array((-theta * pitch_radius, pitch_radius)), theta)
		if prev_X is not None:
			poly_list.append(MultiPoint([x for x in X] + [x for x in prev_X]).convex_hull)
		prev_X = X	

	def circle_sector(angle, r):
		box_a = rotate(box(0., -2 * r, 2 * r, 2 * r), -angle / 2, Point(0., 0.))
		box_b = rotate(box(-2 * r, -2 * r, 0, 2 * r),  angle / 2, Point(0., 0.))
		return Point(0., 0.).buffer(r).difference(box_a.union(box_b))

	# Generate a tooth profile
	tooth_poly = cascaded_union(poly_list)
	tooth_poly = tooth_poly.union(scale(tooth_poly, -1, 1, 1, Point(0., 0.)))

	# Generate the full gear
	gear_poly = Point(0., 0.).buffer(outer_radius)
	for i in range(0, teeth_count):
		gear_poly = rotate(gear_poly.difference(tooth_poly), (2 * numpy.pi) / teeth_count, Point(0., 0.), use_radians = True)
	
	# Job done
	return gear_poly, pitch_radius, outer_radius, inner_radius

def LinearVertDim(pdwg, x, y1, y2, dim, sign):
	pdwg.line(x + sign*1.5, y1, x + sign*12, y1)
	pdwg.line(x + sign*1.5, y2, x + sign*12, y2)
	pdwg.line(x + sign*9, y1, x + sign*9, y2)		
	pdwg.set_font_size(12)
	if sign == -1:
		pdwg.image('U_arrow.png', x = x - 10.7, y = y1, h = 5)
		pdwg.image('D_arrow.png', x = x - 10.4, y = y2 - 5, h = 5)
		pdwg.image('diameter_symbol.png', x = x - 24, y = (y1+y2-4)/2, h = 5)
		pdwg.text(x - 18, (y1+y2+4)/2, str(dim))
	if sign == 1:
		pdwg.image('U_arrow.png', x = x + 7.3, y = y1, h = 5)
		pdwg.image('D_arrow.png', x = x + 7.5, y = y2 - 5, h = 5)
		pdwg.image('diameter_symbol.png', x = x + 10, y = (y1+y2-4)/2, h = 5)
		pdwg.text(x + 16.5, (y1+y2+4)/2, str(dim))

def LinearHorDim(pdwg, y, x1, x2, dim, sign):
	pdwg.line(x1, y + sign*1.5, x1, y + sign*12)
	pdwg.line(x2, y + sign*1.5, x2, y + sign*12)
	pdwg.line(x1, y + sign*9, x2, y + sign*9)		
	pdwg.set_font_size(12)
	if sign == -1:
		pdwg.image('L_arrow.png', y = y - 10.7, x = x1, w = 5)
		pdwg.image('R_arrow.png', y = y - 10.4, x = x2 - 5, w = 5)
		pdwg.text(y - 18, (x1+x2+4)/2, str(dim))
	if sign == 1:
		pdwg.image('L_arrow.png', y = y + 7.5, x = x1, w = 5)
		pdwg.image('R_arrow.png', y = y + 7.3, x = x2 - 5, w = 5)
		pdwg.text((x1+x2 - 4)/2, y + 14, str(dim))

if __name__ == '__main__':

	# Configure pdf
	pdwg = FPDF('L', 'mm', 'A3')
	pdwg.add_page()
	pdwg.set_font('Times', 'B', 16)
	pdwg.set_auto_page_break(False, margin = 0.0)

	# Command line parsing
	parser = argparse.ArgumentParser(description = 'Gear Production Drawings')
	parser.add_argument('-c', '--teeth-count', type = int, default = 17, help = 'Teeth count')
	parser.add_argument('-w', '--tooth-module', type = float, default = 1., help = 'Tooth module')
	parser.add_argument('-p', '--pressure-angle', type = float, default = 20., help = 'Pressure angle in degrees')
	parser.add_argument('-n', '--frame-count', type = int, default = 16, help = 'Number of frames used to build the involute')
	parser.add_argument('-b', '--backlash', type = float, default = 0.2, help = 'Backlash')
	parser.add_argument('-t', '--output-type', choices = ['dxf', 'text'], default = 'dxf', help = 'Output type')
	parser.add_argument('-o', '--output-path', default = 'out', help = 'Output file')
	parser.add_argument('-f', '--hole-diameter', type = float, default = 1., help = 'Gear Hole Diameter')
	parser.add_argument('-g', '--hub-diameter', type = float, default = 0., help = 'Gear Hub Diameter')
	parser.add_argument('-a', '--scale', type = float, default = 1., help = 'Drawing scale')
	parser.add_argument('-d', '--face-width', type = float, default = 1., help = 'Gear Face Width')
	parser.add_argument('-i', '--hub-height', type = float, default = 1., help = 'Gear Hub Height')
	parser.add_argument('-j', '--fillet-radius', type = float, default = 0., help = 'Root Fillet Radius')
	parser.add_argument('-u', '--units', type = str, default = 'SI', help = 'Units')
	parser.add_argument('-T', '--title', type = str, default = 'Spur Gear', help = 'Drawing Title')
	parser.add_argument('-CN', '--Company-Name', type = str, default = 'Indian Institute of Technology Madras', help = 'Units')
	parser.add_argument('-N', '--Name', type = str, default = 'Shashank & Abhishek', help = 'Units')
	parser.add_argument('-P', '--Projection', type = str, default = 'first_angle', help = 'Type of Projection')
	args = parser.parse_args()
	
	# Configure Units
	if(args.units == 'SI'):
		Units = {'length': 'mm', 'Angle': 'deg'}
	if(args.units == 'US'):
		Units = {'length': 'inch', 'Angle': 'deg'}

	# Generate Gear Profile
	poly, pitch_radius, outer_radius, inner_radius = generate(args.teeth_count, args.tooth_module, deg2rad(args.pressure_angle), args.backlash, args.frame_count)

	# Drawing Border
	pdwg.line(10, 10, 410, 10)
	pdwg.line(10, 10, 10, 287)
	pdwg.line(410, 10, 410, 287)
	pdwg.line(410, 287, 10, 287)

	# Cell for drawing
	pdwg.ln(217)
	pdwg.cell(100)

	# Table of details
	pdwg.cell(150, h = 10, txt = 'Gear Specifications', align = 'C', border = 1)
	pdwg.cell(150, h = 10, txt = args.Company_Name, align = 'C', border = 1)
	pdwg.ln(10)
	pdwg.cell(100)
	pdwg.cell(75, h = 10, txt = 'Module: '+str(args.tooth_module) + Units['length'], align = 'L', border = 1)
	pdwg.cell(75, h = 10, txt = 'Face Width: '+str(args.face_width) + Units['length'], align = 'L', border = 1)
	pdwg.cell(80, h = 10, txt = 'Name: '+args.Name, align = 'L', border = 1)
	pdwg.cell(70, h = 20, txt = 'Title: '+args.title, align = 'L', border = 1)
	pdwg.ln(10)
	pdwg.cell(100)
	pdwg.cell(75, h = 10, txt = 'Number of Teeth: '+str(args.teeth_count), align = 'L', border = 1)
	pdwg.cell(75, h = 10, txt = 'Hole Diameter: '+str(args.hole_diameter) + Units['length'], align = 'L', border = 1)
	pdwg.cell(80, h = 40,border = 1)
	if(args.Projection == 'third_angle'): pdwg.image("third_angle_projection.png", x = 270, y = 255, w = 50)
	else: pdwg.image("first_angle_projection.png", x = 270, y = 255, w = 50)
	pdwg.ln(10)
	pdwg.cell(100)
	pdwg.cell(75, h = 10, txt = 'Pitch Diameter: '+str(pitch_radius*2) + Units['length'], align = 'L', border = 1)
	pdwg.cell(75, h = 10, txt = 'Hub Width: '+str(args.hub_height) + Units['length'], align = 'L', border = 1)
	pdwg.cell(80)
	pdwg.cell(70, h = 20, txt = 'Scale: '+str(args.scale), align = 'L', border = 0)
	pdwg.ln(10)
	pdwg.cell(100)
	pdwg.cell(75, h = 10, txt = 'Root Fillet Radius: '+str(args.fillet_radius) + Units['length'], align = 'L', border = 1)
	pdwg.cell(75, h = 10, txt = 'Pressure Angle: '+str(args.pressure_angle) + Units['Angle'], align = 'L', border = 1)

	# Gear Front View
	# Gear Drawing
	x_center = 110
	y_center = 100
	x, y = poly.exterior.coords.xy
	x, y = Scale(x, y, args.scale)
	x, y = Translate(x, y, x_center, y_center)
	for i in range(0, len(x)-2):
		pdwg.line(x[i], y[i], x[i+1], y[i+1])
	
	# Hole circle
	Xcorner, Ycorner, w, h = FindCircleCorner(x_center, y_center, args.hole_diameter*args.scale/2)
	pdwg.ellipse(Xcorner, Ycorner, w, h, style = '')
	
	# Hub Circle
	if(args.Projection == 'third_angle'):
		Xcorner, Ycorner, w, h = FindCircleCorner(x_center, y_center, args.hub_diameter*args.scale/2)
		pdwg.ellipse(Xcorner, Ycorner, w, h, style = '')
	else:
		dashline_specs = [50, 20, 50, 20]
		steps = 1000
		th_inc = 2*numpy.pi/steps
		xPitch_circle = []
		yPitch_circle = []
		for i in range(0, steps):
			xPitch_circle.append(args.hub_diameter*numpy.cos(i*th_inc)/2)
			yPitch_circle.append(args.hub_diameter*numpy.sin(i*th_inc)/2)
		xPitch_circle, yPitch_circle = Scale(xPitch_circle, yPitch_circle, args.scale)
		xPitch_circle, yPitch_circle = Translate(xPitch_circle, yPitch_circle, x_center, y_center)
		DrawasCenterLine(pdwg, xPitch_circle, yPitch_circle, dashline_specs)
		
	# Pitch circle
	centerline_specs = [200, 100, 90, 100]
	steps = 10000
	th_inc = 2*numpy.pi/steps
	xPitch_circle = []
	yPitch_circle = []
	for i in range(0, steps):
		xPitch_circle.append(pitch_radius*numpy.cos(i*th_inc))
		yPitch_circle.append(pitch_radius*numpy.sin(i*th_inc))
	
	xPitch_circle, yPitch_circle = Scale(xPitch_circle, yPitch_circle, args.scale)
	xPitch_circle, yPitch_circle = Translate(xPitch_circle, yPitch_circle, x_center, y_center)
	DrawasCenterLine(pdwg, xPitch_circle, yPitch_circle, centerline_specs)
	
	# Hole Center line
	centerline_specs = [100, 70, 60, 70]
	steps = 1000
	length = args.hub_diameter*args.scale + 4
	increment = length/steps
	xHorline = []
	yHorline = numpy.zeros(steps)
	yVertline = []
	xVertline = numpy.zeros(steps)
	for i in range(0, steps-1):
		xHorline.append(i*increment - length/2)
		yVertline.append(i*increment - length/2)
	
	xHorline, yHorline = Translate(xHorline, yHorline, x_center, y_center)
	xVertline, yVertline = Translate(xVertline, yVertline, x_center, y_center)
	
	DrawasCenterLine(pdwg, xVertline, yVertline, centerline_specs)
	DrawasCenterLine(pdwg, xHorline, yHorline, centerline_specs)
	
	# Gear side view
	xdist = 200
	ytop = y_center - outer_radius*args.scale
	xtop = x_center + xdist - args.face_width*args.scale/2
	
	# Basic shape
	pdwg.rect(xtop, ytop, args.face_width*args.scale, 2*outer_radius*args.scale)
	tooth_height = (outer_radius - inner_radius)*args.scale
	
	# Marking the tooth on both sides
	pdwg.line(xtop, ytop + tooth_height, xtop + args.face_width*args.scale, ytop + tooth_height)
	pdwg.line(xtop, ytop + tooth_height + inner_radius*2*args.scale, xtop + args.face_width*args.scale, ytop + tooth_height + inner_radius*2*args.scale)
	
	# Drawing the hub
	pdwg.line(xtop, ytop + (outer_radius - args.hub_diameter/2)*args.scale, xtop - args.hub_height*args.scale, ytop + (outer_radius - args.hub_diameter/2)*args.scale)
	pdwg.line(xtop - args.hub_height*args.scale, ytop + (outer_radius - args.hub_diameter/2)*args.scale, xtop - args.hub_height*args.scale, ytop + (outer_radius + args.hub_diameter/2)*args.scale)
	pdwg.line(xtop - args.hub_height*args.scale, ytop + (outer_radius + args.hub_diameter/2)*args.scale, xtop, ytop + (outer_radius + args.hub_diameter/2)*args.scale)
	
	# Dashed line for hole
	pdwg.dashed_line(xtop - args.hub_height*args.scale, ytop + (outer_radius + args.hole_diameter/2)*args.scale, xtop + args.face_width*args.scale, ytop + (outer_radius + args.hole_diameter/2)*args.scale, dash_length = 3, space_length = 1)
	pdwg.dashed_line(xtop - args.hub_height*args.scale, ytop + (outer_radius - args.hole_diameter/2)*args.scale, xtop + args.face_width*args.scale, ytop + (outer_radius - args.hole_diameter/2)*args.scale, dash_length = 3, space_length = 1)
	
	# Centerline for gear
	centerline_specs = [100, 70, 60, 70]
	steps = 1000
	xstart = xtop - args.hub_height*args.scale - 4
	ystartstop = ytop + outer_radius*args.scale
	xstop = xstart + 8 + (args.hub_height + args.face_width)*args.scale
	length = abs(xstart - xstop)
	increment = length/steps
	xHorline = []
	yHorline = numpy.multiply(numpy.ones(steps), ystartstop)
	for i in range(0, steps - 1):
		xHorline.append(i*increment + xstart)
	DrawasCenterLine(pdwg, xHorline, yHorline, centerline_specs)
	
	# Centerline for gear teeth - top
	centerline_specs = [100, 70, 60, 70]
	steps = 1000
	xstart = xtop - 4
	ystartstop = ytop + (outer_radius - pitch_radius)*args.scale
	xstop = xstart + 8 + args.face_width*args.scale
	length = abs(xstart - xstop)
	increment = length/steps
	xHorline = []
	yHorline = numpy.multiply(numpy.ones(steps), ystartstop)
	for i in range(0, steps - 1):
		xHorline.append(i*increment + xstart)
	DrawasCenterLine(pdwg, xHorline, yHorline, centerline_specs)
	
	# Centerline for gear teeth - top
	centerline_specs = [100, 70, 60, 70]
	steps = 1000
	xstart = xtop - 4
	ystartstop = ytop + (outer_radius + pitch_radius)*args.scale
	xstop = xstart + 8 + args.face_width*args.scale
	length = abs(xstart - xstop)
	increment = length/steps
	xHorline = []
	yHorline = numpy.multiply(numpy.ones(steps), ystartstop)
	for i in range(0, steps - 1):
		xHorline.append(i*increment + xstart)
	DrawasCenterLine(pdwg, xHorline, yHorline, centerline_specs)
	
	# Dimensions
	
	# Hub diameter
	LinearVertDim(pdwg, xtop - args.hub_height*args.scale, ytop + (outer_radius - args.hub_diameter/2)*args.scale, ytop + (outer_radius + args.hub_diameter/2)*args.scale, args.hub_diameter, -1)	
	
	# Hole diameter
	LinearVertDim(pdwg, xtop + args.face_width*args.scale, ytop + (outer_radius - args.hole_diameter/2)*args.scale, ytop + (outer_radius + args.hole_diameter/2)*args.scale, args.hole_diameter, 1)

	# Hub width
	LinearHorDim(pdwg, ytop + (outer_radius + args.hub_diameter/2)*args.scale, xtop - args.hub_height*args.scale, xtop, args.hub_height, 1)

	# Face width
	LinearHorDim(pdwg, ytop + outer_radius*2*args.scale, xtop, xtop + args.face_width*args.scale, args.face_width, 1)	

	# Print Drawing as pdf
	out_file = pdwg.output('Drawing.pdf', 'S')
	binary_file = ''.join(format(ord(i), 'b') for i in out_file)
	print(out_file)
'''	try:
		connection = mysql.connector.connect(host='localhost',
				                     database='mydatabase',
				                     user='root',
				                     password='')

		cursor = connection.cursor()
		sql_insert_blob_query = "INSERT INTO drawing (id, file) VALUES (%s,%s)"

		binary_file = ''.join(format(ord(i), 'b') for i in out_file)

		# Convert data into tuple format
		insert_blob_tuple = (1, binary_file)
		#print insert_blob_tuple
		cursor.execute("DROP TABLE IF EXISTS drawing")
		cursor.execute("CREATE TABLE drawing (id INT AUTO_INCREMENT PRIMARY KEY, file VARCHAR(255))")
		result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
		connection.commit()
		print("Image and file inserted successfully as a BLOB into python_employee table", result)

	except mysql.connector.Error as error:
		print("Failed inserting BLOB data into MySQL table {}".format(error))

	finally:
		if (connection.is_connected()):
		    cursor.close()
		    connection.close()
		    print("MySQL connection is closed")'''


	
	
	
	
	
	
	
	
	
