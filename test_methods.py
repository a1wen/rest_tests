import methods


def test_method():
    cluster = methods.BasicMethods()
    cluster.path = 'cluster'
    cluster.create_cluster('cluster111')
