from flask import Flask
from redis import Redis
from rq import Queue
import rq_dashboard

app = Flask(__name__)
app.config.from_object(rq_dashboard.default_settings)
app.register_blueprint(rq_dashboard.blueprint, url_prefix="/rq-dashboard")

redis = Redis(host='redis')
queue = Queue(connection=redis)

from app import views, tasks
