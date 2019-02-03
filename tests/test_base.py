import pytest


@pytest.mark.usefixtures('failure_report')
class TestBase:
    last_response = None
    base_path = 'https://jsonplaceholder.typicode.com'

    def assert_response_status_code(self, response, status_code):
        self.last_response = response
        assert response.status_code == status_code
