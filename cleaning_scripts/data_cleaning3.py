import pandas as pd

def read_input_data(input_csv):
    # Read the input CSV file
    df = pd.read_csv(input_csv)
    return df

def rename_columns(df, column_mapping):
    # Rename columns based on the provided mapping
    df.rename(columns=column_mapping, inplace=True)
    return df

def filter_by_id(df, target_id):
    # Filter rows for a specific 'id'
    return df[df['id'] == target_id]

def drop_unnecessary_columns(df, columns_to_drop):
    # Drop unnecessary columns
    return df.drop(columns=columns_to_drop, axis=1)

def convert_drive_time_to_int(df):
    # Convert 'drive_time_min' column to integer
    df['drive_time_min'] = df['drive_time_min'].astype(int)
    return df

def filter_rows_by_drive_time(df, threshold):
    # Filter out rows with 'drive_time_min' greater than a threshold
    return df[df['drive_time_min'] <= threshold]

def fill_missing_values(df, column_to_fill, fill_with_column):
    # Fill missing values in a column with values from another column
    df[column_to_fill] = df[fill_with_column]
    return df

def convert_date_to_datetime(df, date_column, date_format):
    # Convert 'date' column to datetime format
    df[date_column] = pd.to_datetime(df[date_column], format=date_format).dt.strftime('%Y-%m-%d')
    df[date_column] = pd.to_datetime(df[date_column])
    return df

def drop_low_drive_time_rows(df, threshold):
    # Drop rows with 'drive_time_min' less than a threshold
    return df[df['drive_time_min'] >= threshold]

def update_id_column(df, new_id):
    # Update 'id' column to a new value
    df['id'] = new_id
    return df

def calculate_total_time(df):
    # Calculate 'total_time_hour' column
    df['total_time_hour'] = df['drive_time_min'] / 60
    return df

def save_cleaned_data(df, output_csv):
    # Save cleaned data to CSV file
    df.to_csv(output_csv, index=False)

def main(input_csv, output_csv, target_id):
    df = read_input_data(input_csv)
    column_mapping = {'Unnamed: 0': 'id', 'Unnamed: 1': 'date', 'Unnamed: 2': 'drive_time_min', 'Unnamed: 4': 'pause_had_min'}
    columns_to_drop = ['Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 3']
    date_format = '%Y-%m-%d %H:%M:%S'
    threshold = 1000

    df = rename_columns(df, column_mapping)
    df = filter_by_id(df, target_id)
    df = drop_unnecessary_columns(df, columns_to_drop)
    df = convert_drive_time_to_int(df)
    df = filter_rows_by_drive_time(df, threshold)
    df = fill_missing_values(df, 'pause_should_min', 'pause_had_min')
    df = convert_date_to_datetime(df, 'date', date_format)
    df = drop_low_drive_time_rows(df, 180)
    df = update_id_column(df, 'Stipan Aleksandar')
    df = calculate_total_time(df)
    save_cleaned_data(df, output_csv)

if __name__ == "__main__":
    input_csv = './data/combined_dataform3.csv'
    output_csv = './data/cleaned_data3.csv'
    target_id = 'Stipan Alexander'

    main(input_csv, output_csv, target_id)


