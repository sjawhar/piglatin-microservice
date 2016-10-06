import string
#from nltk.tokenize import word_tokenize

class PigLatinTranslator:

    ## Based on http://www.mit.edu/~johnp/6.189/solutions/piglatin.py
    _VOWELS = ('a', 'e', 'i', 'o', 'u')
    _PUNCTUATION = set(string.punctuation)

    def _convert_word(self, word):
        # TODO
        tmp = ''
    
    def _split_text(self, text):
        # TODO
        tmp = ''

    def _split_words(self, text):
        return text.split(' ')

    def _join_words(self, words):
        return ' '.join(words)
    
    def _convert_line(self, line):

        words = self._split_words(line)
        converted_words = []

        # Call _covert_word() for each word
        for word in words:
            converted_words.append(self._convert_word(word))

        # Reassemble text
        text = self._join_words(converted_words)

        # Return result
        return text

    def _split_lines(self, text):
        return text.split(os.linesep)

    def _join_lines(self, lines):
        return os.linesep.join(lines)

    def convert(self, text):
        lines = self._split_lines(text)
        converted_lines = []
        for line in lines:
            converted_lines.append(self._convert_line(line))

        return self._join_lines(converted_lines)
