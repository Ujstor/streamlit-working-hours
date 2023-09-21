import pandas as pd

def combine_and_save_data(cleaned_data_paths, missing_data_path, output_csv):
    cleaned_data1 = pd.read_csv(cleaned_data_paths[0])
    cleaned_data2 = pd.read_csv(cleaned_data_paths[1])
    cleaned_data3 = pd.read_csv(cleaned_data_paths[2])
    missing_data = pd.read_csv(missing_data_path)

    combined_data = pd.concat([cleaned_data3, cleaned_data1, cleaned_data2, missing_data], ignore_index=True)

    combined_data.to_csv(output_csv, index=False)

if __name__ == "__main__":
    cleaned_data_paths = ['./data/cleaned_data1.csv', './data/cleaned_data2.csv', './data/cleaned_data3.csv']
    missing_data_path = './data/missing_data.csv'
    output_csv = './data/final_data.csv'

    combine_and_save_data(cleaned_data_paths, missing_data_path, output_csv)
