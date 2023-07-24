# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.profile_response import ProfileResponse  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestProfileResponse(unittest.TestCase):
    """ProfileResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProfileResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProfileResponse`
        """
        model = twitter_openapi_python_generated.models.profile_response.ProfileResponse()  # noqa: E501
        if include_optional :
            return ProfileResponse(
                data = twitter_openapi_python_generated.models.profile_response_data.ProfileResponseData(
                    user_result_by_screen_name = twitter_openapi_python_generated.models.user_result_by_screen_name.UserResultByScreenName(
                        id = 'C', 
                        result = twitter_openapi_python_generated.models.user_result_by_screen_name_result.UserResultByScreenNameResult(
                            __typename = 'TimelineTweet', 
                            id = 'G', 
                            legacy = twitter_openapi_python_generated.models.user_result_by_screen_name_legacy.UserResultByScreenNameLegacy(
                                blocked_by = True, 
                                blocking = True, 
                                followed_by = True, 
                                following = True, 
                                name = '', 
                                protected = True, 
                                screen_name = '', ), 
                            profilemodules = twitter_openapi_python_generated.models.profilemodules.profilemodules(), 
                            rest_id = '4', ), ), )
            )
        else :
            return ProfileResponse(
                data = twitter_openapi_python_generated.models.profile_response_data.ProfileResponseData(
                    user_result_by_screen_name = twitter_openapi_python_generated.models.user_result_by_screen_name.UserResultByScreenName(
                        id = 'C', 
                        result = twitter_openapi_python_generated.models.user_result_by_screen_name_result.UserResultByScreenNameResult(
                            __typename = 'TimelineTweet', 
                            id = 'G', 
                            legacy = twitter_openapi_python_generated.models.user_result_by_screen_name_legacy.UserResultByScreenNameLegacy(
                                blocked_by = True, 
                                blocking = True, 
                                followed_by = True, 
                                following = True, 
                                name = '', 
                                protected = True, 
                                screen_name = '', ), 
                            profilemodules = twitter_openapi_python_generated.models.profilemodules.profilemodules(), 
                            rest_id = '4', ), ), ),
        )
        """

    def testProfileResponse(self):
        """Test ProfileResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
