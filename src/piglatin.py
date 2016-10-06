import string
import os

_VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
_PUNCTUATION = set(string.punctuation)

def _convert_word(word):
    trimmed_word = _trim_punctuation(word)
    if len(trimmed_word) == 0:
        return word

    first_vowel = -1
    for i in range(len(trimmed_word)):
        if trimmed_word[i] in _VOWELS:
            first_vowel = i
            break

    if first_vowel == -1:
        converted_word = trimmed_word + 'ay'
    elif first_vowel == 0:
        converted_word = trimmed_word + 'yay'
    else:
        converted_word = trimmed_word[first_vowel:] + trimmed_word[:first_vowel] + 'ay'

    converted_word = _match_capitalization(converted_word, trimmed_word)
    return word.replace(trimmed_word, converted_word)

def _trim_punctuation(word):
    return word.strip(''.join(_PUNCTUATION))

def _match_capitalization(word, match_word):
    return word

def _split_words(text):
    return text.split(' ')

def _join_words(words):
    return ' '.join(words)

def _split_lines(text):
    return text.split(os.linesep)

def _join_lines(lines):
    return os.linesep.join(lines)

def to_pig_latin(text):
    """Convert text to pig latin

    Keyword arguments:
        text -- the text to convert

    """
    if not isinstance(text, basestring):
        raise TypeError('Argument passed to to_pig_latin() must be a string.')

    lines = _split_lines(text)
    converted_lines = []

    for line in lines:
        words = _split_words(line)
        converted_words = []
        for word in words:
            converted_words.append(_convert_word(word))
        converted_lines.append(_join_words(converted_words))
    return _join_lines(converted_lines)
