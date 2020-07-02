FROM python:3.6-alpine

WORKDIR /home/flask-rq

ENV FLASK_ENV=development

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./

CMD flask run --host=0.0.0.0