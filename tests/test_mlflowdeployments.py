
from databrickslabs_mlflowdepl import dev_cicd_pipeline
from databrickslabs_mlflowdepl import release_cicd_pipeline
from databrickslabs_mlflowdepl import cluster_and_libraries
from databrickslabs_mlflowdepl import deployment
import unittest

class TestMlflowDeployments(unittest.TestCase):

    def test_dev_cicd_pipeline(self):
        dev_cicd_pipeline.main('mytest/integration')

    def test_create_prod_jobs(self):
        release_cicd_pipeline.main('', 'mytest', False)

    def test_create_cluster_with_libs(self):
        cluster_and_libraries.main('mytest', 'pipeline1', None)


if __name__ == '__main__':
    unittest.main()
