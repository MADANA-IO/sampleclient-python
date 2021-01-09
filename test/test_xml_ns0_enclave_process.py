"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.17
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import madana_apiclient
from madana_apiclient.model.xml_ns0_enclave_port import XmlNs0EnclavePort
from madana_apiclient.model.xml_ns0_enclave_process_all_of import XmlNs0EnclaveProcessAllOf
from madana_apiclient.model.xml_ns0_environment import XmlNs0Environment
from madana_apiclient.model.xml_ns0_input_stream import XmlNs0InputStream
from madana_apiclient.model.xml_ns0_kubernetes_enclave import XmlNs0KubernetesEnclave
from madana_apiclient.model.xml_ns0_process import XmlNs0Process
from madana_apiclient.model.xml_ns0_wireguard_interface import XmlNs0WireguardInterface
globals()['XmlNs0EnclavePort'] = XmlNs0EnclavePort
globals()['XmlNs0EnclaveProcessAllOf'] = XmlNs0EnclaveProcessAllOf
globals()['XmlNs0Environment'] = XmlNs0Environment
globals()['XmlNs0InputStream'] = XmlNs0InputStream
globals()['XmlNs0KubernetesEnclave'] = XmlNs0KubernetesEnclave
globals()['XmlNs0Process'] = XmlNs0Process
globals()['XmlNs0WireguardInterface'] = XmlNs0WireguardInterface
from madana_apiclient.model.xml_ns0_enclave_process import XmlNs0EnclaveProcess


class TestXmlNs0EnclaveProcess(unittest.TestCase):
    """XmlNs0EnclaveProcess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testXmlNs0EnclaveProcess(self):
        """Test XmlNs0EnclaveProcess"""
        # FIXME: construct object with mandatory attributes with example values
        # model = XmlNs0EnclaveProcess()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
