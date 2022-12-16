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


class PAName(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Consumer's Name
    """


    class MetaOapg:
        required = {
            "firstName",
            "lastName",
        }
        
        class properties:
            lastName = schemas.StrSchema
            firstName = schemas.StrSchema
            middleName = schemas.StrSchema
            generationCode = schemas.StrSchema
            __annotations__ = {
                "lastName": lastName,
                "firstName": firstName,
                "middleName": middleName,
                "generationCode": generationCode,
            }
    
    firstName: MetaOapg.properties.firstName
    lastName: MetaOapg.properties.lastName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["middleName"]) -> MetaOapg.properties.middleName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["generationCode"]) -> MetaOapg.properties.generationCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["lastName", "firstName", "middleName", "generationCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["middleName"]) -> typing.Union[MetaOapg.properties.middleName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["generationCode"]) -> typing.Union[MetaOapg.properties.generationCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["lastName", "firstName", "middleName", "generationCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        firstName: typing.Union[MetaOapg.properties.firstName, str, ],
        lastName: typing.Union[MetaOapg.properties.lastName, str, ],
        middleName: typing.Union[MetaOapg.properties.middleName, str, schemas.Unset] = schemas.unset,
        generationCode: typing.Union[MetaOapg.properties.generationCode, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PAName':
        return super().__new__(
            cls,
            *args,
            firstName=firstName,
            lastName=lastName,
            middleName=middleName,
            generationCode=generationCode,
            _configuration=_configuration,
            **kwargs,
        )