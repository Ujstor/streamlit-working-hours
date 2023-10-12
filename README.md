# Working Hours Data Set Analysis

This repository contains data sets and analysis scripts for working hours data spanning multiple years. The raw data is divided into three forms and stored in separate Excel files for each month. The analysis pipeline involves combining the data forms, performing data cleaning, and starning streamlit server for statistical analysis. The final analysis includes various visualizations, statistical measures, and insights into the working hours data.

![](https://i.imgur.com/dGrBO6Q.png)

![](https://i.imgur.com/kFDfezx.png)
<br>


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

Quit app `ctrl-c`
<br>
<br>

# Python Environment Setup and Dependency Installation

run `install_python.bat` script automates the setup process for a Python project by performing the following steps:

1. Checks if Python is installed. If not, it installs Python using the "winget" package manager.
2. Checks if a virtual environment folder named 'env' exists. If not, it creates one.
3. Activates the virtual environment.
4. Installs Python dependencies listed in the `requirements.txt` file using the "pip" package manager.
<br>
<br>

# Docker

To build the Docker image from the code, run:

```
docker compose -f .\docker-compose-dev.yml up
```

If you want to pull the image from the Docker repository instead, use:

```
docker compose -f .\docker-compose-prod.yml up
```

Image is automatically built and deployed through the Jenkins pipeline after tests have passed and are merged into the master branch.

<br/>

![](https://i.imgur.com/s9vVzFo.png)

# Jenkins Pipeline
Pipeline is designed to automate the build, test and deployment process for a project. It includes several stages that are executed when the pipeline is triggered. The pipeline assumes the main development branch is named "master" and tailors its actions accordingly.

### Pipeline Stages

1. **Checkout Code**: This stage fetches the project's source code from a specified Git repository and branch (assumes "master" branch by default).

2. **Test**: Runs tests on the code to ensure its correctness.

3. **Generate Docker Image Tag**: Generates a Docker image tag if the pipeline is running on the "master" branch. The image tag format is determined by the version part specified (Patch, Minor, Major).

4. **Build**: Builds a Docker image using the generated tag. This stage also requires the "master" branch to execute.

5. **Deploy**: Pushes the Docker image to a Docker Hub repository. It is executed only on the "master" branch.

6. **Environment Cleanup**: Cleans up the Docker image. Like the previous stages, it runs exclusively on the "master" branch.

### Skipping Stages

If the branch is not "master," the stages related to Docker image generation, build, deployment, and cleanup will be skipped, ensuring the pipeline continues without failure.
