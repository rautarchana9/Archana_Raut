class UserPreftxt(object):
    '''class for exporting userpreferences to txt file '''
    def __init__(self, prefs):
        for key, value in prefs.iteritems():
            setattr(self, key, value)

    def export(self):
        ''' export user preferences as plain text'''
        target = open('user.txt', 'a')
        target.write(str(self.__dict__))
