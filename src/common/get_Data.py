import json

from flask import jsonify

from src.dataframe_df.dataframe_operations import Dataframe_pandas


class GetData:
    @staticmethod
    def getData_common(id, Table_name):
        try:
            sql_query = f"""SELECT * FROM {Table_name} WHERE id = {id}"""
            # Pass the id parameter to the read_sql_as_df function
            df = Dataframe_pandas.read_sql_as_df(sql_query)
            if df is not None:
                products_json = json.loads(df.to_json(orient='records'))
                return jsonify({'data': products_json,
                                'message': "Data fetch succesfully",
                                'status': 'success'
                                })
            else:
                return jsonify({'message': 'Failed to fetch products data',
                                "status": "error"})
        except Exception as e:
            return {"status": str(e),
                    "message": "failed to fetch Data"}

