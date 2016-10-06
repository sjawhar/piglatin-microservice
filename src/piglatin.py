import string
import os

class PigLatinTranslator:

    _VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    _PUNCTUATION = set(string.punctuation)

    def _convert_word(self, word):
        stripped_word = word.strip(''.join(self._PUNCTUATION))
        first_vowel = -1
        for i in range(len(stripped_word)):
            if stripped_word[i] in self._VOWELS:
                first_vowel = i
                break

        if first_vowel == -1:
            converted_word = stripped_word + 'ay'
        elif first_vowel == 0:
            converted_word = stripped_word + 'yay'
        else:
            converted_word = stripped_word[first_vowel:] + stripped_word[:first_vowel] + 'ay'

        converted_word = self._match_capitalization(converted_word, stripped_word)
        return word.replace(stripped_word, converted_word)

    def _match_capitalization(self, word, match_word):
        return word

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
