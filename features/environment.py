# here to store hooks and Setup/Teardown
import yaml
import os

def before_scenario(context, scenario):

    scenario_name = scenario.name

    data_key = None
    if 'P-1' in scenario_name:
        data_key = 'P-1'
    elif 'P-2' in scenario_name:
        data_key = 'P-2'
    elif 'N-1' in scenario_name:
        data_key = 'N-1'
    elif 'N-2' in scenario_name:
        data_key = 'N-2'
    elif 'N-3' in scenario_name:
        data_key = 'N-3'
    elif 'N-4' in scenario_name:
        data_key = 'N-4'
    elif 'N-5' in scenario_name:
        data_key = 'N-5'
    elif 'N-6' in scenario_name:
        data_key = 'N-6'

    data_path = os.path.join(os.path.dirname(__file__), 'test_data', 'get_candlestick_data.yaml')

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            test_data = yaml.safe_load(f)
            context.candlestick_data = test_data.get(data_key, {})
            print("Loaded candlestick test data successfully.")
    except FileNotFoundError:
        print(f"ERROR: Data file not found at {data_path}")
        context.candlestick_data = {}