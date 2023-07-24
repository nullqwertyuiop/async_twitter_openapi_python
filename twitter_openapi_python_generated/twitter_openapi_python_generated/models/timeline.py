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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, conlist
from twitter_openapi_python_generated.models.instruction_union import InstructionUnion

class Timeline(BaseModel):
    """
    Timeline
    """
    instructions: conlist(InstructionUnion) = Field(...)
    metadata: Optional[Dict[str, Any]] = None
    response_objects: Optional[Dict[str, Any]] = Field(None, alias="responseObjects")
    __properties = ["instructions", "metadata", "responseObjects"]

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
    def from_json(cls, json_str: str) -> Timeline:
        """Create an instance of Timeline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in instructions (list)
        _items = []
        if self.instructions:
            for _item in self.instructions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['instructions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Timeline:
        """Create an instance of Timeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Timeline.parse_obj(obj)

        _obj = Timeline.parse_obj({
            "instructions": [InstructionUnion.from_dict(_item) for _item in obj.get("instructions")] if obj.get("instructions") is not None else None,
            "metadata": obj.get("metadata"),
            "response_objects": obj.get("responseObjects")
        })
        return _obj

