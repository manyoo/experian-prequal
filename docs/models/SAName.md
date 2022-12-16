# experian_prequal.model.sa_name.SAName

Consumer's Name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Consumer&#x27;s Name | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firstName** | str,  | str,  | The full first name is required. The minimum entry is the first name initial. Blanks and special characters (except dash) are not allowed. Compound names should contain a dash (e.g., Billy-Bob). | 
**lastName** | str,  | str,  | The full applicant&#x27;s surname is required. If the surname contains two surnames, then split the surnames with a hyphen (e.g., Smith-Jones). The surname can also be input with an apostrophe (e.g., O&#x27;Brien), although apostrophe usage is limited to the letters D, L, and O. | [optional] 
**middleName** | str,  | str,  | The full middle name should be entered when available. A middle initial is acceptable. Blanks and special characters are not allowed. Omit if the middle name is not available. | [optional] 
**generationCode** | str,  | str,  | Generation Code - Enum - [Jr, Sr, II, III, IV, V, VI, VII, VIII, IX], Default - Sr | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

