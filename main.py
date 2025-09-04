from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/wynik", methods=["POST"])
def wynik():
    rokAktualny = datetime.now().year   # np. 2025
    imie = request.form["imie"]
    rok = request.form["rok"]
    wiadomosc = request.form["wiadomosc"]
    nadawca = request.form["nadawca"]
    wiek = rokAktualny-int(rok)
    # pobiera dane z formularza
    return f"Wszystkiego najlepszego {imie} z okazji {wiek}  urodzin <br> {wiadomosc}<br> {nadawca}"


if __name__ == "__main__":
    #app.run(debug=True)  #to jest uruchamianie lokalnie
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)# http://127.0.0.1:8080/ lokalny port uruchomiony