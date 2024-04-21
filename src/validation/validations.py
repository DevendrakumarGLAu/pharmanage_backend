from src.DB_connect.dbconnection import Dbconnect


class Validators:
    @staticmethod
    def validate_vendor_data(column_data, connection):
        if 'email' in column_data:
            email = column_data['email']
            cursor = connection.cursor()
            cursor.execute(f"SELECT id FROM vendors WHERE email = '{email}'")
            if cursor.fetchone():
                return {'status': 'error', 'message': f'Email "{email}" already exists'}

        if 'mobile' in column_data:
            mobile = column_data['mobile']
            # Check if the mobile number already exists in the table
            cursor.execute(f"SELECT id FROM vendors WHERE mobile = '{mobile}'")
            if cursor.fetchone():
                return {'status': 'error', 'message': f'Mobile number "{mobile}" already exists'}

        return {'status': 'success'}

