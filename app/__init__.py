from flask import Flask
from app.extensions import db,migrate
from app.controllers.students_controller import student


#application factory function
def create_app():
    
    #app instance
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)
    migrate.init_app(app,db)
    
     # Importing and registering models
    from app.models.students import Student



    @app.route("/")
    def home():
        return "Python Exam"
    
  
    
    

    return app

