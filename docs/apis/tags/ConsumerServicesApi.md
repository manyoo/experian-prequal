<a name="__pageTop"></a>
# experian_prequal.apis.tags.consumer_services_api.ConsumerServicesApi

All URIs are relative to *https://sandbox-us-api.experian.com/consumerservices/prequal*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_report**](#credit_report) | **post** /v1/credit-report | Prequalification Credit Report
[**credit_score**](#credit_score) | **post** /v1/credit-score | Prequalification Credit Score

# **credit_report**
<a name="credit_report"></a>
> PrequalResponse credit_report(body)

Prequalification Credit Report

Retrieves a credit report and scores if requested. This is Standard Prequal Version 1.<br><br>We are providing non-executable \"Request schema\" which contains all request parameters and executable 10 test cases for client testing under \"Examples\" dropdown below which includes first 5 positive test cases and rest 5 negative test cases. Eg: Success_1, Failure_Invalid surname etc.

### Example

* OAuth Authentication (OauthSecurity):
```python
import experian_prequal
from experian_prequal.apis.tags import consumer_services_api
from experian_prequal.model.prequal_request import PrequalRequest
from experian_prequal.model.prequal_response import PrequalResponse
from experian_prequal.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-us-api.experian.com/consumerservices/prequal
# See configuration.py for a list of all supported configuration parameters.
configuration = experian_prequal.Configuration(
    host = "https://sandbox-us-api.experian.com/consumerservices/prequal"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OauthSecurity
configuration = experian_prequal.Configuration(
    host = "https://sandbox-us-api.experian.com/consumerservices/prequal"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with experian_prequal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consumer_services_api.ConsumerServicesApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Type': "application/json",
    }
    body = PrequalRequest(
        consumer_pii=PII(
            primary_applicant=PrimaryApplicant(
                name=PAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(
                    dob="dob_example",
                ),
                ssn=SSN(
                    ssn="ssn_example",
                ),
                driverslicense=DriverLicense(
                    number="number_example",
                    state="state_example",
                ),
                phone=[
                    Phone(
                        number="number_example",
                        type="type_example",
                    )
                ],
                employment=Employment(
                    employer_name="employer_name_example",
                    employer_address=Address(
                        line1="line1_example",
                        line2="line2_example",
                        city="city_example",
                        state="state_example",
                        zip_code="zip_code_example",
                    ),
                ),
,
                previous_address=[
                    Address()
                ],
            ),
            secondary_applicant=SecondaryApplicant(
                name=SAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(),
                ssn=SSN(),
                driverslicense=DriverLicense(),
,
                employment=Employment(),
            ),
        ),
        requestor=Requestor(
            subscriber_code="subscriber_code_example",
        ),
        permissible_purpose=PermissiblePurpose(
            type="type_example",
            terms="terms_example",
            abbreviated_amount="abbreviated_amount_example",
        ),
        reseller_info=Reseller(
            end_user_name="end_user_name_example",
        ),
        freeze_override=FreezeOverride(
            primary_appl_freeze_override_code="primary_appl_freeze_override_code_example",
            secondary_appl_freeze_override_code="secondary_appl_freeze_override_code_example",
        ),
        vendor_data=VendorData(
            vendor_number="vendor_number_example",
            vendor_version="vendor_version_example",
        ),
        add_ons=Addons(
            direct_check="direct_check_example",
            demographics="demographics_example",
            stagg_select="stagg_select_example",
            clarity_early_risk_score="clarity_early_risk_score_example",
            clarity_data=ClarityAccountData(
                clarity_account_id="clarity_account_id_example",
                clarity_location_id="clarity_location_id_example",
                clarity_control_file_name="clarity_control_file_name_example",
                clarity_control_file_version="clarity_control_file_version_example",
                clarity_attributes_control_file_name="clarity_attributes_control_file_name_example",
            ),
            e_cbsv="e_cbsv_example",
            e_cbsv_data=ECBSVAttributeData(
                employer_identification_number="employer_identification_number_example",
                consent_date="consent_date_example",
                consent_type="consent_type_example",
            ),
            renter_risk_score="renter_risk_score_example",
            rent_bureau_data=RentBureauAccountData(
                primary_appl_rent_bureau_freeze_pin="primary_appl_rent_bureau_freeze_pin_example",
                secondary_appl_rent_bureau_freeze_pin="secondary_appl_rent_bureau_freeze_pin_example",
            ),
            risk_models=RiskModel(
                model_indicator=[
                    "model_indicator_example"
                ],
                score_percentile="score_percentile_example",
            ),
            summaries=dict(
                summary_type=[
                    "summary_type_example"
                ],
            ),
            fraud_shield="fraud_shield_example",
            mla="mla_example",
            ofacmsg="ofacmsg_example",
            consumer_ident_check=ConsumerIdentifierCheckOptions(
                get_unique_consumer_identifier="get_unique_consumer_identifier_example",
                verify_primary_consumer_identifier="verify_primary_consumer_identifier_example",
                verify_secondary_consumer_identifier="verify_secondary_consumer_identifier_example",
            ),
            joint="joint_example",
            payment_history84="payment_history84_example",
            output_type="output_type_example",
        ),
        custom_options=CustomOptions(
            option_id=[
                "option_id_example"
            ],
        ),
    )
    try:
        # Prequalification Credit Report
        api_response = api_instance.credit_report(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except experian_prequal.ApiException as e:
        print("Exception when calling ConsumerServicesApi->credit_report: %s\n" % e)

    # example passing only optional values
    header_params = {
        'clientReferenceId': "SBMYSQL",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = PrequalRequest(
        consumer_pii=PII(
            primary_applicant=PrimaryApplicant(
                name=PAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(
                    dob="dob_example",
                ),
                ssn=SSN(
                    ssn="ssn_example",
                ),
                driverslicense=DriverLicense(
                    number="number_example",
                    state="state_example",
                ),
                phone=[
                    Phone(
                        number="number_example",
                        type="type_example",
                    )
                ],
                employment=Employment(
                    employer_name="employer_name_example",
                    employer_address=Address(
                        line1="line1_example",
                        line2="line2_example",
                        city="city_example",
                        state="state_example",
                        zip_code="zip_code_example",
                    ),
                ),
,
                previous_address=[
                    Address()
                ],
            ),
            secondary_applicant=SecondaryApplicant(
                name=SAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(),
                ssn=SSN(),
                driverslicense=DriverLicense(),
,
                employment=Employment(),
            ),
        ),
        requestor=Requestor(
            subscriber_code="subscriber_code_example",
        ),
        permissible_purpose=PermissiblePurpose(
            type="type_example",
            terms="terms_example",
            abbreviated_amount="abbreviated_amount_example",
        ),
        reseller_info=Reseller(
            end_user_name="end_user_name_example",
        ),
        freeze_override=FreezeOverride(
            primary_appl_freeze_override_code="primary_appl_freeze_override_code_example",
            secondary_appl_freeze_override_code="secondary_appl_freeze_override_code_example",
        ),
        vendor_data=VendorData(
            vendor_number="vendor_number_example",
            vendor_version="vendor_version_example",
        ),
        add_ons=Addons(
            direct_check="direct_check_example",
            demographics="demographics_example",
            stagg_select="stagg_select_example",
            clarity_early_risk_score="clarity_early_risk_score_example",
            clarity_data=ClarityAccountData(
                clarity_account_id="clarity_account_id_example",
                clarity_location_id="clarity_location_id_example",
                clarity_control_file_name="clarity_control_file_name_example",
                clarity_control_file_version="clarity_control_file_version_example",
                clarity_attributes_control_file_name="clarity_attributes_control_file_name_example",
            ),
            e_cbsv="e_cbsv_example",
            e_cbsv_data=ECBSVAttributeData(
                employer_identification_number="employer_identification_number_example",
                consent_date="consent_date_example",
                consent_type="consent_type_example",
            ),
            renter_risk_score="renter_risk_score_example",
            rent_bureau_data=RentBureauAccountData(
                primary_appl_rent_bureau_freeze_pin="primary_appl_rent_bureau_freeze_pin_example",
                secondary_appl_rent_bureau_freeze_pin="secondary_appl_rent_bureau_freeze_pin_example",
            ),
            risk_models=RiskModel(
                model_indicator=[
                    "model_indicator_example"
                ],
                score_percentile="score_percentile_example",
            ),
            summaries=dict(
                summary_type=[
                    "summary_type_example"
                ],
            ),
            fraud_shield="fraud_shield_example",
            mla="mla_example",
            ofacmsg="ofacmsg_example",
            consumer_ident_check=ConsumerIdentifierCheckOptions(
                get_unique_consumer_identifier="get_unique_consumer_identifier_example",
                verify_primary_consumer_identifier="verify_primary_consumer_identifier_example",
                verify_secondary_consumer_identifier="verify_secondary_consumer_identifier_example",
            ),
            joint="joint_example",
            payment_history84="payment_history84_example",
            output_type="output_type_example",
        ),
        custom_options=CustomOptions(
            option_id=[
                "option_id_example"
            ],
        ),
    )
    try:
        # Prequalification Credit Report
        api_response = api_instance.credit_report(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except experian_prequal.ApiException as e:
        print("Exception when calling ConsumerServicesApi->credit_report: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrequalRequest**](../../models/PrequalRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
clientReferenceId | ClientReferenceIdSchema | | optional
Content-Type | ContentTypeSchema | | 
Accept | AcceptSchema | | optional

# ClientReferenceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SBMYSQL", ] if omitted the server will use the default value of "SBMYSQL"

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["application/json", ] if omitted the server will use the default value of "application/json"

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["application/json", ] if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#credit_report.ApiResponseFor200) | API responds with a JSON.
400 | [ApiResponseFor400](#credit_report.ApiResponseFor400) | Client Exception due to invalid data.
403 | [ApiResponseFor403](#credit_report.ApiResponseFor403) | Request Forbidden.
404 | [ApiResponseFor404](#credit_report.ApiResponseFor404) | Not found Data.
500 | [ApiResponseFor500](#credit_report.ApiResponseFor500) | Server Related Error.
504 | [ApiResponseFor504](#credit_report.ApiResponseFor504) | Timeout.

#### credit_report.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrequalResponse**](../../models/PrequalResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_report.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor400 |  |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_report.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor403 |  |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor403

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_report.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor404 |  |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor404

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_report.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_report.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor504 |  |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor504

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


### Authorization

[OauthSecurity](../../../README.md#OauthSecurity)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **credit_score**
<a name="credit_score"></a>
> PrequalScoreResponse credit_score(body)

Prequalification Credit Score

Retrieves credit scores and addons as requested. <br><br>We are providing non-executable \"Request schema\" which contains all request parameters and executable 10 test cases for client testing under \"Examples\" dropdown below which includes first 5 positive test cases and rest 5 negative test cases. Eg: Success_1, Failure_Invalid surname etc.

### Example

* OAuth Authentication (OauthSecurity):
```python
import experian_prequal
from experian_prequal.apis.tags import consumer_services_api
from experian_prequal.model.prequal_score_response import PrequalScoreResponse
from experian_prequal.model.prequal_score_request import PrequalScoreRequest
from experian_prequal.model.error_response import ErrorResponse
from pprint import pprint
# Defining the host is optional and defaults to https://sandbox-us-api.experian.com/consumerservices/prequal
# See configuration.py for a list of all supported configuration parameters.
configuration = experian_prequal.Configuration(
    host = "https://sandbox-us-api.experian.com/consumerservices/prequal"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OauthSecurity
configuration = experian_prequal.Configuration(
    host = "https://sandbox-us-api.experian.com/consumerservices/prequal"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Enter a context with an instance of the API client
with experian_prequal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = consumer_services_api.ConsumerServicesApi(api_client)

    # example passing only required values which don't have defaults set
    header_params = {
        'Content-Type': "application/json",
    }
    body = PrequalScoreRequest(
        consumer_pii=PIIScoreOnly(
            primary_applicant=PrimaryApplicant(
                name=PAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(
                    dob="dob_example",
                ),
                ssn=SSN(
                    ssn="ssn_example",
                ),
                driverslicense=DriverLicense(
                    number="number_example",
                    state="state_example",
                ),
                phone=[
                    Phone(
                        number="number_example",
                        type="type_example",
                    )
                ],
                employment=Employment(
                    employer_name="employer_name_example",
                    employer_address=Address(
                        line1="line1_example",
                        line2="line2_example",
                        city="city_example",
                        state="state_example",
                        zip_code="zip_code_example",
                    ),
                ),
,
                previous_address=[
                    Address()
                ],
            ),
        ),
        requestor=Requestor(
            subscriber_code="subscriber_code_example",
        ),
        permissible_purpose=PermissiblePurpose(
            type="type_example",
            terms="terms_example",
            abbreviated_amount="abbreviated_amount_example",
        ),
        reseller_info=Reseller(
            end_user_name="end_user_name_example",
        ),
        freeze_override=FreezeOverrideScoreOnly(
            primary_appl_freeze_override_code="primary_appl_freeze_override_code_example",
        ),
        vendor_data=VendorData(
            vendor_number="vendor_number_example",
            vendor_version="vendor_version_example",
        ),
        add_ons=AddonsScoreOnly(
            risk_models=RiskModel(
                model_indicator=[
                    "model_indicator_example"
                ],
                score_percentile="score_percentile_example",
            ),
        ),
        custom_options=CustomOptions(
            option_id=[
                "option_id_example"
            ],
        ),
    )
    try:
        # Prequalification Credit Score
        api_response = api_instance.credit_score(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except experian_prequal.ApiException as e:
        print("Exception when calling ConsumerServicesApi->credit_score: %s\n" % e)

    # example passing only optional values
    header_params = {
        'clientReferenceId': "SBMYSQL",
        'Content-Type': "application/json",
        'Accept': "application/json",
    }
    body = PrequalScoreRequest(
        consumer_pii=PIIScoreOnly(
            primary_applicant=PrimaryApplicant(
                name=PAName(
                    last_name="last_name_example",
                    first_name="first_name_example",
                    middle_name="middle_name_example",
                    generation_code="generation_code_example",
                ),
                dob=DOB(
                    dob="dob_example",
                ),
                ssn=SSN(
                    ssn="ssn_example",
                ),
                driverslicense=DriverLicense(
                    number="number_example",
                    state="state_example",
                ),
                phone=[
                    Phone(
                        number="number_example",
                        type="type_example",
                    )
                ],
                employment=Employment(
                    employer_name="employer_name_example",
                    employer_address=Address(
                        line1="line1_example",
                        line2="line2_example",
                        city="city_example",
                        state="state_example",
                        zip_code="zip_code_example",
                    ),
                ),
,
                previous_address=[
                    Address()
                ],
            ),
        ),
        requestor=Requestor(
            subscriber_code="subscriber_code_example",
        ),
        permissible_purpose=PermissiblePurpose(
            type="type_example",
            terms="terms_example",
            abbreviated_amount="abbreviated_amount_example",
        ),
        reseller_info=Reseller(
            end_user_name="end_user_name_example",
        ),
        freeze_override=FreezeOverrideScoreOnly(
            primary_appl_freeze_override_code="primary_appl_freeze_override_code_example",
        ),
        vendor_data=VendorData(
            vendor_number="vendor_number_example",
            vendor_version="vendor_version_example",
        ),
        add_ons=AddonsScoreOnly(
            risk_models=RiskModel(
                model_indicator=[
                    "model_indicator_example"
                ],
                score_percentile="score_percentile_example",
            ),
        ),
        custom_options=CustomOptions(
            option_id=[
                "option_id_example"
            ],
        ),
    )
    try:
        # Prequalification Credit Score
        api_response = api_instance.credit_score(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except experian_prequal.ApiException as e:
        print("Exception when calling ConsumerServicesApi->credit_score: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrequalScoreRequest**](../../models/PrequalScoreRequest.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
clientReferenceId | ClientReferenceIdSchema | | optional
Content-Type | ContentTypeSchema | | 
Accept | AcceptSchema | | optional

# ClientReferenceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["SBMYSQL", ] if omitted the server will use the default value of "SBMYSQL"

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["application/json", ] if omitted the server will use the default value of "application/json"

# AcceptSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["application/json", ] if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#credit_score.ApiResponseFor200) | API responds with a JSON.
400 | [ApiResponseFor400](#credit_score.ApiResponseFor400) | Client Exception due to invalid data.
403 | [ApiResponseFor403](#credit_score.ApiResponseFor403) | Request Forbidden.
404 | [ApiResponseFor404](#credit_score.ApiResponseFor404) | Not found Data.
500 | [ApiResponseFor500](#credit_score.ApiResponseFor500) | Server Related Error.
504 | [ApiResponseFor504](#credit_score.ApiResponseFor504) | Timeout.

#### credit_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PrequalScoreResponse**](../../models/PrequalScoreResponse.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_score.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor400 |  |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor400

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_score.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor403 |  |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor403

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_score.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor404 |  |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor404

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_score.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor500 |  |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor500

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


#### credit_score.ApiResponseFor504
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor504ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor504 |  |

# SchemaFor504ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorResponse**](../../models/ErrorResponse.md) |  | 

#### ResponseHeadersFor504

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
experianTransactionId | ExperianTransactionIdSchema | | optional
clientReferenceId | ClientReferenceIdSchema | | optional

# ExperianTransactionIdSchema

Unique ID generated by Experian for this API request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Unique ID generated by Experian for this API request | 

# ClientReferenceIdSchema

Echo back of the reference Id , if provided on API request header

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Echo back of the reference Id , if provided on API request header | 


### Authorization

[OauthSecurity](../../../README.md#OauthSecurity)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

