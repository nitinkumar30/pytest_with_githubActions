# 🧪 Selenium Test Automation with Pytest 🚀

<!-- [![Project Status](https://github.com/nitinkumar30/pytest_with_githubActions/actions/workflows/test01.yml/badge.svg)](https://github.com/nitinkumar30/pytest_with_githubActions/actions/workflows/test01.yml) -->

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nitinkumar30/pytest_with_githubActions/.github%2Fworkflows%2Ftest01.yml?branch=master&style=for-the-badge)


## Introduction ✨

This project provides a robust and efficient solution for web application testing using Selenium and Pytest. It's designed to help you write clean, maintainable, and scalable automated tests. We leverage `webdriver-manager` for streamlined driver management, and Pytest fixtures for optimized test setup and teardown.  The project also includes a GitHub Actions workflow for continuous integration.

---
## 📂 Project Structure

Here's how the project is organized:

```
├── conftest.py # ⚙️ Pytest configuration and shared fixtures (e.g., setup).  
├── test_example.py # 🧪 Example test cases for web application testing.  
├── pytest.ini # 📝 Optional: Pytest configuration file.  
├── README.md # 📖 Project documentation (this file!).  
└── .github/workflows/test01.yml # 🤖 GitHub Actions workflow for CI.  
```

* **`conftest.py`**:
    * Contains Pytest fixtures, most importantly the `setup` fixture.
    * The `setup` fixture handles:
        * Browser initialization (e.g., Chrome, Firefox).
        * WebDriver management using `webdriver-manager`.
        * Browser teardown (closing the browser after tests).
    * Uses session-level scope for the `setup` fixture to efficiently manage browser instances across the entire test session.
* **`test_example.py`**:
    * Contains example test cases using Pytest.
    * Demonstrates how to use the `setup` fixture to interact with a web browser.
    * Includes test functions for verifying page titles, and can be expanded to test other web elements and interactions.
* **`pytest.ini`**:
    * Optional Pytest configuration file.
    * Useful for customizing Pytest behavior, such as:
        * Setting default command-line options.
        * Configuring test discovery.
        * Disabling output capture.**`.github/workflows/test01.yml`**:
    * GitHub Actions workflow file.
    * Defines a workflow named "test01" that is triggered manually.
    * The workflow sets up a Python environment, installs dependencies, and runs the Pytest test suite.
* **`README.md`**:
    * This file! 📖
    * Provides project documentation, usage instructions, and a description of the directory structure.

---
## 🚀 Getting Started

> NOTE:- Not using [webdriver-manager](https://pypi.org/project/webdriver-manager/) right now as their workflows are failing with webdriver since some months. Check [here](https://github.com/SergeyPirogov/webdriver_manager/actions/workflows/test.yml) for more info. 

> Project is on hold due to Ukraine war 

### Prerequisites

Before you begin, ensure you have the following installed:

* **Python:** 3.x is required.
* **Selenium:** The Selenium WebDriver library.
* **Pytest:** The Pytest testing framework.
* **WebDriver Manager:** For managing browser drivers.

Install the necessary packages using pip:

```bash
pip install selenium pytest webdriver-manager
```
---
🏃‍♀️ Running the Tests
Navigate to the project directory:
```commandline
cd your_project_directory
```

Run all tests:
To execute all tests in the project, simply use:  
```commandline
pytest
```

This command will discover and run all test functions in test_example.py (and any other files following Pytest's naming conventions), utilizing the setup fixture defined in conftest.py.  
See print statements (Disable output capturing):  
By default, Pytest captures standard output (stdout). To see print statements in your console, use the **-s** or **--capture=no flag**:

```commandline
pytest -s
```

or
```commandline
pytest --capture=no
```

Run a single test file: To run only the tests in a specific file:
```commandline
pytest test_example.py
```

Run a specific test function: To run a single test function:
```commandline
pytest test_example.py::TestExample::test_title
```
---
🤖 Continuous Integration with GitHub Actions
The project includes a GitHub Actions workflow _(.github/workflows/test01.yml)_ for _continuous integration (CI)_. This workflow automates the testing process whenever you make changes to your repository.  

Workflow Details
* Name: test01
* Trigger: The workflow is triggered manually using workflow_dispatch.
* Jobs: The workflow has a single job - test01:
* Runs on Ubuntu.  

Steps:
* Checks out the repository code using actions/checkout@v3.
* Sets up a Python 3.10 environment using actions/setup-python@v4.
* Installs project dependencies from requirements.txt using pip.
* Runs the Pytest test suite using pytest -rA. The -rA flag ensures that all test results are printed.

How to Use the Workflow
* Commit the workflow file: Ensure that the .github/workflows/test01.yml file is committed to your GitHub repository.
* Run the workflow:
* Go to your repository on GitHub.
* Click on the "Actions" tab.
* Find the "test01" workflow in the list on the left.
* Click the "Run workflow" button.
* GitHub Actions will then execute the workflow, running your Pytest tests in a virtual environment. The results of the test run will be displayed in the GitHub Actions console.

---
🎯 Key Concepts  

Pytest Fixtures:  
* We use Pytest fixtures to manage the setup and teardown of the Selenium WebDriver.
* The setup fixture ensures that a browser instance is initialized before the tests run and is closed after the tests finish.
* Fixtures promote code reusability and maintainability.
* Using scope="session" in the setup fixture optimizes browser usage, creating the browser instance only once per test session.

Selenium WebDriver:
* Selenium WebDriver is used to automate web browser interactions.
* It allows us to control the browser programmatically, simulating user actions like navigating to pages, clicking elements, and entering text.

WebDriver Manager:
* webdriver-manager simplifies the process of managing browser drivers (e.g., chromedriver, geckodriver).
* It automatically downloads the correct driver version for your browser, eliminating the need for manual driver installation and updates.

Test Assertions:
* Test functions include assertions (e.g., assert ...) to verify that the actual results match the expected outcomes.
* Assertions are crucial for determining whether a test has passed or failed.

Modular Design:
* The project is structured into separate files (conftest.py,

---

# Author

[Nitin Kumar](https://linkedin.com/in/nitin30kumar/)
