# Working Hours Data Set Analysis

## [Live App Link](https://working-hours.streamlit.app/)

This repository contains data sets and analysis scripts for working hours data spanning multiple years. The raw data is divided into three forms and stored in separate Excel files for each month. The analysis pipeline involves combining the data forms, performing data cleaning, and starning streamlit server for statistical analysis. The final analysis includes various visualizations, statistical measures, and insights into the working hours data.

## Data

The raw data is organized as follows:

`./raw_data`: Contains the three forms of raw data, each stored in separate folders:

  -`data_form1`: Contains the raw data for form 1. (5.2021-9.2022)

  -`data_form2`: Contains the raw data for form 2. (10.2022-present)

  -`data_form3`: Contains the raw data for form 3. (1.2021-4.2021)

  After running `run_data_procsing.bat`, the combined data sets for each form are stored in the following files:

- `./data/combined_dataform2.csv`
- `./data/combined_dataform1.csv`
- `./data/combined_dataform3.csv`

The cleaning process involves extracting relevant columns, handling missing values, and ensuring data consistency.

The cleaned and combined data sets from each form are merged into a single CSV file:

- `./data/final_data.csv`

 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.8.104:8501

Quit app `ctrl-c`

# Python Environment Setup and Dependency Installation

`run_install_python.bat` script automates the setup process for a Python project by performing the following steps:

1. Checks if Python is installed. If not, it installs Python using the "winget" package manager.
2. Checks if a virtual environment folder named 'env' exists. If not, it creates one.
3. Activates the virtual environment.
4. Installs Python dependencies listed in the `requirements.txt` file using the "pip" package manager.
