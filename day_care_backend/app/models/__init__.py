from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .parent import Parent
from .staff import Staff
from .classroom import Classroom
from .child import Child
from .attendance import Attendance
from .enrollment import Enrollment
from .activity import Activity
from .billing import Payment