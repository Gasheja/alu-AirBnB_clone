#!/usr/bin/python3
"""amenity module"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class to represent an 'Amenity' object
        An instance of this class represents a single amenity,"""
    name = ""
