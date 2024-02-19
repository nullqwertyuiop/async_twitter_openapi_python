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

from twitter_openapi_python_generated.models.user_verification_info import UserVerificationInfo

class TestUserVerificationInfo(unittest.TestCase):
    """UserVerificationInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserVerificationInfo:
        """Test UserVerificationInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserVerificationInfo`
        """
        model = UserVerificationInfo()
        if include_optional:
            return UserVerificationInfo(
                is_identity_verified = True,
                reason = twitter_openapi_python_generated.models.user_verification_info_reason.UserVerificationInfoReason(
                    description = twitter_openapi_python_generated.models.user_verification_info_reason_description.UserVerificationInfoReasonDescription(
                        entities = [
                            twitter_openapi_python_generated.models.user_verification_info_reason_description_entities.UserVerificationInfoReasonDescriptionEntities(
                                from_index = 56, 
                                ref = twitter_openapi_python_generated.models.user_verification_info_reason_description_entities_ref.UserVerificationInfoReasonDescriptionEntitiesRef(
                                    url = '', 
                                    url_type = 'ExternalUrl', ), 
                                to_index = 56, )
                            ], 
                        text = '', ), 
                    override_verified_year = 56, 
                    verified_since_msec = '-80728', )
            )
        else:
            return UserVerificationInfo(
                is_identity_verified = True,
        )
        """

    def testUserVerificationInfo(self):
        """Test UserVerificationInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()