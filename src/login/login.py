from src.DB_connect.dbconnection import Dbconnect
# from src.JWTTokens.generate_token import JwtTokens
from src.JWTTokens.generate_token import generate_token


class Login:

    @staticmethod
    def login_api(email,password):
        from src.DB_connect.dbconnection import Dbconnect
        db_connection = Dbconnect()
        connection =db_connection.dbconnects()
        if connection:
            try:
                cursor = connection.cursor()
                query = f"""SELECT * FROM users_details WHERE email = '{email}' AND password = '{password}'"""
                cursor.execute(query)
                result = cursor.fetchone()
                if result:
                    token = generate_token(email)
                    return {
                        "data":result,
                        "token": token,
                        "message":"login succesful",
                        "status":"success"
                    }
                else:
                    return {"data":[],
                        "message":"invalid credentials",
                            "status":"error"}
            except Exception as e:
                return {"error": str(e)}
            finally:
                cursor.close()
                connection.close()
        else:
            return {"error": "Failed to connect to the database"}




