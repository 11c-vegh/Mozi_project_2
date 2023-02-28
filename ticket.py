from fpdf import FPDF

pdf = FPDF('P','mm','Legal')

pdf.add_page()

pdf.set_font('helvetica','', 16)

pdf.cell(40,10,'Jegyfoglalás')

pdf.output('ticket.pdf')