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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictBool, constr, validator
from twitter_openapi_python_generated.models.type_name import TypeName
from twitter_openapi_python_generated.models.user_legacy import UserLegacy

class User(BaseModel):
    """
    User
    """
    typename: TypeName = Field(..., alias="__typename")
    affiliates_highlighted_label: Dict[str, Any] = Field(...)
    business_account: Optional[Dict[str, Any]] = None
    has_graduated_access: Optional[StrictBool] = None
    has_nft_avatar: Optional[StrictBool] = False
    id: constr(strict=True) = Field(...)
    is_blue_verified: StrictBool = Field(...)
    legacy: UserLegacy = Field(...)
    rest_id: constr(strict=True) = Field(...)
    super_follow_eligible: StrictBool = Field(...)
    super_followed_by: StrictBool = Field(...)
    super_following: StrictBool = Field(...)
    __properties = ["__typename", "affiliates_highlighted_label", "business_account", "has_graduated_access", "has_nft_avatar", "id", "is_blue_verified", "legacy", "rest_id", "super_follow_eligible", "super_followed_by", "super_following"]

    @validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-z\-]+[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z\-]+[0-9]+$/")
        return value

    @validator('rest_id')
    def rest_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]+$/")
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
    def from_json(cls, json_str: str) -> User:
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of legacy
        if self.legacy:
            _dict['legacy'] = self.legacy.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> User:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return User.parse_obj(obj)

        _obj = User.parse_obj({
            "typename": obj.get("__typename"),
            "affiliates_highlighted_label": obj.get("affiliates_highlighted_label"),
            "business_account": obj.get("business_account"),
            "has_graduated_access": obj.get("has_graduated_access"),
            "has_nft_avatar": obj.get("has_nft_avatar") if obj.get("has_nft_avatar") is not None else False,
            "id": obj.get("id"),
            "is_blue_verified": obj.get("is_blue_verified") if obj.get("is_blue_verified") is not None else False,
            "legacy": UserLegacy.from_dict(obj.get("legacy")) if obj.get("legacy") is not None else None,
            "rest_id": obj.get("rest_id"),
            "super_follow_eligible": obj.get("super_follow_eligible") if obj.get("super_follow_eligible") is not None else False,
            "super_followed_by": obj.get("super_followed_by") if obj.get("super_followed_by") is not None else False,
            "super_following": obj.get("super_following") if obj.get("super_following") is not None else False
        })
        return _obj

