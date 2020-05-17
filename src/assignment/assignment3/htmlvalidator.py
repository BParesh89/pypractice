# Assignment for Week - 3
# --------------------------------------------------------------
# Q. Create a class named HtmlValidator and define regular expressions inside the class to validate-
# Whether a given html is valid or not ? Note: Create any html file and read it into python using file handling and
# then apply regular expression to it. Create a separate class to open and read html file and use this class object
# reference in HtmlValidator class.
import re

class HtmlValidator:

    def __init__(self, file, readhtmlobject):
        self.file= file
        self.readhtmlobject = readhtmlobject
        self.htmlstring = readhtmlobject.readfile(file)

    def validate(self):
        """
        function to validate whether a given string is a valid html or not
        """

        for line in self.htmlstring.split("\n"):
            if re.search(r"<(\"[^\"]*\"|'[^']*'|[^'\">])*>",line):
                print("Valid html string!")
            else:
                print("Invalid html string - {}".format(line))

