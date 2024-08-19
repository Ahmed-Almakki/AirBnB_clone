#!/usr/bin/python3
"""State Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review inherehnt from Basemodel"""
    place_id = ""
    user_id = ""
    text = ""
