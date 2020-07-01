from flask import Flask, request
from redis import Redis
from rq import Queue
from time import sleep

app = Flask(__name__)

r = Redis()
q = Queue(connection=r)

def background_task(n):
    delay = 2
    print(f'Task running, simulating a {delay} second delay')
    sleep(delay)
    print(len(n))
    print('Task Complete')
    return len(n)

@app.route('/task')
def add_task():
    if request.args.get('n'):
        job = q.enqueue(background_task, request.args.get('n'))
        q_len = len(q)

        return f'Task ({job.id}) added to queue at ({job.enqueued_at}), {q_len} tasks in the queue'

    return 'No value for n provided'

