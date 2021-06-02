""" jwt app """
from app_core import app
from routes import *


if __name__ == '__main__':
    app.run(debug=True, threaded=True ,port = 3000 , )