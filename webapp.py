from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome to my vagina!'


@app.route('/pump-valve-setup')
def pump_valve_setup():
    return jsonify({'test': 0})


if __name__ == '__main__':
    app.run(debug=True)


