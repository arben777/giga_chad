# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import playground_client
from playground_client.models.list_filesystem_dir_response import ListFilesystemDirResponse  # noqa: E501
from playground_client.rest import ApiException

class TestListFilesystemDirResponse(unittest.TestCase):
    """ListFilesystemDirResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListFilesystemDirResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListFilesystemDirResponse`
        """
        model = playground_client.models.list_filesystem_dir_response.ListFilesystemDirResponse()  # noqa: E501
        if include_optional :
            return ListFilesystemDirResponse(
                entries = [
                    playground_client.models.entry_info.EntryInfo(
                        is_dir = True, 
                        name = '', )
                    ]
            )
        else :
            return ListFilesystemDirResponse(
                entries = [
                    playground_client.models.entry_info.EntryInfo(
                        is_dir = True, 
                        name = '', )
                    ],
        )
        """

    def testListFilesystemDirResponse(self):
        """Test ListFilesystemDirResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
