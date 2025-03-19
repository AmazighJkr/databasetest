from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Database configuration
MYSQL_HOST = "db4free.net"  # Hostname for db4free
MYSQL_USER = "vmmachine03"  # Use the username given by db4free
MYSQL_PASSWORD = "vmmachine03"  # Use the password given by db4free
MYSQL_DB = "vmmachine03"  # Use the database name given by db4free
MYSQL_PORT = 3306  # Default MySQL port


def test_database_connection():
    try:
        # Establish a connection to the database
        connection = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            port=MYSQL_PORT,
            connect_timeout=10  # Timeout for the connection
        )
        return True, "Connection to the database was successful!"
    except pymysql.MySQLError as e:
        return False, f"Database connection failed! Error: {e}"


@app.route("/test-db", methods=["GET"])
def test_db():
    success, message = test_database_connection()
    if success:
        return jsonify({"status": "success", "message": message}), 200
    else:
        return jsonify({"status": "error", "message": message}), 500

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "API is up and running!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
