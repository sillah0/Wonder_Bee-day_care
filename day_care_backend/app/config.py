#!/usr/bin/python3

import os
import paypalrestsdk

class Config:
    """
    Configuration class for the daycare management system.
    
    Attributes:
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLite database.
        JWT_SECRET_KEY (str): The secret key used for JWT token generation.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to enable/disable
        SQLAlchemy modification tracking.
    """
    SQLALCHEMY_DATABASE_URI = 'mysql://daycare_user:Qwerty*130#@localhost/daycare_db'
    JWT_SECRET_KEY = ('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    paypalrestsdk.configure({
        "mode": "sandbox", # sandbox or live
        "client_id": "ATXl_fWPLW_DTh3yWuKn6odZGWcd40bsmROPZHANkjNNJQ7fz7FlYODK6HNAD-O1qEqso6QOwaaKJYeY",
        "client_secret": "EAr0fGFYBFUrnyxviDBC2scUumup6X4gJC5fYisucRMFONCNGN2Ibq_7K4gGUYgR2MbtjVqSL2yDfkfM"
    })

