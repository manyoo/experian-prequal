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


class Address(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Consumer's Address
    """


    class MetaOapg:
        required = {
            "line1",
        }
        
        class properties:
            line1 = schemas.StrSchema
            line2 = schemas.StrSchema
            city = schemas.StrSchema
            state = schemas.StrSchema
            zipCode = schemas.StrSchema
            __annotations__ = {
                "line1": line1,
                "line2": line2,
                "city": city,
                "state": state,
                "zipCode": zipCode,
            }
    
    line1: MetaOapg.properties.line1
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line1"]) -> MetaOapg.properties.line1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line2"]) -> MetaOapg.properties.line2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zipCode"]) -> MetaOapg.properties.zipCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["line1", "line2", "city", "state", "zipCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line1"]) -> MetaOapg.properties.line1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line2"]) -> typing.Union[MetaOapg.properties.line2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zipCode"]) -> typing.Union[MetaOapg.properties.zipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["line1", "line2", "city", "state", "zipCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        line1: typing.Union[MetaOapg.properties.line1, str, ],
        line2: typing.Union[MetaOapg.properties.line2, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        zipCode: typing.Union[MetaOapg.properties.zipCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Address':
        return super().__new__(
            cls,
            *args,
            line1=line1,
            line2=line2,
            city=city,
            state=state,
            zipCode=zipCode,
            _configuration=_configuration,
            **kwargs,
        )