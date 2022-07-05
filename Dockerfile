FROM python:3.8-slim-buster

ARG PYTHON_MAIN_FILE

RUN mkdir /app

WORKDIR /app
COPY ./requirements.txt /app
COPY ${PYTHON_MAIN_FILE} /app/app.py

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
