import logging
import flask
from flask import request, jsonify, abort
import json
import os


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return '''<h1>API service</h1>
<p>Prometheus API server</p>'''

@app.route('/api/v1/alerts', methods=['POST'])
def create_task():
    if not request.json:
        logging.error('Cannot recognise json')
        abort(400)
    if request.json[0]['labels']['alertname'] == 'DefaultRequestWeb':
        logging.info('Default Alerts')
        stream = os.popen('docker service scale stack_web-Service=1')
        output = stream.read()
        stream = os.popen('docker service scale stack_cadvisor=1')
        output = stream.read()
        logging.info(output)

    elif request.json[0]['labels']['alertname'] == 'CPUHighAlert':
        stream = os.popen('docker service scale stack_web-Service=2')
        output = stream.read()
        stream = os.popen('docker service scale stack_cadvisor=2')
        output = stream.read()
        logging.info('High Load')
        logging.info(output)

    return jsonify(request.json), 201

app.run(host="localhost", port=5050, debug=True)