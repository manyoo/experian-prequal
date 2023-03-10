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


class InquiryResp(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            amount = schemas.StrSchema
            date = schemas.StrSchema
            kob = schemas.StrSchema
            subscriberCode = schemas.StrSchema
            subscriberName = schemas.StrSchema
            terms = schemas.StrSchema
            type = schemas.StrSchema
            __annotations__ = {
                "amount": amount,
                "date": date,
                "kob": kob,
                "subscriberCode": subscriberCode,
                "subscriberName": subscriberName,
                "terms": terms,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date"]) -> MetaOapg.properties.date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["kob"]) -> MetaOapg.properties.kob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberCode"]) -> MetaOapg.properties.subscriberCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["subscriberName"]) -> MetaOapg.properties.subscriberName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terms"]) -> MetaOapg.properties.terms: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "date", "kob", "subscriberCode", "subscriberName", "terms", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date"]) -> typing.Union[MetaOapg.properties.date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["kob"]) -> typing.Union[MetaOapg.properties.kob, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberCode"]) -> typing.Union[MetaOapg.properties.subscriberCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["subscriberName"]) -> typing.Union[MetaOapg.properties.subscriberName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terms"]) -> typing.Union[MetaOapg.properties.terms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "date", "kob", "subscriberCode", "subscriberName", "terms", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        date: typing.Union[MetaOapg.properties.date, str, schemas.Unset] = schemas.unset,
        kob: typing.Union[MetaOapg.properties.kob, str, schemas.Unset] = schemas.unset,
        subscriberCode: typing.Union[MetaOapg.properties.subscriberCode, str, schemas.Unset] = schemas.unset,
        subscriberName: typing.Union[MetaOapg.properties.subscriberName, str, schemas.Unset] = schemas.unset,
        terms: typing.Union[MetaOapg.properties.terms, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InquiryResp':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            date=date,
            kob=kob,
            subscriberCode=subscriberCode,
            subscriberName=subscriberName,
            terms=terms,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
