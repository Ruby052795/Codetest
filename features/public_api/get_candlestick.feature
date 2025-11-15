Feature: Candlestick Data Retrieval Automation

Background:
  Given I use the Candlestick Public API client
  When I send a GET request with provided parameters

  @public/get-candlestick @positive_case
  Scenario: P-1: Valid required and valid optional parameters with non-default value
    Then the HTTP response status code should be 200
    And every attributes include non-default value in the response should display correctly

  @public/get-candlestick @positive_case
  Scenario: P-2: Valid optional parameters with default value.
    Then the HTTP response status code should be 200
    And every attributes include default value in the response should display correctly

  @public/get-candlestick @negative_case
  Scenario: N-1: Invalid instrument name
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display

  @public/get-candlestick @negative_case
  Scenario: N-2: Invalid timeframe
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display

  @public/get-candlestick @negative_case
  Scenario: N-3: Invalid count value
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display

  @public/get-candlestick @negative_case
  Scenario: N-4: Invalid Timestamp Format - start_ts
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display

  @public/get-candlestick @negative_case
  Scenario: N-5: Invalid Timestamp Format - end_ts
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display

  @public/get-candlestick @negative_case
  Scenario: N-6: Missing Required Parameter
    Then the HTTP response status code should not be 200
    And the API result code should not be 0
    And the error message should display