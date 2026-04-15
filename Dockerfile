FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt gunicorn whitenoise psycopg2-binary

COPY . .

# Выполняем миграции и собираем статику при запуске
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn first_project.wsgi:application --bind 0.0.0.0:8000"]
