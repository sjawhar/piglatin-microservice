import falcon
from middleware import RequireJson, JsonTranslator
import piglatin

class PigLatinProcedure(object):

    def on_post(self, request, response):

        if request.content_length in (None, 0):
            raise falcon.HTTPBadRequest(
                'No text',
                'The request body must contain text to translate.'
            )
        doc = request.context['doc']

        if 'text' not in doc:
            raise falcon.HTTPMissingParam('text')
        elif len(doc['text']) == 0:
            raise falcon.HTTPInvalidParam(
                'The value is empty.',
                'text'
            )
        text = doc['text']
        
        try:
            translation = piglatin.convert(text)
        except Exception,e:
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
