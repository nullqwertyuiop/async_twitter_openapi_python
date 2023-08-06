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

from pydantic import StrictStr

from twitter_openapi_python_generated.models.get_users_by_rest_ids200_response import GetUsersByRestIds200Response

from twitter_openapi_python_generated.api_client import ApiClient
from twitter_openapi_python_generated.api_response import ApiResponse
from twitter_openapi_python_generated.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class UsersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def get_users_by_rest_ids(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> GetUsersByRestIds200Response:  # noqa: E501
        """get_users_by_rest_ids  # noqa: E501

        get users by rest ids  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_by_rest_ids(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetUsersByRestIds200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_users_by_rest_ids_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_users_by_rest_ids_with_http_info(path_query_id, variables, features, **kwargs)  # noqa: E501

    @validate_arguments
    def get_users_by_rest_ids_with_http_info(self, path_query_id : StrictStr, variables : StrictStr, features : StrictStr, **kwargs) -> ApiResponse:  # noqa: E501
        """get_users_by_rest_ids  # noqa: E501

        get users by rest ids  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_users_by_rest_ids_with_http_info(path_query_id, variables, features, async_req=True)
        >>> result = thread.get()

        :param path_query_id: (required)
        :type path_query_id: str
        :param variables: (required)
        :type variables: str
        :param features: (required)
        :type features: str
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
        :rtype: tuple(GetUsersByRestIds200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'path_query_id',
            'variables',
            'features'
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
                    " to method get_users_by_rest_ids" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['path_query_id']:
            _path_params['pathQueryId'] = _params['path_query_id']


        # process the query parameters
        _query_params = []
        if _params.get('variables') is not None:  # noqa: E501
            _query_params.append(('variables', _params['variables']))

        if _params.get('features') is not None:  # noqa: E501
            _query_params.append(('features', _params['features']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ClientLanguage', 'CookieCt0', 'ActiveUser', 'UserAgent', 'CookieAuthToken', 'AuthType', 'CsrfToken', 'GuestToken', 'BearerAuth']  # noqa: E501

        _response_types_map = {
            '200': "GetUsersByRestIds200Response",
        }

        return self.api_client.call_api(
            '/graphql/{pathQueryId}/UsersByRestIds', 'GET',
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
