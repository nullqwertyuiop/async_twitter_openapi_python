# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field, constr, validator
from twitter_openapi_python_generated.models.content_union import ContentUnion

class TimelineAddEntry(BaseModel):
    """
    TimelineAddEntry
    """
    content: ContentUnion = Field(...)
    entry_id: constr(strict=True) = Field(..., alias="entryId")
    sort_index: constr(strict=True) = Field(..., alias="sortIndex")
    __properties = ["content", "entryId", "sortIndex"]

    @validator('entry_id')
    def entry_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z\-]+[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z\-]+[0-9]+$/")
        return value

    @validator('sort_index')
    def sort_index_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /[0-9]+$/")
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
    def from_json(cls, json_str: str) -> TimelineAddEntry:
        """Create an instance of TimelineAddEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict['content'] = self.content.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineAddEntry:
        """Create an instance of TimelineAddEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineAddEntry.parse_obj(obj)

        _obj = TimelineAddEntry.parse_obj({
            "content": ContentUnion.from_dict(obj.get("content")) if obj.get("content") is not None else None,
            "entry_id": obj.get("entryId"),
            "sort_index": obj.get("sortIndex")
        })
        return _obj

