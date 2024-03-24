import pandas as pd

from DB_connect.dbconnection import Dbconnect


class Dataframe_pandas:
    @staticmethod
    def read_sql_as_df(query):
        try:
            db_connection= Dbconnect()
            connection = db_connection.dbconnects()
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            df = pd.DataFrame(result, columns=columns)
            cursor.close()
            connection.close()
            return df

        except Exception as e:
            print(f"Error: {e}")
            return None
