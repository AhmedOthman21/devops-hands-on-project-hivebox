FROM python:3.9-slim-buster

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

EXPOSE 5000

ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "main:app"]
