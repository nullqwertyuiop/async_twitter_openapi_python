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
from twitter_openapi_python_generated.models.users_response_data import UsersResponseData  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestUsersResponseData(unittest.TestCase):
    """UsersResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UsersResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsersResponseData`
        """
        model = twitter_openapi_python_generated.models.users_response_data.UsersResponseData()  # noqa: E501
        if include_optional :
            return UsersResponseData(
                users = [
                    twitter_openapi_python_generated.models.user_results.UserResults(
                        result = null, )
                    ]
            )
        else :
            return UsersResponseData(
                users = [
                    twitter_openapi_python_generated.models.user_results.UserResults(
                        result = null, )
                    ],
        )
        """

    def testUsersResponseData(self):
        """Test UsersResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
