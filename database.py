import mysql.connector as mysql

con=mysql.connect(
        user="root",
        passwd="",
        database="db_ip",
        host="localhost",
        port=3306,
    )