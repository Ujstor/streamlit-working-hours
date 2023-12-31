#!/bin/bash

echo "Combining data..."
python ./cleaning_scripts/combine_data.py

echo "Data combining completed."

echo "Cleaning data form 1..."
python ./cleaning_scripts/data_cleaning1.py

echo "Data cleaning for form 1 completed."

echo "Cleaning data form 2..."
python ./cleaning_scripts/data_cleaning2.py

echo "Data cleaning for form 2 completed."

echo "Cleaning data form 3..."
python ./cleaning_scripts/data_cleaning3.py

echo "Data cleaning for form 3 completed."

echo "Creating final data csv..."
python ./cleaning_scripts/final_data.py

echo "Data processing completed."
