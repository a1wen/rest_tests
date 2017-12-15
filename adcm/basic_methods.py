from adcm.coreapiwrap import ADCMApiWrapper

a = ADCMApiWrapper('http://localhost:8040', 'admin', 'admin')
a.connect()


class Methods:

    def create(self, apitype, cluster_name, description=''):
        print(a.schema)
        result = a.action([apitype, 'create'], params={'name': cluster_name, 'description': description})
        return result

    def get_list_of(self, apitype):
        result = a.action([apitype, 'list'])
        return result

    def get_details_of(self, apitype, cluster_name):
        result = a.action([apitype, 'read'], params={'cluster_name': cluster_name})
        return result

    def delete(self, apitype, cluster_name):
        result = a.action([apitype, 'delete'], params={'cluster_name': cluster_name})
        return result


class ClusterMethods(Methods):
    def create_cluster(self, cluster_name, description=''):
        return self.create('cluster', cluster_name, description)

    def get_cluster_list(self):
        return self.get_list_of('cluster')

    def get_cluster_details(self, cluster_name):
        return self.get_details_of('cluster', cluster_name)

    def delete_cluster(self, cluster_name):
        return self.delete('cluster', cluster_name)

    def get_cluster_service_list(self, cluster_name):
        print(a.url)


class HostMethods:

    def create_host(self, fqdn, cluster):
        result = a.action(['host', 'create'], params={'fqdn': fqdn, 'cluster': cluster})
        return result

    def get_host_list(self):
        result = a.action(['host', 'list'])
        return result

    def get_host_details(self, host):
        result = a.action(['host', 'read'], params={'fqdn': host})
        return result

    def delete_host(self, host):
        result = a.action(['host', 'delete'], params={'fqdn': host})
        return result


class ServiceMethods:

    def get_service_list(self):
        result = a.action(['service', 'list'])
        return result

    def get_service_details(self, service):
        result = a.action(['service', 'read'], params={'name': service})
        return result

    def delete_service(self, service):
        result = a.action(['service', 'delete'], params={'name': service})
        return result


class HostserviceMethods:
    def get_hostservice_list(self):
        result = a.action(['hostservice', 'list'])
        return result

    def create_hostservice(self, cluster, host, service, component, state=''):
        result = a.action(['hostservice', 'create'], params={'cluster': cluster, 'host': host,
                                                             'service': service, 'component': component,
                                                             'state': state})
        return result

    def get_hostservice_details(self, hostservice_id):
        result = a.action(['hostservice', 'read'], params={'id': hostservice_id})
        return result

    def delete_hostservice(self, hostservice_id):
        result = a.action(['hostservice', 'delete'], params={'id': hostservice_id})
        return result


class TaskMethods:

    def get_task_list(self):
        result = a.action(['task', 'list'])
        return result

    def create_task(self, cluster, service, action, state=''):
        result = a.action(['task', 'create'], params={'cluster': cluster, 'service': service,
                                                      'action': action, 'state': state})
        return result

    def get_task_details(self, task_id):
        result = a.action(['task', 'create'], params={'id': task_id})
        return result


class StackMethods:

    def get_stack_list(self):
        result = a.action(['stack', 'list'])
        return result

    def load_stack(self):
        result = a.action(['stack', 'update'])
        return result

    def update_stack(self):
        return self.load_stack()



# def test_create_cluster():
#     bb = Cluster()
#     print(bb.create_cluster('newClusterName7', 'NewClusterName description'))
#
#
# def test_create_invalid_name_cluster(invalid_name):
#     obj = Cluster()
#     print(obj.create_cluster(invalid_name, 'asdfsadfasdf'))
