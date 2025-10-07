# Happy Numbers

A Python implementation to determine whether a number is a "happy number" or not.

## What is a Happy Number?

A happy number is defined by the following process:
1. Start with any positive integer
2. Replace the number by the sum of the squares of its digits
3. Repeat the process until:
   - The number equals 1 (where it will stay) → Happy Number
   - It enters an endless cycle that does not include 1 → Not a Happy Number

For example:
- 19 is happy because:
  - 1² + 9² = 82
  - 8² + 2² = 68
  - 6² + 8² = 100
  - 1² + 0² + 0² = 1

## Implementation

The project contains a single function `is_happy(n)` that determines if a given number is happy or not. The implementation uses a set to detect cycles and avoid infinite loops.

### Features

- Fast cycle detection using a set
- Type hints for better code clarity
- Comprehensive docstring with examples
- Built-in test cases

## Usage

```python
from run import is_happy

# Check if a number is happy
print(is_happy(19))  # True
print(is_happy(2))   # False
print(is_happy(44))  # True
```

### Running Tests

The script includes built-in test cases. To run them:

```bash
python run.py
```

If all tests pass, you'll see the message "All tests passed!"

## Test Cases

The implementation includes verification for several numbers:
- 44 (Happy)
- 2 (Not Happy)
- 86 (Happy)
- 139 (Happy)

## Mathematical Properties

Some interesting properties of happy numbers:
- All happy numbers eventually reach 1
- Numbers that are not happy enter a cycle
- The first few happy numbers are: 1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, ...

## Requirements

- Python 3.6+ (for type hints)
- No external dependencies required

## License

This is a simple educational implementation. Feel free to use and modify as needed.

## Contributing

If you'd like to contribute:
1. Add more test cases
2. Optimize the algorithm
3. Add features (e.g., finding all happy numbers up to n)
4. Improve documentation
