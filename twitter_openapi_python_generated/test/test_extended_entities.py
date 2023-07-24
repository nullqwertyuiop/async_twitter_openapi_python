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
from twitter_openapi_python_generated.models.extended_entities import ExtendedEntities  # noqa: E501
from twitter_openapi_python_generated.rest import ApiException

class TestExtendedEntities(unittest.TestCase):
    """ExtendedEntities unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExtendedEntities
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendedEntities`
        """
        model = twitter_openapi_python_generated.models.extended_entities.ExtendedEntities()  # noqa: E501
        if include_optional :
            return ExtendedEntities(
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
                    ]
            )
        else :
            return ExtendedEntities(
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
        )
        """

    def testExtendedEntities(self):
        """Test ExtendedEntities"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
