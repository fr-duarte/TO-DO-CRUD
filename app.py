#Acá se configura la aplicación
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.secret_key = "llave" #llave para poder acceder a la info encriptada

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from routes.task import task

app.register_blueprint(task) #Vinculacion con las rutas 


