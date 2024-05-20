#!/usr/bin/python3
"""Custmizable Terminal"""
import cmd
from models.base_model import BaseModel
from models import storage
import json


file = storage.__class__.__dict__['_FileStorage__file_path']
print(file)

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


    def do_show(self,arg):
        """Prints the string representation of an instance"""
        args = arg.strip().split(" ")
        
        if len(args) == 2:
            if args[0] == "BaseModel":
                x = storage.all()
                idd = []
                for id in x.keys():
                    idd.append(id.split(".")[1])
                
                if args[1] not in idd:
                    print(" ** no instance found **")
                
                else:
                    obj = x[id]
                    print(obj)
        
        elif args[0] == "BaseModel" and len(args) == 1:
            print("** instance id missing **")
        
        elif not arg:
            print("** class doesn't exist **")
        
        elif args[0] != "BaseModel" and len(args) == 1:
            print("** class name missing **")
        

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.strip().split(" ")
        
        if len(args) == 2:    
            if args[0] == "BaseModel":
                x = storage.all()
                idd = []
                
                for id in x.keys():
                    idd.append(id.split(".")[1])
                
                if args[1] not in idd:
                    print("** no instance found **")
                
                else:
                    with open(file, 'r') as f:
                        js = json.load(f) 
                    key = "{}.{}".format(args[0], args[1])
                    del js[key]
                    del x[key]
                    with open(file, 'w') as f:
                        json.dump(js, f)
                        f.close()

        elif args[0] == "BaseModel" and len(args) == 1:
            print("** instance id missing **")

        elif not arg:
            print("** class doesn't exist **")
   
        elif args[0] != "BaseModel" and len(args) == 1:
            print("** class name missing **")


    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            x = storage.all()
            lst = []
            for all_obj in x.keys():
                lst.append(str(x[all_obj]))
            print(lst)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.strip().split(" ")
        if len(args) >= 4:
            args = args[:4]
            lst = []
            x = storage.all()

            for id in x.keys():
                lst.append(id.split(".")[1])
            
            if args[1] not in lst:
                print("** no instance found **")
            
            else:
                key = "{}.{}".format(args[0], args[1])
#                x[key].update({[args[2]]: args[3]})
                with open(file, 'r') as f:
                    js = json.load(f)
                
                js[key].update({args[2]: args[3]})
                
                with open(file, 'w') as f:
                    json.dump(js, f)
                    f.close()

        elif not arg:
            print("** class name missing **")
       
        elif args[0] != "BaseModel" and len(args) == 1:
            print("** class doesn't exist **")
      
        elif args[0] == "BaseModel" and len(args) == 1:
            print("** instance id missing **") 
      
        elif len(args) < 4 and len(args) > 1:
            if len(args) == 3:
                print("** value missing **")
            elif len(args) == 2:
                print("** attribute name missing **") 
#   alaising
    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
