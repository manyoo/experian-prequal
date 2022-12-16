# experian_prequal.model.address_information_resp.AddressInformationResp

Best Consumer Addresses

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Best Consumer Addresses | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**censusGeoCode** | str,  | str,  | Address range that includes the address and the census geography the address is within | [optional] 
**city** | str,  | str,  | City for the address. | [optional] 
**countyCode** | str,  | str,  | County Code | [optional] 
**dwellingType** | str,  | str,  | Structural Characteristic/Dwelling Configuration | [optional] 
**firstReportedDate** | str,  | str,  | Date address first reported. Format &#x3D; MMDDCCYY  | [optional] 
**lastReportingSubscriberCode** | str,  | str,  | Last Subscriber reporting this address. May be blanks. | [optional] 
**lastUpdatedDate** | str,  | str,  | Date Address last updated. Format &#x3D; MMDDCCYY   | [optional] 
**msaCode** | str,  | str,  | Metropolitan Statistical Area Code when DemographicsAll or DemographicsGeoCode is requested. | [optional] 
**source** | str,  | str,  | Source of Address | [optional] 
**state** | str,  | str,  | Valid two-letter US state code or Canadian province.  | [optional] 
**stateCode** | str,  | str,  | State Geo Code when demographics &#x3D; 1 or 2. | [optional] 
**streetName** | str,  | str,  | Full street name.  | [optional] 
**streetPrefix** | str,  | str,  | Data that precedes the street name like house number and directional. | [optional] 
**streetSuffix** | str,  | str,  | Street name type like ST, LN. | [optional] 
**timesReported** | str,  | str,  | Number of times the Address was reported to Experian. | [optional] 
**unitId** | str,  | str,  | Unit Identifier for Apartment. | [optional] 
**unitType** | str,  | str,  | Words such as apartment, suite, etc.  | [optional] 
**zipCode** | str,  | str,  | ZIP Code. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

