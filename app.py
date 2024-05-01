import gevent.monkey

gevent.monkey.patch_all()

import logfire

logfire.configure(token="")
# todo doing this import shows the error
import magic
from flask import Flask

app = Flask(__name__)


from flask import render_template


@app.route("/")
def hello_world():
    return render_template("index.html", title="Hello")
