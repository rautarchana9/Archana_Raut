from fpdf import FPDF

class UserPrefpdf(object):
    '''class for exporting userpreferences to pdf file '''
    def __init__(self, prefs):
        for key, value in prefs.iteritems():
            setattr(self, key, value)

    def export(self):
        ''' export user preferences as plain pdf '''
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B',8)
        pdf.cell(40, 10, str(self.__dict__))
        pdf.output('user.pdf', 'F')

