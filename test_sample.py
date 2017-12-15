from adcm.basic_methods import ClusterMethods


class TestSample:
    def test_create_cluster(self, cluster_name):
        c = ClusterMethods()
        actual = c.create_cluster(cluster_name)
        expected = c.get_cluster_details(cluster_name)
        assert actual == expected


obj = TestSample()
obj.test_create_cluster('newSampleCluster2')
