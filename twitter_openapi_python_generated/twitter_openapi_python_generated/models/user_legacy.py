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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conlist, constr, validator

class UserLegacy(BaseModel):
    """
    UserLegacy
    """
    blocked_by: StrictBool = Field(...)
    blocking: StrictBool = Field(...)
    can_dm: StrictBool = Field(...)
    can_media_tag: StrictBool = Field(...)
    created_at: constr(strict=True) = Field(...)
    default_profile: StrictBool = Field(...)
    default_profile_image: StrictBool = Field(...)
    description: StrictStr = Field(...)
    entities: Dict[str, Any] = Field(...)
    fast_followers_count: StrictInt = Field(...)
    favourites_count: StrictInt = Field(...)
    follow_request_sent: StrictBool = Field(...)
    followed_by: StrictBool = Field(...)
    followers_count: StrictInt = Field(...)
    following: StrictBool = Field(...)
    friends_count: StrictInt = Field(...)
    has_custom_timelines: StrictBool = Field(...)
    is_translator: StrictBool = Field(...)
    listed_count: StrictInt = Field(...)
    location: StrictStr = Field(...)
    media_count: StrictInt = Field(...)
    muting: StrictBool = Field(...)
    name: StrictStr = Field(...)
    normal_followers_count: StrictInt = Field(...)
    notifications: StrictBool = Field(...)
    pinned_tweet_ids_str: conlist(StrictStr) = Field(...)
    possibly_sensitive: StrictBool = Field(...)
    profile_banner_extensions: Optional[Dict[str, Any]] = None
    profile_banner_url: Optional[StrictStr] = None
    profile_image_extensions: Optional[Dict[str, Any]] = None
    profile_image_url_https: StrictStr = Field(...)
    profile_interstitial_type: StrictStr = Field(...)
    protected: StrictBool = Field(...)
    screen_name: StrictStr = Field(...)
    statuses_count: StrictInt = Field(...)
    translator_type: StrictStr = Field(...)
    url: Optional[StrictStr] = None
    verified: StrictBool = Field(...)
    want_retweets: StrictBool = Field(...)
    __properties = ["blocked_by", "blocking", "can_dm", "can_media_tag", "created_at", "default_profile", "default_profile_image", "description", "entities", "fast_followers_count", "favourites_count", "follow_request_sent", "followed_by", "followers_count", "following", "friends_count", "has_custom_timelines", "is_translator", "listed_count", "location", "media_count", "muting", "name", "normal_followers_count", "notifications", "pinned_tweet_ids_str", "possibly_sensitive", "profile_banner_extensions", "profile_banner_url", "profile_image_extensions", "profile_image_url_https", "profile_interstitial_type", "protected", "screen_name", "statuses_count", "translator_type", "url", "verified", "want_retweets"]

    @validator('created_at')
    def created_at_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0[1-9]|[12][0-9]|3[01]) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]) ([+-][0-9]{4}) ([0-9]{4})$", value):
            raise ValueError(r"must validate the regular expression /^(Sun|Mon|Tue|Wed|Thu|Fri|Sat) (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0[1-9]|[12][0-9]|3[01]) (0[0-9]|1[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]) ([+-][0-9]{4}) ([0-9]{4})$/")
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
    def from_json(cls, json_str: str) -> UserLegacy:
        """Create an instance of UserLegacy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserLegacy:
        """Create an instance of UserLegacy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserLegacy.parse_obj(obj)

        _obj = UserLegacy.parse_obj({
            "blocked_by": obj.get("blocked_by") if obj.get("blocked_by") is not None else False,
            "blocking": obj.get("blocking") if obj.get("blocking") is not None else False,
            "can_dm": obj.get("can_dm") if obj.get("can_dm") is not None else False,
            "can_media_tag": obj.get("can_media_tag") if obj.get("can_media_tag") is not None else False,
            "created_at": obj.get("created_at"),
            "default_profile": obj.get("default_profile") if obj.get("default_profile") is not None else False,
            "default_profile_image": obj.get("default_profile_image") if obj.get("default_profile_image") is not None else False,
            "description": obj.get("description"),
            "entities": obj.get("entities"),
            "fast_followers_count": obj.get("fast_followers_count"),
            "favourites_count": obj.get("favourites_count") if obj.get("favourites_count") is not None else 0,
            "follow_request_sent": obj.get("follow_request_sent") if obj.get("follow_request_sent") is not None else False,
            "followed_by": obj.get("followed_by") if obj.get("followed_by") is not None else False,
            "followers_count": obj.get("followers_count") if obj.get("followers_count") is not None else 0,
            "following": obj.get("following") if obj.get("following") is not None else False,
            "friends_count": obj.get("friends_count") if obj.get("friends_count") is not None else 0,
            "has_custom_timelines": obj.get("has_custom_timelines") if obj.get("has_custom_timelines") is not None else False,
            "is_translator": obj.get("is_translator") if obj.get("is_translator") is not None else False,
            "listed_count": obj.get("listed_count") if obj.get("listed_count") is not None else 0,
            "location": obj.get("location"),
            "media_count": obj.get("media_count") if obj.get("media_count") is not None else 0,
            "muting": obj.get("muting") if obj.get("muting") is not None else False,
            "name": obj.get("name"),
            "normal_followers_count": obj.get("normal_followers_count") if obj.get("normal_followers_count") is not None else 0,
            "notifications": obj.get("notifications") if obj.get("notifications") is not None else False,
            "pinned_tweet_ids_str": obj.get("pinned_tweet_ids_str"),
            "possibly_sensitive": obj.get("possibly_sensitive") if obj.get("possibly_sensitive") is not None else False,
            "profile_banner_extensions": obj.get("profile_banner_extensions"),
            "profile_banner_url": obj.get("profile_banner_url"),
            "profile_image_extensions": obj.get("profile_image_extensions"),
            "profile_image_url_https": obj.get("profile_image_url_https"),
            "profile_interstitial_type": obj.get("profile_interstitial_type"),
            "protected": obj.get("protected") if obj.get("protected") is not None else False,
            "screen_name": obj.get("screen_name"),
            "statuses_count": obj.get("statuses_count") if obj.get("statuses_count") is not None else 0,
            "translator_type": obj.get("translator_type"),
            "url": obj.get("url"),
            "verified": obj.get("verified"),
            "want_retweets": obj.get("want_retweets") if obj.get("want_retweets") is not None else False
        })
        return _obj

