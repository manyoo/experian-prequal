# experian_prequal.model.prequal_request.PrequalRequest

Prequalification Credit Report Request

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Prequalification Credit Report Request | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**consumerPii** | [**PII**](PII.md) | [**PII**](PII.md) |  | [optional] 
**requestor** | [**Requestor**](Requestor.md) | [**Requestor**](Requestor.md) |  | [optional] 
**permissiblePurpose** | [**PermissiblePurpose**](PermissiblePurpose.md) | [**PermissiblePurpose**](PermissiblePurpose.md) |  | [optional] 
**resellerInfo** | [**Reseller**](Reseller.md) | [**Reseller**](Reseller.md) |  | [optional] 
**freezeOverride** | [**FreezeOverride**](FreezeOverride.md) | [**FreezeOverride**](FreezeOverride.md) |  | [optional] 
**vendorData** | [**VendorData**](VendorData.md) | [**VendorData**](VendorData.md) |  | [optional] 
**addOns** | [**Addons**](Addons.md) | [**Addons**](Addons.md) |  | [optional] 
**customOptions** | [**CustomOptions**](CustomOptions.md) | [**CustomOptions**](CustomOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

