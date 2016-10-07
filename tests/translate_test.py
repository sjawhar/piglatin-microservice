import unittest

class TestTranslateEndpoint(unittest.TestCase):
	def test_empty_body_returns_bad_request(self):
		pass

	def test_empty_string_returns_bad_request(self):
		pass

	def test_non_string_returns_bad_request(self):
		pass

	def test_non_empty_string_returns_ok(self):
		pass

	def test_translate_response_body_structure_has_translation_property(self):
		pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestTranslateEndpoint)
unittest.TextTestRunner(verbosity=2).run(suite)
