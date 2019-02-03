import requests

from tests.test_base import TestBase


class TestTwo(TestBase):
    def test_two_a(self):
        response = requests.get(self.base_path + '/nonexisting-resource')
        # There is no such resource so it will fail
        self.assert_response_status_code(response, 200)

