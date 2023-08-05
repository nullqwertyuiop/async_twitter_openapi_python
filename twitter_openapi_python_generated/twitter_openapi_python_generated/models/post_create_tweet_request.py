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



from pydantic import BaseModel, Field, StrictStr
from twitter_openapi_python_generated.models.post_create_tweet_request_features import PostCreateTweetRequestFeatures
from twitter_openapi_python_generated.models.post_create_tweet_request_variables import PostCreateTweetRequestVariables

class PostCreateTweetRequest(BaseModel):
    """
    PostCreateTweetRequest
    """
    features: PostCreateTweetRequestFeatures = Field(...)
    query_id: StrictStr = Field(..., alias="queryId")
    variables: PostCreateTweetRequestVariables = Field(...)
    __properties = ["features", "queryId", "variables"]

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
    def from_json(cls, json_str: str) -> PostCreateTweetRequest:
        """Create an instance of PostCreateTweetRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict['features'] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of variables
        if self.variables:
            _dict['variables'] = self.variables.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PostCreateTweetRequest:
        """Create an instance of PostCreateTweetRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PostCreateTweetRequest.parse_obj(obj)

        _obj = PostCreateTweetRequest.parse_obj({
            "features": PostCreateTweetRequestFeatures.from_dict(obj.get("features")) if obj.get("features") is not None else None,
            "query_id": obj.get("queryId") if obj.get("queryId") is not None else '1RyAhNwby-gzGCRVsMxKbQ',
            "variables": PostCreateTweetRequestVariables.from_dict(obj.get("variables")) if obj.get("variables") is not None else None
        })
        return _obj

