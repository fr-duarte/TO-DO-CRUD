#Acá se ejecuta la aplicación
from app import app
from app import db

#Crea una tabla
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)