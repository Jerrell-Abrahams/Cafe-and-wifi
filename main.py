from flask import Flask, render_template
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True)
    map_url = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    has_sockets = db.Column(db.String, nullable=False)
    has_toilet = db.Column(db.String, nullable=False)
    has_wifi = db.Column(db.String, nullable=False)
    can_take_calls = db.Column(db.String, nullable=False)
    seats = db.Column(db.Integer, nullable=False)
    coffee_price = db.Column(db.String, nullable=False)

print(db.session.query(Cafe).all())

@app.route("/")
def hello_world():
    all_cafes = db.session.query(Cafe).all()
    return render_template("index.html", cafes=all_cafes)




if __name__=="__main__":
    app.run(debug=True)