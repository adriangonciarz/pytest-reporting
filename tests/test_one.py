import requests

from tests.test_base import TestBase


class TestOne(TestBase):
    def test_a(self):
        response = requests.get(self.base_path + '/posts')
        # This assertion should pass
        self.assert_response_status_code(response, 200)

    def test_b(self):
        body = {
                   "userId": 1,
                   "title": "Post title",
                   "body": "Whatever text"
               }
        response = requests.post(self.base_path + '/posts', json=body)
        # OFC it will return 200 OK response
        self.assert_response_status_code(response, 202)
