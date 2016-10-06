import unittest
from src import piglatin

class TestPigLatinMethods(unittest.TestCase):

    ### _split_words() ###
    def test_split_words_returns_array(self):
        pass

    def test_split_words_splits_on_space(self):
        pass

    def test_split_words_empty_string_returns_empty_array(self):
        pass

    ### _join_words() ###        
    def test_join_words_returns_string(self):
        pass

    def test_join_words_joins_with_spaces(self):
        pass

    def test_join_words_empty_array_returns_empty_string(self):
        pass

    ### _split_lines() ###
    def test_split_lines_returns_array(self):
        pass

    def test_split_lines_splits_on_newline(self):
        pass

    def test_split_lines_empty_string_returns_empty_array(self):
        pass

    ### _join_lines() ###
    def test_join_words_returns_string(self):
        pass

    def test_join_words_joins_with_os_newlines(self):
        pass

    def test_join_words_empty_array_returns_empty_string(self):
        pass

    ### _trim_punctuation() ###
    def test_trim_punctuation_preserves_contractions(self):
        pass
    
    ### _match_capitalization() ###
    def test_match_capitalization_preserves_all_caps(self):
        pass

    def test_match_capitalization_preserves_all_lower(self):
        pass

    def test_match_capitalization_perserves_title_case(self):
        pass

    ### _convert_word() ###
    def test_convert_word_works_with_dereks_examples(self):
        dereks_examples = {
            'pig' : 'igpay',
            'banana' : 'ananabay',
            'trash' : 'ashtray',
            'happy' : 'appyhay',
            'duck' : 'uckday',
            'glove' : 'oveglay',
            'eat' : 'eatyay',
            'omelet' : 'omeletyay',
            'are' : 'areyay',
        }

        for (word, translation) in dereks_examples.iteritems():
            test_translation = piglatin.to_pig_latin(word)
            self.assertEqual(
                translation,
                test_translation,
                'translation of ' + word + ' should be ' + translation + ', but instead got ' + test_translation
            )
    
    ### to_pig_latin() ###
    def test_to_pig_latin_preserves_word_count(self):
        pass

    def test_to_pig_latin_preserves_paragraphs(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestPigLatinMethods)
unittest.TextTestRunner(verbosity=2).run(suite)
