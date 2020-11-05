#!/usr/bin/python3
"""
module that contains the class HBNBCommand
the entry point for the command line interpreter
"""
import cmd
import sys
from datetime import datetime
from models import storage
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

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
            return
        strings = arg.split()
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(strings) != 2:
            print("** instance id missing **")
        else:
            instance_key = "{:s}.{:s}".format(strings[0], strings[1])
            objects = storage.all()
            try:
                print(objects[instance_key])
            except Exception:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234
        """
        if not arg:
            print("** class name missing **")
        strings = arg.split()
        if strings[0] not in HBNBCommand.classes:
            print("** class doesn't exist **'")
        elif len(strings) != 2:
            print("** instance id missing **")
        else:
            instance_key = "{:s}.{:s}".format(strings[0], strings[1])
            objects = storage.all()
            try:
                del (objects[instance_key])
            except Exception:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based
        or not on the class name. Ex: $ all BaseModel or $ all
        """
        objects = storage.all()
        if not arg:
            print(objects)
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            list_out = [v for k, v in objects.items()
                        if type(v).__name__ == arg]
            print(list_out)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
