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



from pydantic import BaseModel, Field, StrictStr, validator
from twitter_openapi_python_generated.models.instruction_type import InstructionType

class TimelineTerminateTimeline(BaseModel):
    """
    TimelineTerminateTimeline
    """
    direction: StrictStr = Field(...)
    type: InstructionType = Field(...)
    __properties = ["direction", "type"]

    @validator('direction')
    def direction_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Top', 'Bottom'):
            raise ValueError("must be one of enum values ('Top', 'Bottom')")
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
    def from_json(cls, json_str: str) -> TimelineTerminateTimeline:
        """Create an instance of TimelineTerminateTimeline from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineTerminateTimeline:
        """Create an instance of TimelineTerminateTimeline from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineTerminateTimeline.parse_obj(obj)

        _obj = TimelineTerminateTimeline.parse_obj({
            "direction": obj.get("direction"),
            "type": obj.get("type")
        })
        return _obj

