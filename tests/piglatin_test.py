import unittest
from src import piglatin

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
                'calling _split_words() on ' + sentence + ' should return an array'
            )

    def test_split_words_splits_on_space(self):
        test_sentences = {
            ' ' : ['', ''],
            'test test' : ['test', 'test'],
            ' '.join(['test'] * 1000) : ['test'] * 1000
        }
        
        for (sentence, words) in test_sentences.iteritems():
            test_words = piglatin._split_words(sentence)
            self.assertEqual(
                words,
                test_words,
                'calling _split_words() on ' + sentence + ' returned unexpected result: ' + str(test_words)
            )

    def test_split_words_empty_string_returns_list_with_empty_string(self):
        self.assertEqual(
            [''],
            piglatin._split_words(''),
            'calling _split_words() on an empty string should return a list with one member: an empty string'
        )

    def test_split_words_without_space_returns_list_with_word(self):
        sentence_without_spaces = 'thisisasentencethathasnospaces'
        self.assertEqual(
            [sentence_without_spaces],
            piglatin._split_words(sentence_without_spaces),
            'calling _split_words() on a string with no spaces should return a list with one member: the original string'
        )

    """
    Tests for piglatin._join_words()
    """    
    def test_join_words_returns_string(self):
        test_words = [
            ['test'],
            [''],
            ['', ''],
            ['test', 'test'],
            ['test'] * 1000
        ]
        
        for words in test_words:
            self.assertIsInstance(
                piglatin._join_words(words),
                basestring,
                'calling _join_words() on ' + str(words) + ' should return a string'
            )

    def test_join_words_joins_with_spaces(self):
        test_words = [
            (['', ''], ' '),
            (['test', 'test'], 'test test'),
            (['test'] * 1000, ' '.join(['test'] * 1000))
        ]
        
        for (words, sentence) in test_words:
            test_sentence = piglatin._join_words(words)
            self.assertEqual(
                sentence,
                test_sentence,
                'calling _join_words() on ' + str(words) + ' returned unexpected result: ' + test_sentence
            )

    def test_join_words_empty_list_raises_value_error(self):
        with self.assertRaises(ValueError):
            piglatin._join_words([])

    """
    Tests for piglatin._join_lines()
    """
    def test_join_words_returns_string(self):
        pass

    def test_join_words_joins_with_os_newlines(self):
        pass

    def test_join_words_empty_list_returns_empty_string(self):
        pass

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
                'calling _trim_punctuation() on ' + word + ' returned ' + test_trimmed_word + ', should be ' + trimmed_word
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
                'calling _trim_punctuation() on ' + contraction + ' returned ' + test_trim + ', should be ' + contraction
            )
    
    """
    Tests for piglatin._match_capitalization()
    """
    def test_match_capitalization_perserves_title_case(self):
        self.assertEqual(
            'Isthay',
            piglatin._match_capitalization('isThay', 'This'),
            'calling _match_capitalization() should correct title case'
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
                'translation of ' + word + ' should be ' + translation + ', but instead got ' + test_translation
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
                'translation of ' + word + ' should be ' + translation + ', but instead got ' + test_translation
            )
    """
    Tests for piglatin.to_pig_latin()
    """
    def test_to_pig_latin_preserves_word_count(self):
        pass

    def test_to_pig_latin_preserves_paragraphs(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatinMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
