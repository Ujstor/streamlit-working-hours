FROM python:3.11.5-slim

WORKDIR /src/

COPY . .

EXPOSE 8501

RUN pip3 install -r requirements.txt

RUN chmod +x entrypoint.sh

RUN chmod +x run_data_processing.sh

ENTRYPOINT ["/src/entrypoint.sh"]
