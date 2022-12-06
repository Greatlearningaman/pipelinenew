FROM python:3.8-slim-buster

#ARG PYTHON_MAIN_FILE

RUN mkdir /app

WORKDIR /app
COPY . .

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]
