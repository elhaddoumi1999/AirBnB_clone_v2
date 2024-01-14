import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class TestHBNBCommandPrompt(unittest.TestCase):
    def test_prompt_string(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())


class TestHBNBCommandHelp(unittest.TestCase):
    def test_help(self):
        expected_output = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  create  destroy  help  quit  show  update"
        )

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(expected_output, output.getvalue().strip())


class TestHBNBCommandErrors(unittest.TestCase):
    def test_class_name_missing(self):
        cmd_list = ["create", "update", "show", "destroy"]
        for cmd in cmd_list:
            with patch('sys.stdout', new=StringIO()) as f:
                expected = "** class name missing **"
                HBNBCommand().onecmd(cmd)
                self.assertEqual(expected, f.getvalue().strip())


class TestHBNBCommandCreateObject(unittest.TestCase):

    def test_create_object(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            key = "BaseModel.{}".format(output.getvalue().strip())
            self.assertIn(key, storage.all().keys())

        # Add similar test methods for other classes...

    def test_value_missing(self):
        new_base_model = BaseModel()
        id_base_model = new_base_model.id
        with patch('sys.stdout', new=StringIO()) as f:
            expected = "** value missing **"
            HBNBCommand().onecmd(f"update BaseModel {id_base_model} name")
            self.assertEqual(expected, f.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
