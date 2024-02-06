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

from twitter_openapi_python_generated.models.birdwatch_entity_ref import BirdwatchEntityRef

class TestBirdwatchEntityRef(unittest.TestCase):
    """BirdwatchEntityRef unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BirdwatchEntityRef:
        """Test BirdwatchEntityRef
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BirdwatchEntityRef`
        """
        model = BirdwatchEntityRef()
        if include_optional:
            return BirdwatchEntityRef(
                type = 'TimelineUrl',
                url = '',
                url_type = 'ExternalUrl'
            )
        else:
            return BirdwatchEntityRef(
                type = 'TimelineUrl',
                url = '',
                url_type = 'ExternalUrl',
        )
        """

    def testBirdwatchEntityRef(self):
        """Test BirdwatchEntityRef"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()