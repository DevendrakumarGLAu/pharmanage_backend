from src.DB_connect.dbconnection import Dbconnect


class Bill_payments:
    @staticmethod
    def save_orders(name, mobile, orders):
        connection = Dbconnect.dbconnects()
        if connection:
            cursor = connection.cursor()
            try:
                # Insert order information
                cursor.execute("INSERT INTO Orders (name, mobile) VALUES (%s, %s)", (name, mobile))
                order_id = cursor.lastrowid

                # Insert order details
                for order in orders:
                    sno = order.get('sno')
                    category_id = order.get('category_id')
                    product_id = order.get('product_id')
                    quantity = order.get('quantity')
                    category_name = order.get('category_name')
                    product_name = order.get('product_name')

                    cursor.execute("""
                        INSERT INTO OrderDetails 
                        (order_id, sno, category_id, product_id, quantity, category_name, product_name) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """, (order_id, sno, category_id, product_id, quantity, category_name, product_name))

                connection.commit()
                return {"message": "Order saved successfully", "status": "success"}
            except Exception as e:
                connection.rollback()
                return {"error": str(e), "status": "error"}
            finally:
                cursor.close()
                connection.close()
        else:
            return {"error": "Failed to connect to the database", "status": "error"}