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


class XmlNs0EnclaveProcessAllOf(object):
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
        'attestation_server': 'str',
        'console_output': 'str',
        'enclave_ident': 'str',
        'enclave_inputstream': 'XmlNs0InputStream',
        'ending_time': 'str',
        'environment': 'XmlNs0Environment',
        'internal_attesation_server': 'str',
        'internal_ident': 'str',
        'internal_remote_control_server': 'str',
        'process': 'XmlNs0Process',
        'public_ident': 'str',
        'remote_control_server': 'str',
        'signer_ident': 'str',
        'startup_cmd': 'str',
        'startup_time': 'str',
        'status': 'str',
        'wg_interface': 'XmlNs0WireguardInterface',
        'wireguard_public_key': 'str'
    }

    attribute_map = {
        'attestation_server': 'attestationServer',
        'console_output': 'consoleOutput',
        'enclave_ident': 'enclaveIdent',
        'enclave_inputstream': 'enclaveInputstream',
        'ending_time': 'endingTime',
        'environment': 'environment',
        'internal_attesation_server': 'internalAttesationServer',
        'internal_ident': 'internalIdent',
        'internal_remote_control_server': 'internalRemoteControlServer',
        'process': 'process',
        'public_ident': 'publicIdent',
        'remote_control_server': 'remoteControlServer',
        'signer_ident': 'signerIdent',
        'startup_cmd': 'startupCMD',
        'startup_time': 'startupTime',
        'status': 'status',
        'wg_interface': 'wgInterface',
        'wireguard_public_key': 'wireguardPublicKey'
    }

    def __init__(self, attestation_server=None, console_output=None, enclave_ident=None, enclave_inputstream=None, ending_time=None, environment=None, internal_attesation_server=None, internal_ident=None, internal_remote_control_server=None, process=None, public_ident=None, remote_control_server=None, signer_ident=None, startup_cmd=None, startup_time=None, status=None, wg_interface=None, wireguard_public_key=None, local_vars_configuration=None):  # noqa: E501
        """XmlNs0EnclaveProcessAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._attestation_server = None
        self._console_output = None
        self._enclave_ident = None
        self._enclave_inputstream = None
        self._ending_time = None
        self._environment = None
        self._internal_attesation_server = None
        self._internal_ident = None
        self._internal_remote_control_server = None
        self._process = None
        self._public_ident = None
        self._remote_control_server = None
        self._signer_ident = None
        self._startup_cmd = None
        self._startup_time = None
        self._status = None
        self._wg_interface = None
        self._wireguard_public_key = None
        self.discriminator = None

        if attestation_server is not None:
            self.attestation_server = attestation_server
        if console_output is not None:
            self.console_output = console_output
        if enclave_ident is not None:
            self.enclave_ident = enclave_ident
        if enclave_inputstream is not None:
            self.enclave_inputstream = enclave_inputstream
        if ending_time is not None:
            self.ending_time = ending_time
        if environment is not None:
            self.environment = environment
        if internal_attesation_server is not None:
            self.internal_attesation_server = internal_attesation_server
        if internal_ident is not None:
            self.internal_ident = internal_ident
        if internal_remote_control_server is not None:
            self.internal_remote_control_server = internal_remote_control_server
        if process is not None:
            self.process = process
        if public_ident is not None:
            self.public_ident = public_ident
        if remote_control_server is not None:
            self.remote_control_server = remote_control_server
        if signer_ident is not None:
            self.signer_ident = signer_ident
        if startup_cmd is not None:
            self.startup_cmd = startup_cmd
        if startup_time is not None:
            self.startup_time = startup_time
        if status is not None:
            self.status = status
        if wg_interface is not None:
            self.wg_interface = wg_interface
        if wireguard_public_key is not None:
            self.wireguard_public_key = wireguard_public_key

    @property
    def attestation_server(self):
        """Gets the attestation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The attestation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._attestation_server

    @attestation_server.setter
    def attestation_server(self, attestation_server):
        """Sets the attestation_server of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param attestation_server: The attestation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._attestation_server = attestation_server

    @property
    def console_output(self):
        """Gets the console_output of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The console_output of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._console_output

    @console_output.setter
    def console_output(self, console_output):
        """Sets the console_output of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param console_output: The console_output of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._console_output = console_output

    @property
    def enclave_ident(self):
        """Gets the enclave_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The enclave_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._enclave_ident

    @enclave_ident.setter
    def enclave_ident(self, enclave_ident):
        """Sets the enclave_ident of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param enclave_ident: The enclave_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._enclave_ident = enclave_ident

    @property
    def enclave_inputstream(self):
        """Gets the enclave_inputstream of this XmlNs0EnclaveProcessAllOf.  # noqa: E501


        :return: The enclave_inputstream of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: XmlNs0InputStream
        """
        return self._enclave_inputstream

    @enclave_inputstream.setter
    def enclave_inputstream(self, enclave_inputstream):
        """Sets the enclave_inputstream of this XmlNs0EnclaveProcessAllOf.


        :param enclave_inputstream: The enclave_inputstream of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: XmlNs0InputStream
        """

        self._enclave_inputstream = enclave_inputstream

    @property
    def ending_time(self):
        """Gets the ending_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The ending_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._ending_time

    @ending_time.setter
    def ending_time(self, ending_time):
        """Sets the ending_time of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param ending_time: The ending_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._ending_time = ending_time

    @property
    def environment(self):
        """Gets the environment of this XmlNs0EnclaveProcessAllOf.  # noqa: E501


        :return: The environment of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: XmlNs0Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this XmlNs0EnclaveProcessAllOf.


        :param environment: The environment of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: XmlNs0Environment
        """

        self._environment = environment

    @property
    def internal_attesation_server(self):
        """Gets the internal_attesation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The internal_attesation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._internal_attesation_server

    @internal_attesation_server.setter
    def internal_attesation_server(self, internal_attesation_server):
        """Sets the internal_attesation_server of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param internal_attesation_server: The internal_attesation_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._internal_attesation_server = internal_attesation_server

    @property
    def internal_ident(self):
        """Gets the internal_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The internal_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._internal_ident

    @internal_ident.setter
    def internal_ident(self, internal_ident):
        """Sets the internal_ident of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param internal_ident: The internal_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._internal_ident = internal_ident

    @property
    def internal_remote_control_server(self):
        """Gets the internal_remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The internal_remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._internal_remote_control_server

    @internal_remote_control_server.setter
    def internal_remote_control_server(self, internal_remote_control_server):
        """Sets the internal_remote_control_server of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param internal_remote_control_server: The internal_remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._internal_remote_control_server = internal_remote_control_server

    @property
    def process(self):
        """Gets the process of this XmlNs0EnclaveProcessAllOf.  # noqa: E501


        :return: The process of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: XmlNs0Process
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this XmlNs0EnclaveProcessAllOf.


        :param process: The process of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: XmlNs0Process
        """

        self._process = process

    @property
    def public_ident(self):
        """Gets the public_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The public_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._public_ident

    @public_ident.setter
    def public_ident(self, public_ident):
        """Sets the public_ident of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param public_ident: The public_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._public_ident = public_ident

    @property
    def remote_control_server(self):
        """Gets the remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._remote_control_server

    @remote_control_server.setter
    def remote_control_server(self, remote_control_server):
        """Sets the remote_control_server of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param remote_control_server: The remote_control_server of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._remote_control_server = remote_control_server

    @property
    def signer_ident(self):
        """Gets the signer_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The signer_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._signer_ident

    @signer_ident.setter
    def signer_ident(self, signer_ident):
        """Sets the signer_ident of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param signer_ident: The signer_ident of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._signer_ident = signer_ident

    @property
    def startup_cmd(self):
        """Gets the startup_cmd of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The startup_cmd of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._startup_cmd

    @startup_cmd.setter
    def startup_cmd(self, startup_cmd):
        """Sets the startup_cmd of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param startup_cmd: The startup_cmd of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._startup_cmd = startup_cmd

    @property
    def startup_time(self):
        """Gets the startup_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The startup_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._startup_time

    @startup_time.setter
    def startup_time(self, startup_time):
        """Sets the startup_time of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param startup_time: The startup_time of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._startup_time = startup_time

    @property
    def status(self):
        """Gets the status of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The status of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param status: The status of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def wg_interface(self):
        """Gets the wg_interface of this XmlNs0EnclaveProcessAllOf.  # noqa: E501


        :return: The wg_interface of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: XmlNs0WireguardInterface
        """
        return self._wg_interface

    @wg_interface.setter
    def wg_interface(self, wg_interface):
        """Sets the wg_interface of this XmlNs0EnclaveProcessAllOf.


        :param wg_interface: The wg_interface of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: XmlNs0WireguardInterface
        """

        self._wg_interface = wg_interface

    @property
    def wireguard_public_key(self):
        """Gets the wireguard_public_key of this XmlNs0EnclaveProcessAllOf.  # noqa: E501

          # noqa: E501

        :return: The wireguard_public_key of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :rtype: str
        """
        return self._wireguard_public_key

    @wireguard_public_key.setter
    def wireguard_public_key(self, wireguard_public_key):
        """Sets the wireguard_public_key of this XmlNs0EnclaveProcessAllOf.

          # noqa: E501

        :param wireguard_public_key: The wireguard_public_key of this XmlNs0EnclaveProcessAllOf.  # noqa: E501
        :type: str
        """

        self._wireguard_public_key = wireguard_public_key

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
        if not isinstance(other, XmlNs0EnclaveProcessAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, XmlNs0EnclaveProcessAllOf):
            return True

        return self.to_dict() != other.to_dict()
