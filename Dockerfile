FROM python:3.12

RUN apt-get update && apt-get install -y redis-server && apt-get clean

RUN mkdir -p /data

RUN chmod 777 /data

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & celery -A settings.celery worker --loglevel=info & celery -A settings.celery beat"]