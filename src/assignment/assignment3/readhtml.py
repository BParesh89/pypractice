import codecs
class readhtml:

    def readfile(self, file):
        f = codecs.open(file, "r")
        return f.read()
