from flask import jsonify, render_template

from errata import app, settings


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', settings=settings)


@app.route('/feeds', methods=['GET'])
def feeds():
    return jsonify({
        'hello': 'there'
    })
