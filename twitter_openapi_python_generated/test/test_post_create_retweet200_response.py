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

from twitter_openapi_python_generated.models.post_create_retweet200_response import PostCreateRetweet200Response

class TestPostCreateRetweet200Response(unittest.TestCase):
    """PostCreateRetweet200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCreateRetweet200Response:
        """Test PostCreateRetweet200Response
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCreateRetweet200Response`
        """
        model = PostCreateRetweet200Response()
        if include_optional:
            return PostCreateRetweet200Response(
                data = twitter_openapi_python_generated.models.errors_data.ErrorsData(
                    user = 'dummy', ),
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ]
            )
        else:
            return PostCreateRetweet200Response(
                data = twitter_openapi_python_generated.models.errors_data.ErrorsData(
                    user = 'dummy', ),
                errors = [
                    twitter_openapi_python_generated.models.error.Error(
                        code = 56, 
                        extensions = twitter_openapi_python_generated.models.error_extensions.ErrorExtensions(
                            code = 56, 
                            kind = '', 
                            name = '', 
                            retry_after = 56, 
                            source = '', 
                            tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                                trace_id = 'bf325375e030fccb', ), ), 
                        kind = '', 
                        locations = [
                            twitter_openapi_python_generated.models.location.Location(
                                column = 56, 
                                line = 56, )
                            ], 
                        message = '', 
                        name = '', 
                        path = [
                            ''
                            ], 
                        retry_after = 56, 
                        source = '', 
                        tracing = twitter_openapi_python_generated.models.tracing.Tracing(
                            trace_id = 'bf325375e030fccb', ), )
                    ],
        )
        """

    def testPostCreateRetweet200Response(self):
        """Test PostCreateRetweet200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
