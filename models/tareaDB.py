#Definis como va a ser la tabla
from app import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    tarea_text = db.Column(db.String(100))
    
    def __init__(self, tarea_text):
        self.tarea_text = tarea_text
    