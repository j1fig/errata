from flask import jsonify

from errata import app


@app.route('/', methods=['GET'])
def predict():
    return jsonify({
        'hello': 'there'
    })
