# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.0.1-master.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import madana_apiclient
from madana_apiclient.api.account_service_api import AccountServiceApi  # noqa: E501
from madana_apiclient.rest import ApiException


class TestAccountServiceApi(unittest.TestCase):
    """AccountServiceApi unit test stubs"""

    def setUp(self):
        self.api = madana_apiclient.api.account_service_api.AccountServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_user(self):
        """Test case for activate_user

        """
        pass

    def test_create_password_reset(self):
        """Test case for create_password_reset

        Sends an Password reset mail to the given MailAddress.  # noqa: E501
        """
        pass

    def test_request_verification_mail(self):
        """Test case for request_verification_mail

        Used to request a new  activation-mail for the user.  # noqa: E501
        """
        pass

    def test_update_password(self):
        """Test case for update_password

        Receives the Password reset and tries to set the provided password for the user.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
