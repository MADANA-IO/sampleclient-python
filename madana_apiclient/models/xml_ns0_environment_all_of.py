# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.0.1-master.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class XmlNs0EnvironmentAllOf(object):
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
        'content': 'list[str]',
        'default_run_configuration': 'XmlNs0RunConfig',
        'description': 'str',
        'ipfs_hash': 'str',
        'name': 'str',
        'packages': 'list[str]',
        'published': 'bool',
        'root_hash_offset': 'str',
        'roothash': 'str',
        'size': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'content': 'content',
        'default_run_configuration': 'defaultRunConfiguration',
        'description': 'description',
        'ipfs_hash': 'ipfsHash',
        'name': 'name',
        'packages': 'packages',
        'published': 'published',
        'root_hash_offset': 'rootHashOffset',
        'roothash': 'roothash',
        'size': 'size',
        'uuid': 'uuid'
    }

    def __init__(self, content=None, default_run_configuration=None, description=None, ipfs_hash=None, name=None, packages=None, published=None, root_hash_offset=None, roothash=None, size=None, uuid=None, local_vars_configuration=None):  # noqa: E501
        """XmlNs0EnvironmentAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._content = None
        self._default_run_configuration = None
        self._description = None
        self._ipfs_hash = None
        self._name = None
        self._packages = None
        self._published = None
        self._root_hash_offset = None
        self._roothash = None
        self._size = None
        self._uuid = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if default_run_configuration is not None:
            self.default_run_configuration = default_run_configuration
        if description is not None:
            self.description = description
        if ipfs_hash is not None:
            self.ipfs_hash = ipfs_hash
        if name is not None:
            self.name = name
        if packages is not None:
            self.packages = packages
        if published is not None:
            self.published = published
        if root_hash_offset is not None:
            self.root_hash_offset = root_hash_offset
        if roothash is not None:
            self.roothash = roothash
        if size is not None:
            self.size = size
        if uuid is not None:
            self.uuid = uuid

    @property
    def content(self):
        """Gets the content of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The content of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param content: The content of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: list[str]
        """

        self._content = content

    @property
    def default_run_configuration(self):
        """Gets the default_run_configuration of this XmlNs0EnvironmentAllOf.  # noqa: E501


        :return: The default_run_configuration of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: XmlNs0RunConfig
        """
        return self._default_run_configuration

    @default_run_configuration.setter
    def default_run_configuration(self, default_run_configuration):
        """Sets the default_run_configuration of this XmlNs0EnvironmentAllOf.


        :param default_run_configuration: The default_run_configuration of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: XmlNs0RunConfig
        """

        self._default_run_configuration = default_run_configuration

    @property
    def description(self):
        """Gets the description of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The description of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param description: The description of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ipfs_hash(self):
        """Gets the ipfs_hash of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The ipfs_hash of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ipfs_hash

    @ipfs_hash.setter
    def ipfs_hash(self, ipfs_hash):
        """Sets the ipfs_hash of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param ipfs_hash: The ipfs_hash of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._ipfs_hash = ipfs_hash

    @property
    def name(self):
        """Gets the name of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The name of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param name: The name of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def packages(self):
        """Gets the packages of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The packages of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: list[str]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """Sets the packages of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param packages: The packages of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: list[str]
        """

        self._packages = packages

    @property
    def published(self):
        """Gets the published of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The published of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param published: The published of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def root_hash_offset(self):
        """Gets the root_hash_offset of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The root_hash_offset of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._root_hash_offset

    @root_hash_offset.setter
    def root_hash_offset(self, root_hash_offset):
        """Sets the root_hash_offset of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param root_hash_offset: The root_hash_offset of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._root_hash_offset = root_hash_offset

    @property
    def roothash(self):
        """Gets the roothash of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The roothash of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._roothash

    @roothash.setter
    def roothash(self, roothash):
        """Sets the roothash of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param roothash: The roothash of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._roothash = roothash

    @property
    def size(self):
        """Gets the size of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The size of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param size: The size of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def uuid(self):
        """Gets the uuid of this XmlNs0EnvironmentAllOf.  # noqa: E501

          # noqa: E501

        :return: The uuid of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this XmlNs0EnvironmentAllOf.

          # noqa: E501

        :param uuid: The uuid of this XmlNs0EnvironmentAllOf.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if not isinstance(other, XmlNs0EnvironmentAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlNs0EnvironmentAllOf):
            return True

        return self.to_dict() != other.to_dict()
