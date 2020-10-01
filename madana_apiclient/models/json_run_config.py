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


class JsonRunConfig(object):
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
        'args': 'list[str]',
        'disk_config': 'list[JsonDiskConfig]',
        'run': 'str',
        'environment': 'dict(str, str)'
    }

    attribute_map = {
        'args': 'args',
        'disk_config': 'disk_config',
        'run': 'run',
        'environment': 'environment'
    }

    def __init__(self, args=None, disk_config=None, run=None, environment=None, local_vars_configuration=None):  # noqa: E501
        """JsonRunConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._disk_config = None
        self._run = None
        self._environment = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if disk_config is not None:
            self.disk_config = disk_config
        if run is not None:
            self.run = run
        if environment is not None:
            self.environment = environment

    @property
    def args(self):
        """Gets the args of this JsonRunConfig.  # noqa: E501

          # noqa: E501

        :return: The args of this JsonRunConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this JsonRunConfig.

          # noqa: E501

        :param args: The args of this JsonRunConfig.  # noqa: E501
        :type args: list[str]
        """

        self._args = args

    @property
    def disk_config(self):
        """Gets the disk_config of this JsonRunConfig.  # noqa: E501

          # noqa: E501

        :return: The disk_config of this JsonRunConfig.  # noqa: E501
        :rtype: list[JsonDiskConfig]
        """
        return self._disk_config

    @disk_config.setter
    def disk_config(self, disk_config):
        """Sets the disk_config of this JsonRunConfig.

          # noqa: E501

        :param disk_config: The disk_config of this JsonRunConfig.  # noqa: E501
        :type disk_config: list[JsonDiskConfig]
        """

        self._disk_config = disk_config

    @property
    def run(self):
        """Gets the run of this JsonRunConfig.  # noqa: E501

          # noqa: E501

        :return: The run of this JsonRunConfig.  # noqa: E501
        :rtype: str
        """
        return self._run

    @run.setter
    def run(self, run):
        """Sets the run of this JsonRunConfig.

          # noqa: E501

        :param run: The run of this JsonRunConfig.  # noqa: E501
        :type run: str
        """

        self._run = run

    @property
    def environment(self):
        """Gets the environment of this JsonRunConfig.  # noqa: E501

          # noqa: E501

        :return: The environment of this JsonRunConfig.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this JsonRunConfig.

          # noqa: E501

        :param environment: The environment of this JsonRunConfig.  # noqa: E501
        :type environment: dict(str, str)
        """

        self._environment = environment

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
        if not isinstance(other, JsonRunConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonRunConfig):
            return True

        return self.to_dict() != other.to_dict()
