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
    """Convert a single word to pig latin
    Assumes that the word is just letters

    Keyword arguments:
        word -- the word to translate. Should be only letters.

    Returns:
        string -- the translated word
    """

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

    return _fix_title_case(converted_word, word)

def _split_words(text):
    """Split a string on any whitespace (including newlines)
    Returns a list, which includes the whitespace delimiters

    Keyword arguments:
        text -- the text to split

    Returns:
        list -- the words and whitespace delimiters, in order
    """

    if not isinstance(text, basestring):
        raise TypeError('Argument passed to _split_words() must be a string.')

    return split('(\s+)', text)

def _join_words(words):
    """Recombine word-tokenized text into strings.
    Works with _split_words. Currently, simply joins all list elements together.
    Included in case _split_words() logic changes.

    Keyword arguments:
        words -- the words to recombine

    Returns:
        string -- recombined text
    """

    if type(words) not in [list, tuple]:
        raise TypeError('Argument passed to _join_words() must be a list or a tuple')
    elif len(words) == 0:
        raise ValueError('List passed to _join_words() must have at least one element')

    return ''.join(words)

def _trim_punctuation(word):
    """Trim punctuation from the beginning or end of a word.
    Preserves contractions with punctuation in the middle of the word.

    Keyword arguments:
        word -- the word to trim

    Returns:
        string -- the word without leading or trailing punctuation
    """

    if not isinstance(word, basestring):
        raise TypeError('Argument passed to _trim_punctuation() must be a string.')

    return word.strip(''.join(_PUNCTUATION))

def _fix_title_case(word, match_word):
    """Match pig latin translation to capitalization of original word if it was title case
    e.g. You're -> ou'reYay -> Ou'reyay
    
    Only needed for Title Case. If the original word is either all lower or all upper case,
    the translation will be as well and no conversion is needed.

    Keywork arguments:
        word -- the word to change
        match_word -- the word to match

    Returns:
        string -- word with capitalization fixed if needed, otherwise unaltered
    """

    match_word = sub('[^a-zA-Z]', '', match_word)
    if match_word.istitle():
        return word[0].upper() + word[1:].lower()
    return word
