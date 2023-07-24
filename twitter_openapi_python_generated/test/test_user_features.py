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
from twitter_openapi_python_generated.models.user_features import UserFeatures  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestUserFeatures(unittest.TestCase):
    """UserFeatures unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserFeatures
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserFeatures`
        """
        model = twitter_openapi_python_generated.models.user_features.UserFeatures()  # noqa: E501
        if include_optional :
            return UserFeatures(
                mediatool_studio_library = True
            )
        else :
            return UserFeatures(
                mediatool_studio_library = True,
        )
        """

    def testUserFeatures(self):
        """Test UserFeatures"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
