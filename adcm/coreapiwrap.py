import coreapi
import requests


class ADCMApiWrapper():

    api_url = "/api/v1/"

    # def __init__(self, url, username, password):
    #     # Basic auth only
    #     auth = coreapi.auth.BasicAuthentication(
    #         username=username,
    #         password=password
    #     )
    #     self.client = coreapi.Client(auth=auth)
    #     self.url = url

    def __init__(self, url, username, password):
        self.client = coreapi.Client()
        self.url = url
        result = requests.request('POST', url + '/api/v1/token/', data={'username': username, 'password': password})
        b = result.json()
        auth = coreapi.auth.TokenAuthentication(
            token=b['token']
        )
        self.client = coreapi.Client(auth=auth)

    def connect(self):
        self.schema = self.client.get("{}{}schema/".format(self.url, self.api_url))

    def action(self, *args, **kvargs):
        return self.client.action(self.schema, *args, **kvargs)
