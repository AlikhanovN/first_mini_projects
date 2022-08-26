from flask import Flask, render_template, url_for, request, redirect

import game
from models import *
from game import *

app = Flask(__name__, static_url_path="/static")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        game.diler = ["Diler "]
        game.player1 = ["Alex "]
        game.player2 = ["Kairat "]
        return render_template("index.html", data=winner())
# Записываем данные в таблицу request_call_table
    if request.method == "POST":
        name = request.form["Name"]
        phone = request.form["Phone number"]
        email = request.form["Email"]
        message = request.form["Message"]
        # print(name, phone, email, message)
        cursor.execute(f"INSERT INTO request_call_table(name, phone_number, email, message) VALUES('{name}', '{phone}', '{email}', '{message}');")
        connection.commit()
        # cursor.execute("SELECT * FROM request_call_table")
        # print(cursor.fetchall())
        return redirect("/")




if __name__ == "__main__":
    app.run(debug=True)