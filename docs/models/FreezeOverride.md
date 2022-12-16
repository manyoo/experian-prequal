# experian_prequal.model.freeze_override.FreezeOverride

If a consumer's profile is frozen, then consumer can get a password using which a lender can override the freeze and get credit data. This parameter is provided when consumer has provided the lender with the password to override his profile freeze.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | If a consumer&#x27;s profile is frozen, then consumer can get a password using which a lender can override the freeze and get credit data. This parameter is provided when consumer has provided the lender with the password to override his profile freeze. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**primaryApplFreezeOverrideCode** | str,  | str,  | This is the freeze override code for the primary applicant Used when a consumer has authorized the client to access his or her frozen file and has provided the client with his or her pass code. This passcode is to be provided to Experian so that Experian can override the freeze and return credit data for the consumer back to the client. | [optional] 
**secondaryApplFreezeOverrideCode** | str,  | str,  | This is the freeze override code for the secondary applicant Used when a consumer has authorized the client to access his or her frozen file and has provided the client with his or her pass code. This passcode is to be provided to Experian so that Experian can override the freeze and return credit data for the consumer back to the client. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

