#### Flask and python-rq
A simple example of app using Flask and python-rq  
Source: [https://pythonise.com/series/learning-flask/flask-rq-task-queue](https://pythonise.com/series/learning-flask/flask-rq-task-queue)

Running:
  - Clone project,
  - Enter in project folder,
  - Create virtualenv: ```python -m venv .venv```,
  - Activate virtualenv: ```source .venv/bin/activate```,
  - Install packages: ```pip install -r requirements.txt```,
  - Start ```redis```: ```docker-compose up -d```,
  - Start Flask app: ```export FLASK_ENV=development && flask run```,
  - Start ```rq``` worker in another terminal: ```rq worker```
  - Enqueue requisitions acessing: [http://localhost:5000?n=hello-world](http://localhost:5000?n=hello-world).
