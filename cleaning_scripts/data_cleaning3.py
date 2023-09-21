import os
import pandas as pd

def read_input_data(input_csv):
    df = pd.read_csv(input_csv)
    return df

def rename_columns(df, column_mapping):
    df.rename(columns=column_mapping, inplace=True)
    return df

def filter_by_id(df, target_id):
    return df[df['id'] == target_id]

def convert_drive_time_to_int(df):
    df['drive_time_min'] = df['drive_time_min'].astype(int)
    return df

def filter_rows_by_drive_time(df, threshold):
    return df[df['drive_time_min'] <= threshold]

def fill_missing_values(df, column_to_fill, fill_with_column):
    df[column_to_fill] = df[fill_with_column]
    return df

def convert_date_to_datetime(df, date_column, date_format):
    df[date_column] = pd.to_datetime(df[date_column], format=date_format).dt.strftime('%Y-%m-%d')
    df[date_column] = pd.to_datetime(df[date_column])
    return df

def drop_low_drive_time_rows(df, threshold):
    return df[df['drive_time_min'] >= threshold]

def update_id_column(df, new_id):
    df['id'] = new_id
    return df

def calculate_total_time(df):
    df['total_time_hour'] = df['drive_time_min'] / 60
    return df

def save_cleaned_data(df, output_csv):
    df.to_csv(output_csv, index=False)

def drop_unnecessary_columns(df):
    unnecessary_columns = [f'Unnamed: {i}' for i in range(5, 18)]
    existing_columns = [col for col in unnecessary_columns if col in df.columns]
    df = df.drop(columns=existing_columns, axis=1)
    return df

def main(input_csv, output_csv, target_id):
    df = read_input_data(input_csv)
    column_mapping = {'Unnamed: 0': 'id', 'Unnamed: 1': 'date', 'Unnamed: 2': 'drive_time_min', 'Unnamed: 4': 'pause_had_min'}
    date_format = '%Y-%m-%d %H:%M:%S'
    threshold = 1000

    df = rename_columns(df, column_mapping)
    df = filter_by_id(df, target_id)
    df = drop_unnecessary_columns(df)
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


