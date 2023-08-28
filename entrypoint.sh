#!/bin/bash

# Execute the data processing script
./run_data_processing.sh

# Navigate to the subdirectory containing your Streamlit app
cd ./streamlit

# Start the Streamlit app
streamlit run Home.py