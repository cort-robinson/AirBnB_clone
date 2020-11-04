#!/usr/bin/python3
"""
module that contains the class HBNBCommand
the entry point for the command line interpreter
"""
import cmd
import sys
from datetime import datetime
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB console"""

    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "Place", "State",
               "City", "Amenity", "Review"]

    def emptyline(self):
        """leaves blank line afrer return"""
        pass

    def do_EOF(self, arg):
        """exits console"""
        if sys.stdin.isatty() is False:
            print()
        return True

    def do_quit(self, arg):
        """exits the console"""
        return True

    def do_create(self, arg):
        """
        Creates a new object instance, save it (to the JSON file)
        and prints the id. EX: $ create BaseModel
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            new = eval("{:s}()".format(arg))
            print(new.id)
            new.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
