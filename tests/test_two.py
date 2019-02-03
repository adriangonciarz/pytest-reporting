import requests

from tests.test_base import TestBase


class TestTwo(TestBase):
    def test_two_a(self):
        response = requests.get(self.base_path + '/animals')
        self.assert_response_status_code(response, 202)

