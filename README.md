# API Test Automation with Python and pytest

This project demonstrates a simple example of API testing using Python's `requests` library and the `pytest` framework. It includes methods for sending GET and POST requests to an API, along with test cases to validate the responses.

Code is here API Python+JavaScript.zip -> Api test Python -> python_api_tests.py

## Prerequisites

Make sure you have the following tools installed:

- Python 3.x
- `requests` library
- `pytest` library

## Install Required Packages

You can install the required libraries using pip:

```bash
pip install requests pytest
```

## Run tests

```bash
pytest python_api_tests.py
```

# Api test with Postman

Open API Python+JavaScript -> Postman -> API test task.postman_collection.json

* In Postman click on the "Import" button
* Put API test task.postman_collection.json
* Run tests

# UI test with JavaScript + Cypress

Code Code is here is here API API Python+JavaScript.zip -> JS_cypress_UI -> e2e -> tests.js

## Prerequisites

- **Node.js**: Ensure you have Node.js installed on your machine. You can download it from [here](https://nodejs.org/).
- **npm or yarn**: You'll need npm (comes with Node.js) or yarn to install Cypress.

## Install Cypress

To get started, you need to install Cypress as a development dependency in your project.

1. Open your terminal and navigate to your project directory.
2. Run the following command to install Cypress:

```bash
npm install cypress --save-dev
```

## Steps to Execute Cypress

### 1. Open Cypress Test Runner

Cypress provides an interactive Test Runner for running tests visually.

Run the following command in your terminal:

```bash
npx cypress open
```

This will launch the Cypress Test Runner interface. From there, you can click on the test file you want to run.

# How to Execute Selenium Tests with Python

Selenium is a popular tool for automating web browsers. This guide explains how to execute Selenium tests using Python.

Code is here  API Python+JavaScript.zip -> Python_selenium_ui -> selenium_ui_test

## Prerequisites

1. **Python Installed**:
   - [Download Python](https://www.python.org/downloads/) if not already installed.
   - Ensure `pip` (Python package manager) is available.

2. **Install Selenium**:
   Run the following command to install Selenium:
   ```bash
   pip install selenium
   ```

3. **Execute test file (selenium_ui_test.py)**