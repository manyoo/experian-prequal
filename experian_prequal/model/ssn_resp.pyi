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


class SsnResp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            number = schemas.StrSchema
            ssnIndicators = schemas.StrSchema
            variationIndicator = schemas.StrSchema
            __annotations__ = {
                "number": number,
                "ssnIndicators": ssnIndicators,
                "variationIndicator": variationIndicator,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ssnIndicators"]) -> MetaOapg.properties.ssnIndicators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["variationIndicator"]) -> MetaOapg.properties.variationIndicator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["number", "ssnIndicators", "variationIndicator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ssnIndicators"]) -> typing.Union[MetaOapg.properties.ssnIndicators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["variationIndicator"]) -> typing.Union[MetaOapg.properties.variationIndicator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["number", "ssnIndicators", "variationIndicator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        ssnIndicators: typing.Union[MetaOapg.properties.ssnIndicators, str, schemas.Unset] = schemas.unset,
        variationIndicator: typing.Union[MetaOapg.properties.variationIndicator, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SsnResp':
        return super().__new__(
            cls,
            *args,
            number=number,
            ssnIndicators=ssnIndicators,
            variationIndicator=variationIndicator,
            _configuration=_configuration,
            **kwargs,
        )
