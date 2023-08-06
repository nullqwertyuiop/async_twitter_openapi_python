# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class TypeName(str, Enum):
    """
    TypeName
    """

    """
    allowed enum values
    """
    TIMELINETWEET = 'TimelineTweet'
    TIMELINETIMELINEITEM = 'TimelineTimelineItem'
    TIMELINEUSER = 'TimelineUser'
    TIMELINETIMELINECURSOR = 'TimelineTimelineCursor'
    TWEETWITHVISIBILITYRESULTS = 'TweetWithVisibilityResults'
    TIMELINETIMELINEMODULE = 'TimelineTimelineModule'
    TWEETTOMBSTONE = 'TweetTombstone'
    TIMELINEPROMPT = 'TimelinePrompt'
    TIMELINEMESSAGEPROMPT = 'TimelineMessagePrompt'
    TWEET = 'Tweet'
    USER = 'User'
    USERUNAVAILABLE = 'UserUnavailable'

    @classmethod
    def from_json(cls, json_str: str) -> TypeName:
        """Create an instance of TypeName from a JSON string"""
        return TypeName(json.loads(json_str))


