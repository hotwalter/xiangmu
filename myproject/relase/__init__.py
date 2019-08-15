from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1/relese"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config.from_envvar("FLASKR_SETTINGS", silent=True)
db = SQLAlchemy(app)
from relase.admin import admin as admin_printbule

app.register_blueprint(admin_printbule,url_prefix='/index')
