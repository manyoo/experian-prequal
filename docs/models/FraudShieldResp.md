# experian_prequal.model.fraud_shield_resp.FraudShieldResp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**addressCount** | str,  | str,  | Number of times the address was used in the last 90-120 days. | [optional] 
**addressDate** | str,  | str,  | Format &#x3D; MMDDCCYY. Date when address counter accumulation started.   | [optional] 
**addressErrorCode** | str,  | str,  | Address Error Code if applicable. | [optional] 
**dateOfBirth** | str,  | str,  | Format &#x3D; MMDDCCYY | [optional] 
**dateOfDeath** | str,  | str,  | Format &#x3D; MMDDCCYY | [optional] 
**fraudShieldIndicators** | [**FraudShieldIndicators**](FraudShieldIndicators.md) | [**FraudShieldIndicators**](FraudShieldIndicators.md) |  | [optional] 
**sic** | str,  | str,  | Group Identifiers if applicable. | [optional] 
**socialCount** | str,  | str,  | Number of times the social was used in the last 90-120 days. | [optional] 
**socialDate** | str,  | str,  | Date posted when social counter accumulation started. Format &#x3D; MMDDCCYY. | [optional] 
**socialErrorCode** | str,  | str,  | Social error code if applicable. | [optional] 
**ssnFirstPossibleIssuanceYear** | str,  | str,  | First year possible for SSN issuance (YYYY). | [optional] 
**ssnLastPossibleIssuanceYear** | str,  | str,  | Last year possible for SSN issuance (YYYY). | [optional] 
**text** | str,  | str,  | Shield message. | [optional] 
**type** | str,  | str,  | Fraus Shield Record Type | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

