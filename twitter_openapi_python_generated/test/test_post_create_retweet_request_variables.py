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
from twitter_openapi_python_generated.models.post_create_retweet_request_variables import PostCreateRetweetRequestVariables  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestPostCreateRetweetRequestVariables(unittest.TestCase):
    """PostCreateRetweetRequestVariables unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostCreateRetweetRequestVariables
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateRetweetRequestVariables`
        """
        model = twitter_openapi_python_generated.models.post_create_retweet_request_variables.PostCreateRetweetRequestVariables()  # noqa: E501
        if include_optional :
            return PostCreateRetweetRequestVariables(
                dark_request = False, 
                tweet_id = '1349129669258448897'
            )
        else :
            return PostCreateRetweetRequestVariables(
                dark_request = False,
                tweet_id = '1349129669258448897',
        )
        """

    def testPostCreateRetweetRequestVariables(self):
        """Test PostCreateRetweetRequestVariables"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
