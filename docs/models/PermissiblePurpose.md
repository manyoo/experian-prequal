# experian_prequal.model.permissible_purpose.PermissiblePurpose

Specifies information on why this credit inquiry is being submitted This is used to denote the purpose type, terms, and amount.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifies information on why this credit inquiry is being submitted This is used to denote the purpose type, terms, and amount. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Permissible Purpose Type Code. 2 digits containing the account type code only. Enum - [3F, 0B], Default - 3F | [optional] 
**terms** | str,  | str,  | The Terms must be 3 digits.  Type codes 08, 19, 25, 26,2C, 5A, 6B, 85, and 87 are mortgage loans with terms expressed in YEARS. Type codes 07, 15, 18, 37, 47, 4D, 89, 2A, 7A, 8A and 9B are revolving accounts with terms expressed as either \&quot;001\&quot; to indicate a monthly  payment plan or \&quot;010\&quot; to indicate a revolving account.All other type codes have terms that are expressed in MONTHS. | [optional] 
**abbreviatedAmount** | str,  | str,  | Input the amount of the account. Must be 3 digits. Type codes 08, 19, 25, 26, 5A, 85, and 87 are mortgage loans with amounts expressed in THOUSANDS. For example, a $100,000 VA mortgagefor 30 years would be entered as\&quot;100\&quot;. Under 1000; enter 000.  All other type accounts are expressed in HUNDREDS. For example, a $15,000 auto loan would be entered as \&quot;150\&quot;. Under 100; input 000. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

