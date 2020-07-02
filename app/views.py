from app import app, queue, redis
from rq.job import Job

from flask import render_template, request

from app.tasks import count_words


@app.route("/", methods=["GET", "POST"])
def add_task():
    url = ''
    jobs = ''
    message = None

    q_len = len(queue)
    f_len = len(queue.finished_job_registry)

    if request.method == 'POST':
        url = request.form.get('url')
        if url.startswith('http://') or url.startswith('https://'):
            queue.enqueue(count_words, url, result_ttl=600, ttl=40)
            jobs = queue.jobs
        else:
            message = "Url must be start with https:// or http://"

    return render_template(
        "tasks/index.html",
        jobs=jobs,
        url=url,
        q_len=q_len,
        f_len=f_len,
        message=message,
    )


@app.route("/queue", methods=["GET"])
def tasks_in_queue():
    jobs = queue.jobs  # Get a list of jobs in the queue
    
    q_len = len(queue)
    f_len = len(queue.finished_job_registry)

    return render_template(
        "tasks/queue_tasks.html",
        jobs=jobs,
        q_len=q_len,
        f_len=f_len
    )


@app.route("/finished", methods=["GET"])
def finished_tasks():
    q_len = len(queue)
    f_len = len(queue.finished_job_registry)

    jobs = Job.fetch_many(
        queue.finished_job_registry.get_job_ids(),
        connection=redis
    )

    return render_template(
        "tasks/finished_tasks.html",
        f_len=f_len,
        q_len=q_len,
        jobs=jobs,
    )
