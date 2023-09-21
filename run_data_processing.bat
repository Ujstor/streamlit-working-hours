@echo off

@REM REM Check if the virtual environment is activated
@REM if NOT "%VIRTUAL_ENV%"=="" (
@REM     echo Virtual environment is already activated.
@REM ) else (
@REM     echo Activating virtual environment...
@REM     call .\env\Scripts\activate.bat
@REM )

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