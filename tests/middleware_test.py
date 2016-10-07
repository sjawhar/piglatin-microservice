import unittest

class TestRequireJson(unittest.TestCase):
    def test_process_request_raises_error_if_client_doesnt_accept_json(self):
        pass

    def test_process_request_raises_error_if_content_type_not_set(self):
        # Test POST, PATCH, and PUT
        pass

    def test_process_request_raises_error_if_content_type_not_json(self):
        # Test POST, PATCH, and PUT
        pass

    def test_process_request_doesnt_raise_content_type_error_if_method_not_post_patch_or_put(self):
        # Test GET and DELETE 
        pass

class TestJsonTranslator(unittest.TestCase):
    def test_process_request_has_no_effect_if_content_length_is_empty(self):
        pass

    def test_process_request_raises_error_if_body_not_valid_json(self):
        pass

    def test_process_request_converts_body_to_json(self):
        pass

    def test_process_response_has_no_effect_if_request_context_result_not_set(self):
        # Check request and response are unchanged
        pass

    def test_process_response_jsonifies_request_context_result(self):
        # Check simple and complex objects, lists
        pass

require_json_suite = unittest.TestLoader().loadTestsFromTestCase(TestRequireJson)
json_translator_suite = unittest.TestLoader().loadTestsFromTestCase(TestJsonTranslator)
suite = unittest.TestSuite([require_json_suite, json_translator_suite])

unittest.TextTestRunner(verbosity=2).run(suite)
