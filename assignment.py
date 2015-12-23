'''Movie Aggregrator'''
import sys
from fpdf import FPDF

class UserPref(object):
    ''' class for userpreferences '''
    def __init__(self, prefs):
        for key, value in prefs.iteritems():
            setattr(self, key, value)

class UserPrefTxt(UserPref):
    '''class for exporting userpreferences to txt file '''
    def export(self):
        ''' export user preferences as plain text'''
        target = open('user.txt', 'a')
        target.write(str(self.__dict__))

class UserPrefPdf(UserPref):
    '''class for exporting userpreferences to pdf file '''
    def export(self):
        ''' export user preferences as plain pdf '''
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B',8)
        pdf.cell(40, 10, str(self.__dict__))
        pdf.output('user.pdf', 'F')

EXPORT_METHOD = {
    "txt" : UserPrefTxt,
    "pdf" : UserPrefPdf,
}

def select_exportclass(prefs):
    ''' find the right class for exporting user preferences'''
    return EXPORT_METHOD[prefs["ext"]](prefs)

def main():
    """ Get user preferences"""
    while True:
        print "Type:\n\t*write to export your preferences to a desired file format\n\t*exit to exit"
        action = raw_input("\n> ")
        if "write" in action:
            prefs = {}
            prefs["name"] = raw_input("Enter name\n> ")
            prefs["movie_name"] = raw_input("Enter a movie name\n> ")
            prefs["run_time"] = raw_input("Enter runtime of the movie\n> ")
            prefs["lang"] = raw_input("Enter language\n>")
            prefs["leadactor"] = raw_input("Enter the name of the lead actor\n>")
            prefs["genre"] = raw_input("Enter the genre\n>")
            prefs["ext"] = raw_input("Enter file format to save your preferences. e.g. pdf, txt\n>")
            method = select_exportclass(prefs)
            getattr(method, "export")()
        else:
            sys.exit(0)
if __name__ == "__main__":
    main()
