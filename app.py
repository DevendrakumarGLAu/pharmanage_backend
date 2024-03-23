from flask import Flask
from DB_connect.dbconnection import Dbconnect

METHODS = ['GET', 'POST']

app = Flask(__name__)
# CORS(app)

@app.route('/mysql', methods = METHODS)
def connectionss():
	db_connection = Dbconnect()
	connection = db_connection.dbconnects()
	if connection:
		return 'Connected to MySQL database'
	else:
		return 'Failed to connect to MySQL database'




if __name__=='__main__':
	app.run(debug=True)
