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
from typing import Any, ClassVar, Dict, List, Optional
from twitter_openapi_python_generated.models.tweet_interstitial import TweetInterstitial
from twitter_openapi_python_generated.models.type_name import TypeName
from typing import Optional, Set
from typing_extensions import Self

class TweetWithVisibilityResults(BaseModel):
    """
    TweetWithVisibilityResults
    """ # noqa: E501
    typename: TypeName = Field(alias="__typename")
    limited_action_results: Optional[Dict[str, Any]] = Field(default=None, alias="limitedActionResults")
    tweet: Tweet
    tweet_interstitial: Optional[TweetInterstitial] = Field(default=None, alias="tweetInterstitial")
    __properties: ClassVar[List[str]] = ["__typename", "limitedActionResults", "tweet", "tweetInterstitial"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TweetWithVisibilityResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tweet
        if self.tweet:
            _dict['tweet'] = self.tweet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tweet_interstitial
        if self.tweet_interstitial:
            _dict['tweetInterstitial'] = self.tweet_interstitial.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TweetWithVisibilityResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "__typename": obj.get("__typename"),
            "limitedActionResults": obj.get("limitedActionResults"),
            "tweet": Tweet.from_dict(obj["tweet"]) if obj.get("tweet") is not None else None,
            "tweetInterstitial": TweetInterstitial.from_dict(obj["tweetInterstitial"]) if obj.get("tweetInterstitial") is not None else None
        })
        return _obj

from twitter_openapi_python_generated.models.tweet import Tweet
# TODO: Rewrite to not use raise_errors
TweetWithVisibilityResults.model_rebuild(raise_errors=False)

