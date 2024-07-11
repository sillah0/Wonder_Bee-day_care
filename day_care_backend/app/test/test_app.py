#!/usr/bin/python3

import unittest
from datetime import datetime
from flask import Flask
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
    def test_user_creation(self):
        user = User(
            first_name='Test', 
            last_name='User', 
            email='test@example.com', 
            password='password', 
            role='user'
        )
        db.session.add(user)
        db.session.commit()
        
        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().email, 'test@example.com')

class TestStaffModel(BaseTestCase):
    def test_staff_creation(self):
        user = User(
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='password123',
            role='staff'
        )
        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().first_name, 'Test')
        self.assertEqual(User.query.first().last_name, 'User')
        self.assertEqual(User.query.first().email, 'testuser@example.com')
        self.assertEqual(User.query.first().role, 'staff')

class TestClassroomModel(BaseTestCase):
    def test_classroom_creation(self):
        classroom = Classroom(class_name='Class A')
        db.session.add(classroom)
        db.session.commit()
        self.assertEqual(Classroom.query.count(), 1)
        self.assertEqual(Classroom.query.first().class_name, 'Class A')

class TestPaymentModel(BaseTestCase):
    def test_payment_creation(self):
        user = User(
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='password123',
            role='user'
        )
        db.session.add(user)
        db.session.commit()

        payment = Payment(
            amount=100.0,
            user_id=user.user_id,
            created_at=datetime.utcnow(),  # Use 'created_at' field
            status='completed'
        )
        db.session.add(payment)
        db.session.commit()

        self.assertEqual(Payment.query.count(), 1)
        self.assertEqual(Payment.query.first().amount, 100.0)
        self.assertEqual(Payment.query.first().user_id, user.user_id)
        self.assertEqual(Payment.query.first().status, 'completed')

class TestParentModel(BaseTestCase):
    def test_parent_creation(self):
        parent = Parent(address='123 Main St', contacts=1234567890, reg_status='active')
        db.session.add(parent)
        db.session.commit()
        self.assertEqual(Parent.query.count(), 1)
        self.assertEqual(Parent.query.first().address, '123 Main St')
        self.assertEqual(Parent.query.first().contacts, 1234567890)
        self.assertEqual(Parent.query.first().reg_status, 'active')

class TestChildModel(BaseTestCase):
    def test_child_creation(self):
        child = Child(first_name='Baby', last_name='Doe')
        db.session.add(child)
        db.session.commit()
        self.assertEqual(Child.query.count(), 1)
        self.assertEqual(Child.query.first().first_name, 'Baby')
        self.assertEqual(Child.query.first().last_name, 'Doe')

class TestActivityModel(BaseTestCase):
    def test_activity_creation(self):
        activity = Activity(name='Drawing')
        db.session.add(activity)
        db.session.commit()
        self.assertEqual(Activity.query.count(), 1)
        self.assertEqual(Activity.query.first().name, 'Drawing')

class TestEnrollmentModel(BaseTestCase):
    def test_enrollment_creation(self):
        enrollment = Enrollment()
        db.session.add(enrollment)
        db.session.commit()
        self.assertEqual(Enrollment.query.count(), 1)

class TestAttendanceModel(BaseTestCase):
    def test_attendance_creation(self):
        # Create a User instance
        user = User(
            first_name='Test', 
            last_name='User', 
            email='test@example.com', 
            password='password', 
            role='staff'
        )
        db.session.add(user)
        db.session.commit()

        staff = Staff(user_id=user.user_id)
        db.session.add(staff)
        db.session.commit()
        
        # Create a Child instance
        child = Child(first_name='Baby', last_name='Doe')
        db.session.add(child)
        db.session.commit()

        # Create a Classroom instance
        classroom = Classroom(class_name='Class A')
        db.session.add(classroom)
        db.session.commit()

        # Create an Attendance instance
        attendance = Attendance(
            present_status=True,
            date='2023-10-01',
            child_id=child.child_id,
            class_id=classroom.class_id,
            staff_id=user.user_id
        )
        db.session.add(attendance)
        db.session.commit()

        self.assertEqual(Attendance.query.count(), 1)
        self.assertTrue(Attendance.query.first().present_status)
        

if __name__ == '__main__':
    unittest.main()
