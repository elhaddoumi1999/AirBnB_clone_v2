#!/usr/bin/python3
"""
instantiates storage object
if environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
instantiate database storage
otherwise instantiates FileStorage
"""
from os import getenv


if getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
