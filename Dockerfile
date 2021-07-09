FROM python:3.7.6-alpine

RUN pip install flask

WORKDIR /app
COPY app.py /app

EXPOSE 5000
CMD ["python", "-m", "flask", "run"]