# Taken from Falcon docs: http://falcon.readthedocs.io/en/stable/user/quickstart.html
import json
import falcon

class RequireJson(object):

    def process_request(self, request, response):
        if not request.client_accepts_json:
            raise falcon.HTTPNotAcceptable('This API only supports responses encoded as JSON.')

        if request.method in ('POST', 'PATCH', 'PUT'):
            if request.content_type is None or 'application/json' not in request.content_type:
                raise falcon.HTTPUnsupportedMediaType('This API only supports requests encoded as JSON.')


class JsonTranslator(object):

    def process_request(self, request, response):
        # request.stream corresponds to the WSGI wsgi.input environ variable,
        # and allows you to read bytes from the request body.
        #
        # See also: PEP 3333
        if request.content_length in (None, 0):
            # Nothing to do
            return

        body = request.stream.read()
        if not body:
            raise falcon.HTTPBadRequest(
                'Empty request body',
                'A valid JSON document is required.'
            )

        try:
            request.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(
                falcon.HTTP_753,
                'Malformed JSON',
                'Could not decode the request body. The JSON was incorrect or not encoded as UTF-8.'
            )

    def process_response(self, request, response, resource):
        if 'result' not in request.context:
            return

        response.body = json.dumps(request.context['result'], indent=4)
