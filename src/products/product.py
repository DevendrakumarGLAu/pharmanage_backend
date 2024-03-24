import json

from flask import jsonify

from DB_connect.dbconnection import Dbconnect
import pandas as pd

from src.dataframe_df.dataframe_operations import Dataframe_pandas


class Product:
    def __init__(self):
        self.db_connection = Dbconnect()

    def save_product(self, category, quantity, productName,costPrice ,sellingPrice):
        connection = self.db_connection.dbconnects()
        if connection:
            try:
                cursor = connection.cursor()
                sql_query = "INSERT INTO products (category, quantity, productName,costPrice ,sellingPrice) VALUES (%s, %s, %s,%s, %s)"
                cursor.execute(sql_query, (category, quantity, productName,costPrice ,sellingPrice))
                connection.commit()
                cursor.close()
                connection.close()

                return {"message": "Data saved successfully"}
            except Exception as e:
                return {"error": str(e)}
        else:
            return {"message": "Failed to connect to MySQL database"}
    # @statistics
    def update_product(self, id, name, qty, amount):
        connection = self.db_connection.dbconnects()
        if connection:
            try:
                cursor = connection.cursor()
                sql_query = "UPDATE addproduct SET name = %s, qty = %s, amount = %s WHERE id = %s"
                cursor.execute(sql_query, (name, qty, amount, id))
                connection.commit()
                cursor.close()
                connection.close()

                return {"message": "Data updated successfully"}
            except Exception as e:
                return {"error": str(e)}
        else:
            return {"message": "Failed to connect to MySQL database"}

    @staticmethod
    def get_products():
        try:
            query = f"""SELECT * FROM products"""
            products_df = Dataframe_pandas.read_sql_as_df(query)
            if products_df is not None:
                products_json = json.loads(products_df.to_json(orient='records'))
                return jsonify({'data': products_json})
            else:
                return jsonify({'error': 'Failed to fetch products data'})
        except Exception as e:
            return jsonify({'error': str(e)})
