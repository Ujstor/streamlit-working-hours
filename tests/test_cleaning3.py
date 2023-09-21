import os
import pandas as pd
import pytest
from cleaning_scripts.data_cleaning3 import (
    read_input_data, rename_columns, filter_by_id,
    convert_drive_time_to_int, fill_missing_values,
    convert_date_to_datetime, drop_low_drive_time_rows, update_id_column,
    calculate_total_time, save_cleaned_data, main
)

# Define test data
@pytest.fixture
def test_data():
    data = {
        'id': [1, 2, 3],
        'date': ['2023-09-21 08:00:00', '2023-09-21 09:00:00', '2023-09-21 10:00:00'],
        'drive_time_min': [120, 1050, 900],
        'pause_had_min': [10, 8, 15],
    }
    return pd.DataFrame(data)

# Test the read_input_data function
def test_read_input_data(test_data):
    input_csv = './data/test_data3.csv'
    test_data.to_csv(input_csv, index=False)
    df = read_input_data(input_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (3, 4)

# Test the rename_columns function
def test_rename_columns(test_data):
    column_mapping = {'id': 'new_id', 'date': 'new_date', 'drive_time_min': 'new_drive_time_min', 'pause_had_min': 'new_pause_had_min'}
    renamed_df = rename_columns(test_data.copy(), column_mapping)
    assert list(renamed_df.columns) == list(column_mapping.values())

# Test the filter_by_id function
def test_filter_by_id(test_data):
    filtered_df = filter_by_id(test_data.copy(), target_id=2)
    assert filtered_df.shape == (1, 4)

# Test the convert_drive_time_to_int function
def test_convert_drive_time_to_int(test_data):
    df = convert_drive_time_to_int(test_data.copy())
    assert df['drive_time_min'].dtype == int

# Test the fill_missing_values function
def test_fill_missing_values(test_data):
    df = fill_missing_values(test_data.copy(), 'drive_time_min', 'pause_had_min')
    assert df['drive_time_min'].equals(test_data['pause_had_min'])

# Test the convert_date_to_datetime function
def test_convert_date_to_datetime(test_data):
    date_format = '%Y-%m-%d %H:%M:%S'
    df = convert_date_to_datetime(test_data.copy(), 'date', date_format)
    assert df['date'].dtype == 'datetime64[ns]'

# Test the drop_low_drive_time_rows function
def test_drop_low_drive_time_rows(test_data):
    threshold = 180
    df = drop_low_drive_time_rows(test_data.copy(), threshold)
    assert df.shape == (2, 4)

# Test the update_id_column function
def test_update_id_column(test_data):
    new_id = 'Ivan Horvat'
    df = update_id_column(test_data.copy(), new_id)
    assert df['id'].unique() == [new_id]

# Test the calculate_total_time function
def test_calculate_total_time(test_data):
    df = calculate_total_time(test_data.copy())
    assert 'total_time_hour' in df.columns

# Test the save_cleaned_data function
def test_save_cleaned_data(test_data):
    output_csv = './data/test_cleaned_data3.csv'
    save_cleaned_data(test_data.copy(), output_csv)
    assert os.path.exists(output_csv)

# Test the main function
def test_main_function(test_data):
    input_csv = './data/test_data3.csv'
    output_csv = './data/test_cleaned_data3.csv'
    test_data.to_csv(input_csv, index=False)
    
    # Call the main function
    main(input_csv, output_csv, target_id=2)
    
    # Read the output CSV and check its content and structure
    df = pd.read_csv(output_csv)
    assert isinstance(df, pd.DataFrame)
    assert 'id' in df.columns
    assert 'date' in df.columns
    assert 'drive_time_min' in df.columns
    assert 'pause_had_min' in df.columns
    assert 'pause_should_min' in df.columns
    assert 'total_time_hour' in df.columns

    # Clean up temporary files
    if os.path.exists(input_csv):
        os.remove(input_csv)
    if os.path.exists(output_csv):
        os.remove(output_csv)



if __name__ == "__main__":
    pytest.main()
