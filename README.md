# Python Project Template
Welcome to this Python project template! This repository provides a basic structure for your Python projects, including pre-configured tools for code formatting, linting, and testing.


### Dependencies
Before running this project, make sure to install all required dependencies by running the following command in your terminal:
```sh
pip install -r requirements.txt
```

### Code Formatting
We use the black code formatter to ensure consistent code formatting across the entire project. To format your code, simply run the following command:
```sh
black .
```

### Pre-commit Hooks
We use pre-commit to run a set of checks on every commit to ensure that the codebase is always clean and consistent. To install the pre-commit hooks, run:
```sh
pre-commit install
```
The pre-commit hooks include the following checks:

* `black`: checks that your code is properly formatted

You can add other hooks such as:
* `flake8`: checks your code for PEP 8 compliance and other common issues
* `mypy`: checks your code for type annotations
* `pytest`: runs all unit tests

To run the pre-commit hooks manually on all files in the repository, run:
```sh
pre-commit run --all-files
```


