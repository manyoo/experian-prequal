# experian_prequal.model.prequal_score_request.PrequalScoreRequest

Prequalification Credit Score Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Prequalification Credit Score Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**consumerPii** | [**PIIScoreOnly**](PIIScoreOnly.md) | [**PIIScoreOnly**](PIIScoreOnly.md) |  | [optional] 
**requestor** | [**Requestor**](Requestor.md) | [**Requestor**](Requestor.md) |  | [optional] 
**permissiblePurpose** | [**PermissiblePurpose**](PermissiblePurpose.md) | [**PermissiblePurpose**](PermissiblePurpose.md) |  | [optional] 
**resellerInfo** | [**Reseller**](Reseller.md) | [**Reseller**](Reseller.md) |  | [optional] 
**freezeOverride** | [**FreezeOverrideScoreOnly**](FreezeOverrideScoreOnly.md) | [**FreezeOverrideScoreOnly**](FreezeOverrideScoreOnly.md) |  | [optional] 
**vendorData** | [**VendorData**](VendorData.md) | [**VendorData**](VendorData.md) |  | [optional] 
**addOns** | [**AddonsScoreOnly**](AddonsScoreOnly.md) | [**AddonsScoreOnly**](AddonsScoreOnly.md) |  | [optional] 
**customOptions** | [**CustomOptions**](CustomOptions.md) | [**CustomOptions**](CustomOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

