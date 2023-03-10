# experian
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: OpenAPI3.1.0.12
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python &gt;&#x3D;3.7

## Migration from other generators like python and python-legacy

### Changes
1. This generator uses spec case for all (object) property names and parameter names.
    - So if the spec has a property name like camelCase, it will use camelCase rather than camel_case
    - So you will need to update how you input and read properties to use spec case
2. Endpoint parameters are stored in dictionaries to prevent collisions (explanation below)
    - So you will need to update how you pass data in to endpoints
3. Endpoint responses now include the original response, the deserialized response body, and (todo)the deserialized headers
    - So you will need to update your code to use response.body to access deserialized data
4. All validated data is instantiated in an instance that subclasses all validated Schema classes and Decimal/str/list/tuple/frozendict/NoneClass/BoolClass/bytes/io.FileIO
    - This means that you can use isinstance to check if a payload validated against a schema class
    - This means that no data will be of type None/True/False
        - ingested None will subclass NoneClass
        - ingested True will subclass BoolClass
        - ingested False will subclass BoolClass
        - So if you need to check is True/False/None, instead use instance.is_true_oapg()/.is_false_oapg()/.is_none_oapg()
5. All validated class instances are immutable except for ones based on io.File
    - This is because if properties were changed after validation, that validation would no longer apply
    - So no changing values or property values after a class has been instantiated
6. String + Number types with formats
    - String type data is stored as a string and if you need to access types based on its format like date,
    date-time, uuid, number etc then you will need to use accessor functions on the instance
    - type string + format: See .as_date_oapg, .as_datetime_oapg, .as_decimal_oapg, .as_uuid_oapg
    - type number + format: See .as_float_oapg, .as_int_oapg
    - this was done because openapi/json-schema defines constraints. string data may be type string with no format
    keyword in one schema, and include a format constraint in another schema
    - So if you need to access a string format based type, use as_date_oapg/as_datetime_oapg/as_decimal_oapg/as_uuid_oapg
    - So if you need to access a number format based type, use as_int_oapg/as_float_oapg
7. Property access on AnyType(type unset) or object(dict) schemas
    - Only required keys with valid python names are properties like .someProp and have type hints
    - All optional keys may not exist, so properties are not defined for them
    - One can access optional values with dict_instance['optionalProp'] and KeyError will be raised if it does not exist
    - Use get_item_oapg if you need a way to always get a value whether or not the key exists
        - If the key does not exist, schemas.unset is returned from calling dict_instance.get_item_oapg('optionalProp')
        - All required and optional keys have type hints for this method, and @typing.overload is used
        - A type hint is also generated for additionalProperties accessed using this method
    - So you will need to update you code to use some_instance['optionalProp'] to access optional property
    and additionalProperty values
8. The location of the api classes has changed
    - Api classes are located in your_package.apis.tags.some_api
    - This change was made to eliminate redundant code generation
    - Legacy generators generated the same endpoint twice if it had > 1 tag on it
    - This generator defines an endpoint in one class, then inherits that class to generate
      apis by tags and by paths
    - This change reduces code and allows quicker run time if you use the path apis
        - path apis are at your_package.apis.paths.some_path
    - Those apis will only load their needed models, which is less to load than all of the resources needed in a tag api
    - So you will need to update your import paths to the api classes

### Why are Oapg and _oapg used in class and method names?
Classes can have arbitrarily named properties set on them
Endpoints can have arbitrary operationId method names set
For those reasons, I use the prefix Oapg and _oapg to greatly reduce the likelihood of collisions
on protected + public classes/methods.
oapg stands for OpenApi Python Generator.

### Object property spec case
This was done because when payloads are ingested, they can be validated against N number of schemas.
If the input signature used a different property name then that has mutated the payload.
So SchemaA and SchemaB must both see the camelCase spec named variable.
Also it is possible to send in two properties, named camelCase and camel_case in the same payload.
That use case should be support so spec case is used.

### Parameter spec case
Parameters can be included in different locations including:
- query
- path
- header
- cookie

Any of those parameters could use the same parameter names, so if every parameter
was included as an endpoint parameter in a function signature, they would collide.
For that reason, each of those inputs have been separated out into separate typed dictionaries:
- query_params
- path_params
- header_params
- cookie_params

So when updating your code, you will need to pass endpoint parameters in using those
dictionaries.

### Endpoint responses
Endpoint responses have been enriched to now include more information.
Any response reom an endpoint will now include the following properties:
response: urllib3.HTTPResponse
body: typing.Union[Unset, Schema]
headers: typing.Union[Unset, TODO]
Note: response header deserialization has not yet been added


## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/manyoo/experian-prequal.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/manyoo/experian-prequal.git`)

Then import the package:
```python
import experian_prequal
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import experian_prequal
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import experian_prequal
from pprint import pprint
from experian_prequal.apis.tags import consumer_services_api
from experian_prequal.model.error_response import ErrorResponse
from experian_prequal.model.prequal_request import PrequalRequest
from experian_prequal.model.prequal_response import PrequalResponse
from experian_prequal.model.prequal_score_request import PrequalScoreRequest
from experian_prequal.model.prequal_score_response import PrequalScoreResponse
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
    content_type = "application/json" # str | Input Request format (default to CodegenParameter{isFormParam=false, isQueryParam=false, isPathParam=false, isHeaderParam=true, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=false, baseName='Content-Type', paramName='content_type', dataType='str', datatypeWithEnum='Content_typeEnum', dataFormat='null', collectionFormat='null', description='Input Request format', unescapedDescription='Input Request format', baseType='null', defaultValue='"application/json"', enumDefaultValue='"application/json"', enumName='Content_typeEnum', style='SIMPLE', deepObject='false', allowEmptyValue='false', example='"application/json"', jsonSchema='{
  "name" : "Content-Type",
  "in" : "header",
  "description" : "Input Request format",
  "required" : true,
  "style" : "simple",
  "explode" : false,
  "schema" : {
    "type" : "string",
    "default" : "application/json",
    "enum" : [ "application/json" ]
  }
}', isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=true, _enum=[application/json], allowableValues={values=[application/json], enumVars=[{name=APPLICATION_JSON, isString=true, value="application/json"}]}, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=true, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='string', baseName='ContentTypeSchema', complexType='null', getter='getContentType', setter='setContentType', description='null', dataType='str', datatypeWithEnum='Content_typeEnum', dataFormat='null', name='content_type', min='null', max='null', defaultValue='"application/json"', defaultValueWithParam=' = data.Content-Type;', baseType='str', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='"application/json"', jsonSchema='{
  "type" : "string",
  "default" : "application/json",
  "enum" : [ "application/json" ]
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=true, isInnerEnum=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=[application/json], allowableValues={enumVars=[{name=APPLICATION_JSON, isString=true, value="application/json"}], values=[application/json]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='ContentType', nameInSnakeCase='null', enumName='Content_typeEnum', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
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
    ) # PrequalRequest | Consumer's PII , Requestor Information, Addons and any custom options to be specified here.
client_reference_id = "SBMYSQL" # str | API client generated reference Id to uniquely identify the API request. (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=false, isPathParam=false, isHeaderParam=true, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=false, baseName='clientReferenceId', paramName='client_reference_id', dataType='str', datatypeWithEnum='Client_reference_idEnum', dataFormat='null', collectionFormat='null', description='API client generated reference Id to uniquely identify the API request.', unescapedDescription='API client generated reference Id to uniquely identify the API request.', baseType='null', defaultValue='"SBMYSQL"', enumDefaultValue='"SBMYSQL"', enumName='Client_reference_idEnum', style='SIMPLE', deepObject='false', allowEmptyValue='false', example='"SBMYSQL"', jsonSchema='{
  "name" : "clientReferenceId",
  "in" : "header",
  "description" : "API client generated reference Id to uniquely identify the API request.",
  "required" : false,
  "style" : "simple",
  "explode" : false,
  "schema" : {
    "type" : "string",
    "default" : "SBMYSQL",
    "enum" : [ "SBMYSQL" ]
  }
}', isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=true, _enum=[SBMYSQL], allowableValues={values=[SBMYSQL], enumVars=[{name=SBMYSQL, isString=true, value="SBMYSQL"}]}, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='string', baseName='ClientReferenceIdSchema', complexType='null', getter='getClientReferenceId', setter='setClientReferenceId', description='null', dataType='str', datatypeWithEnum='Client_reference_idEnum', dataFormat='null', name='client_reference_id', min='null', max='null', defaultValue='"SBMYSQL"', defaultValueWithParam=' = data.clientReferenceId;', baseType='str', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='"SBMYSQL"', jsonSchema='{
  "type" : "string",
  "default" : "SBMYSQL",
  "enum" : [ "SBMYSQL" ]
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=true, isInnerEnum=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=[SBMYSQL], allowableValues={enumVars=[{name=SBMYSQL, isString=true, value="SBMYSQL"}], values=[SBMYSQL]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='ClientReferenceId', nameInSnakeCase='null', enumName='Client_reference_idEnum', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})
accept = "application/json" # str | Output Response format (optional) (default to CodegenParameter{isFormParam=false, isQueryParam=false, isPathParam=false, isHeaderParam=true, isCookieParam=false, isBodyParam=false, isContainer=false, isCollectionFormatMulti=false, isPrimitiveType=true, isModel=false, isExplode=false, baseName='Accept', paramName='accept', dataType='str', datatypeWithEnum='AcceptEnum', dataFormat='null', collectionFormat='null', description='Output Response format', unescapedDescription='Output Response format', baseType='null', defaultValue='"application/json"', enumDefaultValue='"application/json"', enumName='AcceptEnum', style='SIMPLE', deepObject='false', allowEmptyValue='false', example='"application/json"', jsonSchema='{
  "name" : "Accept",
  "in" : "header",
  "description" : "Output Response format",
  "required" : false,
  "style" : "simple",
  "explode" : false,
  "schema" : {
    "type" : "string",
    "default" : "application/json",
    "enum" : [ "application/json" ]
  }
}', isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isAnyType=false, isArray=false, isMap=false, isFile=false, isEnum=true, _enum=[application/json], allowableValues={values=[application/json], enumVars=[{name=APPLICATION_JSON, isString=true, value="application/json"}]}, items=null, mostInnerItems=null, additionalProperties=null, vars=[], requiredVars=[], vendorExtensions={}, hasValidation=false, maxProperties=null, minProperties=null, isNullable=false, isDeprecated=false, required=false, maximum='null', exclusiveMaximum=false, minimum='null', exclusiveMinimum=false, maxLength=null, minLength=null, pattern='null', maxItems=null, minItems=null, uniqueItems=false, uniqueItemsBoolean=null, contentType=null, multipleOf=null, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, schema=CodegenProperty{openApiType='string', baseName='AcceptSchema', complexType='null', getter='getAccept', setter='setAccept', description='null', dataType='str', datatypeWithEnum='AcceptEnum', dataFormat='null', name='accept', min='null', max='null', defaultValue='"application/json"', defaultValueWithParam=' = data.Accept;', baseType='str', containerType='null', title='null', unescapedDescription='null', maxLength=null, minLength=null, pattern='null', example='"application/json"', jsonSchema='{
  "type" : "string",
  "default" : "application/json",
  "enum" : [ "application/json" ]
}', minimum='null', maximum='null', exclusiveMinimum=false, exclusiveMaximum=false, required=false, deprecated=false, hasMoreNonReadOnly=false, isPrimitiveType=true, isModel=false, isContainer=false, isString=true, isNumeric=false, isInteger=false, isShort=false, isLong=false, isUnboundedInteger=false, isNumber=false, isFloat=false, isDouble=false, isDecimal=false, isByteArray=false, isBinary=false, isFile=false, isBoolean=false, isDate=false, isDateTime=false, isUuid=false, isUri=false, isEmail=false, isFreeFormObject=false, isArray=false, isMap=false, isEnum=true, isInnerEnum=true, isAnyType=false, isReadOnly=false, isWriteOnly=false, isNullable=false, isSelfReference=false, isCircularReference=false, isDiscriminator=false, _enum=[application/json], allowableValues={enumVars=[{name=APPLICATION_JSON, isString=true, value="application/json"}], values=[application/json]}, items=null, additionalProperties=null, vars=[], requiredVars=[], mostInnerItems=null, vendorExtensions={}, hasValidation=false, isInherited=false, discriminatorValue='null', nameInCamelCase='Accept', nameInSnakeCase='null', enumName='AcceptEnum', maxItems=null, minItems=null, maxProperties=null, minProperties=null, uniqueItems=false, uniqueItemsBoolean=null, multipleOf=null, isXmlAttribute=false, xmlPrefix='null', xmlName='null', xmlNamespace='null', isXmlWrapped=false, isNull=false, getAdditionalPropertiesIsAnyType=false, getHasVars=false, getHasRequired=false, getHasDiscriminatorWithNonEmptyMapping=false, composedSchemas=null, hasMultipleTypes=false, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false, isBooleanSchemaTrue=false, isBooleanSchemaFalse=false, format=null, dependentRequired=null, contains=null}, content=null, requiredVarsMap=null, ref=null, schemaIsFromAdditionalProperties=false})

    try:
        # Prequalification Credit Report
        api_response = api_instance.credit_report(content_typebodyclient_reference_id=client_reference_idaccept=accept)
        pprint(api_response)
    except experian_prequal.ApiException as e:
        print("Exception when calling ConsumerServicesApi->credit_report: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://sandbox-us-api.experian.com/consumerservices/prequal*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ConsumerServicesApi* | [**credit_report**](docs/apis/tags/ConsumerServicesApi.md#credit_report) | **post** /v1/credit-report | Prequalification Credit Report
*ConsumerServicesApi* | [**credit_score**](docs/apis/tags/ConsumerServicesApi.md#credit_score) | **post** /v1/credit-score | Prequalification Credit Score

## Documentation For Models

 - [Addons](docs/models/Addons.md)
 - [AddonsScoreOnly](docs/models/AddonsScoreOnly.md)
 - [Address](docs/models/Address.md)
 - [AddressInformationResp](docs/models/AddressInformationResp.md)
 - [Arf](docs/models/Arf.md)
 - [AttributeResp](docs/models/AttributeResp.md)
 - [ClarityAccountData](docs/models/ClarityAccountData.md)
 - [ClarityAttributesResp](docs/models/ClarityAttributesResp.md)
 - [ConsumerAssistanceReferralAddress](docs/models/ConsumerAssistanceReferralAddress.md)
 - [ConsumerIdentifierCheckOptions](docs/models/ConsumerIdentifierCheckOptions.md)
 - [ConsumerIdentity](docs/models/ConsumerIdentity.md)
 - [ConsumerIdentityDob](docs/models/ConsumerIdentityDob.md)
 - [ConsumerIdentityName](docs/models/ConsumerIdentityName.md)
 - [ConsumerIdentityNameResp](docs/models/ConsumerIdentityNameResp.md)
 - [ConsumerIdentityPhone](docs/models/ConsumerIdentityPhone.md)
 - [ConsumerIdentityPhoneResp](docs/models/ConsumerIdentityPhoneResp.md)
 - [CustomOptions](docs/models/CustomOptions.md)
 - [DOB](docs/models/DOB.md)
 - [DirectCheck](docs/models/DirectCheck.md)
 - [DirectCheckResp](docs/models/DirectCheckResp.md)
 - [DriverLicense](docs/models/DriverLicense.md)
 - [ECBSVAttributeData](docs/models/ECBSVAttributeData.md)
 - [Employment](docs/models/Employment.md)
 - [EmploymentInformation](docs/models/EmploymentInformation.md)
 - [EmploymentInformationResp](docs/models/EmploymentInformationResp.md)
 - [EnhancedPaymentData](docs/models/EnhancedPaymentData.md)
 - [Error](docs/models/Error.md)
 - [ErrorResponse](docs/models/ErrorResponse.md)
 - [FraudShield](docs/models/FraudShield.md)
 - [FraudShieldIndicators](docs/models/FraudShieldIndicators.md)
 - [FraudShieldResp](docs/models/FraudShieldResp.md)
 - [FreezeOverride](docs/models/FreezeOverride.md)
 - [FreezeOverrideScoreOnly](docs/models/FreezeOverrideScoreOnly.md)
 - [InformationalMessage](docs/models/InformationalMessage.md)
 - [InformationalMessageResp](docs/models/InformationalMessageResp.md)
 - [Inquiry](docs/models/Inquiry.md)
 - [InquiryResp](docs/models/InquiryResp.md)
 - [MlaResp](docs/models/MlaResp.md)
 - [ModelAttributes](docs/models/ModelAttributes.md)
 - [ModelAttributesResp0](docs/models/ModelAttributesResp0.md)
 - [ModelAttributesResp1](docs/models/ModelAttributesResp1.md)
 - [Ofac](docs/models/Ofac.md)
 - [OfacResp](docs/models/OfacResp.md)
 - [PAName](docs/models/PAName.md)
 - [PII](docs/models/PII.md)
 - [PIIScoreOnly](docs/models/PIIScoreOnly.md)
 - [PermissiblePurpose](docs/models/PermissiblePurpose.md)
 - [Phone](docs/models/Phone.md)
 - [PrequalRequest](docs/models/PrequalRequest.md)
 - [PrequalResp](docs/models/PrequalResp.md)
 - [PrequalResponse](docs/models/PrequalResponse.md)
 - [PrequalScoreRequest](docs/models/PrequalScoreRequest.md)
 - [PrequalScoreResp](docs/models/PrequalScoreResp.md)
 - [PrequalScoreResponse](docs/models/PrequalScoreResponse.md)
 - [PrimaryApplicant](docs/models/PrimaryApplicant.md)
 - [PublicRecord](docs/models/PublicRecord.md)
 - [PublicRecordResp](docs/models/PublicRecordResp.md)
 - [RentBureauAccountData](docs/models/RentBureauAccountData.md)
 - [Requestor](docs/models/Requestor.md)
 - [Reseller](docs/models/Reseller.md)
 - [RiskModel](docs/models/RiskModel.md)
 - [RiskModelPrequal](docs/models/RiskModelPrequal.md)
 - [RiskModelResp](docs/models/RiskModelResp.md)
 - [RiskModelRespPrequal](docs/models/RiskModelRespPrequal.md)
 - [SAName](docs/models/SAName.md)
 - [SSN](docs/models/SSN.md)
 - [ScoreFactor](docs/models/ScoreFactor.md)
 - [SecondaryApplicant](docs/models/SecondaryApplicant.md)
 - [Ssn](docs/models/Ssn.md)
 - [SsnResp](docs/models/SsnResp.md)
 - [Statement](docs/models/Statement.md)
 - [StatementResp](docs/models/StatementResp.md)
 - [Summaries](docs/models/Summaries.md)
 - [Summary](docs/models/Summary.md)
 - [Tradeline](docs/models/Tradeline.md)
 - [TradelineResp](docs/models/TradelineResp.md)
 - [Tty](docs/models/Tty.md)
 - [UniqueConsumerIdentifier](docs/models/UniqueConsumerIdentifier.md)
 - [VendorData](docs/models/VendorData.md)

## Documentation For Authorization

 Authentication schemes defined for the API:
## OauthSecurity

- **Type**: OAuth
- **Flow**: password
- **Authorization URL**: 
- **Scopes**: 
 - **user**: user scope


## Author



## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in experian_prequal.apis and experian_prequal.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from experian_prequal.apis.default_api import DefaultApi`
- `from experian_prequal.model.pet import Pet`

Solution 1:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import experian_prequal
from experian_prequal.apis import *
from experian_prequal.models import *
```
