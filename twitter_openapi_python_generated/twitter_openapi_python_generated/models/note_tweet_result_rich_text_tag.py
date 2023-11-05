# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator

class NoteTweetResultRichTextTag(BaseModel):
    """
    NoteTweetResultRichTextTag
    """
    from_index: StrictInt = Field(...)
    richtext_types: conlist(StrictStr) = Field(...)
    to_index: StrictInt = Field(...)
    __properties = ["from_index", "richtext_types", "to_index"]

    @validator('richtext_types')
    def richtext_types_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in ('Bold', 'Italic'):
                raise ValueError("each list item must be one of ('Bold', 'Italic')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> NoteTweetResultRichTextTag:
        """Create an instance of NoteTweetResultRichTextTag from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> NoteTweetResultRichTextTag:
        """Create an instance of NoteTweetResultRichTextTag from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return NoteTweetResultRichTextTag.parse_obj(obj)

        _obj = NoteTweetResultRichTextTag.parse_obj({
            "from_index": obj.get("from_index"),
            "richtext_types": obj.get("richtext_types"),
            "to_index": obj.get("to_index")
        })
        return _obj


