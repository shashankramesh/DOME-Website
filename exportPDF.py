from fpdf import FPDF
import sys

def simple_table(spacing=1):
    data = [['Parameter', 'Value'],
            ['Applied Torque', sys.argv[4]],
            ['Speed', sys.argv[1]],
            ['Module', sys.argv[2]],
            ['Quality Factor', sys.argv[5]],
            ['Enclosure', sys.argv[11]],
            ['Gear Ratio', sys.argv[15]],
            ['Pressure Angle', sys.argv[17]],
            ]
 
    pdf = FPDF()
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    for row in data:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

    pdf.output('simple_table.pdf')
 
if __name__ == '__main__':
    simple_table()