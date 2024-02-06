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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from typing_extensions import Annotated
from twitter_openapi_python_generated.models.entities import Entities
from twitter_openapi_python_generated.models.note_tweet_result_media import NoteTweetResultMedia
from twitter_openapi_python_generated.models.note_tweet_result_rich_text import NoteTweetResultRichText
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class NoteTweetResultData(BaseModel):
    """
    NoteTweetResultData
    """ # noqa: E501
    entity_set: Entities
    id: Annotated[str, Field(strict=True)]
    media: Optional[NoteTweetResultMedia] = None
    richtext: Optional[NoteTweetResultRichText] = None
    text: StrictStr
    __properties: ClassVar[List[str]] = ["entity_set", "id", "media", "richtext", "text"]

    @field_validator('id')
    def id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^([A-Za-z0-9+\/]{4})*([A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}==)?$", value):
            raise ValueError(r"must validate the regular expression /^([A-Za-z0-9+\/]{4})*([A-Za-z0-9+\/]{3}=|[A-Za-z0-9+\/]{2}==)?$/")
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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of NoteTweetResultData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of entity_set
        if self.entity_set:
            _dict['entity_set'] = self.entity_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of richtext
        if self.richtext:
            _dict['richtext'] = self.richtext.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of NoteTweetResultData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "entity_set": Entities.from_dict(obj.get("entity_set")) if obj.get("entity_set") is not None else None,
            "id": obj.get("id"),
            "media": NoteTweetResultMedia.from_dict(obj.get("media")) if obj.get("media") is not None else None,
            "richtext": NoteTweetResultRichText.from_dict(obj.get("richtext")) if obj.get("richtext") is not None else None,
            "text": obj.get("text")
        })
        return _obj

