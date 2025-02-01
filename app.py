import os
from flask import Flask
import db_util
import dotenv


app = Flask(__name__)
dotenv.load_dotenv()

dbname = os.getenv("DATABASE_NAME")
port = os.getenv("PORT")
host = os.getenv("HOST")
db_user = os.getenv("USER")
db_pass = os.getenv("PASSWORD")


@app.route("/")
def test():
    sql_connector = db_util.DatabaseManager(
        dbname=dbname,
        port=port,
        host=host,
        user=db_user,
        password=db_pass
    )
    result = sql_connector.fetch_first_vehicle()
    sql_connector.close_all()
    return f"{result[0]} {result[1]} {result[2]} {result[3]} {result[4]}"


app.run(debug=True)
