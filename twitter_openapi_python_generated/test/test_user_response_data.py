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
from twitter_openapi_python_generated.models.user_response_data import UserResponseData  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestUserResponseData(unittest.TestCase):
    """UserResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserResponseData`
        """
        model = twitter_openapi_python_generated.models.user_response_data.UserResponseData()  # noqa: E501
        if include_optional :
            return UserResponseData(
                user = twitter_openapi_python_generated.models.user_results.UserResults(
                    result = twitter_openapi_python_generated.models.user.User(
                        __typename = 'TimelineTweet', 
                        affiliates_highlighted_label = twitter_openapi_python_generated.models.affiliates_highlighted_label.affiliates_highlighted_label(), 
                        business_account = twitter_openapi_python_generated.models.business_account.business_account(), 
                        has_graduated_access = True, 
                        has_nft_avatar = True, 
                        id = 'q072888001528021798096225500850762068629', 
                        is_blue_verified = True, 
                        legacy = twitter_openapi_python_generated.models.user_legacy.UserLegacy(
                            blocked_by = True, 
                            blocking = True, 
                            can_dm = True, 
                            can_media_tag = True, 
                            created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                            default_profile = True, 
                            default_profile_image = True, 
                            description = '', 
                            entities = twitter_openapi_python_generated.models.entities.entities(), 
                            fast_followers_count = 56, 
                            favourites_count = 56, 
                            follow_request_sent = True, 
                            followed_by = True, 
                            followers_count = 56, 
                            following = True, 
                            friends_count = 56, 
                            has_custom_timelines = True, 
                            is_translator = True, 
                            listed_count = 56, 
                            location = '', 
                            media_count = 56, 
                            muting = True, 
                            name = '', 
                            normal_followers_count = 56, 
                            notifications = True, 
                            pinned_tweet_ids_str = [
                                ''
                                ], 
                            possibly_sensitive = True, 
                            profile_banner_extensions = twitter_openapi_python_generated.models.profile_banner_extensions.profile_banner_extensions(), 
                            profile_banner_url = '', 
                            profile_image_extensions = twitter_openapi_python_generated.models.profile_image_extensions.profile_image_extensions(), 
                            profile_image_url_https = '', 
                            profile_interstitial_type = '', 
                            protected = True, 
                            screen_name = '', 
                            statuses_count = 56, 
                            translator_type = '', 
                            url = '', 
                            verified = True, 
                            want_retweets = True, ), 
                        rest_id = '4', 
                        super_follow_eligible = True, 
                        super_followed_by = True, 
                        super_following = True, ), )
            )
        else :
            return UserResponseData(
                user = twitter_openapi_python_generated.models.user_results.UserResults(
                    result = twitter_openapi_python_generated.models.user.User(
                        __typename = 'TimelineTweet', 
                        affiliates_highlighted_label = twitter_openapi_python_generated.models.affiliates_highlighted_label.affiliates_highlighted_label(), 
                        business_account = twitter_openapi_python_generated.models.business_account.business_account(), 
                        has_graduated_access = True, 
                        has_nft_avatar = True, 
                        id = 'q072888001528021798096225500850762068629', 
                        is_blue_verified = True, 
                        legacy = twitter_openapi_python_generated.models.user_legacy.UserLegacy(
                            blocked_by = True, 
                            blocking = True, 
                            can_dm = True, 
                            can_media_tag = True, 
                            created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                            default_profile = True, 
                            default_profile_image = True, 
                            description = '', 
                            entities = twitter_openapi_python_generated.models.entities.entities(), 
                            fast_followers_count = 56, 
                            favourites_count = 56, 
                            follow_request_sent = True, 
                            followed_by = True, 
                            followers_count = 56, 
                            following = True, 
                            friends_count = 56, 
                            has_custom_timelines = True, 
                            is_translator = True, 
                            listed_count = 56, 
                            location = '', 
                            media_count = 56, 
                            muting = True, 
                            name = '', 
                            normal_followers_count = 56, 
                            notifications = True, 
                            pinned_tweet_ids_str = [
                                ''
                                ], 
                            possibly_sensitive = True, 
                            profile_banner_extensions = twitter_openapi_python_generated.models.profile_banner_extensions.profile_banner_extensions(), 
                            profile_banner_url = '', 
                            profile_image_extensions = twitter_openapi_python_generated.models.profile_image_extensions.profile_image_extensions(), 
                            profile_image_url_https = '', 
                            profile_interstitial_type = '', 
                            protected = True, 
                            screen_name = '', 
                            statuses_count = 56, 
                            translator_type = '', 
                            url = '', 
                            verified = True, 
                            want_retweets = True, ), 
                        rest_id = '4', 
                        super_follow_eligible = True, 
                        super_followed_by = True, 
                        super_following = True, ), ),
        )
        """

    def testUserResponseData(self):
        """Test UserResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
