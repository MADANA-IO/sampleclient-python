"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.39
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import madana_apiclient
from madana_apiclient.model.json_enclave_port import JsonEnclavePort
from madana_apiclient.model.json_environment import JsonEnvironment
from madana_apiclient.model.json_kubernetes_enclave import JsonKubernetesEnclave
from madana_apiclient.model.json_process import JsonProcess
from madana_apiclient.model.json_wireguard_interface import JsonWireguardInterface
globals()['JsonEnclavePort'] = JsonEnclavePort
globals()['JsonEnvironment'] = JsonEnvironment
globals()['JsonKubernetesEnclave'] = JsonKubernetesEnclave
globals()['JsonProcess'] = JsonProcess
globals()['JsonWireguardInterface'] = JsonWireguardInterface
from madana_apiclient.model.json_enclave_process import JsonEnclaveProcess


class TestJsonEnclaveProcess(unittest.TestCase):
    """JsonEnclaveProcess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testJsonEnclaveProcess(self):
        """Test JsonEnclaveProcess"""
        # FIXME: construct object with mandatory attributes with example values
        # model = JsonEnclaveProcess()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
