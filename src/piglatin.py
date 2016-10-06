import string
import os

_VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
_PUNCTUATION = set(string.punctuation)

def _convert_word(word):
    stripped_word = word.strip(''.join(_PUNCTUATION))
    if len(stripped_word) == 0:
        return word

    first_vowel = -1
    for i in range(len(stripped_word)):
        if stripped_word[i] in _VOWELS:
            first_vowel = i
            break

    if first_vowel == -1:
        converted_word = stripped_word + 'ay'
    elif first_vowel == 0:
        converted_word = stripped_word + 'yay'
    else:
        converted_word = stripped_word[first_vowel:] + stripped_word[:first_vowel] + 'ay'

    converted_word = _match_capitalization(converted_word, stripped_word)
    return word.replace(stripped_word, converted_word)

def _match_capitalization(word, match_word):
    return word

def _split_words(text):
    return text.split(' ')

def _join_words(words):
    return ' '.join(words)

def _convert_line(line):

    words = _split_words(line)
    converted_words = []

    # Call _covert_word() for each word
    for word in words:
        converted_words.append(_convert_word(word))

    # Reassemble text
    text = _join_words(converted_words)

    # Return result
    return text

def _split_lines(text):
    return text.split(os.linesep)

def _join_lines(lines):
    return os.linesep.join(lines)

def convert(text):
    """Convert text to pig latin, using the standard 

    Keyword arguments:
        text -- the text to convert

    """

    lines = _split_lines(text)
    converted_lines = []
    for line in lines:
        converted_lines.append(_convert_line(line))

    return _join_lines(converted_lines)
