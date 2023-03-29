FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=app/__init__.py

RUN ls /app   # <-- added command to list contents of /app directory

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
