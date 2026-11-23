import mysql.connector as SQLC

def DatabaseConnection():
    try:
        db_config = SQLC.connect(
            host='localhost',
            user='root',
            password='1810', #  sql password
            database = "sns"
        )
        return db_config
    except Exception as e:
        return "Something wrong in database connection"