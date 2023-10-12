import pandas as pd

def read_input_data(input_csv):
    df = pd.read_csv(input_csv)
    return df

def filter_by_id(df, target_id):
    return df[df['Personal'] == target_id]

def drop_invalid_rows(df):
    return df[~((df['Tag'] == 'Beginn Arbeit') | (df['Tag'] == 'Beginn Pause'))]

def rename_columns(df):
    df.rename(columns={'Personal': 'id', 'Tag': 'date', 'T.Summe': 'drive_time_min',
                       'T.Pause': 'pause_had_min', 'gesetzl. Pause': 'pause_should_min'}, inplace=True)
    return df

def drop_unnecessary_columns(df, columns_to_drop):
    return df.drop(columns=columns_to_drop, axis=1)

def convert_columns_to_int(df):
    df['drive_time_min'] = df['drive_time_min'].astype(int)
    df['pause_had_min'] = df['pause_had_min'].astype(int)
    df['pause_should_min'] = df['pause_should_min'].astype(int)
    return df

def convert_date_to_datetime(df, date_column, date_format):
    df[date_column] = df[date_column].str.strip()
    df[date_column] = pd.to_datetime(df[date_column], format=date_format, errors='coerce')
    return df

def calculate_total_time(df):
    df['drive_time_min'] = df['drive_time_min'] - df['pause_should_min']
    df['total_time_hour'] = df['drive_time_min'] / 60
    return df

def sort_by_date(df):
    return df.sort_values(by='date')

def save_cleaned_data(df, output_csv):
    df.to_csv(output_csv, index=False)

def main(input_csv, output_csv, target_id):
    df = read_input_data(input_csv)
    columns_to_drop = ['T.Summe (-Pause)', 'Verdienst', 'Soll', '+- Diff.']
    date_format = '%d.%m.%Y'

    df = filter_by_id(df, target_id)
    df = drop_invalid_rows(df)
    df = rename_columns(df)
    df = drop_unnecessary_columns(df, columns_to_drop)
    df = convert_columns_to_int(df)
    df = convert_date_to_datetime(df, 'date', date_format)
    df = calculate_total_time(df)
    df = sort_by_date(df)
    save_cleaned_data(df, output_csv)

if __name__ == "__main__":
    input_csv = './data/combined_dataform2.csv'
    output_csv = './data/cleaned_data2.csv'
    target_id = 'Stipan Aleksandar'

    main(input_csv, output_csv, target_id)
