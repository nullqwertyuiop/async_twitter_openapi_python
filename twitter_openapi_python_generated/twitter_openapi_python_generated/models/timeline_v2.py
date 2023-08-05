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



from pydantic import BaseModel, Field
from twitter_openapi_python_generated.models.timeline import Timeline

class TimelineV2(BaseModel):
    """
    TimelineV2
    """
    timeline: Timeline = Field(...)
    __properties = ["timeline"]

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
    def from_json(cls, json_str: str) -> TimelineV2:
        """Create an instance of TimelineV2 from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of timeline
        if self.timeline:
            _dict['timeline'] = self.timeline.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineV2:
        """Create an instance of TimelineV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineV2.parse_obj(obj)

        _obj = TimelineV2.parse_obj({
            "timeline": Timeline.from_dict(obj.get("timeline")) if obj.get("timeline") is not None else None
        })
        return _obj

