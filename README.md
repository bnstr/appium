# Appium Framework

This is a sample project for an Appium automation framework using Python for an iOS app.

## Structure
````
├── tests/
│   // test cases grouped based on their functionality / feature being tested
│   ├── login/
│   │   ├── test_login.py
│   │   ├── test_login_invalid.py
│   ├── signup/
│   │   ├── test_signup.py
│   │   ├── test_signup_invalid.py
│   ├── todo/
│   │   ├── test_create_todo.py
│   │   ├── test_delete_todo.py
│   │   ├── test_edit_todo.py
│   └── common/
│       ├── test_common_functions.py
├── page_objects/
│   // classes that represent web pages or components, encapsulating the page's elements and interactions
│   ├── login_page.py
│   ├── signup_page.py
│   ├── todo_page.py
│   └── common_elements.py
├── utils/
│   // utility scripts for setup and configuration
│   ├── appium_setup.py
├── resources/
│   // configuration files and test data
│   ├── config.json
├── reports/
│   // store the output of test execution
│   ├── test_report.html
````


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/<user>/appium.git
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Start the Appium server:
    ```sh
    appium
    ```

## Running Tests

1. Run tests using `unittest`:
    ```sh
    python -m unittest discover -s tests
    ```

2. Run tests using `pytest`:
    ```sh
    pytest --html=reports/test_report.html
    ```
