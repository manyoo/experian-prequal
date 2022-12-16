# experian_prequal.model.public_record_resp.PublicRecordResp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**adjustmentPercent** | str,  | str,  | For BK Chapter 13 Only. | [optional] 
**amount** | str,  | str,  | Full rounded dollar amount or rounded amount. | [optional] 
**bankruptcyAssetAmount** | str,  | str,  | Full dollar amount for Bankruptcies.  | [optional] 
**bankruptcyVoluntaryIndicator** | str,  | str,  | Bankruptcy Voluntary Indicator | [optional] 
**bookPageSequence** | str,  | str,  | Book, page and sequence number. | [optional] 
**consumerComment** | str,  | str,  | Public Record Comment Text (Free Form). | [optional] 
**courtCode** | str,  | str,  | Seven-digit code unique to each court. | [optional] 
**courtName** | str,  | str,  | Court name | [optional] 
**disputeFlag** | str,  | str,  | Indicates a dispute. | [optional] 
**ecoa** | str,  | str,  |  | [optional] 
**evaluation** | str,  | str,  | N (constant) &#x3D; negative | [optional] 
**filingDate** | str,  | str,  | Original filing date Format &#x3D; MMDDCCYY. | [optional] 
**plaintiffName** | str,  | str,  | Plaintiff Name | [optional] 
**referenceNumber** | str,  | str,  | Contains docket number or certificate ID. | [optional] 
**repaymentPercent** | str,  | str,  | For BK Chapter 13 Only | [optional] 
**status** | str,  | str,  | Public Record Status Codes. | [optional] 
**statusDate** | str,  | str,  | Date of court action associated with status. Format &#x3D; MMDDCCYY.  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

