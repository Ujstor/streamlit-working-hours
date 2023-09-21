import os
import pytest
import pandas as pd
from cleaning_scripts.data_cleaning1 import (
    read_input_data, rename_columns, filter_by_id, main,
    drop_unnecessary_columns, convert_drive_time_to_int,
    filter_invalid_rows, convert_date_to_datetime, 
    drop_low_drive_time_rows, calculate_total_time,
    save_cleaned_data,
)

# Define test data
@pytest.fixture
def test_data():
    data = {
        'id': [1, 2],
        'date': ['2023-09-21 08:00:00', '2023-09-21 09:00:00'],
        'drive_time_min': [120, 150],
        'pause_had_min': [10, 'Hinfahrt'],
        'pause_should_min': [8, 10],
    }
    return pd.DataFrame(data)

# Test the read_input_data function
def test_read_input_data(test_data):
    input_csv = './data/test_data.csv'
    test_data.to_csv(input_csv, index=False)
    df = read_input_data(input_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 5)

# Test the rename_columns function
def test_rename_columns(test_data):
    renamed_df = rename_columns(test_data.copy())
    assert list(renamed_df.columns) == ['id', 'date', 'drive_time_min', 'pause_had_min', 'pause_should_min']

# Test the filter_by_id function
def test_filter_by_id(test_data):
    filtered_df = filter_by_id(test_data.copy(), target_id=2)
    assert filtered_df.shape == (1, 5)

# Test the drop_unnecessary_columns function
def test_drop_unnecessary_columns(test_data):
    df = drop_unnecessary_columns(test_data.copy())
    assert 'Unnamed: 5' not in df.columns
    assert 'Unnamed: 6' not in df.columns

# Test the convert_drive_time_to_int function
def test_convert_drive_time_to_int(test_data):
    df = convert_drive_time_to_int(test_data.copy())
    assert df['drive_time_min'].dtype == int

# Test the filter_invalid_rows function
def test_filter_invalid_rows(test_data):
    df = filter_invalid_rows(test_data.copy())
    assert df.shape == (1, 5)

# Test the convert_date_to_datetime function
def test_convert_date_to_datetime(test_data):
    df = convert_date_to_datetime(test_data.copy())
    assert df['date'].dtype == 'datetime64[ns]'

# Test the drop_low_drive_time_rows function
def test_drop_low_drive_time_rows(test_data):
    df = drop_low_drive_time_rows(test_data.copy(), threshold=130)
    assert df.shape == (1, 5)

# Test the calculate_total_time function
def test_calculate_total_time(test_data):
    df = calculate_total_time(test_data.copy())
    assert 'total_time_hour' in df.columns

# Test the save_cleaned_data function
def test_save_cleaned_data(test_data):
    output_csv = './data/test_cleaned_data.csv'
    save_cleaned_data(test_data.copy(), output_csv)
    assert os.path.exists(output_csv)

# Test the main function (integration test)
def test_main_function(test_data):
    input_csv = './data/test_data.csv'
    output_csv = './data/test_cleaned_data.csv'
    test_data.to_csv(input_csv, index=False)
    main(input_csv, output_csv, target_id=2)

if __name__ == "__main__":
    pytest.main()

