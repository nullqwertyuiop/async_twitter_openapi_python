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
from twitter_openapi_python_generated.models.tweet_retweeters_response import TweetRetweetersResponse  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestTweetRetweetersResponse(unittest.TestCase):
    """TweetRetweetersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TweetRetweetersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TweetRetweetersResponse`
        """
        model = twitter_openapi_python_generated.models.tweet_retweeters_response.TweetRetweetersResponse()  # noqa: E501
        if include_optional :
            return TweetRetweetersResponse(
                data = twitter_openapi_python_generated.models.tweet_retweeters_response_data.TweetRetweetersResponseData(
                    retweeters_timeline = twitter_openapi_python_generated.models.timeline_v2.TimelineV2(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = twitter_openapi_python_generated.models.metadata.metadata(), 
                            response_objects = twitter_openapi_python_generated.models.response_objects.responseObjects(), ), ), )
            )
        else :
            return TweetRetweetersResponse(
                data = twitter_openapi_python_generated.models.tweet_retweeters_response_data.TweetRetweetersResponseData(
                    retweeters_timeline = twitter_openapi_python_generated.models.timeline_v2.TimelineV2(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = twitter_openapi_python_generated.models.metadata.metadata(), 
                            response_objects = twitter_openapi_python_generated.models.response_objects.responseObjects(), ), ), ),
        )
        """

    def testTweetRetweetersResponse(self):
        """Test TweetRetweetersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
