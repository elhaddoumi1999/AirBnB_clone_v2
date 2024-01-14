#!/usr/bin/env python3
"""Console Module"""

import cmd
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command that interpreter class"""

    prompt = '(hbnb) '
    valid_classes = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

    def do_quit(self, arg):
        """The command that exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF\n"""
        print("")
        return True

    def emptyline(self):
        """Execute anything\n"""
        pass

    def do_help(self, arg):
        """The help command\n"""
        cmd.Cmd.do_help(self, arg)

    def do_create(self, arg):
        """Creates a new instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
        else:
            del all_objects[key]
            models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        all_objects = models.storage.all()
        if not args:
            print([str(all_objects[obj]) for obj in all_objects])
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            print([str(all_objects[obj]) for obj in all_objects
                   if args[0] in obj])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        all_objects = models.storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(all_objects[key], args[2], eval(args[3]))
        models.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
