# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import StrictBool, StrictInt, StrictStr


from twitter_openapi_python_generated.api_client import ApiClient
from twitter_openapi_python_generated.api_response import ApiResponse
from twitter_openapi_python_generated.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class V20GetApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_search_adaptive(self, include_profile_interstitial_type : StrictInt, include_blocking : StrictInt, include_blocked_by : StrictInt, include_followed_by : StrictInt, include_want_retweets : StrictInt, include_mute_edge : StrictInt, include_can_dm : StrictInt, include_can_media_tag : StrictInt, include_ext_has_nft_avatar : StrictInt, include_ext_is_blue_verified : StrictInt, include_ext_verified_type : StrictInt, include_ext_profile_image_shape : StrictInt, skip_status : StrictInt, cards_platform : StrictStr, include_cards : StrictInt, include_ext_alt_text : StrictBool, include_ext_limited_action_results : StrictBool, include_quote_count : StrictBool, include_reply_count : StrictInt, tweet_mode : StrictStr, include_ext_views : StrictBool, include_entities : StrictBool, include_user_entities : StrictBool, include_ext_media_color : StrictBool, include_ext_media_availability : StrictBool, include_ext_sensitive_media_warning : StrictBool, include_ext_trusted_friends_metadata : StrictBool, send_error_codes : StrictBool, simple_quoted_tweet : StrictBool, q : StrictStr, query_source : StrictStr, count : StrictInt, request_context : StrictStr, pc : StrictInt, spelling_corrections : StrictInt, include_ext_edit_control : StrictBool, ext : StrictStr, **kwargs) -> None:  # noqa: E501
        """get_search_adaptive  # noqa: E501

        get search adaptive  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_search_adaptive(include_profile_interstitial_type, include_blocking, include_blocked_by, include_followed_by, include_want_retweets, include_mute_edge, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_verified_type, include_ext_profile_image_shape, skip_status, cards_platform, include_cards, include_ext_alt_text, include_ext_limited_action_results, include_quote_count, include_reply_count, tweet_mode, include_ext_views, include_entities, include_user_entities, include_ext_media_color, include_ext_media_availability, include_ext_sensitive_media_warning, include_ext_trusted_friends_metadata, send_error_codes, simple_quoted_tweet, q, query_source, count, request_context, pc, spelling_corrections, include_ext_edit_control, ext, async_req=True)
        >>> result = thread.get()

        :param include_profile_interstitial_type: (required)
        :type include_profile_interstitial_type: int
        :param include_blocking: (required)
        :type include_blocking: int
        :param include_blocked_by: (required)
        :type include_blocked_by: int
        :param include_followed_by: (required)
        :type include_followed_by: int
        :param include_want_retweets: (required)
        :type include_want_retweets: int
        :param include_mute_edge: (required)
        :type include_mute_edge: int
        :param include_can_dm: (required)
        :type include_can_dm: int
        :param include_can_media_tag: (required)
        :type include_can_media_tag: int
        :param include_ext_has_nft_avatar: (required)
        :type include_ext_has_nft_avatar: int
        :param include_ext_is_blue_verified: (required)
        :type include_ext_is_blue_verified: int
        :param include_ext_verified_type: (required)
        :type include_ext_verified_type: int
        :param include_ext_profile_image_shape: (required)
        :type include_ext_profile_image_shape: int
        :param skip_status: (required)
        :type skip_status: int
        :param cards_platform: (required)
        :type cards_platform: str
        :param include_cards: (required)
        :type include_cards: int
        :param include_ext_alt_text: (required)
        :type include_ext_alt_text: bool
        :param include_ext_limited_action_results: (required)
        :type include_ext_limited_action_results: bool
        :param include_quote_count: (required)
        :type include_quote_count: bool
        :param include_reply_count: (required)
        :type include_reply_count: int
        :param tweet_mode: (required)
        :type tweet_mode: str
        :param include_ext_views: (required)
        :type include_ext_views: bool
        :param include_entities: (required)
        :type include_entities: bool
        :param include_user_entities: (required)
        :type include_user_entities: bool
        :param include_ext_media_color: (required)
        :type include_ext_media_color: bool
        :param include_ext_media_availability: (required)
        :type include_ext_media_availability: bool
        :param include_ext_sensitive_media_warning: (required)
        :type include_ext_sensitive_media_warning: bool
        :param include_ext_trusted_friends_metadata: (required)
        :type include_ext_trusted_friends_metadata: bool
        :param send_error_codes: (required)
        :type send_error_codes: bool
        :param simple_quoted_tweet: (required)
        :type simple_quoted_tweet: bool
        :param q: (required)
        :type q: str
        :param query_source: (required)
        :type query_source: str
        :param count: (required)
        :type count: int
        :param request_context: (required)
        :type request_context: str
        :param pc: (required)
        :type pc: int
        :param spelling_corrections: (required)
        :type spelling_corrections: int
        :param include_ext_edit_control: (required)
        :type include_ext_edit_control: bool
        :param ext: (required)
        :type ext: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_search_adaptive_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_search_adaptive_with_http_info(include_profile_interstitial_type, include_blocking, include_blocked_by, include_followed_by, include_want_retweets, include_mute_edge, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_verified_type, include_ext_profile_image_shape, skip_status, cards_platform, include_cards, include_ext_alt_text, include_ext_limited_action_results, include_quote_count, include_reply_count, tweet_mode, include_ext_views, include_entities, include_user_entities, include_ext_media_color, include_ext_media_availability, include_ext_sensitive_media_warning, include_ext_trusted_friends_metadata, send_error_codes, simple_quoted_tweet, q, query_source, count, request_context, pc, spelling_corrections, include_ext_edit_control, ext, **kwargs)  # noqa: E501

    @validate_arguments
    def get_search_adaptive_with_http_info(self, include_profile_interstitial_type : StrictInt, include_blocking : StrictInt, include_blocked_by : StrictInt, include_followed_by : StrictInt, include_want_retweets : StrictInt, include_mute_edge : StrictInt, include_can_dm : StrictInt, include_can_media_tag : StrictInt, include_ext_has_nft_avatar : StrictInt, include_ext_is_blue_verified : StrictInt, include_ext_verified_type : StrictInt, include_ext_profile_image_shape : StrictInt, skip_status : StrictInt, cards_platform : StrictStr, include_cards : StrictInt, include_ext_alt_text : StrictBool, include_ext_limited_action_results : StrictBool, include_quote_count : StrictBool, include_reply_count : StrictInt, tweet_mode : StrictStr, include_ext_views : StrictBool, include_entities : StrictBool, include_user_entities : StrictBool, include_ext_media_color : StrictBool, include_ext_media_availability : StrictBool, include_ext_sensitive_media_warning : StrictBool, include_ext_trusted_friends_metadata : StrictBool, send_error_codes : StrictBool, simple_quoted_tweet : StrictBool, q : StrictStr, query_source : StrictStr, count : StrictInt, request_context : StrictStr, pc : StrictInt, spelling_corrections : StrictInt, include_ext_edit_control : StrictBool, ext : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_search_adaptive  # noqa: E501

        get search adaptive  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_search_adaptive_with_http_info(include_profile_interstitial_type, include_blocking, include_blocked_by, include_followed_by, include_want_retweets, include_mute_edge, include_can_dm, include_can_media_tag, include_ext_has_nft_avatar, include_ext_is_blue_verified, include_ext_verified_type, include_ext_profile_image_shape, skip_status, cards_platform, include_cards, include_ext_alt_text, include_ext_limited_action_results, include_quote_count, include_reply_count, tweet_mode, include_ext_views, include_entities, include_user_entities, include_ext_media_color, include_ext_media_availability, include_ext_sensitive_media_warning, include_ext_trusted_friends_metadata, send_error_codes, simple_quoted_tweet, q, query_source, count, request_context, pc, spelling_corrections, include_ext_edit_control, ext, async_req=True)
        >>> result = thread.get()

        :param include_profile_interstitial_type: (required)
        :type include_profile_interstitial_type: int
        :param include_blocking: (required)
        :type include_blocking: int
        :param include_blocked_by: (required)
        :type include_blocked_by: int
        :param include_followed_by: (required)
        :type include_followed_by: int
        :param include_want_retweets: (required)
        :type include_want_retweets: int
        :param include_mute_edge: (required)
        :type include_mute_edge: int
        :param include_can_dm: (required)
        :type include_can_dm: int
        :param include_can_media_tag: (required)
        :type include_can_media_tag: int
        :param include_ext_has_nft_avatar: (required)
        :type include_ext_has_nft_avatar: int
        :param include_ext_is_blue_verified: (required)
        :type include_ext_is_blue_verified: int
        :param include_ext_verified_type: (required)
        :type include_ext_verified_type: int
        :param include_ext_profile_image_shape: (required)
        :type include_ext_profile_image_shape: int
        :param skip_status: (required)
        :type skip_status: int
        :param cards_platform: (required)
        :type cards_platform: str
        :param include_cards: (required)
        :type include_cards: int
        :param include_ext_alt_text: (required)
        :type include_ext_alt_text: bool
        :param include_ext_limited_action_results: (required)
        :type include_ext_limited_action_results: bool
        :param include_quote_count: (required)
        :type include_quote_count: bool
        :param include_reply_count: (required)
        :type include_reply_count: int
        :param tweet_mode: (required)
        :type tweet_mode: str
        :param include_ext_views: (required)
        :type include_ext_views: bool
        :param include_entities: (required)
        :type include_entities: bool
        :param include_user_entities: (required)
        :type include_user_entities: bool
        :param include_ext_media_color: (required)
        :type include_ext_media_color: bool
        :param include_ext_media_availability: (required)
        :type include_ext_media_availability: bool
        :param include_ext_sensitive_media_warning: (required)
        :type include_ext_sensitive_media_warning: bool
        :param include_ext_trusted_friends_metadata: (required)
        :type include_ext_trusted_friends_metadata: bool
        :param send_error_codes: (required)
        :type send_error_codes: bool
        :param simple_quoted_tweet: (required)
        :type simple_quoted_tweet: bool
        :param q: (required)
        :type q: str
        :param query_source: (required)
        :type query_source: str
        :param count: (required)
        :type count: int
        :param request_context: (required)
        :type request_context: str
        :param pc: (required)
        :type pc: int
        :param spelling_corrections: (required)
        :type spelling_corrections: int
        :param include_ext_edit_control: (required)
        :type include_ext_edit_control: bool
        :param ext: (required)
        :type ext: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'include_profile_interstitial_type',
            'include_blocking',
            'include_blocked_by',
            'include_followed_by',
            'include_want_retweets',
            'include_mute_edge',
            'include_can_dm',
            'include_can_media_tag',
            'include_ext_has_nft_avatar',
            'include_ext_is_blue_verified',
            'include_ext_verified_type',
            'include_ext_profile_image_shape',
            'skip_status',
            'cards_platform',
            'include_cards',
            'include_ext_alt_text',
            'include_ext_limited_action_results',
            'include_quote_count',
            'include_reply_count',
            'tweet_mode',
            'include_ext_views',
            'include_entities',
            'include_user_entities',
            'include_ext_media_color',
            'include_ext_media_availability',
            'include_ext_sensitive_media_warning',
            'include_ext_trusted_friends_metadata',
            'send_error_codes',
            'simple_quoted_tweet',
            'q',
            'query_source',
            'count',
            'request_context',
            'pc',
            'spelling_corrections',
            'include_ext_edit_control',
            'ext'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_search_adaptive" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('include_profile_interstitial_type') is not None:  # noqa: E501
            _query_params.append(('include_profile_interstitial_type', _params['include_profile_interstitial_type']))

        if _params.get('include_blocking') is not None:  # noqa: E501
            _query_params.append(('include_blocking', _params['include_blocking']))

        if _params.get('include_blocked_by') is not None:  # noqa: E501
            _query_params.append(('include_blocked_by', _params['include_blocked_by']))

        if _params.get('include_followed_by') is not None:  # noqa: E501
            _query_params.append(('include_followed_by', _params['include_followed_by']))

        if _params.get('include_want_retweets') is not None:  # noqa: E501
            _query_params.append(('include_want_retweets', _params['include_want_retweets']))

        if _params.get('include_mute_edge') is not None:  # noqa: E501
            _query_params.append(('include_mute_edge', _params['include_mute_edge']))

        if _params.get('include_can_dm') is not None:  # noqa: E501
            _query_params.append(('include_can_dm', _params['include_can_dm']))

        if _params.get('include_can_media_tag') is not None:  # noqa: E501
            _query_params.append(('include_can_media_tag', _params['include_can_media_tag']))

        if _params.get('include_ext_has_nft_avatar') is not None:  # noqa: E501
            _query_params.append(('include_ext_has_nft_avatar', _params['include_ext_has_nft_avatar']))

        if _params.get('include_ext_is_blue_verified') is not None:  # noqa: E501
            _query_params.append(('include_ext_is_blue_verified', _params['include_ext_is_blue_verified']))

        if _params.get('include_ext_verified_type') is not None:  # noqa: E501
            _query_params.append(('include_ext_verified_type', _params['include_ext_verified_type']))

        if _params.get('include_ext_profile_image_shape') is not None:  # noqa: E501
            _query_params.append(('include_ext_profile_image_shape', _params['include_ext_profile_image_shape']))

        if _params.get('skip_status') is not None:  # noqa: E501
            _query_params.append(('skip_status', _params['skip_status']))

        if _params.get('cards_platform') is not None:  # noqa: E501
            _query_params.append(('cards_platform', _params['cards_platform']))

        if _params.get('include_cards') is not None:  # noqa: E501
            _query_params.append(('include_cards', _params['include_cards']))

        if _params.get('include_ext_alt_text') is not None:  # noqa: E501
            _query_params.append(('include_ext_alt_text', _params['include_ext_alt_text']))

        if _params.get('include_ext_limited_action_results') is not None:  # noqa: E501
            _query_params.append(('include_ext_limited_action_results', _params['include_ext_limited_action_results']))

        if _params.get('include_quote_count') is not None:  # noqa: E501
            _query_params.append(('include_quote_count', _params['include_quote_count']))

        if _params.get('include_reply_count') is not None:  # noqa: E501
            _query_params.append(('include_reply_count', _params['include_reply_count']))

        if _params.get('tweet_mode') is not None:  # noqa: E501
            _query_params.append(('tweet_mode', _params['tweet_mode']))

        if _params.get('include_ext_views') is not None:  # noqa: E501
            _query_params.append(('include_ext_views', _params['include_ext_views']))

        if _params.get('include_entities') is not None:  # noqa: E501
            _query_params.append(('include_entities', _params['include_entities']))

        if _params.get('include_user_entities') is not None:  # noqa: E501
            _query_params.append(('include_user_entities', _params['include_user_entities']))

        if _params.get('include_ext_media_color') is not None:  # noqa: E501
            _query_params.append(('include_ext_media_color', _params['include_ext_media_color']))

        if _params.get('include_ext_media_availability') is not None:  # noqa: E501
            _query_params.append(('include_ext_media_availability', _params['include_ext_media_availability']))

        if _params.get('include_ext_sensitive_media_warning') is not None:  # noqa: E501
            _query_params.append(('include_ext_sensitive_media_warning', _params['include_ext_sensitive_media_warning']))

        if _params.get('include_ext_trusted_friends_metadata') is not None:  # noqa: E501
            _query_params.append(('include_ext_trusted_friends_metadata', _params['include_ext_trusted_friends_metadata']))

        if _params.get('send_error_codes') is not None:  # noqa: E501
            _query_params.append(('send_error_codes', _params['send_error_codes']))

        if _params.get('simple_quoted_tweet') is not None:  # noqa: E501
            _query_params.append(('simple_quoted_tweet', _params['simple_quoted_tweet']))

        if _params.get('q') is not None:  # noqa: E501
            _query_params.append(('q', _params['q']))

        if _params.get('query_source') is not None:  # noqa: E501
            _query_params.append(('query_source', _params['query_source']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('request_context') is not None:  # noqa: E501
            _query_params.append(('requestContext', _params['request_context']))

        if _params.get('pc') is not None:  # noqa: E501
            _query_params.append(('pc', _params['pc']))

        if _params.get('spelling_corrections') is not None:  # noqa: E501
            _query_params.append(('spelling_corrections', _params['spelling_corrections']))

        if _params.get('include_ext_edit_control') is not None:  # noqa: E501
            _query_params.append(('include_ext_edit_control', _params['include_ext_edit_control']))

        if _params.get('ext') is not None:  # noqa: E501
            _query_params.append(('ext', _params['ext']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['ClientLanguage', 'CookieCt0', 'ActiveUser', 'UserAgent', 'CookieAuthToken', 'AuthType', 'CsrfToken', 'GuestToken', 'BearerAuth']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/2/search/adaptive.json', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
