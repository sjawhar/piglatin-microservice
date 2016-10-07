from string import punctuation
from os import linesep
from re import split, search, sub

def to_pig_latin(text):
    """Convert text to pig latin

    Keyword arguments:
        text -- the text to convert

    """
    if not isinstance(text, basestring):
        raise TypeError('Argument passed to to_pig_latin() must be a string.')

    converted_words = []
    for word in _split_words(text):
        if not search('[a-zA-Z]', word):
            converted_words.append(word)
            continue

        trimmed_word = _trim_punctuation(word)
        if len(trimmed_word) == 0:
            converted_words.append(word)
            continue

        converted_word = word.replace(trimmed_word, _convert_word(trimmed_word))
        converted_words.append(converted_word)

    return _join_words(converted_words)

"""
Helper functions and constants
"""
_VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
_PUNCTUATION = set(punctuation)

def _convert_word(word):
    if not isinstance(word, basestring):
        raise TypeError('Argument passed to _convert_word() must be a string.')

    first_vowel = -1
    for i in range(len(word)):
        if word[i] in _VOWELS:
            first_vowel = i
            break

    if first_vowel == -1:
        converted_word = word + 'ay'
    elif first_vowel == 0:
        converted_word = word + 'yay'
    else:
        converted_word = word[first_vowel:] + word[:first_vowel] + 'ay'

    return _match_capitalization(converted_word, word)

def _split_words(text):
    if not isinstance(text, basestring):
        raise TypeError('Argument passed to _split_words() must be a string.')

    return split('(\s+)', text)

def _join_words(words):
    if type(words) not in [list, tuple]:
        raise TypeError('Argument passed to _join_words() must be a list or a tuple')
    elif len(words) == 0:
        raise ValueError('List passed to _join_words() must have at least one element')

    return ''.join(words)

def _trim_punctuation(word):
    if not isinstance(word, basestring):
        raise TypeError('Argument passed to _trim_punctuation() must be a string.')

    return word.strip(''.join(_PUNCTUATION))

def _match_capitalization(word, match_word):
    match_word = sub('[^a-zA-Z]', '', match_word)
    if match_word.istitle():
        return word[0].upper() + word[1:].lower()
    return word
