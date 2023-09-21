FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app


#RUN ./launch_tests
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "8000"]
