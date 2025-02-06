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

def test_calculate_crew_size():
    """
    Test that calculate_crew_size returns the expected crew size
    """
    actual_result = calculate_crew_size('sara doe; john connor;')
    expected_result = 2
    assert actual_result == expected_result
