# coding: utf-8

"""
    madana-api

    <h1>Using the madana-api</h1>        <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available         endpoints and used datamodels.   </p>       <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p>   <br>   <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>       <br>  # noqa: E501

    The version of the OpenAPI document: 0.4.15-master.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from madana_apiclient.configuration import Configuration


class JsonMDNAUserObject(object):
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
        'user_name': 'str',
        'activated': 'str',
        'created': 'str',
        'last_active': 'str',
        'image': 'str'
    }

    attribute_map = {
        'user_name': 'userName',
        'activated': 'activated',
        'created': 'created',
        'last_active': 'lastActive',
        'image': 'image'
    }

    def __init__(self, user_name=None, activated=None, created=None, last_active=None, image=None, local_vars_configuration=None):  # noqa: E501
        """JsonMDNAUserObject - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_name = None
        self._activated = None
        self._created = None
        self._last_active = None
        self._image = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if activated is not None:
            self.activated = activated
        if created is not None:
            self.created = created
        if last_active is not None:
            self.last_active = last_active
        if image is not None:
            self.image = image

    @property
    def user_name(self):
        """Gets the user_name of this JsonMDNAUserObject.  # noqa: E501

          # noqa: E501

        :return: The user_name of this JsonMDNAUserObject.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this JsonMDNAUserObject.

          # noqa: E501

        :param user_name: The user_name of this JsonMDNAUserObject.  # noqa: E501
        :type user_name: str
        """

        self._user_name = user_name

    @property
    def activated(self):
        """Gets the activated of this JsonMDNAUserObject.  # noqa: E501

          # noqa: E501

        :return: The activated of this JsonMDNAUserObject.  # noqa: E501
        :rtype: str
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this JsonMDNAUserObject.

          # noqa: E501

        :param activated: The activated of this JsonMDNAUserObject.  # noqa: E501
        :type activated: str
        """

        self._activated = activated

    @property
    def created(self):
        """Gets the created of this JsonMDNAUserObject.  # noqa: E501

          # noqa: E501

        :return: The created of this JsonMDNAUserObject.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this JsonMDNAUserObject.

          # noqa: E501

        :param created: The created of this JsonMDNAUserObject.  # noqa: E501
        :type created: str
        """

        self._created = created

    @property
    def last_active(self):
        """Gets the last_active of this JsonMDNAUserObject.  # noqa: E501

          # noqa: E501

        :return: The last_active of this JsonMDNAUserObject.  # noqa: E501
        :rtype: str
        """
        return self._last_active

    @last_active.setter
    def last_active(self, last_active):
        """Sets the last_active of this JsonMDNAUserObject.

          # noqa: E501

        :param last_active: The last_active of this JsonMDNAUserObject.  # noqa: E501
        :type last_active: str
        """

        self._last_active = last_active

    @property
    def image(self):
        """Gets the image of this JsonMDNAUserObject.  # noqa: E501

          # noqa: E501

        :return: The image of this JsonMDNAUserObject.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this JsonMDNAUserObject.

          # noqa: E501

        :param image: The image of this JsonMDNAUserObject.  # noqa: E501
        :type image: str
        """

        self._image = image

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
        if not isinstance(other, JsonMDNAUserObject):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, JsonMDNAUserObject):
            return True

        return self.to_dict() != other.to_dict()
