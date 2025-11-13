# here to store hooks and Setup/Teardown
import yaml
import os
import subprocess

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

def after_all(context):
    print("\n=== Test execution is completed, Allure report is generating... ===")
    allure_cmd = ["allure","generate","allure-results","-o", "allure-report","--clean"]

    try:
        result = subprocess.run(
            allure_cmd,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            env = os.environ
        )
        print("Allure Report is generated：allure-report")
        subprocess.run(allure_cmd, env=os.environ, check=False)
        open_cmd = ["allure", "open", "allure-report"]
        subprocess.run(open_cmd, env=os.environ, check=False)
        print("Allure Report is opened!")

    except subprocess.CalledProcessError as e:
        print(f"Allure Report is generated failed")
        print(f"Error：{e.stderr}")
    except FileNotFoundError as e:
        print(f"Error：{e}")