import os
import pandas as pd


def read_input_data(input_csv):
    df = pd.read_csv(input_csv)
    return df

def rename_columns(df):
    df.rename(columns={'Unnamed: 0': 'id', 'Unnamed: 1': 'date', 'Unnamed: 2': 'drive_time_min',
                       'Unnamed: 3': 'pause_had_min', 'Unnamed: 4': 'pause_should_min'}, inplace=True)
    return df

def filter_by_id(df, target_id):
    return df[df['id'] == target_id]

def drop_unnecessary_columns(df):
    unnecessary_columns = [f'Unnamed: {i}' for i in range(5, 18)]
    existing_columns = [col for col in unnecessary_columns if col in df.columns]
    df = df.drop(columns=existing_columns, axis=1)
    return df

def convert_drive_time_to_int(df):
    df['drive_time_min'] = df['drive_time_min'].astype(int)
    return df

def filter_invalid_rows(df):
    return df[~((df['pause_had_min'] == 'Hinfahrt') | (df['drive_time_min'] > 1000))]

def fill_missing_values(df):
    return df.fillna(0)

def convert_columns_to_int(df):
    df['pause_should_min'] = df['pause_should_min'].astype(int)
    df['pause_had_min'] = df['pause_had_min'].astype(int)
    return df

def convert_date_to_datetime(df):
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S').dt.strftime('%Y-%m-%d')
    df['date'] = pd.to_datetime(df['date'])
    return df

def drop_low_drive_time_rows(df, threshold=180):
    return df[df['drive_time_min'] >= threshold]

def calculate_total_time(df):
    df['drive_time_min'] = df['drive_time_min'] - df['pause_should_min']
    df['total_time_hour'] = (df['drive_time_min'] / 60)
    return df

def sort_by_date(df):
    return df.sort_values('date')

def save_cleaned_data(df, output_csv):
    df.to_csv(output_csv, index=False)

def main(input_csv, output_csv, target_id):
    df = read_input_data(input_csv)
    df = rename_columns(df)
    df = filter_by_id(df, target_id)
    df = drop_unnecessary_columns(df)
    df = convert_drive_time_to_int(df)
    df = filter_invalid_rows(df)
    df = fill_missing_values(df)
    df = convert_columns_to_int(df)
    df = convert_date_to_datetime(df)
    df = drop_low_drive_time_rows(df)
    df = calculate_total_time(df)
    df = sort_by_date(df)
    save_cleaned_data(df, output_csv)

if __name__ == "__main__":
    input_csv = './data/combined_dataform1.csv'
    output_csv = './data/cleaned_data1.csv'
    target_id = 'Stipan Aleksandar'
    main(input_csv, output_csv, target_id)
