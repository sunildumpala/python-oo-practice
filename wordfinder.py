import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    """
    Class to read and maintain a list of words from a file
    """

    def __init__(self, filepath):
        """ Constructor to initialize class by reading the contents of file at the filepath
        """
        file = open(filepath)
        self.text = self.parse(file)
        # self.text = []
        # for line in file:
        #     self.text.append(line.strip())
        # file.close

    def parse(self, dict_file):
        text = []
        for line in dict_file:
            text.append(line.strip())
        return text


    def getText(self):
        return self.text
    
    def random(self):
        """ Returns a random word(element) from the file read from the filepath(array)"""
        return random.choice(self.text)

class SpecialWordFinder(WordFinder):
    """ Subclass of WordFinder, can read and clean files with blanks and comments"""

    def parse(self, dict_file):
        text = []
        for line in dict_file:
            if (line.strip() and not line.startswith("#")):
                text.append(line.strip())
        return text
