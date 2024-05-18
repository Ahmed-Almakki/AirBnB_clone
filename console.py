#!/usr/bin/python3
"""Custmizable Terminal"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Creating a terminal"""
    prompt = "(hbnb) "

    def parising(self, a):
        return a.split(" ")

    def do_quit(self, arg):
        """Quit command to exit the program """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg == "BaseModel":
            a = BaseModel()
            a.save()
            print(a.id)
        elif not arg:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

#    def do_show(arg, id_a):
#        """Prints the string representation of an instance"""
#        restored = storage.reload()
#        print(restored)
    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if globals().get(arg) is None:
            print("** class doesn't exist **")
        else:
            x = BaseModel()
            print(list(x))

#   #alaising
    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
