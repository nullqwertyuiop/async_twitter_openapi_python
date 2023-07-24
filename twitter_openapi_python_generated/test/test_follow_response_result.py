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
from twitter_openapi_python_generated.models.follow_response_result import FollowResponseResult  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestFollowResponseResult(unittest.TestCase):
    """FollowResponseResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FollowResponseResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FollowResponseResult`
        """
        model = twitter_openapi_python_generated.models.follow_response_result.FollowResponseResult()  # noqa: E501
        if include_optional :
            return FollowResponseResult(
                typename = 'TimelineTweet', 
                timeline = twitter_openapi_python_generated.models.follow_timeline.FollowTimeline(
                    timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                        instructions = [
                            null
                            ], 
                        metadata = twitter_openapi_python_generated.models.metadata.metadata(), 
                        response_objects = twitter_openapi_python_generated.models.response_objects.responseObjects(), ), )
            )
        else :
            return FollowResponseResult(
                typename = 'TimelineTweet',
                timeline = twitter_openapi_python_generated.models.follow_timeline.FollowTimeline(
                    timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                        instructions = [
                            null
                            ], 
                        metadata = twitter_openapi_python_generated.models.metadata.metadata(), 
                        response_objects = twitter_openapi_python_generated.models.response_objects.responseObjects(), ), ),
        )
        """

    def testFollowResponseResult(self):
        """Test FollowResponseResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
