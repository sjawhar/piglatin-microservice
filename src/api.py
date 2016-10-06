import falcon
from middleware import RequireJson, JsonTranslator
from piglatin import PigLatinTranslator

class PigLatinProcedure(object):
    def on_post(self, request, response):
        try:
            doc = request.context['doc']
            text = doc['text']
            
            translator = PigLatinTranslator()
            translation = translator.convert(text)
        except KeyError:
            raise falcon.HTTPBadRequest(
                'No text',
                'The request body must contain text to translate.'
            )
        except Exception,e:
            description = None
            if (len(e.args) > 0):
                description = e.args[0]

            raise falcon.HTTPInternalServerError(
                'Server error',
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
