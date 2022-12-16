# experian_prequal.model.risk_model_resp.RiskModelResp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**evaluation** | str,  | str,  | Sign of risk score. | [optional] 
**modelIndicator** | str,  | str,  | Indicates which model is being returned. | [optional] 
**score** | str,  | str,  | Present when RiskModels is requested on input or via subcode. 4 character score for the model requested. | [optional] 
**[scoreFactors](#scoreFactors)** | list, tuple,  | tuple,  | Score Factor Codes (Upto 5 items can be returned) | [optional] 
**scorePercentile** | str,  | str,  | Present when ScorePercentile is requested on input and is available for a score. Nation Score Percentile. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scoreFactors

Score Factor Codes (Upto 5 items can be returned)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Score Factor Codes (Upto 5 items can be returned) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ScoreFactor**](ScoreFactor.md) | [**ScoreFactor**](ScoreFactor.md) | [**ScoreFactor**](ScoreFactor.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

