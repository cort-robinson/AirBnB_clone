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

    prompt = '(HBNB) '

    classes = {
        "BaseModel"
    }

    def do_EOF(self, line):
        """exits console"""
        return (True)

    def emptyline(self):
        """overwrites emptyline"""
        pass

    def do_quit(self, arg):
        """exits the console"""
        return (True)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
