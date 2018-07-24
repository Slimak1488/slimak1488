import datetime

from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/time", methods=['GET'])
def get_time():
    return jsonify(now1=datetime.datetime.now().strftime('%H'), now2=datetime.datetime.now().strftime('%M'))


if __name__ == "__main__":
    app.run()


#New line