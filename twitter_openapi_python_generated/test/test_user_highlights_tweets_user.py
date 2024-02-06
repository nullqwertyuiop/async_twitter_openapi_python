# coding: utf-8

"""
    Twitter OpenAPI

    Twitter OpenAPI(Swagger) specification

    The version of the OpenAPI document: 0.0.1
    Contact: yuki@yuki0311.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from twitter_openapi_python_generated.models.user_highlights_tweets_user import UserHighlightsTweetsUser

class TestUserHighlightsTweetsUser(unittest.TestCase):
    """UserHighlightsTweetsUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserHighlightsTweetsUser:
        """Test UserHighlightsTweetsUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserHighlightsTweetsUser`
        """
        model = UserHighlightsTweetsUser()
        if include_optional:
            return UserHighlightsTweetsUser(
                result = twitter_openapi_python_generated.models.user_highlights_tweets_result.UserHighlightsTweetsResult(
                    __typename = 'TimelineTweet', 
                    timeline = twitter_openapi_python_generated.models.user_highlights_tweets_timeline.UserHighlightsTweetsTimeline(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), )
            )
        else:
            return UserHighlightsTweetsUser(
                result = twitter_openapi_python_generated.models.user_highlights_tweets_result.UserHighlightsTweetsResult(
                    __typename = 'TimelineTweet', 
                    timeline = twitter_openapi_python_generated.models.user_highlights_tweets_timeline.UserHighlightsTweetsTimeline(
                        timeline = twitter_openapi_python_generated.models.timeline.Timeline(
                            instructions = [
                                null
                                ], 
                            metadata = { }, 
                            response_objects = { }, ), ), ),
        )
        """

    def testUserHighlightsTweetsUser(self):
        """Test UserHighlightsTweetsUser"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
