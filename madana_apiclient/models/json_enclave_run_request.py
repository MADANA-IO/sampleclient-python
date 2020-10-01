# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15-master.4
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class JsonEnclaveRunRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'enclave_execution_type': 'str',
        'wireguard_public_key': 'str',
        'environment_uuid': 'str',
        'using_default_run_config': 'bool'
    }

    attribute_map = {
        'enclave_execution_type': 'enclaveExecutionType',
        'wireguard_public_key': 'wireguardPublicKey',
        'environment_uuid': 'environmentUUID',
        'using_default_run_config': 'usingDefaultRunConfig'
    }

    def __init__(self, enclave_execution_type=None, wireguard_public_key=None, environment_uuid=None, using_default_run_config=None, local_vars_configuration=None):  # noqa: E501
        """JsonEnclaveRunRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enclave_execution_type = None
        self._wireguard_public_key = None
        self._environment_uuid = None
        self._using_default_run_config = None
        self.discriminator = None

        if enclave_execution_type is not None:
            self.enclave_execution_type = enclave_execution_type
        if wireguard_public_key is not None:
            self.wireguard_public_key = wireguard_public_key
        if environment_uuid is not None:
            self.environment_uuid = environment_uuid
        if using_default_run_config is not None:
            self.using_default_run_config = using_default_run_config

    @property
    def enclave_execution_type(self):
        """Gets the enclave_execution_type of this JsonEnclaveRunRequest.  # noqa: E501

          # noqa: E501

        :return: The enclave_execution_type of this JsonEnclaveRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._enclave_execution_type

    @enclave_execution_type.setter
    def enclave_execution_type(self, enclave_execution_type):
        """Sets the enclave_execution_type of this JsonEnclaveRunRequest.

          # noqa: E501

        :param enclave_execution_type: The enclave_execution_type of this JsonEnclaveRunRequest.  # noqa: E501
        :type enclave_execution_type: str
        """

        self._enclave_execution_type = enclave_execution_type

    @property
    def wireguard_public_key(self):
        """Gets the wireguard_public_key of this JsonEnclaveRunRequest.  # noqa: E501

          # noqa: E501

        :return: The wireguard_public_key of this JsonEnclaveRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._wireguard_public_key

    @wireguard_public_key.setter
    def wireguard_public_key(self, wireguard_public_key):
        """Sets the wireguard_public_key of this JsonEnclaveRunRequest.

          # noqa: E501

        :param wireguard_public_key: The wireguard_public_key of this JsonEnclaveRunRequest.  # noqa: E501
        :type wireguard_public_key: str
        """

        self._wireguard_public_key = wireguard_public_key

    @property
    def environment_uuid(self):
        """Gets the environment_uuid of this JsonEnclaveRunRequest.  # noqa: E501

          # noqa: E501

        :return: The environment_uuid of this JsonEnclaveRunRequest.  # noqa: E501
        :rtype: str
        """
        return self._environment_uuid

    @environment_uuid.setter
    def environment_uuid(self, environment_uuid):
        """Sets the environment_uuid of this JsonEnclaveRunRequest.

          # noqa: E501

        :param environment_uuid: The environment_uuid of this JsonEnclaveRunRequest.  # noqa: E501
        :type environment_uuid: str
        """

        self._environment_uuid = environment_uuid

    @property
    def using_default_run_config(self):
        """Gets the using_default_run_config of this JsonEnclaveRunRequest.  # noqa: E501

          # noqa: E501

        :return: The using_default_run_config of this JsonEnclaveRunRequest.  # noqa: E501
        :rtype: bool
        """
        return self._using_default_run_config

    @using_default_run_config.setter
    def using_default_run_config(self, using_default_run_config):
        """Sets the using_default_run_config of this JsonEnclaveRunRequest.

          # noqa: E501

        :param using_default_run_config: The using_default_run_config of this JsonEnclaveRunRequest.  # noqa: E501
        :type using_default_run_config: bool
        """

        self._using_default_run_config = using_default_run_config

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JsonEnclaveRunRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonEnclaveRunRequest):
            return True

        return self.to_dict() != other.to_dict()
