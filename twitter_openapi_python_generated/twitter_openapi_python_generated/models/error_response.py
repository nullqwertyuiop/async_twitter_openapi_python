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



from pydantic import BaseModel, Field
from twitter_openapi_python_generated.models.errors import Errors

class ErrorResponse(BaseModel):
    """
    ErrorResponse
    """
    errors: Errors = Field(...)
    __properties = ["errors"]

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
    def from_json(cls, json_str: str) -> ErrorResponse:
        """Create an instance of ErrorResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ErrorResponse:
        """Create an instance of ErrorResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ErrorResponse.parse_obj(obj)

        _obj = ErrorResponse.parse_obj({
            "errors": Errors.from_dict(obj.get("errors")) if obj.get("errors") is not None else None
        })
        return _obj


