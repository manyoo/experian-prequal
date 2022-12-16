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


class Statement(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Consumer Statements present onfile.
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['StatementResp']:
            return StatementResp

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['StatementResp'], typing.List['StatementResp']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Statement':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'StatementResp':
        return super().__getitem__(i)

from experian_prequal.model.statement_resp import StatementResp