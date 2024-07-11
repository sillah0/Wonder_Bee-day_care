#!/ussr/bin/python3

import unittest
import flask from Flask
from flask_testing import TestCase
from app import create_app, db
from models import User, Staff, Classroom, Payment, Parent, Child, Activity, Enrollment, Attendance

class BaseTestCase(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://daycare_user:Qwerty*130#@localhost/daycare_db'
        return app

    def setUp(self):
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        
class TestUserModel(BaseTestCase):
      user = User(username='testuser', email='test@example.com')
        db.session.add(user)
        db.session.commit()
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().username, 'testuser')

class TestStaffModel(BaseTestCase):
    def test_staff_creation(self):
        staff = Staff(name='John Doe', position='Teacher')
        db.session.add(staff)
        db.session.commit()
        self.assertEqual(Staff.query.count(), 1)
        self.assertEqual(Staff.query.first().name, 'John Doe')

class TestClassroomModel(BaseTestCase):
    def test_classroom_creation(self):
        classroom = Classroom(name='Class A')
        db.session.add(classroom)
        db.session.commit()
        self.assertEqual(Classroom.query.count(), 1)
        self.assertEqual(Classroom.query.first().name, 'Class A')

class TestPaymentModel(BaseTestCase):
    def test_payment_creation(self):
        payment = Payment(amount=100.0, status='Paid')
        db.session.add(payment)
        db.session.commit()
        self.assertEqual(Payment.query.count(), 1)
        self.assertEqual(Payment.query.first().amount, 100.0)

class TestParentModel(BaseTestCase):
    def test_parent_creation(self):
        parent = Parent(name='Jane Doe')
        db.session.add(parent)
        db.session.commit()
        self.assertEqual(Parent.query.count(), 1)
        self.assertEqual(Parent.query.first().name, 'Jane Doe')

class TestChildModel(BaseTestCase):
    def test_child_creation(self):
        child = Child(name='Baby Doe')
        db.session.add(child)
        db.session.commit()
        self.assertEqual(Child.query.count(), 1)
        self.assertEqual(Child.query.first().name, 'Baby Doe')

class TestActivityModel(BaseTestCase):
    def test_activity_creation(self):
        activity = Activity(name='Drawing')
        db.session.add(activity)
        db.session.commit()
        self.assertEqual(Activity.query.count(), 1)
        self.assertEqual(Activity.query.first().name, 'Drawing')

class TestEnrollmentModel(BaseTestCase):
    def test_enrollment_creation(self):
        enrollment = Enrollment(status='Enrolled')
        db.session.add(enrollment)
        db.session.commit()
        self.assertEqual(Enrollment.query.count(), 1)
        self.assertEqual(Enrollment.query.first().status, 'Enrolled')

class TestAttendanceModel(BaseTestCase):
    def test_attendance_creation(self):
        attendance = Attendance(status='Present')
        db.session.add(attendance)
        db.session.commit()
        self.assertEqual(Attendance.query.count(), 1)
        self.assertEqual(Attendance.query.first().status, 'Present')

if __name__ == '__main__':
    unittest.main()