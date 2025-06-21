from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    try:
        connection = mysql.connector.connect(
            host="db",       # service name from docker-compose
            user="root",
            password="password",
            database="mydb"
        )
        return "Connected to MySQL DB!"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
