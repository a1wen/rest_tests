import requests
import pytest
import json

DEFAULT_HEADER = 'application/json'
BASICAUTH = 'Basic YWRtaW46YWRtaW4='


class BasicMethods:
    def __init__(self, *a):
        super(BasicMethods, self).__init__(*a)
        self.host = '104.155.2.103:8000/api/v1'
        self.path = a
        self.url = 'http://{}/{}/'.format(self.host, self.path)

    def _create_(self, path, name, description, headers=DEFAULT_HEADER, authorization=BASICAUTH):
        _headers = {'content-type': headers, 'authorization': authorization}
        _payload = json.dumps({'name': name, 'description': description})
        _response = requests.post(self.url, data=_payload, headers=_headers)
        return _response.status_code, _response.json()

    def _get_list_of_(self, path, headers=DEFAULT_HEADER, authorization=BASICAUTH):
        _headers = {'content-type': headers, 'authorization': authorization}
        _response = requests.get(self.url, headers=_headers)
        return _response.status_code, _response.json()

    def _get_details_of(self, path, name, headers=DEFAULT_HEADER, authorization=BASICAUTH):
        _headers = {'content-type': headers, 'authorization': authorization}
        _response = requests.get(self.url, name, headers=_headers)
        return _response.status_code, _response.json()

    def _delete_(self, path, name, headers=DEFAULT_HEADER, authorization=BASICAUTH):
        _headers = {'content-type': headers, 'authorization': authorization}
        _response = requests.delete(self.url, name, headers=_headers)
        return _response.status_code, _response.json()

    def create_cluster(self, path):
        self.path = path
        return self._create_('cluster', 'newCluster2', 'Description')

a = BasicMethods()
print(a.__dict__)
