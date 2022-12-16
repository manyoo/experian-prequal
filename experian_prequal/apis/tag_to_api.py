import typing_extensions

from experian_prequal.apis.tags import TagValues
from experian_prequal.apis.tags.consumer_services_api import ConsumerServicesApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CONSUMER_SERVICES: ConsumerServicesApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CONSUMER_SERVICES: ConsumerServicesApi,
    }
)
