from flask import Flask, Response, request
import json
from db_connection import cursor
app = Flask(__name__)
@app.route("/kentta/<icao_koodi>")
def kentta(icao_koodi):
    sql = f"SELECT * from airport where ident = '{icao_koodi}';"

    cursor.execute(sql)
    tulos = cursor.fetchall()

    brr = {
        "ICAO": icao_koodi,
        "Name": tulos[0][3],
        "Municipality": tulos[0][10]
    }

    return json.dumps(brr)




if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)