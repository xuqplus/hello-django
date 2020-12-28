FROM python:alpine

COPY . /app

RUN pip install django

EXPOSE 8000

CMD cd app && python manage.py runserver