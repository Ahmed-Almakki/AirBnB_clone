#!/usr/bin/python3
"""Custmizable Terminal"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex
import json
from models.user import User
from models.review import Review
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity

class_map = {"BaseModel": BaseModel, "User": User,
             "Place": Place, "State": State,
             "City": City, "Amenity": Amenity,
             "Review": Review}


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
            if line[0] not in class_map.keys():
                print("** class doesn't exist **")
            else:
                for i in class_map.keys():
                    if i == line[0]:
                        obj = class_map.get(line[0])
                        new = obj()
                        new.save()
                        print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        line = shlex.split(arg)
        lst = [i for i in storage.all().keys()]
        lst = [i.split(".")[1] for i in lst if i.split('.')[0] == line[0]]
        if len(line) < 1:
            print("** class name missing **")
        elif len(line) == 1:
            print("** instance id missing **")
        else:
            if line[0] not in class_map.keys():
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
        lst = [i.split(".")[1] for i in lst if i.split('.')[0] == line[0]]
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in class_map.keys():
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
        if (len(line) == 0) or (line[0] in class_map.keys()):
            lst = []
            with open("file.json", "r") as file:
                data = json.load(file)
                for i in data.values():
                    obj = class_map.get(line[0])
                    x = obj(**i)
                    lst.append(str(x))
                print(lst)
                file.close()
        elif line[0] and line[0] not in class_map.keys():
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        line = shlex.split(arg)
        lst = [i for i in storage.all().keys()]
        lst = [i.split(".")[1] for i in lst]
        if len(line) < 1:
            print("** class name missing **")
        elif line[0] not in class_map.keys():
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
