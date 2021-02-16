import flask
from flask import request, jsonify, abort

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Prom web API</h1>
<p>Prom web service</p>'''

# A route to return all of the available entries in our catalog.

@app.route('/api/v1/alerts', methods=['POST'])
def create_task():
    if not request.json: 
        print(request)
        abort(400)
#    task = {
#        'id': tasks[-1]['id'] + 1,
#        'title': request.json['title'],
#        'description': request.json.get('description', ""),
#        'done': False
#    }
#    tasks.append(task)
    print(request.json)
    return jsonify(books), 201

app.run()