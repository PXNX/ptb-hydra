from flask import Flask

from main import main

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    main()
    app.run(port=8001)

