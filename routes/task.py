from flask import Flask, Blueprint, redirect, url_for, render_template, request
from models.tareaDB import Task
from app import db  # Importa db aquí

task = Blueprint('task', __name__)  #Crea una variable que esta vinculada a la app 

@task.route('/')
def home():
    tareas = Task.query.all()
    return render_template("index.html", tareas = tareas)

@task.route('/add_task', methods=['POST'])
def add_task():
    if request.method == 'POST':
        #Recibe los datos del form y los imprime en terminal
        tarea = request.form['new-task-input']
        nueva_tarea = Task(tarea)
        print(nueva_tarea)
        
        #Añade el dato guardado
        db.session.add(nueva_tarea)
        db.session.commit()
        
    return redirect(url_for("task.home")) #Te redirije al index

@task.route('/edit/<id>', methods=['POST', "GET"])
def editTask(id):
    tarea = Task.query.get(id)
    
    if request.method == 'POST':
        #Recibe los datos del form y cambia los datos
        tarea.tarea_text = request.form["tarea_text"]
        
        db.session.commit()
        return redirect(url_for("task.home")) #Te redirije al index
    
    return render_template("edit.html", tarea = tarea)

@task.route('/delete/<id>')
def delete(id):
    #Obtengo el id con el query y luego elimino
    tarea = Task.query.get(id)
    db.session.delete(tarea)
    db.session.commit()
    
    return redirect(url_for("task.home")) #Te redirije al index