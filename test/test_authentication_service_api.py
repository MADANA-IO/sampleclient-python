"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.5.0-master.41
    Generated by: https://openapi-generator.tech
"""


import unittest

import madana_apiclient
from madana_apiclient.api.authentication_service_api import AuthenticationServiceApi  # noqa: E501


class TestAuthenticationServiceApi(unittest.TestCase):
    """AuthenticationServiceApi unit test stubs"""

    def setUp(self):
        self.api = AuthenticationServiceApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_authenticate_application(self):
        """Test case for authenticate_application

        Authenticates a new application and returns the token.  # noqa: E501
        """
        pass

    def test_authenticate_ethereum_wallet(self):
        """Test case for authenticate_ethereum_wallet

        """
        pass

    def test_authenticate_user(self):
        """Test case for authenticate_user

        Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated ).  # noqa: E501
        """
        pass

    def test_authenticate_with_ethereum_challenge(self):
        """Test case for authenticate_with_ethereum_challenge

        """
        pass

    def test_get_fractal_authentication_url(self):
        """Test case for get_fractal_authentication_url

        Returns the AUthorization URL to verify a Twitter Accounts.  # noqa: E501
        """
        pass

    def test_get_nonce_for_ethereum_wallet(self):
        """Test case for get_nonce_for_ethereum_wallet

        Returns a nonce for the client which is used as content for the to be created signature.  # noqa: E501
        """
        pass

    def test_get_object(self):
        """Test case for get_object

        Used to validate the active connection with the API.  # noqa: E501
        """
        pass

    def test_get_twitter_authentication_url(self):
        """Test case for get_twitter_authentication_url

        Returns the AUthorization URL to verify a Twitter Accounts.  # noqa: E501
        """
        pass

    def test_set_facebook_uid(self):
        """Test case for set_facebook_uid

        Used as Callback URL when users have successfully authorized their facbeook account.  # noqa: E501
        """
        pass

    def test_set_fractal_uid(self):
        """Test case for set_fractal_uid

        """
        pass

    def test_set_twitter_uid(self):
        """Test case for set_twitter_uid

        """
        pass


if __name__ == '__main__':
    unittest.main()
