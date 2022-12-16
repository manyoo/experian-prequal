# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from experian_prequal.paths.v1_credit_score import Api

from experian_prequal.paths import PathValues

path = PathValues.V1_CREDITSCORE