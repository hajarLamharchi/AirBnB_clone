#!/usr/bin/python3
"""
    define a program that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re


class HBNBCommand(cmd.Cmd):
    """
        define  command interpreter
        Attributes:
            prompt(string): cmd prompt
    """
    prompt = "(hbnb) "
    __classes = [
                'BaseModel',
                'User',
                'State',
                'City',
                'Amenity',
                'Place',
                'Review']

    def precmd(self, line):
        """Called just before a command is executed to modify the line"""
        pattern = (
                r'^([A-Za-z][A-Za-z0-9_]*)\.'
                r'(all|count|destroy|update|show)\((.*)\)$')
        match = re.match(pattern, line)
        if match:
            cls_name = match.group(1)
            cmd = match.group(2)
            arg = match.group(3)
            char = {"'", "{", "\"", ",", ":", "}"}
            arg = arg.translate({ord(i): None for i in char})
            if cls_name in HBNBCommand.__classes:
                return f"{cmd} {cls_name} {arg}"
            else:
                print("** class doesn't exist **")
                return ""
        else:
            return line

    def do_EOF(self, line):
        'Quit command to exit the program\n'
        print("")
        return True

    def do_quit(self, line):
        'Quit command to exit the program'
        return True

    def help_quit(self):
        print('Quit command to exit the program\n')

    def emptyline(self):
        print

    def do_create(self, clas):
        'Creates a new instance of BaseModel and saves it\n'
        if clas:
            if clas in HBNBCommand.__classes:
                new = eval(clas)()
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        'Prints the string representation of an instance'
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        cls_name = arg_list[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        id = arg_list[1]
        obj = storage.all()
        key = f"{cls_name}.{id}"
        if key in obj:
            print(obj[key])
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        'Deletes an instance based on class name and id'
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        cls_name = arg_list[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        id = arg_list[1]
        obj = storage.all()
        key = f"{cls_name}.{id}"
        if key in obj:
            del obj[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        'Prints all strings representation of all instances'
        if line:
            if line in HBNBCommand.__classes:
                obj = storage.all()
                obj_list = []
                for k, v in obj.items():
                    if k.split('.')[0] == line:
                        obj_list.append(str(v))
                print(obj_list)
            else:
                print("** invalid syntax **")
        else:
            obj = storage.all()
            obj_list = []
            for k, v in obj.items():
                obj_list.append(str(v))
            print(obj_list)

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating"""
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        cls_name = arg_list[0]
        if cls_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        if len(arg_list) < 2:
            print("** instance id missing **")
            return
        if len(arg_list) < 3:
            print("** attribute name missing **")
            return
        if len(arg_list) < 4:
            print("** value missing **")
            return
        id = arg_list[1]
        obj = storage.all()
        key = f"{cls_name}.{id}"
        if key in obj:
            obj2 = obj[key]
            for i in range(2, len(arg_list), 2):
                new_attr = arg_list[i]
                val = arg_list[i + 1]
                obj2.__dict__[new_attr] = val
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, line):
        'the number of instances of a class'
        if line:
            obj = storage.all()
            nb = 0
            for k, v in obj.items():
                if k.split('.')[0] == line:
                    nb += 1
            print(nb)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
