from flask import render_template, redirect, request, session, flash
from flask_app import app

#Importamos modelo
from flask_app.models.users import User
from flask_app.models.citas import Cita

@app.route('/add/cita')
def add_cita():

    if 'user_id' not in session:
        return redirect('/')


    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    return render_template('nueva_cita.html', user=user)


@app.route('/save/cita', methods=['POST'])
def save_cita():

    if 'user_id' not in session:
        return redirect('/')

    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    if not Cita.valida_cita(request.form):
        return redirect('/add/cita')

    Cita.save(request.form)
    return redirect('/dashboard')



@app.route('/edit/citas/<int:id>')
def edit_cita(id):
    
    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID

    formulario_citas = {"id": id}
    citaId = Cita.get_by_id(formulario_citas)

    return render_template('editar_cita.html', user=user, citaId=citaId)


@app.route('/update/cita', methods=['POST'])
def update():
    if 'user_id' not in session:
        return redirect('/')

    #Yo sé que en sesión tengo el id de mi usuario (session['user_id'])
    #Queremos una función que en base a ese id me regrese una instancia del usuario
    formulario = {"id": session['user_id']}

    user = User.get_by_id(formulario) #Recibo la instancia de usuario en base a su ID


    if not Cita.valida_cita(request.form):
        return redirect('/edit/citas/'+request.form['cita_id']) 

    Cita.update_citas(request.form) 

    return redirect ('/dashboard')

@app.route('/delete/citas/<int:id>')

def delete(id):
    if 'user_id' not in session:
        return redirect('/')



    formulario = {"id": id}    #ID DE LA RECETA PARA PODER, EDITAR BORRAR ECT *estenombre debe ser igual
    Cita.delete_citas(formulario) #<- a este nombre

    return redirect ('/dashboard')

