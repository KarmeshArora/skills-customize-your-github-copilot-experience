# 📘 Assignment: Testing with pytest

## 🎯 Objective

Learn how to write automated tests using pytest to verify that Python functions behave correctly, handle edge cases, and raise errors as expected.

## 📝 Tasks

### 🛠️ Write Your First Tests

#### Description
A `calculator.py` module with basic math functions is provided. Write a test file that verifies each function returns the correct result for normal inputs.

#### Requirements
Completed program should:

- Create a file named `test_calculator.py`
- Import the functions from `calculator.py`
- Write at least one test function for each of `add`, `subtract`, `multiply`, and `divide`
- Each test must use `assert` to check the return value
- All tests must pass when running `pytest`


### 🛠️ Test Edge Cases and Exceptions

#### Description
Extend your test file to cover edge cases and verify that functions raise errors when given invalid inputs.

#### Requirements
Completed program should:

- Add tests for edge cases such as adding negative numbers or multiplying by zero
- Use `pytest.raises` to verify that `divide` raises a `ValueError` when dividing by zero
- Include at least four additional test functions beyond Task 1


### 🛠️ Organize Tests with a Fixture

#### Description
Refactor your tests to use a `pytest` fixture that provides shared test data, reducing repeated setup code.

#### Requirements
Completed program should:

- Define a `@pytest.fixture` that returns a dictionary of sample numbers to use in tests
- Update at least two existing test functions to use the fixture as a parameter
- All previously passing tests must still pass after the refactor
