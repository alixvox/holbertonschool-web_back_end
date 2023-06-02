#!/usr/bin/env python3
"""
Module for testing the client module.
"""

import unittest
import fixtures
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Class for testing the class GithubOrgClient.
    """

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org_name, mock_get):
        """
        Test that GithubOrgClient.org returns the correct value.
        """

        test_client = GithubOrgClient(org_name)
        response = test_client.org

        mock_get.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}')
        self.assertEqual(response, {"payload": True})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url
        returns the correct value.
        """

        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload
        test_client = GithubOrgClient('google')

        self.assertEqual(test_client._public_repos_url, payload["repos_url"])

    @patch('client.get_json', return_value=[{"name": "repo1"},
                                            {"name": "repo2"}])
    def test_public_repos(self, mock_get):
        """
        Test that GithubOrgClient.public_repos
        returns the correct list of repos.
        """

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "\
                https://api.github.com/orgs/google/repos"
            test_client = GithubOrgClient('google')

            self.assertEqual(test_client.public_repos(), ["repo1", "repo2"])
            mock_get.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct value.
        """
        test_client = GithubOrgClient('google')

        self.assertEqual(test_client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": fixtures.org_with_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.repos,
     "apache2_repos": fixtures.repos_with_payload}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Class for integration testing the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up the class with mocked requests.get.
        """
        cls.get_patcher = patch('requests.get')
        cls.get_mock = cls.get_patcher.start()

        def side_effect(url):
            if url.endswith("/orgs/org"):
                return Mock(json=lambda: cls.org_payload)
            elif url.endswith("/orgs/org/repos"):
                return Mock(json=lambda: cls.repos_payload)
            else:
                return Mock(json=lambda: [])

        cls.get_mock.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.
        """
        cls.get_patcher.stop()
