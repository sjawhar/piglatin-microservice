import falcon
from middleware import RequireJson, JsonTranslator
import piglatin

class PigLatinProcedure(object):

    def on_post(self, request, response):
        if request.content_length in (None, 0):
            raise falcon.HTTPBadRequest(
                'Request body is empty.',
                'The request body must contain JSON.'
            )
        doc = request.context['doc']

        if 'text' not in doc:
            raise falcon.HTTPMissingParam('text')
        elif not isinstance(doc['text'], basestring):
            raise falcon.HTTPInvalidParam(
                'The value is not a string.',
                'text'
            )
        elif len(doc['text']) == 0:
            raise falcon.HTTPInvalidParam(
                'The value is empty.',
                'text'
            )
        text = doc['text']

        try:
            translation = piglatin.to_pig_latin(text)
        except Exception,e:
            """API-specific input validation was handled before calling piglatin.to_pig_latin().
            So any errors are unexpected and given generic 500 code.
            Error message is retained, if possible"""
            description = None
            if (len(e.args) > 0):
                description = e.args[0]

            raise falcon.HTTPInternalServerError(
                'Unexpected error',
                description
            )

        response.status = falcon.HTTP_200
        request.context['result'] = {'translation': translation}

procedure = PigLatinProcedure()
api = falcon.API(middleware=[
    RequireJson(),
    JsonTranslator(),
])
api.add_route('/', procedure)
