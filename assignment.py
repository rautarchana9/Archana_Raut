'''Movie Aggregrator'''
import sys
import os

def load_modules_from_path(path):
    """ Import all modules from a given directory"""
    if path[-1:] != "/":
        path += "/"
    sys.path.append(path)
    for doc in os.listdir(path):
        if len(doc) > 3 and doc[-3:] == '.py':
            modname = doc[:-3]
            __import__(modname, globals(), locals(), ['*'])

def select_exportclass(prefs):
    ''' Find the right class for exporting user preferences'''
    modulename = prefs["ext"].lower()
    method = getattr(sys.modules[modulename], "UserPref" + modulename)
    return method(prefs)

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
            load_modules_from_path('modules')
            method = select_exportclass(prefs)
            getattr(method, "export")()
        else:
            sys.exit(0)
if __name__ == "__main__":
    main()
