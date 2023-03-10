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


class ConsumerAssistanceReferralAddress(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            cityStateZip = schemas.StrSchema
            officeName = schemas.StrSchema
            phone = schemas.StrSchema
            poBox = schemas.StrSchema
            streetName = schemas.StrSchema
            __annotations__ = {
                "cityStateZip": cityStateZip,
                "officeName": officeName,
                "phone": phone,
                "poBox": poBox,
                "streetName": streetName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cityStateZip"]) -> MetaOapg.properties.cityStateZip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["officeName"]) -> MetaOapg.properties.officeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["poBox"]) -> MetaOapg.properties.poBox: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["streetName"]) -> MetaOapg.properties.streetName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cityStateZip", "officeName", "phone", "poBox", "streetName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cityStateZip"]) -> typing.Union[MetaOapg.properties.cityStateZip, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["officeName"]) -> typing.Union[MetaOapg.properties.officeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["poBox"]) -> typing.Union[MetaOapg.properties.poBox, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["streetName"]) -> typing.Union[MetaOapg.properties.streetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cityStateZip", "officeName", "phone", "poBox", "streetName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cityStateZip: typing.Union[MetaOapg.properties.cityStateZip, str, schemas.Unset] = schemas.unset,
        officeName: typing.Union[MetaOapg.properties.officeName, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, str, schemas.Unset] = schemas.unset,
        poBox: typing.Union[MetaOapg.properties.poBox, str, schemas.Unset] = schemas.unset,
        streetName: typing.Union[MetaOapg.properties.streetName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConsumerAssistanceReferralAddress':
        return super().__new__(
            cls,
            *args,
            cityStateZip=cityStateZip,
            officeName=officeName,
            phone=phone,
            poBox=poBox,
            streetName=streetName,
            _configuration=_configuration,
            **kwargs,
        )
