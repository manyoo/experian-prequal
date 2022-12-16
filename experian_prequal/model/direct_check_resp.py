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


class DirectCheckResp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            subscriberAddress = schemas.StrSchema
            subscriberCity = schemas.StrSchema
            subscriberCode = schemas.StrSchema
            subscriberName = schemas.StrSchema
            subscriberPhone = schemas.StrSchema
            subscriberState = schemas.StrSchema
            subscriberZipCode = schemas.StrSchema
            __annotations__ = {
                "subscriberAddress": subscriberAddress,
                "subscriberCity": subscriberCity,
                "subscriberCode": subscriberCode,
                "subscriberName": subscriberName,
                "subscriberPhone": subscriberPhone,
                "subscriberState": subscriberState,
                "subscriberZipCode": subscriberZipCode,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberAddress"]) -> MetaOapg.properties.subscriberAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberCity"]) -> MetaOapg.properties.subscriberCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberCode"]) -> MetaOapg.properties.subscriberCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberName"]) -> MetaOapg.properties.subscriberName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberPhone"]) -> MetaOapg.properties.subscriberPhone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberState"]) -> MetaOapg.properties.subscriberState: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberZipCode"]) -> MetaOapg.properties.subscriberZipCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["subscriberAddress", "subscriberCity", "subscriberCode", "subscriberName", "subscriberPhone", "subscriberState", "subscriberZipCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberAddress"]) -> typing.Union[MetaOapg.properties.subscriberAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberCity"]) -> typing.Union[MetaOapg.properties.subscriberCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberCode"]) -> typing.Union[MetaOapg.properties.subscriberCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberName"]) -> typing.Union[MetaOapg.properties.subscriberName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberPhone"]) -> typing.Union[MetaOapg.properties.subscriberPhone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberState"]) -> typing.Union[MetaOapg.properties.subscriberState, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberZipCode"]) -> typing.Union[MetaOapg.properties.subscriberZipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["subscriberAddress", "subscriberCity", "subscriberCode", "subscriberName", "subscriberPhone", "subscriberState", "subscriberZipCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        subscriberAddress: typing.Union[MetaOapg.properties.subscriberAddress, str, schemas.Unset] = schemas.unset,
        subscriberCity: typing.Union[MetaOapg.properties.subscriberCity, str, schemas.Unset] = schemas.unset,
        subscriberCode: typing.Union[MetaOapg.properties.subscriberCode, str, schemas.Unset] = schemas.unset,
        subscriberName: typing.Union[MetaOapg.properties.subscriberName, str, schemas.Unset] = schemas.unset,
        subscriberPhone: typing.Union[MetaOapg.properties.subscriberPhone, str, schemas.Unset] = schemas.unset,
        subscriberState: typing.Union[MetaOapg.properties.subscriberState, str, schemas.Unset] = schemas.unset,
        subscriberZipCode: typing.Union[MetaOapg.properties.subscriberZipCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DirectCheckResp':
        return super().__new__(
            cls,
            *args,
            subscriberAddress=subscriberAddress,
            subscriberCity=subscriberCity,
            subscriberCode=subscriberCode,
            subscriberName=subscriberName,
            subscriberPhone=subscriberPhone,
            subscriberState=subscriberState,
            subscriberZipCode=subscriberZipCode,
            _configuration=_configuration,
            **kwargs,
        )
