#!/usr/bin/python3
"""Custmizable Terminal"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import json


file = storage.__class__.__dict__['_FileStorage__file_path']


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
        line = shlex.split(arg)
        if len(line) < 1:
            print("** class name missing **")
        else:
            if line[0] != "BaseModel":
                print("** class doesn't exist **")
            else:
                nw = BaseModel()
                nw.save()
                print(nw.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        line = shlex.split(arg)
        lst = [i for i in storage.all().keys()]
        lst = [i.split(".")[1] for i in lst]
        if len(line) < 1:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            if line[0] != "BaseModel":
                print("** class doesn't exist **")
            elif line[1] not in lst:
                print("** no instance found **")
            else:
                x = storage.all()
                k = line[0] + "." + line[1]
                print(x[k])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        line = shlex.split(arg)
        lst = [i for i in storage.all().keys()]
        lst = [i.split(".")[1] for i in lst]
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            if line[1] not in lst:
                print("** no instance found **")
            else:
                stor = storage.all()
                for i in stor.keys():
                    if i == line[0] + '.' + line[1]:
                        stor.pop(i)
                        break
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        line = shlex.split(arg)
        if (len(line) == 0) or (line[0] == "BaseModel"):
            lst = []
            with open("file.json", "r") as file:
                data = json.load(file)
                for i in data.values():
                    x = BaseModel(**i)
                    lst.append(str(x))
                print(lst)
                file.close()
        elif line[0] and line[0] != "BaseModel":
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        line = shlex.split(arg)
        lst = [i for i in storage.all().keys()]
        lst = [i.split(".")[1] for i in lst]
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line) == 1:
            print("** instance id missing **")
        elif line[1] not in lst:
            print("** no instance found **")
        elif len(line) == 2:
            print("** attribute name missing **")
        elif len(line) == 3:
            print("** value missing **")
        else:
            kkey = line[0] + '.' + line[1]
            obj = storage.all().get(kkey)
            setattr(obj, line[2], line[3])
            obj.save()
            storage.save()


#   alaising
    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
