import falcon

class PigLatinProcedure(object):
    def on_post(self, request, response):
        # Return error if request does not contain a word
        response.status = falcon.HTTP_200
        response.body = 'Hello world!'

procedure = PigLatinProcedure()
app = falcon.API()
app.add_route('/piglatin', procedure)
