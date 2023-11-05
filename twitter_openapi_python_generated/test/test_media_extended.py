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

import twitter_openapi_python_generated
from twitter_openapi_python_generated.models.media_extended import MediaExtended  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestMediaExtended(unittest.TestCase):
    """MediaExtended unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MediaExtended
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MediaExtended`
        """
        model = twitter_openapi_python_generated.models.media_extended.MediaExtended()  # noqa: E501
        if include_optional :
            return MediaExtended(
                additional_media_info = twitter_openapi_python_generated.models.additional_media_info.AdditionalMediaInfo(
                    monetizable = True, ), 
                display_url = '', 
                expanded_url = '', 
                ext_media_availability = twitter_openapi_python_generated.models.ext_media_availability.extMediaAvailability(
                    reason = '', 
                    status = 'Available', ), 
                features = twitter_openapi_python_generated.models.features.features(), 
                id_str = '4', 
                indices = [
                    56
                    ], 
                media_stats = twitter_openapi_python_generated.models.media_stats.mediaStats(
                    view_count = 56, ), 
                media_key = '', 
                media_url_https = '', 
                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                    focus_rects = [
                        twitter_openapi_python_generated.models.media_original_info_focus_rect.MediaOriginalInfoFocusRect(
                            h = 56, 
                            w = 56, 
                            x = 56, 
                            y = 56, )
                        ], 
                    height = 56, 
                    width = 56, ), 
                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                    large = twitter_openapi_python_generated.models.media_size.MediaSize(
                        h = 56, 
                        resize = 'crop', 
                        w = 56, ), 
                    medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                        h = 56, 
                        resize = 'crop', 
                        w = 56, ), 
                    small = , 
                    thumb = , ), 
                type = 'photo', 
                url = '', 
                video_info = twitter_openapi_python_generated.models.media_video_info.MediaVideoInfo(
                    aspect_ratio = [
                        56
                        ], 
                    duration_millis = 56, 
                    variants = [
                        twitter_openapi_python_generated.models.media_video_info_variant.MediaVideoInfoVariant(
                            bitrate = 56, 
                            content_type = '', 
                            url = '', )
                        ], )
            )
        else :
            return MediaExtended(
                display_url = '',
                expanded_url = '',
                id_str = '4',
                indices = [
                    56
                    ],
                media_key = '',
                media_url_https = '',
                original_info = twitter_openapi_python_generated.models.media_original_info.MediaOriginalInfo(
                    focus_rects = [
                        twitter_openapi_python_generated.models.media_original_info_focus_rect.MediaOriginalInfoFocusRect(
                            h = 56, 
                            w = 56, 
                            x = 56, 
                            y = 56, )
                        ], 
                    height = 56, 
                    width = 56, ),
                sizes = twitter_openapi_python_generated.models.media_sizes.MediaSizes(
                    large = twitter_openapi_python_generated.models.media_size.MediaSize(
                        h = 56, 
                        resize = 'crop', 
                        w = 56, ), 
                    medium = twitter_openapi_python_generated.models.media_size.MediaSize(
                        h = 56, 
                        resize = 'crop', 
                        w = 56, ), 
                    small = , 
                    thumb = , ),
                type = 'photo',
                url = '',
        )
        """

    def testMediaExtended(self):
        """Test MediaExtended"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
