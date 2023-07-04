FROM python:3.9

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV PORT 8080
ENV PYTHONUNBUFFERED TRUE
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main.wsgi:application