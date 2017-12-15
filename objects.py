class Cluster:
    def __init__(self, name, description='', url, service, host):
        self.name = name
        self.description = description
        self.url = url
        self.service = service
        self.host = host

class Host:
    def __init__(self, fqdn, cluster='', url):
        self.fqdn = fqdn
        self.cluster = cluster
        self.url = url

class Service:
    def __init__(self, name, version, desciption, url):
        self.name = name
        self.version = version
        self.description = desciption
        self.url = url

class HostService():
    def __init__(self, cluster, host, service, component, state=''):
        self.cluster = cluster
        self.host = host
        self.service = service
        self.component = component
        self.state = state

class Task:
    def __init__(self, cluster, service, action, status=''):
        self.cluster = cluster
        self.service = service
        self.action = action
        self.status = status
