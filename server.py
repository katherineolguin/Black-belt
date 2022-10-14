from flask_app import app

# Importar controlador
from flask_app.controllers import users_controllers
from flask_app.controllers import citas_controllers

#Ejecutamos variable app
if __name__=="__main__":
    app.run(debug =True)
