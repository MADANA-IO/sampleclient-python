# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import madana_apiclient
from madana_apiclient.models.xml_ns0_mdn_user_profile_image_all_of import XmlNs0MDNUserProfileImageAllOf  # noqa: E501
from madana_apiclient.rest import ApiException

class TestXmlNs0MDNUserProfileImageAllOf(unittest.TestCase):
    """XmlNs0MDNUserProfileImageAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test XmlNs0MDNUserProfileImageAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = madana_apiclient.models.xml_ns0_mdn_user_profile_image_all_of.XmlNs0MDNUserProfileImageAllOf()  # noqa: E501
        if include_optional :
            return XmlNs0MDNUserProfileImageAllOf(
                id = '0', 
                image = '0'
            )
        else :
            return XmlNs0MDNUserProfileImageAllOf(
        )

    def testXmlNs0MDNUserProfileImageAllOf(self):
        """Test XmlNs0MDNUserProfileImageAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
