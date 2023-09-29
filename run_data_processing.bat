@echo off

REM Check if the virtual environment is activated
if NOT "%VIRTUAL_ENV%"=="" (
    echo Virtual environment is already activated.
) else (
    echo Activating virtual environment...
    call .\env\Scripts\activate.bat
)

echo Combining data...
python ./cleaning_scripts/combine_data.py

echo Data combining completed.

echo Cleaning data form 1...
python ./cleaning_scripts/data_cleaning1.py

echo Data cleaning for form 1 completed.

echo Cleaning data form 2...
python ./cleaning_scripts/data_cleaning2.py

echo Data cleaning for form 2 completed.

echo Cleaning data form 3...
python ./cleaning_scripts/data_cleaning3.py

echo Data cleaning for form 3 completed.

echo Creating final data csv
python ./cleaning_scripts/final_data.py

echo Data processing completed.

@REM cd .\streamlit\
@REM streamlit run Home.py