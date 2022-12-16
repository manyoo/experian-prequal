# experian_prequal.model.enhanced_payment_data.EnhancedPaymentData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actualPaymentAmount** | str,  | str,  | Full dollar amount. | [optional] 
**chargeoffAmount** | str,  | str,  | Full dollar amount. | [optional] 
**ciiCode** | str,  | str,  | Consumer Information Indicator. | [optional] 
**complianceCondition** | str,  | str,  | Compliance Conditon Code. | [optional] 
**creditLimitAmount** | str,  | str,  | Full dollar amount. | [optional] 
**enhancedAccountCondition** | str,  | str,  | Account Condition Code. Codes.  | [optional] 
**enhancedAccountType** | str,  | str,  | Indicates Type of Account. | [optional] 
**enhancedPaymentHistory84** | str,  | str,  | 84 Month enhanced payment history.  | [optional] 
**enhancedPaymentStatus** | str,  | str,  | Payment Status Codes. | [optional] 
**enhancedSpecialComment** | str,  | str,  | Special Comments. | [optional] 
**enhancedTerms** | str,  | str,  | Payment Terms. | [optional] 
**enhancedTermsFrequency** | str,  | str,  | Frequency for Payments Due. | [optional] 
**firstDelinquencyDate** | str,  | str,  | Most Recent Delinquency Date (MMDDCCYY) | [optional] 
**highBalanceAmount** | str,  | str,  | Full dollar amount. | [optional] 
**maxDelinquencyCode** | str,  | str,  | Highest payment code for maximum delinquency date | [optional] 
**mortgageId** | str,  | str,  | Mortgage ID. | [optional] 
**originalCreditorClassificationCode** | str,  | str,  | General type of business of the Original Creditor.  | [optional] 
**originalLoanAmount** | str,  | str,  | Full dollar amount. | [optional] 
**paymentLevelDate** | str,  | str,  | Date the account first reached present status level. Format &#x3D; MMDDCCYY. | [optional] 
**purchasedPortfolioFromName** | str,  | str,  | Purchased Portfolio Name. | [optional] 
**secondDelinquencyDate** | str,  | str,  | Second Most Recent Delinquency Date(MMDDCCYY) | [optional] 
**secondaryAgencyCode** | str,  | str,  | Secondary Agency Code. | [optional] 
**secondaryAgencyId** | str,  | str,  | Secondary Agency Id | [optional] 
**specialPaymentAmount** | str,  | str,  | Full dollar amount | [optional] 
**specialPaymentCode** | str,  | str,  | Additional Information about the Payment Amount. | [optional] 
**specialPaymentDate** | str,  | str,  | Special Payment Date Format &#x3D; MMDDCCYY. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

