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
from twitter_openapi_python_generated.models.post_create_tweet_request import PostCreateTweetRequest  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestPostCreateTweetRequest(unittest.TestCase):
    """PostCreateTweetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PostCreateTweetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateTweetRequest`
        """
        model = twitter_openapi_python_generated.models.post_create_tweet_request.PostCreateTweetRequest()  # noqa: E501
        if include_optional :
            return PostCreateTweetRequest(
                features = twitter_openapi_python_generated.models.post_create_tweet_request_features.postCreateTweet_request_features(
                    blue_business_profile_image_shape_enabled = True, 
                    freedom_of_speech_not_reach_fetch_enabled = True, 
                    graphql_is_translatable_rweb_tweet_is_translatable_enabled = True, 
                    interactive_text_enabled = True, 
                    longform_notetweets_consumption_enabled = True, 
                    longform_notetweets_rich_text_read_enabled = True, 
                    responsive_web_edit_tweet_api_enabled = True, 
                    responsive_web_enhance_cards_enabled = False, 
                    responsive_web_graphql_exclude_directive_enabled = True, 
                    responsive_web_graphql_skip_user_profile_image_extensions_enabled = False, 
                    responsive_web_graphql_timeline_navigation_enabled = True, 
                    responsive_web_text_conversations_enabled = False, 
                    standardized_nudges_misinfo = True, 
                    tweet_awards_web_tipping_enabled = False, 
                    tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled = False, 
                    tweetypie_unmention_optimization_enabled = True, 
                    verified_phone_label_enabled = False, 
                    vibe_api_enabled = True, 
                    view_counts_everywhere_api_enabled = True, ), 
                query_id = '1RyAhNwby-gzGCRVsMxKbQ', 
                variables = twitter_openapi_python_generated.models.post_create_tweet_request_variables.postCreateTweet_request_variables(
                    dark_request = False, 
                    media = twitter_openapi_python_generated.models.post_create_tweet_request_variables_media.postCreateTweet_request_variables_media(
                        media_entities = [
                            None
                            ], 
                        possibly_sensitive = False, ), 
                    semantic_annotation_ids = [
                        None
                        ], 
                    tweet_text = 'test', )
            )
        else :
            return PostCreateTweetRequest(
                features = twitter_openapi_python_generated.models.post_create_tweet_request_features.postCreateTweet_request_features(
                    blue_business_profile_image_shape_enabled = True, 
                    freedom_of_speech_not_reach_fetch_enabled = True, 
                    graphql_is_translatable_rweb_tweet_is_translatable_enabled = True, 
                    interactive_text_enabled = True, 
                    longform_notetweets_consumption_enabled = True, 
                    longform_notetweets_rich_text_read_enabled = True, 
                    responsive_web_edit_tweet_api_enabled = True, 
                    responsive_web_enhance_cards_enabled = False, 
                    responsive_web_graphql_exclude_directive_enabled = True, 
                    responsive_web_graphql_skip_user_profile_image_extensions_enabled = False, 
                    responsive_web_graphql_timeline_navigation_enabled = True, 
                    responsive_web_text_conversations_enabled = False, 
                    standardized_nudges_misinfo = True, 
                    tweet_awards_web_tipping_enabled = False, 
                    tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled = False, 
                    tweetypie_unmention_optimization_enabled = True, 
                    verified_phone_label_enabled = False, 
                    vibe_api_enabled = True, 
                    view_counts_everywhere_api_enabled = True, ),
                query_id = '1RyAhNwby-gzGCRVsMxKbQ',
                variables = twitter_openapi_python_generated.models.post_create_tweet_request_variables.postCreateTweet_request_variables(
                    dark_request = False, 
                    media = twitter_openapi_python_generated.models.post_create_tweet_request_variables_media.postCreateTweet_request_variables_media(
                        media_entities = [
                            None
                            ], 
                        possibly_sensitive = False, ), 
                    semantic_annotation_ids = [
                        None
                        ], 
                    tweet_text = 'test', ),
        )
        """

    def testPostCreateTweetRequest(self):
        """Test PostCreateTweetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
