import typing_extensions

from experian_prequal.paths import PathValues
from experian_prequal.apis.paths.v1_credit_score import V1CreditScore
from experian_prequal.apis.paths.v1_credit_report import V1CreditReport

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_CREDITSCORE: V1CreditScore,
        PathValues.V1_CREDITREPORT: V1CreditReport,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_CREDITSCORE: V1CreditScore,
        PathValues.V1_CREDITREPORT: V1CreditReport,
    }
)
