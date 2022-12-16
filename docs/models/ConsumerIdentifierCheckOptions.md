# experian_prequal.model.consumer_identifier_check_options.ConsumerIdentifierCheckOptions

Output a 17 byte unique consumer identifier for requestor and/or verify an input 17 byte unique consumer identifier.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Output a 17 byte unique consumer identifier for requestor and/or verify an input 17 byte unique consumer identifier. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**getUniqueConsumerIdentifier** | str,  | str,  | Y -17 byte unique consumer identifier on output. | [optional] 
**verifyPrimaryConsumerIdentifier** | str,  | str,  | Y - 17 byte unique consumer identifier output for Primary Applicant. | [optional] 
**verifySecondaryConsumerIdentifier** | str,  | str,  | Y - 17 byte unique consumer identifier output for Secondary Applicant. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

