#!/usr/bin/python3
"""Unit tests for FileStorage class"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json
import models


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up for test methods"""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test method"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_FileStorage_instance(self):
        """Test the creation of FileStorage instance"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(type(self.storage).__name__, "FileStorage")

    def test_FileStorage_attributes(self):
        """Test the attributes of FileStorage"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertIsInstance(FileStorage._FileStorage__objects, dict)

    def test_all_method(self):
        """Test the all() method of FileStorage"""
        # Clear the storage
        self.storage._FileStorage__objects = {}

        # Create a new BaseModel
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.storage.new(new_instance)
        self.storage.save()

        # Retrieve all objects
        all_objects = self.storage.all()

        self.assertEqual(all_objects, {key: new_instance})

    def test_new_method(self):
        """Test the new() method of FileStorage"""
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.storage.new(new_instance)
        self.assertIn(key, self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects[key], new_instance)

    def test_save_method(self):
        """Test the save() method of FileStorage"""
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.storage.new(new_instance)
        self.storage.save()

        with open(FileStorage._FileStorage__file_path, 'r') as file:
            saved_data = json.load(file)

        self.assertIn(key, saved_data)
        self.assertEqual(saved_data[key], new_instance.to_dict())

    def test_reload_method(self):
        """Test the reload() method of FileStorage"""
        new_instance = BaseModel()
        key = f"{new_instance.__class__.__name__}.{new_instance.id}"
        self.storage.new(new_instance)
        self.storage.save()
        self.storage.reload()

        self.assertIn(key, self.storage._FileStorage__objects)
        reloaded_instance = self.storage._FileStorage__objects[key]
        self.assertIsInstance(reloaded_instance, BaseModel)
        self.assertEqual(reloaded_instance.to_dict(), new_instance.to_dict())

    def test_reload_method_file_not_found(self):
        """Test the reload() method when file not found"""
        self.storage.all().clear()
        self.storage.reload()
        # file
        with self.assertRaises(FileNotFoundError):
            with open(FileStorage._FileStorage__file_path, 'r') as file:
                json.load(file)

    def test_reload_method_invalid_json(self):
        """Test the reload() method with invalid JSON in file"""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
        self.assertFalse(os.path.exists(FileStorage._FileStorage__file_path))
        models.storage.reload()


if __name__ == '__main__':
    unittest.main()
