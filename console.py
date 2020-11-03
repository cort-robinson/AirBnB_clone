#!/usr/bin/python3
"""
module that contains the class HBNBCommand
"""

import cmd
from datetime import datetime
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """HBNB console"""
    prompt = '(HBNB)'

    def do_EOF(self, arg):
        """exits console"""
        return True

    def emptyline(self):
        """overwrites emptyline"""
        return False

    def do_quit(self, arg):
        """exits the console"""
        return True

if __name__ == 'main':
    HBNBCommand().cmdloop()
