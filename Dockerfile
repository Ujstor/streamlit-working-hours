# Use the official Python 3.7 image as the base image
FROM python:3.11.5-slim

# Set the working directory inside the container
WORKDIR /src/

# Copy the contents of your current directory into the container's working directory
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Install the Python dependencies listed in requirements.txt
RUN pip3 install -r requirements.txt

# make script executable
RUN chmod +x entrypoint.sh
RUN chmod +x run_data_processing.sh

# Set the entry point to your custom shell script
ENTRYPOINT ["/src/entrypoint.sh"]
