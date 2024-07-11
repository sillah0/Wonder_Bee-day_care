#!/usr/bin/python3

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from models import User, Staff, Classroom, Payment, Parent, Child, Activity, Enrollment, Attendance, db
from config import Config
from routes.content import content
from routes.auth import auth as auth_blueprint
from routes.parent import parent
from routes.staff import staff
from routes.attendance import attendance
from routes.activity import activity
from routes.classroom import classroom
from routes.enrollment import enrollment
from routes.billing import payment
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    db.init_app(app)
    JWTManager(app)
    migrate = Migrate(app, db)
    
    app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
    app.register_blueprint(content, url_prefix='/api/content')
    app.register_blueprint(parent, url_prefix='/api/parent')
    app.register_blueprint(staff, url_prefix='/api/staff')
    app.register_blueprint(attendance, url_prefix='/api/attendance')
    app.register_blueprint(activity, url_prefix='/api/activity')
    app.register_blueprint(classroom, url_prefix='/api/classroom')
    app.register_blueprint(enrollment, url_prefix='/api/enrollment')
    app.register_blueprint(payment, url_prefix='/api/payment')
    with app.app_context():
        db.create_all()
    
    return app
    
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
