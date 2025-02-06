import pytest
from eva_data_analysis import text_to_duration
from eva_data_analysis import calculate_crew_size

def test_text_to_duration_float():

    """
    Test that text_to_duration returns expected float value
    for durations with a non-zero minute component
    """

    assert abs(text_to_duration('10:20') - 10.3333333) < 1e-5

def test_text_to_duration_integer():

    """
    Test that text_to_duration returns expected integer value
    for durations with a zero minute component
    """

    assert text_to_duration('10:00') == 10

@pytest.mark.parametrize("input_text, expected_output", [
    ('valentina tereshkova;', 1),
    ('Judith Resnik; ellison Onizuka; Ronald McNair;', 3),
])
def test_calculate_crew_size(input_text, expected_output):
    """
    Test that calculate_crew_size returns the expected crew size
    """
    actual_result = calculate_crew_size(input_text)
    assert actual_result == expected_output
