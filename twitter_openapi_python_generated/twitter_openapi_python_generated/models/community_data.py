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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from twitter_openapi_python_generated.models.community_actions import CommunityActions
from twitter_openapi_python_generated.models.community_invites_result import CommunityInvitesResult
from twitter_openapi_python_generated.models.community_join_requests_result import CommunityJoinRequestsResult
from twitter_openapi_python_generated.models.community_rule import CommunityRule
from twitter_openapi_python_generated.models.community_urls import CommunityUrls
from twitter_openapi_python_generated.models.primary_community_topic import PrimaryCommunityTopic
from twitter_openapi_python_generated.models.type_name import TypeName
from twitter_openapi_python_generated.models.user_results import UserResults
from typing import Optional, Set
from typing_extensions import Self

class CommunityData(BaseModel):
    """
    CommunityData
    """ # noqa: E501
    typename: TypeName = Field(alias="__typename")
    actions: CommunityActions
    admin_results: UserResults
    created_at: Optional[StrictInt] = None
    creator_results: UserResults
    custom_banner_media: Optional[Dict[str, Any]] = None
    default_banner_media: Optional[Dict[str, Any]] = None
    description: StrictStr
    id_str: Annotated[str, Field(strict=True)]
    invites_policy: StrictStr
    invites_result: CommunityInvitesResult
    is_pinned: StrictBool
    join_policy: StrictStr
    join_requests_result: Optional[CommunityJoinRequestsResult] = None
    member_count: StrictInt
    members_facepile_results: List[UserResults]
    moderator_count: StrictInt
    name: StrictStr
    primary_community_topic: Optional[PrimaryCommunityTopic] = None
    question: StrictStr
    role: StrictStr
    rules: List[CommunityRule]
    search_tags: List[StrictStr]
    show_only_users_to_display: Optional[List[StrictStr]] = None
    urls: Optional[CommunityUrls] = None
    viewer_relationship: Optional[Dict[str, Any]] = None
    __properties: ClassVar[List[str]] = ["__typename", "actions", "admin_results", "created_at", "creator_results", "custom_banner_media", "default_banner_media", "description", "id_str", "invites_policy", "invites_result", "is_pinned", "join_policy", "join_requests_result", "member_count", "members_facepile_results", "moderator_count", "name", "primary_community_topic", "question", "role", "rules", "search_tags", "show_only_users_to_display", "urls", "viewer_relationship"]

    @field_validator('id_str')
    def id_str_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[0-9]+$", value):
            raise ValueError(r"must validate the regular expression /^[0-9]+$/")
        return value

    @field_validator('invites_policy')
    def invites_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MemberInvitesAllowed']):
            raise ValueError("must be one of enum values ('MemberInvitesAllowed')")
        return value

    @field_validator('join_policy')
    def join_policy_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['Open']):
            raise ValueError("must be one of enum values ('Open')")
        return value

    @field_validator('role')
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['NonMember']):
            raise ValueError("must be one of enum values ('NonMember')")
        return value

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
        """Create an instance of CommunityData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actions
        if self.actions:
            _dict['actions'] = self.actions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of admin_results
        if self.admin_results:
            _dict['admin_results'] = self.admin_results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator_results
        if self.creator_results:
            _dict['creator_results'] = self.creator_results.to_dict()
        # override the default output from pydantic by calling `to_dict()` of invites_result
        if self.invites_result:
            _dict['invites_result'] = self.invites_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of join_requests_result
        if self.join_requests_result:
            _dict['join_requests_result'] = self.join_requests_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in members_facepile_results (list)
        _items = []
        if self.members_facepile_results:
            for _item in self.members_facepile_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['members_facepile_results'] = _items
        # override the default output from pydantic by calling `to_dict()` of primary_community_topic
        if self.primary_community_topic:
            _dict['primary_community_topic'] = self.primary_community_topic.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in rules (list)
        _items = []
        if self.rules:
            for _item in self.rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['rules'] = _items
        # override the default output from pydantic by calling `to_dict()` of urls
        if self.urls:
            _dict['urls'] = self.urls.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CommunityData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "__typename": obj.get("__typename"),
            "actions": CommunityActions.from_dict(obj["actions"]) if obj.get("actions") is not None else None,
            "admin_results": UserResults.from_dict(obj["admin_results"]) if obj.get("admin_results") is not None else None,
            "created_at": obj.get("created_at"),
            "creator_results": UserResults.from_dict(obj["creator_results"]) if obj.get("creator_results") is not None else None,
            "custom_banner_media": obj.get("custom_banner_media"),
            "default_banner_media": obj.get("default_banner_media"),
            "description": obj.get("description"),
            "id_str": obj.get("id_str"),
            "invites_policy": obj.get("invites_policy"),
            "invites_result": CommunityInvitesResult.from_dict(obj["invites_result"]) if obj.get("invites_result") is not None else None,
            "is_pinned": obj.get("is_pinned"),
            "join_policy": obj.get("join_policy"),
            "join_requests_result": CommunityJoinRequestsResult.from_dict(obj["join_requests_result"]) if obj.get("join_requests_result") is not None else None,
            "member_count": obj.get("member_count"),
            "members_facepile_results": [UserResults.from_dict(_item) for _item in obj["members_facepile_results"]] if obj.get("members_facepile_results") is not None else None,
            "moderator_count": obj.get("moderator_count"),
            "name": obj.get("name"),
            "primary_community_topic": PrimaryCommunityTopic.from_dict(obj["primary_community_topic"]) if obj.get("primary_community_topic") is not None else None,
            "question": obj.get("question"),
            "role": obj.get("role"),
            "rules": [CommunityRule.from_dict(_item) for _item in obj["rules"]] if obj.get("rules") is not None else None,
            "search_tags": obj.get("search_tags"),
            "show_only_users_to_display": obj.get("show_only_users_to_display"),
            "urls": CommunityUrls.from_dict(obj["urls"]) if obj.get("urls") is not None else None,
            "viewer_relationship": obj.get("viewer_relationship")
        })
        return _obj

