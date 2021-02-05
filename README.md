# madana-apiclient
<h1>Using the madana-api</h1>
       <p>This documentation contains a Quickstart Guide, relating client functionality and information about the available 
       endpoints and used datamodels.   </p>    

 <p> The madana-api and its implementations are still in heavy development. This means that there may be problems in our protocols, or there may be mistakes in our implementations. We take security vulnerabilities very seriously. If you discover a security issue, please bring it to our attention right away! If you find a vulnerability that may affect live deployments -- for example, by exposing a remote execution exploit -- please send your report privately to info@madana.io. Please DO NOT file a public issue. If the issue is a protocol weakness that cannot be immediately exploited or something not yet deployed, just discuss it openly   </p> 
 <br>
  <p> Note: Not all functionality might be acessible without having accquired and api-license token. For more information visit <a href=\"https://www.madana.io\">www.madana.io</a> </p>    
  <br>

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.5.0-master.48
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https:////.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https:////.git`)

Then import the package:
```python
import madana_apiclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import madana_apiclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import madana_apiclient
from pprint import pprint
from madana_apiclient.api import account_service_api
from madana_apiclient.model.json_mdn_mail_address import JsonMDNMailAddress
from madana_apiclient.model.json_mdn_password_reset import JsonMDNPasswordReset
# Defining the host is optional and defaults to http://api.madana.io/rest
# See configuration.py for a list of all supported configuration parameters.
configuration = madana_apiclient.Configuration(
    host = "http://api.madana.io/rest"
)



# Enter a context with an instance of the API client
with madana_apiclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_service_api.AccountServiceApi(api_client)
    token = "token_example" # str | 

    try:
        api_response = api_instance.activate_user(token)
        pprint(api_response)
    except madana_apiclient.ApiException as e:
        print("Exception when calling AccountServiceApi->activate_user: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://api.madana.io/rest*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountServiceApi* | [**activate_user**](docs/AccountServiceApi.md#activate_user) | **GET** /account/activation/{token} | 
*AccountServiceApi* | [**create_password_reset**](docs/AccountServiceApi.md#create_password_reset) | **POST** /account/password | Sends an Password reset mail to the given MailAddress.
*AccountServiceApi* | [**request_verification_mail**](docs/AccountServiceApi.md#request_verification_mail) | **GET** /account/verifymail | Used to request a new  activation-mail for the user.
*AccountServiceApi* | [**update_password**](docs/AccountServiceApi.md#update_password) | **PUT** /account/password | Receives the Password reset and tries to set the provided password for the user.
*AuthenticationServiceApi* | [**authenticate_application**](docs/AuthenticationServiceApi.md#authenticate_application) | **POST** /authentication/application | Authenticates a new application and returns the token.
*AuthenticationServiceApi* | [**authenticate_ethereum_wallet**](docs/AuthenticationServiceApi.md#authenticate_ethereum_wallet) | **POST** /authentication/ethereum/{wallet} | 
*AuthenticationServiceApi* | [**authenticate_user**](docs/AuthenticationServiceApi.md#authenticate_user) | **POST** /authentication | Authenticates a new user and returns the token (  forbidden if the credentials cannot be validated ).
*AuthenticationServiceApi* | [**authenticate_with_ethereum_challenge**](docs/AuthenticationServiceApi.md#authenticate_with_ethereum_challenge) | **POST** /authentication/ethereum/{wallet}/challenge | 
*AuthenticationServiceApi* | [**get_fractal_authentication_url**](docs/AuthenticationServiceApi.md#get_fractal_authentication_url) | **GET** /authentication/fractal | Returns the AUthorization URL to verify a Twitter Accounts.
*AuthenticationServiceApi* | [**get_nonce_for_ethereum_wallet**](docs/AuthenticationServiceApi.md#get_nonce_for_ethereum_wallet) | **GET** /authentication/ethereum/{wallet} | Returns a nonce for the client which is used as content for the to be created signature.
*AuthenticationServiceApi* | [**get_object**](docs/AuthenticationServiceApi.md#get_object) | **GET** /authentication | Used to validate the active connection with the API.
*AuthenticationServiceApi* | [**get_twitter_authentication_url**](docs/AuthenticationServiceApi.md#get_twitter_authentication_url) | **GET** /authentication/twitter | Returns the AUthorization URL to verify a Twitter Accounts.
*AuthenticationServiceApi* | [**set_facebook_uid**](docs/AuthenticationServiceApi.md#set_facebook_uid) | **POST** /authentication/facebook | Used as Callback URL when users have successfully authorized their facbeook account.
*AuthenticationServiceApi* | [**set_fractal_uid**](docs/AuthenticationServiceApi.md#set_fractal_uid) | **POST** /authentication/fractal | 
*AuthenticationServiceApi* | [**set_twitter_uid**](docs/AuthenticationServiceApi.md#set_twitter_uid) | **POST** /authentication/twitter | 
*CertificateServiceApi* | [**authenticate_certificate**](docs/CertificateServiceApi.md#authenticate_certificate) | **POST** /certificates | Issues certificates for logged-in users.
*CertificateServiceApi* | [**get_certificate_by_fingerprint**](docs/CertificateServiceApi.md#get_certificate_by_fingerprint) | **GET** /certificates/{fingerprint} | 
*CertificateServiceApi* | [**get_root_certificate**](docs/CertificateServiceApi.md#get_root_certificate) | **GET** /certificates/root | 
*DataCollectionServiceApi* | [**get_methods_for_type**](docs/DataCollectionServiceApi.md#get_methods_for_type) | **GET** /datacollection/types/{name}/methods | 
*DataCollectionServiceApi* | [**get_nodes**](docs/DataCollectionServiceApi.md#get_nodes) | **GET** /datacollection/methods | 
*DataCollectionServiceApi* | [**get_types**](docs/DataCollectionServiceApi.md#get_types) | **GET** /datacollection/types | 
*EnclaveServiceApi* | [**add_history**](docs/EnclaveServiceApi.md#add_history) | **POST** /enclaves/{uuid}/history | 
*EnclaveServiceApi* | [**approve_enclave**](docs/EnclaveServiceApi.md#approve_enclave) | **POST** /enclaves/{uuid}/approval | 
*EnclaveServiceApi* | [**assign_enclave_agent**](docs/EnclaveServiceApi.md#assign_enclave_agent) | **POST** /enclaves/{uuid}/assign | 
*EnclaveServiceApi* | [**attestate_enclave**](docs/EnclaveServiceApi.md#attestate_enclave) | **POST** /enclaves/{uuid}/attestation | 
*EnclaveServiceApi* | [**create_enclave_run_request**](docs/EnclaveServiceApi.md#create_enclave_run_request) | **POST** /enclaves | 
*EnclaveServiceApi* | [**get_enclave**](docs/EnclaveServiceApi.md#get_enclave) | **GET** /enclaves/{uuid} | 
*EnclaveServiceApi* | [**get_enclave_types**](docs/EnclaveServiceApi.md#get_enclave_types) | **GET** /enclaves/types | 
*EnclaveServiceApi* | [**get_enclaves**](docs/EnclaveServiceApi.md#get_enclaves) | **GET** /enclaves | Returns UUIDs of existing analyses.
*EnclaveServiceApi* | [**kill_enclave**](docs/EnclaveServiceApi.md#kill_enclave) | **POST** /enclaves/{uuid}/kill | 
*EnvironmentServiceApi* | [**delete_environment**](docs/EnvironmentServiceApi.md#delete_environment) | **DELETE** /environments/{uuid} | 
*EnvironmentServiceApi* | [**delete_environment_subscription**](docs/EnvironmentServiceApi.md#delete_environment_subscription) | **DELETE** /environments/{uuid}/subscribe | 
*EnvironmentServiceApi* | [**get_environment**](docs/EnvironmentServiceApi.md#get_environment) | **GET** /environments/{uuid} | 
*EnvironmentServiceApi* | [**get_environments**](docs/EnvironmentServiceApi.md#get_environments) | **GET** /environments | Returns UUIDs of existing analyses.
*EnvironmentServiceApi* | [**get_published_environments**](docs/EnvironmentServiceApi.md#get_published_environments) | **GET** /environments/published | 
*EnvironmentServiceApi* | [**get_subscribed_environments**](docs/EnvironmentServiceApi.md#get_subscribed_environments) | **GET** /environments/subscriptions | 
*EnvironmentServiceApi* | [**publish_environment**](docs/EnvironmentServiceApi.md#publish_environment) | **POST** /environments | 
*EnvironmentServiceApi* | [**subscribe_environment**](docs/EnvironmentServiceApi.md#subscribe_environment) | **POST** /environments/{uuid}/subscribe | 
*EnvironmentServiceApi* | [**update_environment**](docs/EnvironmentServiceApi.md#update_environment) | **PUT** /environments/{uuid} | 
*InvoiceServiceApi* | [**get_billing_portal_url**](docs/InvoiceServiceApi.md#get_billing_portal_url) | **GET** /invoices/portal | 
*InvoiceServiceApi* | [**get_invoices**](docs/InvoiceServiceApi.md#get_invoices) | **GET** /invoices | 
*NodeServiceApi* | [**get_bootstrap**](docs/NodeServiceApi.md#get_bootstrap) | **GET** /nodes/bootstrap | 
*NodeServiceApi* | [**get_nodes2**](docs/NodeServiceApi.md#get_nodes2) | **GET** /nodes | 
*NodeServiceApi* | [**post_node_info**](docs/NodeServiceApi.md#post_node_info) | **POST** /nodes | 
*OrganizationServiceApi* | [**get_nodes3**](docs/OrganizationServiceApi.md#get_nodes3) | **GET** /organizations | 
*RequestServiceApi* | [**add_data**](docs/RequestServiceApi.md#add_data) | **POST** /requests/{uuid}/data | Is used to upload and park the data till the AnalysisRequest gets processed.
*RequestServiceApi* | [**cancel_processing**](docs/RequestServiceApi.md#cancel_processing) | **POST** /requests/{uuid}/cancel | Endpoint is called from the Analysis Processing entity to submit the result.
*RequestServiceApi* | [**create_new_request**](docs/RequestServiceApi.md#create_new_request) | **POST** /requests | Endpoint used to create a new Analysis Request.
*RequestServiceApi* | [**get_actions**](docs/RequestServiceApi.md#get_actions) | **GET** /requests/actions | 
*RequestServiceApi* | [**get_agent**](docs/RequestServiceApi.md#get_agent) | **GET** /requests/{uuid}/agent | Is called from the APE to request all parked datasets.
*RequestServiceApi* | [**get_all_requests**](docs/RequestServiceApi.md#get_all_requests) | **GET** /requests | Returns UUIDs of existing analyses.
*RequestServiceApi* | [**get_data**](docs/RequestServiceApi.md#get_data) | **GET** /requests/{uuid}/data | Is called from the APE to request all parked datasets.
*RequestServiceApi* | [**get_request**](docs/RequestServiceApi.md#get_request) | **GET** /requests/{uuid} | Returns the details for certain Request.
*RequestServiceApi* | [**get_result**](docs/RequestServiceApi.md#get_result) | **GET** /requests/{uuid}/result | Can be called from creator to request the AnalysisResult.
*RequestServiceApi* | [**get_status**](docs/RequestServiceApi.md#get_status) | **GET** /requests/stats | 
*RequestServiceApi* | [**give_consent**](docs/RequestServiceApi.md#give_consent) | **POST** /requests/{uuid}/consent | Used to give consent for request.
*RequestServiceApi* | [**init_request_parameters**](docs/RequestServiceApi.md#init_request_parameters) | **POST** /requests/{uuid} | Endpoint used initialized addition datacollection parameters for requester.
*RequestServiceApi* | [**set_agent**](docs/RequestServiceApi.md#set_agent) | **POST** /requests/{uuid}/agent | Is called from the APE to request all parked datasets.
*RequestServiceApi* | [**set_result**](docs/RequestServiceApi.md#set_result) | **POST** /requests/{uuid}/result | Endpoint is called from the Analysis Processing entity to submit the result.
*SocialPlatformServiceApi* | [**get_platforms**](docs/SocialPlatformServiceApi.md#get_platforms) | **GET** /platforms | Used to Handle Incoming Webhooks from Facebook.
*SocialPlatformServiceApi* | [**listen_twitter_webhook**](docs/SocialPlatformServiceApi.md#listen_twitter_webhook) | **POST** /platforms/twitter | Used to Handle Incoming Webhooks from Facebook.
*SocialPlatformServiceApi* | [**register_twitter_webhook**](docs/SocialPlatformServiceApi.md#register_twitter_webhook) | **GET** /platforms/twitter | Used to Handle Incoming Webhooks from Twitter.
*SocialServiceApi* | [**get_my_profile**](docs/SocialServiceApi.md#get_my_profile) | **GET** /social/profiles/me | 
*SocialServiceApi* | [**get_platforms2**](docs/SocialServiceApi.md#get_platforms2) | **GET** /social | Returns all Platforms / Systems that can be Connected to the MADANA Service.
*SocialServiceApi* | [**get_ranking**](docs/SocialServiceApi.md#get_ranking) | **GET** /social/ranking | Returns the Ranking by PTS within the System.
*SocialServiceApi* | [**get_social_platform_feed**](docs/SocialServiceApi.md#get_social_platform_feed) | **GET** /social/feed/{platform} | 
*SocialServiceApi* | [**get_user_profile**](docs/SocialServiceApi.md#get_user_profile) | **GET** /social/profiles/{username} | 
*SocialServiceApi* | [**get_user_profile_0**](docs/SocialServiceApi.md#get_user_profile_0) | **GET** /social/profiles/{username}/simple | 
*SubscriptionServiceApi* | [**add_free_subscription**](docs/SubscriptionServiceApi.md#add_free_subscription) | **POST** /subscriptions/saas/free | 
*SubscriptionServiceApi* | [**add_pass_trial_subscription**](docs/SubscriptionServiceApi.md#add_pass_trial_subscription) | **POST** /subscriptions/paas/trial | 
*SubscriptionServiceApi* | [**get_application**](docs/SubscriptionServiceApi.md#get_application) | **GET** /subscriptions/active | 
*SubscriptionServiceApi* | [**get_checkout_session**](docs/SubscriptionServiceApi.md#get_checkout_session) | **GET** /subscriptions/{productname}/checkout | 
*SubscriptionServiceApi* | [**get_checkout_session2**](docs/SubscriptionServiceApi.md#get_checkout_session2) | **POST** /subscriptions/{productname}/{newplan} | 
*SystemServiceApi* | [**get_all_objects**](docs/SystemServiceApi.md#get_all_objects) | **GET** /system/health | 
*SystemServiceApi* | [**get_application2**](docs/SystemServiceApi.md#get_application2) | **GET** /system/usage | Return the current application usage.
*UserServiceApi* | [**cancel_subscription**](docs/UserServiceApi.md#cancel_subscription) | **POST** /users/{username}/subscriptions/{planname}/cancel | 
*UserServiceApi* | [**create_object**](docs/UserServiceApi.md#create_object) | **POST** /users | Creates a new user object.
*UserServiceApi* | [**delete_object**](docs/UserServiceApi.md#delete_object) | **DELETE** /users/{username} | Deletes an User based on the provided id and securitycontext.
*UserServiceApi* | [**delete_object_0**](docs/UserServiceApi.md#delete_object_0) | **DELETE** /users/{username}/social/{platform}/{ident} | Deletes linked account from the user and securitycontext.
*UserServiceApi* | [**get_avatars**](docs/UserServiceApi.md#get_avatars) | **GET** /users/{username}/avatars | 
*UserServiceApi* | [**get_certificates**](docs/UserServiceApi.md#get_certificates) | **GET** /users/{username}/certificates | 
*UserServiceApi* | [**get_enclave_history**](docs/UserServiceApi.md#get_enclave_history) | **GET** /users/{username}/enclavehistory | 
*UserServiceApi* | [**get_object2**](docs/UserServiceApi.md#get_object2) | **GET** /users/{username} | 
*UserServiceApi* | [**set_avatar**](docs/UserServiceApi.md#set_avatar) | **POST** /users/{username}/avatars | 
*UserServiceApi* | [**set_settings**](docs/UserServiceApi.md#set_settings) | **POST** /users/{username}/settings | 
*UserServiceApi* | [**update_object**](docs/UserServiceApi.md#update_object) | **PUT** /users/{username} | Updates Userproperties based on the provided user object.


## Documentation For Models

 - [JsonDiskConfig](docs/JsonDiskConfig.md)
 - [JsonEnclavePort](docs/JsonEnclavePort.md)
 - [JsonEnclaveProcess](docs/JsonEnclaveProcess.md)
 - [JsonEnclaveRunRequest](docs/JsonEnclaveRunRequest.md)
 - [JsonEnclaveRunningAttestation](docs/JsonEnclaveRunningAttestation.md)
 - [JsonEnclaveRunningAttestationApproval](docs/JsonEnclaveRunningAttestationApproval.md)
 - [JsonEnclaveRunningAttestationApprovalAllOf](docs/JsonEnclaveRunningAttestationApprovalAllOf.md)
 - [JsonEnvironment](docs/JsonEnvironment.md)
 - [JsonEnvironmentPublishingRequest](docs/JsonEnvironmentPublishingRequest.md)
 - [JsonIPFSSystemInfo](docs/JsonIPFSSystemInfo.md)
 - [JsonKubernetesEnclave](docs/JsonKubernetesEnclave.md)
 - [JsonKubernetesEnclaveAllOf](docs/JsonKubernetesEnclaveAllOf.md)
 - [JsonMDNAUserObject](docs/JsonMDNAUserObject.md)
 - [JsonMDNCertificate](docs/JsonMDNCertificate.md)
 - [JsonMDNData](docs/JsonMDNData.md)
 - [JsonMDNMailAddress](docs/JsonMDNMailAddress.md)
 - [JsonMDNOAuthToken](docs/JsonMDNOAuthToken.md)
 - [JsonMDNPasswordReset](docs/JsonMDNPasswordReset.md)
 - [JsonMDNSetting](docs/JsonMDNSetting.md)
 - [JsonMDNSocialUserObject](docs/JsonMDNSocialUserObject.md)
 - [JsonMDNToken](docs/JsonMDNToken.md)
 - [JsonMDNUser](docs/JsonMDNUser.md)
 - [JsonMDNUserAllOf](docs/JsonMDNUserAllOf.md)
 - [JsonMDNUserCredentials](docs/JsonMDNUserCredentials.md)
 - [JsonMDNUserProfileImage](docs/JsonMDNUserProfileImage.md)
 - [JsonMDNUserSetting](docs/JsonMDNUserSetting.md)
 - [JsonMDNUserSettingAllOf](docs/JsonMDNUserSettingAllOf.md)
 - [JsonNetworkInterface](docs/JsonNetworkInterface.md)
 - [JsonNodeInfo](docs/JsonNodeInfo.md)
 - [JsonProcess](docs/JsonProcess.md)
 - [JsonRunConfig](docs/JsonRunConfig.md)
 - [JsonSGXInfo](docs/JsonSGXInfo.md)
 - [JsonSignedData](docs/JsonSignedData.md)
 - [JsonSignedDataUtils](docs/JsonSignedDataUtils.md)
 - [JsonV1Event](docs/JsonV1Event.md)
 - [JsonV1EventList](docs/JsonV1EventList.md)
 - [JsonV1EventSeries](docs/JsonV1EventSeries.md)
 - [JsonV1EventSource](docs/JsonV1EventSource.md)
 - [JsonV1ListMeta](docs/JsonV1ListMeta.md)
 - [JsonV1ManagedFieldsEntry](docs/JsonV1ManagedFieldsEntry.md)
 - [JsonV1ObjectMeta](docs/JsonV1ObjectMeta.md)
 - [JsonV1ObjectReference](docs/JsonV1ObjectReference.md)
 - [JsonV1OwnerReference](docs/JsonV1OwnerReference.md)
 - [JsonWireguardInterface](docs/JsonWireguardInterface.md)
 - [JsonWireguardInterfaceAllOf](docs/JsonWireguardInterfaceAllOf.md)
 - [XmlNs0DiskConfig](docs/XmlNs0DiskConfig.md)
 - [XmlNs0DiskConfigAllOf](docs/XmlNs0DiskConfigAllOf.md)
 - [XmlNs0EnclavePort](docs/XmlNs0EnclavePort.md)
 - [XmlNs0EnclavePortAllOf](docs/XmlNs0EnclavePortAllOf.md)
 - [XmlNs0EnclaveProcess](docs/XmlNs0EnclaveProcess.md)
 - [XmlNs0EnclaveProcessAllOf](docs/XmlNs0EnclaveProcessAllOf.md)
 - [XmlNs0EnclaveRunningAttestation](docs/XmlNs0EnclaveRunningAttestation.md)
 - [XmlNs0EnclaveRunningAttestationAllOf](docs/XmlNs0EnclaveRunningAttestationAllOf.md)
 - [XmlNs0EnclaveRunningAttestationApproval](docs/XmlNs0EnclaveRunningAttestationApproval.md)
 - [XmlNs0EnclaveRunningAttestationApprovalAllOf](docs/XmlNs0EnclaveRunningAttestationApprovalAllOf.md)
 - [XmlNs0Environment](docs/XmlNs0Environment.md)
 - [XmlNs0EnvironmentAllOf](docs/XmlNs0EnvironmentAllOf.md)
 - [XmlNs0IPFSSystemInfo](docs/XmlNs0IPFSSystemInfo.md)
 - [XmlNs0IPFSSystemInfoAllOf](docs/XmlNs0IPFSSystemInfoAllOf.md)
 - [XmlNs0InputStream](docs/XmlNs0InputStream.md)
 - [XmlNs0KubernetesEnclave](docs/XmlNs0KubernetesEnclave.md)
 - [XmlNs0KubernetesEnclaveAllOf](docs/XmlNs0KubernetesEnclaveAllOf.md)
 - [XmlNs0MDNSetting](docs/XmlNs0MDNSetting.md)
 - [XmlNs0MDNSettingAllOf](docs/XmlNs0MDNSettingAllOf.md)
 - [XmlNs0MDNUserProfileImage](docs/XmlNs0MDNUserProfileImage.md)
 - [XmlNs0MDNUserProfileImageAllOf](docs/XmlNs0MDNUserProfileImageAllOf.md)
 - [XmlNs0MDNUserSetting](docs/XmlNs0MDNUserSetting.md)
 - [XmlNs0MDNUserSettingAllOf](docs/XmlNs0MDNUserSettingAllOf.md)
 - [XmlNs0NetworkInterface](docs/XmlNs0NetworkInterface.md)
 - [XmlNs0NetworkInterfaceAllOf](docs/XmlNs0NetworkInterfaceAllOf.md)
 - [XmlNs0NodeInfo](docs/XmlNs0NodeInfo.md)
 - [XmlNs0NodeInfoAllOf](docs/XmlNs0NodeInfoAllOf.md)
 - [XmlNs0Process](docs/XmlNs0Process.md)
 - [XmlNs0RunConfig](docs/XmlNs0RunConfig.md)
 - [XmlNs0RunConfigAllOf](docs/XmlNs0RunConfigAllOf.md)
 - [XmlNs0SGXInfo](docs/XmlNs0SGXInfo.md)
 - [XmlNs0SGXInfoAllOf](docs/XmlNs0SGXInfoAllOf.md)
 - [XmlNs0SignedData](docs/XmlNs0SignedData.md)
 - [XmlNs0SignedDataAllOf](docs/XmlNs0SignedDataAllOf.md)
 - [XmlNs0WireguardInterface](docs/XmlNs0WireguardInterface.md)
 - [XmlNs0WireguardInterfaceAllOf](docs/XmlNs0WireguardInterfaceAllOf.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in madana_apiclient.apis and madana_apiclient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from madana_apiclient.api.default_api import DefaultApi`
- `from madana_apiclient.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import madana_apiclient
from madana_apiclient.apis import *
from madana_apiclient.models import *
```

