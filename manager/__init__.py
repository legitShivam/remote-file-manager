from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///settings.db'
app.config['SECRET_KEY'] = 'cf00678a1daa58ccdca17384'   # Hex key created by os.urandom(12).hex()

db = SQLAlchemy(app)









    