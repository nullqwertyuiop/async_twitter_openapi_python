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

from twitter_openapi_python_generated.models.birdwatch_pivot import BirdwatchPivot

class TestBirdwatchPivot(unittest.TestCase):
    """BirdwatchPivot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BirdwatchPivot:
        """Test BirdwatchPivot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BirdwatchPivot`
        """
        model = BirdwatchPivot()
        if include_optional:
            return BirdwatchPivot(
                destination_url = '',
                footer = twitter_openapi_python_generated.models.birdwatch_pivot_footer.BirdwatchPivotFooter(
                    entities = [
                        twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    text = '', ),
                icon_type = 'BirdwatchV1Icon',
                note = twitter_openapi_python_generated.models.birdwatch_pivot_note.BirdwatchPivotNote(
                    rest_id = '4', ),
                shorttitle = '',
                subtitle = twitter_openapi_python_generated.models.birdwatch_pivot_subtitle.BirdwatchPivotSubtitle(
                    entities = [
                        twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    text = '', ),
                title = '',
                visual_style = 'Default'
            )
        else:
            return BirdwatchPivot(
                destination_url = '',
                footer = twitter_openapi_python_generated.models.birdwatch_pivot_footer.BirdwatchPivotFooter(
                    entities = [
                        twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    text = '', ),
                icon_type = 'BirdwatchV1Icon',
                note = twitter_openapi_python_generated.models.birdwatch_pivot_note.BirdwatchPivotNote(
                    rest_id = '4', ),
                shorttitle = '',
                subtitle = twitter_openapi_python_generated.models.birdwatch_pivot_subtitle.BirdwatchPivotSubtitle(
                    entities = [
                        twitter_openapi_python_generated.models.birdwatch_entity.BirdwatchEntity(
                            from_index = 56, 
                            ref = twitter_openapi_python_generated.models.birdwatch_entity_ref.BirdwatchEntityRef(
                                type = 'TimelineUrl', 
                                url = '', 
                                url_type = 'ExternalUrl', ), 
                            to_index = 56, )
                        ], 
                    text = '', ),
                title = '',
        )
        """

    def testBirdwatchPivot(self):
        """Test BirdwatchPivot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()