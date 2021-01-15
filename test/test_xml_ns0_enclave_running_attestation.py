"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.30
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import madana_apiclient
from madana_apiclient.model.xml_ns0_enclave_process import XmlNs0EnclaveProcess
from madana_apiclient.model.xml_ns0_enclave_running_attestation_all_of import XmlNs0EnclaveRunningAttestationAllOf
from madana_apiclient.model.xml_ns0_node_info import XmlNs0NodeInfo
globals()['XmlNs0EnclaveProcess'] = XmlNs0EnclaveProcess
globals()['XmlNs0EnclaveRunningAttestationAllOf'] = XmlNs0EnclaveRunningAttestationAllOf
globals()['XmlNs0NodeInfo'] = XmlNs0NodeInfo
from madana_apiclient.model.xml_ns0_enclave_running_attestation import XmlNs0EnclaveRunningAttestation


class TestXmlNs0EnclaveRunningAttestation(unittest.TestCase):
    """XmlNs0EnclaveRunningAttestation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testXmlNs0EnclaveRunningAttestation(self):
        """Test XmlNs0EnclaveRunningAttestation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = XmlNs0EnclaveRunningAttestation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
