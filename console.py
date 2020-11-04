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

    prompt = "(HBNB) "

    def get_help(self, commands):
        msg = set()
        for name in commands:
            if name != 'do_help':
                try:
                    doc = getattr(self, name).__doc__.split('\n')
                except Exception:
                    return ( "No help available when Python"
                             " is run with the -OO switch." )
                for x in doc:
                    x = x.strip()
                    if x:
                        msg.add('  %s' % x)
        msg = list(msg)
        msg.sort()
        msg = '\n'.join(msg)
        return msg

    def emptyline(self):
        """leaves blank line afrer return"""
        pass

    def do_EOF(self, arg):
        """exits console"""
        return True

    def do_quit(self, arg):
        """exits the console"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
