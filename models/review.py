#!/usr/bin/python3
"""Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
