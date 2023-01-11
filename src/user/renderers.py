from rest_framework import renderers
import json

#show errors for the blank email and password fields

class UserRenderer(renderers.JSONRenderer):
    charset='utf-8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response=''
        if 'EroorDetail' in str(data):
            response=json.dumps ({'erros':data})
        else:
            response=json.dumps(data)
        return response