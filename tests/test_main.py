# pylint: disable=redefined-outer-name
"Tests for the main.py"
from unittest.mock import patch
import pytest
from main import repl  # Ensure this import is correct based on your file structure

@pytest.fixture
def inputs_and_expected_outputs():
    """Fixture providing simulated REPL inputs and their expected outputs.

    Returns:
        list of tuples: Each tuple contains a user command and the expected result.
    """
    return [
        ("add 10 5", "The result of adding 10.0 and 5.0 is: 15.0"),           # Add two numbers
        ("sub 10 5", "The result of subtracting 5.0 from 10.0 is: 5.0"),     # Subtract two numbers
        ("mul 3 4", "The result of multiplying 3.0 and 4.0 is: 12.0"),       # Multiply two numbers
        ("div 10 2", "The result of dividing 10.0 by 2.0 is: 5.0"),          # Divide two numbers
        ("div 10 0", "Error: Division by zero!"),                             # Division by zero
    ]

def test_repl_integration(inputs_and_expected_outputs, capsys):
    """Test the REPL integration with various commands."""
    for user_input, expected_output in inputs_and_expected_outputs:
        with patch("builtins.input", side_effect=[user_input, "exit"]):
            repl()  # Call the REPL function

        # Capture the output printed by REPL
        captured = capsys.readouterr().out

        # Validate that the expected result is part of the printed output
        assert expected_output in captured

def test_repl_integration_with_sequence(capsys):
    """Test REPL with a sequence of commands."""
    commands = ["add 1 2", "sub 2 1", "mul 3 4", "div 10 2", "exit"]
    expected_outputs = [
        "The result of adding 1.0 and 2.0 is: 3.0",   # Result of adding
        "The result of subtracting 1.0 from 2.0 is: 1.0",   # Result of subtracting
        "The result of multiplying 3.0 and 4.0 is: 12.0",  # Result of multiplying
        "The result of dividing 10.0 by 2.0 is: 5.0",   # Result of dividing
        "Thank you for using the calculator! Goodbye!"
    ]

    with patch("builtins.input", side_effect=commands):
        repl()  # Call the REPL function

    # Capture the output printed by REPL
    captured = capsys.readouterr().out

    # Validate that all expected outputs are part of the printed output
    for expected_output in expected_outputs:
        assert expected_output in captured
