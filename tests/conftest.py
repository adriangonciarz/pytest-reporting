import json

import pytest
import curlify

@pytest.fixture
def failure_report(request):
    yield
    if request.node.rep_call.failed:
        last_response = getattr(request.node.parent.obj, "last_response")
        _debug_print(last_response)


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    setattr(item, "rep_" + report.when, report)
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        last_response = getattr(item.parent.obj, "last_response")
        request_curl = _prepare_request_curl(last_response)
        extra.append(pytest_html.extras.html(_curl_to_html(request_curl)))
        extra.append(pytest_html.extras.json(_prepare_json_response(last_response), name='JSON Reponse'))
        report.extra = extra


def _prepare_request_curl(response):
    return curlify.to_curl(response.request)


def _prepare_json_response(response):
    return response.json()


def _curl_to_html(curl):
    css_definition = "background-color: #eee;" \
                     "border: 1px solid #999;" \
                     "display: block;" \
                     "padding: 20px;"
    return '<code style="{}">{}</code>'.format(css_definition, curl)


def _debug_print(response):
    print('Request cURL\n{}\n' \
           'Response JSON\n{}'.format(
        _prepare_request_curl(response), json.dumps(response.json(), indent=2)
    ))
