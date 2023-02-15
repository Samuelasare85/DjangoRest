FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN pip install -r requirements.txt
COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate

EXPOSE 8000
CMD [  "python", "manage.py", "runserver", "0.0.0.0:8000" ]
