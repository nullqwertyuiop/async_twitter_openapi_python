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
from twitter_openapi_python_generated.models.other200_response import Other200Response  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestOther200Response(unittest.TestCase):
    """Other200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Other200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Other200Response`
        """
        model = twitter_openapi_python_generated.models.other200_response.Other200Response()  # noqa: E501
        if include_optional :
            return Other200Response(
                session = twitter_openapi_python_generated.models.session.Session(
                    sso_init_tokens = twitter_openapi_python_generated.models.sso_init_tokens.SsoInitTokens(), 
                    communities_actions = twitter_openapi_python_generated.models.communities_actions.CommunitiesActions(
                        create = True, ), 
                    country = 'AE', 
                    guest_id = '4', 
                    has_community_memberships = True, 
                    is_active_creator = True, 
                    is_restricted_session = True, 
                    is_super_follow_subscriber = True, 
                    language = 'ae', 
                    one_factor_login_eligibility = twitter_openapi_python_generated.models.one_factor_login_eligibility.OneFactorLoginEligibility(
                        fetch_status = '', ), 
                    super_followers_count = 56, 
                    super_follows_application_status = '', 
                    user_features = twitter_openapi_python_generated.models.user_features.UserFeatures(
                        mediatool_studio_library = True, ), 
                    user_id = '4', )
            )
        else :
            return Other200Response(
        )
        """

    def testOther200Response(self):
        """Test Other200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
