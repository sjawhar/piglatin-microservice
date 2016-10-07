import unittest
from src import piglatin
from os import linesep

class TestPigLatinMethods(unittest.TestCase):

    """
    Tests for piglatin._split_words()
    """
    def test_split_words_returns_list(self):
        test_sentences = [
            'test',
            '',
            ' ',
            'test test',
            ' '.join(['test'] * 1000)
        ]

        for sentence in test_sentences:
            self.assertIsInstance(
                piglatin._split_words(sentence),
                list,
                'Calling _split_words() on %s should return an array.' % sentence
            )

    def test_split_words_splits_on_space(self):
        test_sentences = {
            'test test' : ['test', ' ', 'test'],
            'test  test' : ['test', '  ', 'test']
        }
        
        for (sentence, words) in test_sentences.iteritems():
            test_words = piglatin._split_words(sentence)
            self.assertEqual(
                words,
                test_words,
                """
                Calling _split_words() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (sentence, words, test_words)
            )

    def test_split_words_splits_on_newline(self):
        test_sentences = {
            'test\rtest' : ['test', '\r', 'test'],
            'test\r\ntest' : ['test', '\r\n', 'test'],
            'test' + linesep + 'test' : ['test', linesep, 'test']
        }

        for (sentence, words) in test_sentences.iteritems():
            test_words = piglatin._split_words(sentence)
            self.assertEqual(
                words,
                test_words,
                """
                Calling _split_words() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (sentence, words, test_words)
            )

    def test_split_words_empty_string_returns_list_with_empty_string(self):
        self.assertEqual(
            [''],
            piglatin._split_words(''),
            'Calling _split_words() on an empty string should return a list with one member: an empty string.'
        )

    def test_split_words_without_space_returns_list_with_word(self):
        sentence_without_spaces = 'thisisasentencethathasnospaces'
        self.assertEqual(
            [sentence_without_spaces],
            piglatin._split_words(sentence_without_spaces),
            'Calling _split_words() on a string with no spaces should return a list with one member: the original string.'
        )

    """
    Tests for piglatin._join_words()
    """    
    def test_join_words_returns_string(self):
        test_words = [
            ['test'],
            [' '],
            ['', ''],
            ['test', ' ', 'test'],
            ['test', '\r\n', 'test'],
            [linesep, 'test'],
            ['test'] * 1000
        ]
        
        for words in test_words:
            self.assertIsInstance(
                piglatin._join_words(words),
                basestring,
                'Calling _join_words() on %s should return a string.' % words
            )

    def test_join_words_joins_elements(self):
        test_words = [
            (['', ''], ''),
            (['test', ' ', 'test'], 'test test'),
            (['test', '   ', 'test'], 'test   test'),
            (['test', ' ', ' ', 'test'], 'test  test'),
            ([linesep, 'test'], linesep + 'test')
        ]
        
        for (words, sentence) in test_words:
            test_sentence = piglatin._join_words(words)
            self.assertEqual(
                sentence,
                test_sentence,
                """
                Calling _join_words() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (words, sentence, test_sentence)
            )

    def test_join_words_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            piglatin._join_words([])

    """
    Tests for piglatin._trim_punctuation()
    """
    def test_trim_punctuation(self):
        test_words = [
            ('Hello!', 'Hello'),
            ("'This", 'This')
        ]

        for (word, trimmed_word) in test_words:
            test_trimmed_word = piglatin._trim_punctuation(word)
            self.assertEqual(
                trimmed_word,
                test_trimmed_word,
                """
                Calling _trim_punctuation() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, trimmed_word, test_trimmed_word)
            )

    def test_trim_punctuation_preserves_contractions(self):
        test_contractions = [
            "ain't",
            "could've",
            "shouldn't",
            "s'pose"
        ]

        for contraction in test_contractions:
            test_trim = piglatin._trim_punctuation(contraction)
            self.assertEqual(
                contraction,
                test_trim,
                """
                Calling _trim_punctuation() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (contraction, contraction, test_trim)
            )
    
    """
    Tests for piglatin._fix_title_case()
    """
    def test_fix_title_case_matches_title_case(self):
        test_words = [
            ('isThay', 'This', 'Isthay'),
            ("ou'reYay", "You're", "Ou'reyay"),
            ("Isn'tyay", "Isn't", "Isn'tyay")
        ]
        for (word, match_word, capitalization) in test_words:
            test_capitalization = piglatin._fix_title_case(word, match_word)
            self.assertEqual(
                capitalization,
                test_capitalization,
                """
                Calling _fix_title_case() on (%s, %s) returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, match_word, capitalization, test_capitalization)
            )

    """
    Tests for piglatin._convert_word()
    """
    def test_convert_word_works_with_dereks_examples(self):
        dereks_examples = [
            ('pig', 'igpay'),
            ('banana', 'ananabay'),
            ('trash', 'ashtray'),
            ('happy', 'appyhay'),
            ('duck', 'uckday'),
            ('glove', 'oveglay'),
            ('eat', 'eatyay'),
            ('omelet', 'omeletyay'),
            ('are', 'areyay')
        ]

        for (word, translation) in dereks_examples:
            test_translation = piglatin._convert_word(word)
            self.assertEqual(
                translation,
                test_translation,
                """
                Calling _convert_word() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, translation, test_translation)
            )
    
    def test_convert_word_works_with_contractions(self):
        contractions = [
            ("ain't", "ain'tyay"),
            ("could've", "ould'vecay"),
            ("shouldn't", "ouldn'tshay"),
            ("s'pose", "oses'pay")
        ]

        for (word, translation) in contractions:
            test_translation = piglatin._convert_word(word)
            self.assertEqual(
                translation,
                test_translation,
                """
                Calling _convert_word() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (word, translation, test_translation)
            )

    """
    Tests for piglatin.to_pig_latin()
    """
    def test_to_pig_latin(self):
        corpora = [
            ('Good day to you, sir!', 'Oodgay ayday otay ouyay, irsay!'),
            ('This is the first paragraph.\r\nAnd this is the second.', 'Isthay isyay ethay irstfay aragraphpay.\r\nAndyay isthay isyay ethay econdsay.'),
            ("You're thrilled, I'm sure, that contractions aren't a problem.", "Ou'reyay illedthray, I'myay uresay, atthay ontractionscay aren'tyay ayay oblempray.")
        ]

        for (text, translation) in corpora:
            test_translation = piglatin.to_pig_latin(text)
            self.assertEqual(
                translation,
                test_translation,
                """
                Calling to_pig_latin() on %s returned an unexpected result.
                Expected: %s
                Actual: %s
                """ % (text, translation, test_translation)
            )

suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatinMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
