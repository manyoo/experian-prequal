# coding: utf-8

"""
    Prequalification Credit Report

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: OpenAPI3.1.0.12
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from experian_prequal import schemas  # noqa: F401


class FreezeOverride(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    If a consumer's profile is frozen, then consumer can get a password using which a lender can override the freeze and get credit data. This parameter is provided when consumer has provided the lender with the password to override his profile freeze.
    """


    class MetaOapg:
        
        class properties:
            primaryApplFreezeOverrideCode = schemas.StrSchema
            secondaryApplFreezeOverrideCode = schemas.StrSchema
            __annotations__ = {
                "primaryApplFreezeOverrideCode": primaryApplFreezeOverrideCode,
                "secondaryApplFreezeOverrideCode": secondaryApplFreezeOverrideCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primaryApplFreezeOverrideCode"]) -> MetaOapg.properties.primaryApplFreezeOverrideCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryApplFreezeOverrideCode"]) -> MetaOapg.properties.secondaryApplFreezeOverrideCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["primaryApplFreezeOverrideCode", "secondaryApplFreezeOverrideCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primaryApplFreezeOverrideCode"]) -> typing.Union[MetaOapg.properties.primaryApplFreezeOverrideCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryApplFreezeOverrideCode"]) -> typing.Union[MetaOapg.properties.secondaryApplFreezeOverrideCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["primaryApplFreezeOverrideCode", "secondaryApplFreezeOverrideCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        primaryApplFreezeOverrideCode: typing.Union[MetaOapg.properties.primaryApplFreezeOverrideCode, str, schemas.Unset] = schemas.unset,
        secondaryApplFreezeOverrideCode: typing.Union[MetaOapg.properties.secondaryApplFreezeOverrideCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FreezeOverride':
        return super().__new__(
            cls,
            *args,
            primaryApplFreezeOverrideCode=primaryApplFreezeOverrideCode,
            secondaryApplFreezeOverrideCode=secondaryApplFreezeOverrideCode,
            _configuration=_configuration,
            **kwargs,
        )
