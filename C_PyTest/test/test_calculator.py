import sys
import os
from calculator import Calculator

# Añade el directorio padre a sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_add():
    a = 1
    b = 2
    expected = 3
    calculator = Calculator()
    result = calculator.add(a, b)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_subtract():
    a = 5
    b = 3
    expected = 2
    calculator = Calculator()
    result = calculator.subtract(a, b)
    assert result == expected, f"Expected {expected}, but got {result}"

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("All tests passed!")
