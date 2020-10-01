# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15-master.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class XmlNs0EnclaveRunningAttestationAllOf(object):
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
        'enclave_process': 'XmlNs0EnclaveProcess',
        'node_info': 'XmlNs0NodeInfo'
    }

    attribute_map = {
        'enclave_process': 'enclaveProcess',
        'node_info': 'nodeInfo'
    }

    def __init__(self, enclave_process=None, node_info=None, local_vars_configuration=None):  # noqa: E501
        """XmlNs0EnclaveRunningAttestationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enclave_process = None
        self._node_info = None
        self.discriminator = None

        if enclave_process is not None:
            self.enclave_process = enclave_process
        if node_info is not None:
            self.node_info = node_info

    @property
    def enclave_process(self):
        """Gets the enclave_process of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501


        :return: The enclave_process of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501
        :rtype: XmlNs0EnclaveProcess
        """
        return self._enclave_process

    @enclave_process.setter
    def enclave_process(self, enclave_process):
        """Sets the enclave_process of this XmlNs0EnclaveRunningAttestationAllOf.


        :param enclave_process: The enclave_process of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501
        :type enclave_process: XmlNs0EnclaveProcess
        """

        self._enclave_process = enclave_process

    @property
    def node_info(self):
        """Gets the node_info of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501


        :return: The node_info of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501
        :rtype: XmlNs0NodeInfo
        """
        return self._node_info

    @node_info.setter
    def node_info(self, node_info):
        """Sets the node_info of this XmlNs0EnclaveRunningAttestationAllOf.


        :param node_info: The node_info of this XmlNs0EnclaveRunningAttestationAllOf.  # noqa: E501
        :type node_info: XmlNs0NodeInfo
        """

        self._node_info = node_info

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
        if not isinstance(other, XmlNs0EnclaveRunningAttestationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlNs0EnclaveRunningAttestationAllOf):
            return True

        return self.to_dict() != other.to_dict()
