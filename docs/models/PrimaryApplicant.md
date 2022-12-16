# experian_prequal.model.primary_applicant.PrimaryApplicant

Primary Credit Applicant Information

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Primary Credit Applicant Information | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | [**PAName**](PAName.md) | [**PAName**](PAName.md) |  | 
**currentAddress** | [**Address**](Address.md) | [**Address**](Address.md) |  | 
**dob** | [**DOB**](DOB.md) | [**DOB**](DOB.md) |  | [optional] 
**ssn** | [**SSN**](SSN.md) | [**SSN**](SSN.md) |  | [optional] 
**driverslicense** | [**DriverLicense**](DriverLicense.md) | [**DriverLicense**](DriverLicense.md) |  | [optional] 
**[phone](#phone)** | list, tuple,  | tuple,  |  | [optional] 
**employment** | [**Employment**](Employment.md) | [**Employment**](Employment.md) |  | [optional] 
**[previousAddress](#previousAddress)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# phone

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Phone**](Phone.md) | [**Phone**](Phone.md) | [**Phone**](Phone.md) |  | 

# previousAddress

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Address**](Address.md) | [**Address**](Address.md) | [**Address**](Address.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

