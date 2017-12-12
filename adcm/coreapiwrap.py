import coreapi


class ADCMApiWrapper():

    api_url = "/api/v1/"

    def __init__(self, url, username, password):
        # Basic auth only
        auth = coreapi.auth.BasicAuthentication(
            username=username,
            password=password
        )
        self.client = coreapi.Client(auth=auth)
        self.url = url

    def connect(self):
        self.schema = self.client.get("{}{}schema/".format(self.url, self.api_url))

    def action(self, *args, **kvargs):
        return self.client.action(self.schema, *args, **kvargs)
