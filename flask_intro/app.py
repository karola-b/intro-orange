# uruchamiamyk komendą: flask run --debug
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello/')
def hello():
    return "Hello world!"


@app.route('/template/')
def hello_template():
    return render_template('hello.html')


@app.route('/hello/<string:name>/')
def hello_name(name):
    return render_template(
        'hello_name.html',
        name=name,
    )

@app.route('/day/<string:answer>/')
def is_it_a_good_day(answer):
    return render_template(
        'day.html',
        answer=answer
    )


@app.route('/test/')
def test():
    return render_template('test.html')


@app.route('/form_get/')
def hello_form():
    data = request.args
    name = data.get('name')

    if name:
        return render_template(
            'hello_name.html',
            name=name
        )

    return render_template(
        'hello_form.html'
    )


@app.route('/form_post/', methods = ["POST", "GET"])
def hello_form_post():
    if request.method == "GET":
        return render_template(
            'hello_form_post.html'
        )

    elif request.method == "POST":
        data = request.form
        name = data.get('name')

        if name:
            return render_template(
                'hello_name.html',
                name=name
            )

    return render_template(
        'hello_form_post.html'
    )
