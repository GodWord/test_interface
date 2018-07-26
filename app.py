from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello 王木木!'


if __name__ == '__main__':
    app.run('0.0.0.0')
