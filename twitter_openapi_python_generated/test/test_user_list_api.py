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

from twitter_openapi_python_generated.api.user_list_api import UserListApi


class TestUserListApi(unittest.TestCase):
    """UserListApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserListApi()

    def tearDown(self) -> None:
        pass

    def test_get_favoriters(self) -> None:
        """Test case for get_favoriters

        """
        pass

    def test_get_followers(self) -> None:
        """Test case for get_followers

        """
        pass

    def test_get_followers_you_know(self) -> None:
        """Test case for get_followers_you_know

        """
        pass

    def test_get_following(self) -> None:
        """Test case for get_following

        """
        pass

    def test_get_retweeters(self) -> None:
        """Test case for get_retweeters

        """
        pass


if __name__ == '__main__':
    unittest.main()
