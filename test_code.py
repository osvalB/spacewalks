from eva_data_analysis import text_to_duration

def test_text_to_duration_integer():
    input_value = '10:00'
    test_results = text_to_duration(input_value) == 10
    print(f'text_to_duration({input_value}) == 10? {test_results}')

test_text_to_duration_integer()