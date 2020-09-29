# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.0.1-master.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import madana_apiclient
from madana_apiclient.models.json_enclave_process import JsonEnclaveProcess  # noqa: E501
from madana_apiclient.rest import ApiException

class TestJsonEnclaveProcess(unittest.TestCase):
    """JsonEnclaveProcess unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JsonEnclaveProcess
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = madana_apiclient.models.json_enclave_process.JsonEnclaveProcess()  # noqa: E501
        if include_optional :
            return JsonEnclaveProcess(
                wireguard_server = '0', 
                internal_remote_control_server = '0', 
                console_output = '0', 
                attestation_server = '0', 
                environment = {size=..., published=true, defaultRunConfiguration={args=[..., ...], disk_config=[{readonly=true, disk=..., roothash_offset=12345, roothash=...}, {readonly=true, disk=..., roothash_offset=12345, roothash=...}], run=..., environment={property1=..., property2=...}}, content=[..., ...], name=..., uuid=..., packages=[..., ...], rootHashOffset=..., ipfsHash=..., roothash=..., description=...}, 
                enclave_ident = '0', 
                public_ident = '0', 
                process = {outputStream={}, errorStream={}, inputStream={}, alive=true}, 
                ending_time = '0', 
                status = '0', 
                internal_wireguard_server = '0', 
                enclave_inputstream = {}, 
                wireguard_public_key = '0', 
                startup_cmd = '0', 
                internal_attesation_server = '0', 
                wg_interface = null, 
                signer_ident = '0', 
                internal_ident = '0', 
                remote_control_server = '0', 
                startup_time = '0'
            )
        else :
            return JsonEnclaveProcess(
        )

    def testJsonEnclaveProcess(self):
        """Test JsonEnclaveProcess"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
