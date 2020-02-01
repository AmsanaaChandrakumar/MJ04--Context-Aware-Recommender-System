import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():

    return render_template("index.html")

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	# POST request: goes from broweser to flask
    if request.method == 'POST':
    	print('Incoming..')
    	jsonData = request.get_json(force=True)
        print(jsonData.get('greeting'))  # parse as JSON
        return str(jsonData.get('greeting')), 200

    # GET request: goes from flask to browser
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
