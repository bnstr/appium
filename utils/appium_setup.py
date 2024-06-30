import json
import os
from appium import webdriver

def get_desired_capabilities():
    config_path = os.path.join(os.path.dirname(__file__), '../resources/config.json')
    with open(config_path) as config_file:
        return json.load(config_file)

def setup_appium():
    desired_caps = get_desired_capabilities()
    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
