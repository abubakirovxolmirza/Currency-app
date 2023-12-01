FROM python:3.11-alpine

RUN pip install --upgrade pip

WORKDIR /currency
COPY . /currency

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]