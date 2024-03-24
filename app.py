import requests
from flask import Flask, request, jsonify  # Import request object
from flask_cors import CORS
from DB_connect.dbconnection import Dbconnect
from src.routes.routes import Routes

METHODS = ['GET', 'POST']

app = Flask(__name__)
CORS(app)

@app.route('/mysql', methods=METHODS)
def connectionss():
    db_connection = Dbconnect()
    connection = db_connection.dbconnects()
    if connection:
        return 'Connected to MySQL database'
    else:
        return 'Failed to connect to MySQL database'

@app.route('/addproduct', methods=METHODS)
def add_product():
    return Routes.addproduct(request)

@app.route('/getproducts', methods=METHODS)
def get_products():
    return Routes.get_products()

if __name__ == '__main__':
    app.run(debug=True)
