import falcon
from middleware import RequireJson, JsonTranslator
from piglatin import PigLatinTranslator

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
            translator = PigLatinTranslator()
            translation = translator.convert(text)
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
app = falcon.API(middleware=[
    RequireJson(),
    JsonTranslator(),
])
app.add_route('/piglatin', procedure)
