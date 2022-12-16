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


class ConsumerIdentityPhone(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Present when DemographicsAll or DemographicsPhone is requested on input or via subcode option.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ConsumerIdentityPhoneResp']:
            return ConsumerIdentityPhoneResp

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ConsumerIdentityPhoneResp'], typing.List['ConsumerIdentityPhoneResp']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ConsumerIdentityPhone':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ConsumerIdentityPhoneResp':
        return super().__getitem__(i)

from experian_prequal.model.consumer_identity_phone_resp import ConsumerIdentityPhoneResp
