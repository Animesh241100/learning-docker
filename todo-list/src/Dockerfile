FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app/
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN rm -rf lists/migrations/
RUN apt-get update && apt-get install -y iputils-ping
RUN mkdir lists/migrations
RUN touch lists/migrations/__init__.py
RUN python manage.py makemigrations
# RUN python manage.py migrate
# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]