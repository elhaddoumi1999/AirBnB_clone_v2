<<<<<<< HEAD
#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
=======
#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.place import place_amenity


class Amenity(BaseModel, Base):
<<<<<<< HEAD
    """Representation of Amenity """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
=======
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
>>>>>>> a1a68afd0dca7866b0e2a5e292f4e0a52be6468c
