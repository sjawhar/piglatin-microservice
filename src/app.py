import falcon
from middleware import RequireJson, JsonTranslator
import piglatin

class PigLatinProcedure(object):

    def on_post(self, request, response):
        """Validates request and calls pig latin translation library

        Required Body Properties:
            text -- string of length > 0

        Success Response:
            Code -- 200
            Content -- { translation : string }

        Error Response:
            Code -- 400 or 500
            Content -- { title : string[, description : string]}
        """

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

class StatusPageProcedure(object):

    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = 'The pig latin translation microservice is running. POST to /translate to check it out!\r\nTODO: Add docs here'

api = falcon.API(middleware=[
    RequireJson(),
    JsonTranslator(),
])
api.add_route('/', StatusPageProcedure())
api.add_route('/translate', PigLatinProcedure())
