import mysql.connector as myConn

def connect():
    return myConn.connect(
        host="localhost",
        user="root",
        password="mrfaisu07",
        database="bank_system"
    )
