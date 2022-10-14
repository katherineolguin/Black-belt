from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash #Encargado de mostrar mensajes o errores

from datetime import datetime

import re #Importando las expresiones regulares
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

class Cita: 

    def __init__(self, data):

        self.id = data['id']
        self.nombre = data['nombre']
        self.fecha = data['fecha']
        self.estado = data['estado']
        self.create_at = data['create_at']
        self.updated_at = data['updated_at']
        self.first_name = data['first_name']
        
        
    @staticmethod
    def valida_cita(formulario):
        es_valido = True

        #Validamos que el nombre tenga al menos 3 caracteres
        if len(formulario['nombre'])  <3:
            flash('La cita debe tener un nombre','cita')
            es_valido = False
        
        if formulario ['fecha'] =='':
            flash('Tu cita debe tener una  fecha', 'cita')
            es_valido = False
        else:
            fecha_obj = datetime.strptime(formulario['fecha'], '%Y-%m-%d') #Estamos transformando un tecto a formato de fecha

            hoy = datetime.now() #me da la fecha de hoy
            if hoy > fecha_obj:
                flash('La fecha tiene que ser para un futuro', 'cita')
                es_valido = False
        
        return es_valido
            
        

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO citas (nombre,fecha,estado,user_id ) VALUES (%(nombre)s, %(fecha)s, %(estado)s, %(user_id)s)"
        resut = connectToMySQL('black_belt').query_db(query, formulario)
        return resut #El ID del nuevo registro que se realizo 


    @classmethod
    def get_all_citas(cls):
        query = "SELECT citas.*, first_name FROM citas LEFT JOIN users ON users.id = citas.user_id"

        results = connectToMySQL('black_belt').query_db(query)
        citas = []

        for cita in results:
            citas.append(cls(cita))

        return citas

    # @classmethod
    # def update_recipe(cls, formulario):
    #     query = "UPDATE recipes SET name=%()s, description=%(description)s, instructioms=%(instructioms)s, date_made=%(date_made)s, under_30=%(under_30)s "

    #     results = connectToMySQL('recetas_practica_examen').query_db(query, formulario)

    #     return results


    @classmethod
    def get_by_id(cls, formulario):

        query = "SELECT citas.*, first_name FROM citas LEFT JOIN users ON users.id = citas.user_id WHERE  citas.id = %(id)s ;"
        results = connectToMySQL('black_belt').query_db(query, formulario)

        citaId = cls(results[0]) #result[0] = diccionario con todos los datos de la receta; cls() creamos la instancia en base a ese diccionario
        return citaId
        

    @classmethod
    def update_citas(cls, formulario):

        query = "UPDATE citas SET nombre=%(nombre)s, fecha=%(fecha)s, estado=%(estado)s WHERE id=%(cita_id)s "
        result = connectToMySQL('black_belt').query_db(query, formulario)
        return result


    @classmethod
    def delete_citas(cls, formulario):
        query = "DELETE FROM citas WHERE id = %(id)s"
        result = connectToMySQL('black_belt').query_db(query, formulario)
        return result

