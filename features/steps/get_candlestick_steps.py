from behave import given, when, then
from behave.formatter import null

from src.api_client.public_api_client import PublicApiClient


@given('I use the Candlestick Public API client')
def step_impl(context):
    context.client = PublicApiClient()
    context.request_params = {}


@when('I send a GET request with provided parameters')
def step_impl(context):
    context.request_params['instrument_name'] = context.candlestick_data.get('instrument_name')
    context.request_params['timeframe'] = context.candlestick_data.get('timeframe')
    context.request_params['count'] = context.candlestick_data.get('count')
    context.request_params['start_ts'] = context.candlestick_data.get('start_ts')
    context.request_params['end_ts'] = context.candlestick_data.get('end_ts')
    print(f"Parameters: {context.request_params}")

    context.response = context.client.get_candlestick(context.request_params)
    context.response_data = context.response.json()


@then('the HTTP response status code should be 200')
def step_impl(context):
    assert context.response.status_code == 200, f"Status Code: {context.response.status_code}"

@then('every attributes include non-default value in the response should display correctly')
def step_impl(context):
    assert context.response_data.get('method', {}) == "public/get-candlestick", \
        f"method: {context.response_data.get('method', {})} is not correct."
    assert context.response_data.get('code', {}) == 0, \
        f"code: {context.response_data.get('code', {})} is not correct"
    assert context.response_data.get('result', {}).get('instrument_name', []) == context.request_params['instrument_name'], \
        f"instrument_name: {context.response_data.get('result', {}).get('instrument_name', [])} is not as expected."
    assert context.response_data.get('result', {}).get('interval', []) == context.request_params['timeframe'], \
        f"interval: {context.response_data.get('result', {}).get('interval', [])} is not as expected."

    data_list = context.response_data.get('result', {}).get('data', [])
    candlestick = data_list[0]

    required_fields = ['t', 'o', 'h', 'l', 'c', 'v']
    for field in required_fields:
        assert field in candlestick, f"Candlestick data misses required field '{field}'."

@then('every attributes include default value in the response should display correctly')
def step_impl(context):
    assert context.response_data.get('method', {}) == "public/get-candlestick", \
        f"method: {context.response_data.get('method', {})} is not correct."
    assert context.response_data.get('code', {}) == 0, \
        f"code: {context.response_data.get('code', {})} is not correct"
    assert context.response_data.get('result', {}).get('instrument_name', []) == context.request_params['instrument_name'], \
        f"instrument_name: {context.response_data.get('result', {}).get('instrument_name', [])} is not as expected."
    assert context.response_data.get('result', {}).get('interval', []) == '1m', \
        f"interval: {context.response_data.get('result', {}).get('interval', [])} is not as expected."

    data_list = context.response_data.get('result', {}).get('data', [])
    candlestick = data_list[0]

    required_fields = ['t', 'o', 'h', 'l', 'c', 'v']
    for field in required_fields:
        assert field in candlestick, f"Candlestick data misses required field '{field}'."

@then('the HTTP response status code should not be 200')
def step_impl(context):
    assert context.response.status_code != 200, f"Status Code: {context.response.status_code} is not expected"

@then('the API result code should not be 0')
def step_impl(context):
    assert context.response_data.get('code', {}) != 0, \
        f"code: {context.response_data.get('code', {})} is not expected"

@then('the error message should display')
def step_impl(context):
    assert context.response_data.get('message', {}) is not null, \
        f"message: {context.response_data.get('message', {})}"
