#!/usr/bin/python3
""" User MOdule"""
from models.base_model import BaseModel


class User(BaseModel):
    """User object management class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
