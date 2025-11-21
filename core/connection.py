import mysql.connector

mysql_config = {
    'host' : 'localhost',
    'user' : 'root',
    'database' : 'BD_QuickSales',
    'password' : 'Haidercc10**',
    'auth_plugin' : 'mysql_native_password'
}

connection = mysql.connector.connect(**mysql_config)

def get_connection():
    return connection