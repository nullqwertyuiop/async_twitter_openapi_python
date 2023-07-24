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
from twitter_openapi_python_generated.models.create_tweet import CreateTweet  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestCreateTweet(unittest.TestCase):
    """CreateTweet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateTweet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateTweet`
        """
        model = twitter_openapi_python_generated.models.create_tweet.CreateTweet()  # noqa: E501
        if include_optional :
            return CreateTweet(
                result = twitter_openapi_python_generated.models.tweet.Tweet(
                    __typename = 'TimelineTweet', 
                    card = twitter_openapi_python_generated.models.tweet_card.Tweet_card(
                        legacy = twitter_openapi_python_generated.models.tweet_card_legacy.Tweet_card_legacy(
                            binding_values = [
                                twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner.Tweet_card_legacy_binding_values_inner(
                                    key = '', 
                                    value = twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner_value.Tweet_card_legacy_binding_values_inner_value(
                                        boolean_value = True, 
                                        scribe_key = '', 
                                        string_value = '', 
                                        type = '', ), )
                                ], 
                            name = '', 
                            url = '', ), 
                        rest_id = '', ), 
                    core = twitter_openapi_python_generated.models.user_result_core.UserResultCore(
                        user_results = twitter_openapi_python_generated.models.user_results.UserResults(
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
                                super_following = True, ), ), ), 
                    edit_control = twitter_openapi_python_generated.models.tweet_edit_control.Tweet_edit_control(
                        edit_tweet_ids = [
                            '4'
                            ], 
                        editable_until_msecs = '4', 
                        edits_remaining = '4', 
                        is_edit_eligible = True, ), 
                    edit_prespective = twitter_openapi_python_generated.models.tweet_edit_prespective.Tweet_edit_prespective(
                        favorited = True, 
                        retweeted = True, ), 
                    is_translatable = True, 
                    legacy = twitter_openapi_python_generated.models.tweet_legacy.TweetLegacy(
                        bookmark_count = 56, 
                        bookmarked = True, 
                        conversation_id_str = '4', 
                        created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                        display_text_range = [
                            56
                            ], 
                        entities = twitter_openapi_python_generated.models.entities.Entities(
                            hashtags = [
                                twitter_openapi_python_generated.models.hashtag.Hashtag()
                                ], 
                            media = [
                                twitter_openapi_python_generated.models.media.Media(
                                    display_url = '', 
                                    expanded_url = '', 
                                    ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.ext_media_availability(), 
                                    id_str = '4', 
                                    indices = [
                                        56
                                        ], 
                                    media_key = '4_072888001528021798096225500850762068629', 
                                    media_url_https = '', 
                                    original_info = twitter_openapi_python_generated.models.media_original_info.Media_original_info(
                                        focus_rects = [
                                            None
                                            ], 
                                        height = 56, 
                                        width = 56, ), 
                                    sizes = twitter_openapi_python_generated.models.sizes.sizes(), 
                                    type = '', 
                                    url = '', )
                                ], 
                            symbols = [
                                twitter_openapi_python_generated.models.symbol.Symbol()
                                ], 
                            urls = [
                                twitter_openapi_python_generated.models.url.Url(
                                    display_url = '', 
                                    expanded_url = '', 
                                    indices = [
                                        56
                                        ], 
                                    url = '', )
                                ], 
                            user_mentions = [
                                twitter_openapi_python_generated.models.user_mention.UserMention()
                                ], ), 
                        extended_entities = twitter_openapi_python_generated.models.extended_entities.ExtendedEntities(
                            media = [
                                twitter_openapi_python_generated.models.media.Media(
                                    display_url = '', 
                                    expanded_url = '', 
                                    ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.ext_media_availability(), 
                                    id_str = '4', 
                                    indices = , 
                                    media_key = '4_072888001528021798096225500850762068629', 
                                    media_url_https = '', 
                                    original_info = twitter_openapi_python_generated.models.media_original_info.Media_original_info(
                                        height = 56, 
                                        width = 56, ), 
                                    sizes = twitter_openapi_python_generated.models.sizes.sizes(), 
                                    type = '', 
                                    url = '', )
                                ], ), 
                        favorite_count = 56, 
                        favorited = True, 
                        full_text = '', 
                        id_str = '4', 
                        is_quote_status = True, 
                        lang = '', 
                        possibly_sensitive = True, 
                        possibly_sensitive_editable = True, 
                        quote_count = 56, 
                        reply_count = 56, 
                        retweet_count = 56, 
                        retweeted = True, 
                        retweeted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(
                            result = null, ), 
                        self_thread = twitter_openapi_python_generated.models.tweet_legacy_self_thread.TweetLegacy_self_thread(
                            id_str = '4', ), 
                        user_id_str = '4', ), 
                    quoted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(
                        result = null, ), 
                    rest_id = '4', 
                    unmention_data = twitter_openapi_python_generated.models.unmention_data.unmention_data(), 
                    views = twitter_openapi_python_generated.models.tweet_views.Tweet_views(
                        count = '4', 
                        state = '', ), )
            )
        else :
            return CreateTweet(
                result = twitter_openapi_python_generated.models.tweet.Tweet(
                    __typename = 'TimelineTweet', 
                    card = twitter_openapi_python_generated.models.tweet_card.Tweet_card(
                        legacy = twitter_openapi_python_generated.models.tweet_card_legacy.Tweet_card_legacy(
                            binding_values = [
                                twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner.Tweet_card_legacy_binding_values_inner(
                                    key = '', 
                                    value = twitter_openapi_python_generated.models.tweet_card_legacy_binding_values_inner_value.Tweet_card_legacy_binding_values_inner_value(
                                        boolean_value = True, 
                                        scribe_key = '', 
                                        string_value = '', 
                                        type = '', ), )
                                ], 
                            name = '', 
                            url = '', ), 
                        rest_id = '', ), 
                    core = twitter_openapi_python_generated.models.user_result_core.UserResultCore(
                        user_results = twitter_openapi_python_generated.models.user_results.UserResults(
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
                                super_following = True, ), ), ), 
                    edit_control = twitter_openapi_python_generated.models.tweet_edit_control.Tweet_edit_control(
                        edit_tweet_ids = [
                            '4'
                            ], 
                        editable_until_msecs = '4', 
                        edits_remaining = '4', 
                        is_edit_eligible = True, ), 
                    edit_prespective = twitter_openapi_python_generated.models.tweet_edit_prespective.Tweet_edit_prespective(
                        favorited = True, 
                        retweeted = True, ), 
                    is_translatable = True, 
                    legacy = twitter_openapi_python_generated.models.tweet_legacy.TweetLegacy(
                        bookmark_count = 56, 
                        bookmarked = True, 
                        conversation_id_str = '4', 
                        created_at = 'Sat Dec 31 23:59:59 +0000 2023', 
                        display_text_range = [
                            56
                            ], 
                        entities = twitter_openapi_python_generated.models.entities.Entities(
                            hashtags = [
                                twitter_openapi_python_generated.models.hashtag.Hashtag()
                                ], 
                            media = [
                                twitter_openapi_python_generated.models.media.Media(
                                    display_url = '', 
                                    expanded_url = '', 
                                    ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.ext_media_availability(), 
                                    id_str = '4', 
                                    indices = [
                                        56
                                        ], 
                                    media_key = '4_072888001528021798096225500850762068629', 
                                    media_url_https = '', 
                                    original_info = twitter_openapi_python_generated.models.media_original_info.Media_original_info(
                                        focus_rects = [
                                            None
                                            ], 
                                        height = 56, 
                                        width = 56, ), 
                                    sizes = twitter_openapi_python_generated.models.sizes.sizes(), 
                                    type = '', 
                                    url = '', )
                                ], 
                            symbols = [
                                twitter_openapi_python_generated.models.symbol.Symbol()
                                ], 
                            urls = [
                                twitter_openapi_python_generated.models.url.Url(
                                    display_url = '', 
                                    expanded_url = '', 
                                    indices = [
                                        56
                                        ], 
                                    url = '', )
                                ], 
                            user_mentions = [
                                twitter_openapi_python_generated.models.user_mention.UserMention()
                                ], ), 
                        extended_entities = twitter_openapi_python_generated.models.extended_entities.ExtendedEntities(
                            media = [
                                twitter_openapi_python_generated.models.media.Media(
                                    display_url = '', 
                                    expanded_url = '', 
                                    ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.ext_media_availability(), 
                                    id_str = '4', 
                                    indices = , 
                                    media_key = '4_072888001528021798096225500850762068629', 
                                    media_url_https = '', 
                                    original_info = twitter_openapi_python_generated.models.media_original_info.Media_original_info(
                                        height = 56, 
                                        width = 56, ), 
                                    sizes = twitter_openapi_python_generated.models.sizes.sizes(), 
                                    type = '', 
                                    url = '', )
                                ], ), 
                        favorite_count = 56, 
                        favorited = True, 
                        full_text = '', 
                        id_str = '4', 
                        is_quote_status = True, 
                        lang = '', 
                        possibly_sensitive = True, 
                        possibly_sensitive_editable = True, 
                        quote_count = 56, 
                        reply_count = 56, 
                        retweet_count = 56, 
                        retweeted = True, 
                        retweeted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(
                            result = null, ), 
                        self_thread = twitter_openapi_python_generated.models.tweet_legacy_self_thread.TweetLegacy_self_thread(
                            id_str = '4', ), 
                        user_id_str = '4', ), 
                    quoted_status_result = twitter_openapi_python_generated.models.item_result.ItemResult(
                        result = null, ), 
                    rest_id = '4', 
                    unmention_data = twitter_openapi_python_generated.models.unmention_data.unmention_data(), 
                    views = twitter_openapi_python_generated.models.tweet_views.Tweet_views(
                        count = '4', 
                        state = '', ), ),
        )
        """

    def testCreateTweet(self):
        """Test CreateTweet"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
