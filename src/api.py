import falcon
from middleware import RequireJson, JsonTranslator
from piglatin import PigLatinTranslator

class PigLatinProcedure(object):
    def on_post(self, request, response):
        try:
            doc = request.context['doc']
            text = doc['text']
        except KeyError:
            raise falcon.HTTPBadRequest(
                'No text',
                'The request body must contain text to translate.'
            )

        translator = PigLatinTranslator()
        response.status = falcon.HTTP_200
        request.context['result'] = {'translation': translator.convert(text)}

procedure = PigLatinProcedure()
app = falcon.API(middleware=[
    RequireJson(),
    JsonTranslator(),
])
app.add_route('/piglatin', procedure)
