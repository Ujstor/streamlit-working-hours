import pandas as pd
import pytest
import os
from cleaning_scripts.data_cleaning2 import (
    read_input_data, filter_by_id, drop_invalid_rows,
    rename_columns, convert_date_to_datetime,
    main,save_cleaned_data
)

# Sample test data
@pytest.fixture
def sample_dataframe():
    data = {
        'Personal': ['Stipan Aleksandar', 'John Doe', 'Stipan Aleksandar'],
        'Tag': ['2023-09-20', 'Beginn Arbeit', '2023-09-21'],
        'T.Summe': [300, 200, 400],
        'T.Pause': [30, 20, 40],
        'gesetzl. Pause': [20, 10, 30],
        'T.Summe (-Pause)': [300, 200, 400],
        'Verdienst': [200, 150, 250],  
        'Soll': [100, 50, 150], 
        '+- Diff.': [100, 100, 100],  
    }
    return pd.DataFrame(data)

# Test read_input_data function
def test_read_input_data(sample_dataframe):
    input_csv = 'dummy_input.csv'
    sample_dataframe.to_csv(input_csv, index=False)
    df = read_input_data(input_csv)
    assert isinstance(df, pd.DataFrame)
    assert df.shape == sample_dataframe.shape
    # Add more specific assertions if needed

# Test filter_by_id function
def test_filter_by_id(sample_dataframe):
    target_id = 'Stipan Aleksandar'
    filtered_df = filter_by_id(sample_dataframe, target_id)
    assert isinstance(filtered_df, pd.DataFrame)
    assert 'Stipan Aleksandar' in filtered_df['Personal'].values
    assert 'John Doe' not in filtered_df['Personal'].values

# Test drop_invalid_rows function
def test_drop_invalid_rows(sample_dataframe):
    cleaned_df = drop_invalid_rows(sample_dataframe)
    assert isinstance(cleaned_df, pd.DataFrame)
    assert 'Beginn Arbeit' not in cleaned_df['Tag'].values
    assert 'Beginn Pause' not in cleaned_df['Tag'].values

# Test rename_columns function
def test_rename_columns(sample_dataframe):
    renamed_df = rename_columns(sample_dataframe)
    assert isinstance(renamed_df, pd.DataFrame)
    assert 'id' in renamed_df.columns
    assert 'date' in renamed_df.columns
    assert 'drive_time_min' in renamed_df.columns
    assert 'pause_had_min' in renamed_df.columns
    assert 'pause_should_min' in renamed_df.columns

# Test convert_date_to_datetime function
def test_convert_date_to_datetime(sample_dataframe):
    date_format = '%Y-%m-%d'
    converted_df = convert_date_to_datetime(sample_dataframe, 'Tag', date_format)
    assert isinstance(converted_df, pd.DataFrame)
    assert converted_df['Tag'].dtype == 'datetime64[ns]'

# Test save_cleaned_data function
def test_save_cleaned_data(sample_dataframe):
    output_csv = './data/test_cleaned_data2.csv'
    save_cleaned_data(sample_dataframe, output_csv)
    assert os.path.exists(output_csv)
    os.remove(output_csv)

# Clean up temporary files if needed
def teardown_function(function):
    if function.__name__ == 'test_read_input_data':
        input_csv = 'dummy_input.csv'
        if os.path.exists(input_csv):
            os.remove(input_csv)
    if function.__name__ == 'test_save_cleaned_data':
        output_csv = 'dummy_output.csv'
        if os.path.exists(output_csv):
            os.remove(output_csv)


def test_main(sample_dataframe):
    input_csv = './data/test_data2.csv'
    output_csv = './data/test_cleaned_data.csv2'

    # Create a sample input CSV file
    sample_dataframe.to_csv(input_csv, index=False)

    # Check if the columns to drop are present in the sample_dataframe
    assert 'T.Summe (-Pause)' in sample_dataframe.columns
    assert 'Verdienst' in sample_dataframe.columns
    assert 'Soll' in sample_dataframe.columns
    assert '+- Diff.' in sample_dataframe.columns

    # Call the main function
    main(input_csv, output_csv, target_id = 'Stipan Aleksandar')

    # Check if the output CSV file exists
    assert os.path.exists(output_csv)

    # Read the output CSV and check its content and structure
    df = pd.read_csv(output_csv)
    assert isinstance(df, pd.DataFrame)
    assert 'id' in df.columns
    assert 'date' in df.columns
    assert 'drive_time_min' in df.columns
    assert 'pause_had_min' in df.columns
    assert 'pause_should_min' in df.columns
    assert 'total_time_hour' in df.columns
    assert df.shape == (2, 6)  # Assuming two rows are filtered after cleaning

    # Clean up temporary files
    if os.path.exists(input_csv):
        os.remove(input_csv)
    if os.path.exists(output_csv):
        os.remove(output_csv)

# Run tests
if __name__ == "__main__":
    pytest.main()

