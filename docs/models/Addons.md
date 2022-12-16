# experian_prequal.model.addons.Addons

Add on products that can be requested. Each add on is billable. These are optional parameters and can be omitted if not needed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Add on products that can be requested. Each add on is billable. These are optional parameters and can be omitted if not needed. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**directCheck** | str,  | str,  | Send back subscriber information on the credit profile. When set to Y indicates that subscriber and court names, addresses, and phone numbers who have reported data on the consumer&#x27;s profile will be sent back on the response. | [optional] 
**demographics** | str,  | str,  | Indicates the type of demographic data that should be returned back. - Geocode + Phone - 1 - Only Geocode - 2 - Only Phone - 3 | [optional] 
**staggSelect** | str,  | str,  | Y - Returns a select amount of Standard Aggregated (STAGG) Attribute data. N or Blank - Indicates this to be omitted if STAGG Attributes are not needed. | [optional] 
**clarityEarlyRiskScore** | str,  | str,  | Y.  Returns Clarity&#x27;s 90 day Clear Early Risk Score (CERS) which predict the risk of a consumer going 90 days past due in first 12 months of a traditional bureau trade. This can be omitted if Clarity Early Risk Score is not needed. | [optional] 
**clarityData** | [**ClarityAccountData**](ClarityAccountData.md) | [**ClarityAccountData**](ClarityAccountData.md) |  | [optional] 
**eCBSV** | str,  | str,  | Y - Makes these fields mandatory - first name, last name, current address and ssn, dob elements of primary applicant  along with employer identification number, primary applicant date of consent and primary applicant signature type elements of eCBSVData. | [optional] 
**eCBSVData** | [**ECBSVAttributeData**](ECBSVAttributeData.md) | [**ECBSVAttributeData**](ECBSVAttributeData.md) |  | [optional] 
**renterRiskScore** | str,  | str,  | Y.  Returns the rent Bureau&#x27;s 90 day Rent Risk Score which predict the risk of a renter going 90 days past due in first 12 months of a rental lease. This can be omitted if Renter Risk Score is not needed. | [optional] 
**rentBureauData** | [**RentBureauAccountData**](RentBureauAccountData.md) | [**RentBureauAccountData**](RentBureauAccountData.md) |  | [optional] 
**riskModels** | [**RiskModel**](RiskModel.md) | [**RiskModel**](RiskModel.md) |  | [optional] 
**[summaries](#summaries)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of what summaries are requested in output like profile summary or auto summary | [optional] 
**fraudShield** | str,  | str,  | Y - Fraud Shield Product Option will be output | [optional] 
**mla** | str,  | str,  | Y - Trigger a screening process of taking the consumer data from an inquiry to match against the Dept of Defense MLA lists. Message codes 1203-1207 could be returned. Permissible Purpose with valid YOB required for getting this option. | [optional] 
**ofacmsg** | str,  | str,  | Y- Trigger a screening process of taking the consumer data from an inquiry to match against the OFAC (Office of Foreign Asset Control) and PLC (Palestinian Legislative Council) lists. A message 1202 NAME DOES NOT MATCH OFAC/PLC LIST will be printed on credit profile if the consumer is not found on either OFAC or PLC list. A message 1200 NAME MATCHES OFAC/PLC LIST will be printed on credit profile if the consumer is found on either OFAC or PLC list. | [optional] 
**consumerIdentCheck** | [**ConsumerIdentifierCheckOptions**](ConsumerIdentifierCheckOptions.md) | [**ConsumerIdentifierCheckOptions**](ConsumerIdentifierCheckOptions.md) |  | [optional] 
**joint** | str,  | str,  | If specified as Y it means that the client is requesting a joint credit report. This is used to request the Dual or Joint Report. Two separate credit reports are returned?one on the primary applicant and one on the secondary applicant. The joint applicant should have the same current address as the primary applicant. Include as much information on the joint applicant as possible, including the surname if it is different from the primary applicant. If NOt specified or N it means that a joint report is NOT being requested. | [optional] 
**paymentHistory84** | str,  | str,  | Y.  84 month payment history is requested instead of the 25 month history. This can be omitted if 84 month history is not needed | [optional] 
**outputType** | str,  | str,  | Output response varies based on the value entered. Supported Output types are - JSON, ARF and TTY | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# summaries

Details of what summaries are requested in output like profile summary or auto summary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of what summaries are requested in output like profile summary or auto summary | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[summaryType](#summaryType)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# summaryType

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Summary Type being requested, Enum [Profile Summary, Auto Summary] | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

