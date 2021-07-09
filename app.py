import os

from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/secretvariable', methods=['POST'])
def variable_get():
    if request.data.decode('utf8') != os.environ.get("SECRET", "1234"):
        return make_response("U know nothing!", 401)
    print("TEST_VARIABLE is:", os.environ.get("TEST_VARIABLE"))
    return os.environ.get("TEST_VARIABLE")


@app.route('/file')
def file_get():
    file = os.environ.get("TEST_FILE", None)
    if not file:
        print("No file set!")
        return make_response("Error", 500)

    if not os.path.isfile(file):
        print("is not a file!")
        return make_response("Error", 500)

    with open(file) as f:
        return make_response(f.read(), 200)


if not os.environ.get("ENVSET", None):
    raise RuntimeError("Missing ENVSET")

if __name__ == '__main__':
    app.run()
