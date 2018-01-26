from flask import Flask


app = Flask(__name__)


import errata.views
from errata.models.database import init_db, clear_db


if __name__ == '__main__':
    app.run(debug=True)
