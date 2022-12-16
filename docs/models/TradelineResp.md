# experian_prequal.model.tradeline_resp.TradelineResp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**accountType** | str,  | str,  | Indicates Type of Account. | [optional] 
**amount1** | str,  | str,  | Full dollar amount. | [optional] 
**amount1Qualifier** | str,  | str,  | Amount Type. | [optional] 
**amount2** | str,  | str,  | Full dollar amount. | [optional] 
**amount2Qualifier** | str,  | str,  | Amount Type. | [optional] 
**amountBalloonPayment** | str,  | str,  | Full dollar amount | [optional] 
**amountPastDue** | str,  | str,  | Full dollar amount | [optional] 
**balanceAmount** | str,  | str,  | Full dollar amount | [optional] 
**balanceDate** | str,  | str,  | Date account was last updated. Format &#x3D; MMDDCCYY. | [optional] 
**bankruptcyChapterNumber** | str,  | str,  | Bankruptcy Chapter Number. | [optional] 
**consumerComment** | str,  | str,  | Free Form Text from consumer. | [optional] 
**consumerDisputeFlag** | str,  | str,  | Indicates if trade is disputed by consumer. | [optional] 
**datePaymentDue** | str,  | str,  | Date balloon payment due. Format &#x3D; MMDDCCYY. | [optional] 
**delinquencies30Days** | str,  | str,  | 30 to 59 day delinquencies | [optional] 
**delinquencies60Days** | str,  | str,  | 60 to 89 day delinquencies | [optional] 
**delinquencies90to180Days** | str,  | str,  | 90 to 180 day delinquencies | [optional] 
**derogCounter** | str,  | str,  | Indicates the number of months the account has been reported as seriously derogatory. | [optional] 
**ecoa** | str,  | str,  | Attribute code. | [optional] 
**enhancedPaymentData** | [**EnhancedPaymentData**](EnhancedPaymentData.md) | [**EnhancedPaymentData**](EnhancedPaymentData.md) |  | [optional] 
**evaluation** | str,  | str,  | Indicates if additional review is required. | [optional] 
**kob** | str,  | str,  | Kind of business code of subscriber | [optional] 
**lastPaymentDate** | str,  | str,  | Date of last payment. Format &#x3D; MMDDCCYY. | [optional] 
**maxDelinquencyDate** | str,  | str,  | Date of worst payment code beyond the monthly payment profile. Format &#x3D; (MMDDCCYY) | [optional] 
**monthlyPaymentAmount** | str,  | str,  | Full dollar amount. | [optional] 
**monthlyPaymentType** | str,  | str,  |  | [optional] 
**monthsHistory** | str,  | str,  | Number of Months Reviewed | [optional] 
**openDate** | str,  | str,  | Date account opened. Format &#x3D; MMDDCCYY.  | [optional] 
**openOrClosed** | str,  | str,  | Indicates if trade is Open or Closed | [optional] 
**originalCreditorName** | str,  | str,  | Name of original creditor if a collection account. | [optional] 
**paymentHistory** | str,  | str,  | 84 Month payment history when requested on input. Otherwise 25 month payment history. | [optional] 
**revolvingOrInstallment** | str,  | str,  |  | [optional] 
**soldToName** | str,  | str,  | Name of the creditor to whom the account was sold. | [optional] 
**specialComment** | str,  | str,  | Special Comments. | [optional] 
**status** | str,  | str,  | Account Condition/Payment Status Codes. | [optional] 
**statusDate** | str,  | str,  | Account Status Date. Format &#x3D; MMDDCCYY. | [optional] 
**subscriberCode** | str,  | str,  | Subscriber number that reported tradeline. | [optional] 
**subscriberName** | str,  | str,  | Name of Subscriber | [optional] 
**terms** | str,  | str,  | Payment terms for the Account. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

