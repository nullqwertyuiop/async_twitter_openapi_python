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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from twitter_openapi_python_generated.models.social_context import SocialContext
from twitter_openapi_python_generated.models.type_name import TypeName
from twitter_openapi_python_generated.models.user_results import UserResults

class TimelineUser(BaseModel):
    """
    TimelineUser
    """
    social_context: Optional[SocialContext] = Field(None, alias="SocialContext")
    typename: TypeName = Field(..., alias="__typename")
    item_type: StrictStr = Field(..., alias="itemType")
    user_display_type: StrictStr = Field(..., alias="userDisplayType")
    user_results: UserResults = Field(...)
    __properties = ["SocialContext", "__typename", "itemType", "userDisplayType", "user_results"]

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
    def from_json(cls, json_str: str) -> TimelineUser:
        """Create an instance of TimelineUser from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of social_context
        if self.social_context:
            _dict['SocialContext'] = self.social_context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_results
        if self.user_results:
            _dict['user_results'] = self.user_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TimelineUser:
        """Create an instance of TimelineUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TimelineUser.parse_obj(obj)

        _obj = TimelineUser.parse_obj({
            "social_context": SocialContext.from_dict(obj.get("SocialContext")) if obj.get("SocialContext") is not None else None,
            "typename": obj.get("__typename"),
            "item_type": obj.get("itemType"),
            "user_display_type": obj.get("userDisplayType"),
            "user_results": UserResults.from_dict(obj.get("user_results")) if obj.get("user_results") is not None else None
        })
        return _obj

