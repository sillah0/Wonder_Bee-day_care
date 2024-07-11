from flask import Blueprint
from .auth  import auth
from .content import content

api = Blueprint('api', __name__)

api.register_blueprint(auth, url_prefix='/auth')
api.register_blueprint(content)
