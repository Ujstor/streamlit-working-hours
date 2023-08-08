import pandas as pd

cleaned_data1 = pd.read_csv('./data/cleaned_data1.csv')
cleaned_data2 = pd.read_csv('./data/cleaned_data2.csv')
cleaned_data3 = pd.read_csv('./data/cleaned_data3.csv')
missing_data = pd.read_csv('./data/missing_data.csv')

combined_data = pd.concat([cleaned_data3, cleaned_data1, cleaned_data2, missing_data], ignore_index=True)

combined_data.to_csv('./data/final_data.csv', index=False)