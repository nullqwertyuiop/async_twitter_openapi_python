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
from twitter_openapi_python_generated.models.delete_tweet_response_result import DeleteTweetResponseResult  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestDeleteTweetResponseResult(unittest.TestCase):
    """DeleteTweetResponseResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DeleteTweetResponseResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeleteTweetResponseResult`
        """
        model = twitter_openapi_python_generated.models.delete_tweet_response_result.DeleteTweetResponseResult()  # noqa: E501
        if include_optional :
            return DeleteTweetResponseResult(
                tweet_results = twitter_openapi_python_generated.models.tweet_results.tweet_results()
            )
        else :
            return DeleteTweetResponseResult(
                tweet_results = twitter_openapi_python_generated.models.tweet_results.tweet_results(),
        )
        """

    def testDeleteTweetResponseResult(self):
        """Test DeleteTweetResponseResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
