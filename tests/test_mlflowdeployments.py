
from databrickslabs_mlflowdepl import dev_cicd_pipeline
from databrickslabs_mlflowdepl import release_cicd_pipeline
from databrickslabs_mlflowdepl import cluster_and_libraries
from databrickslabs_mlflowdepl import deployment
import unittest

class TestMlflowDeployments(unittest.TestCase):
    def test_dev_cicd_pipeline(self):
        dev_cicd_pipeline.main('tests/integration')

    def test_create_prod_jobs(self):
        release_cicd_pipeline.main('', 'tests', False)

    def test_create_cluster_with_libs(self):
        cluster_and_libraries.main('tests/integration', 'pipeline1', None)

    """
        def test_install_libs(self):
        api_client = deployment.getDatabricksAPIClient()
        job_spec = check_if_dir_is_pipeline_def('dev-tests/pipeline1', 'aws')
        cluster_id = deployment.create_cluster(api_client, job_spec)
        deployment.wait_for_cluster_to_start(api_client, cluster_id)
        cluster_and_libraries.main('dev-tests', 'pipeline1', cluster_id)
    """

if __name__ == '__main__':
    unittest.main()
