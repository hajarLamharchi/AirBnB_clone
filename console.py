#!/usr/bin/python3
"""
    define a program that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

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
        'Creates a new instance of BaseModel, saves it'
        if clas:
            if clas == 'BaseModel':
                new = BaseModel()
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
        if cls_name not in ['BaseModel']:
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
        if cls_name not in ['BaseModel']:
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
        if line not in ['BaseModel']:
            print("** class doesn't exist **")
        else:
            obj = storage.all()
            obj_list = []
            for k, v in obj.items():
                obj_list.append(str(v))
            print(obj_list)

    def do_update(self, args):
        'Updates an instance based on the class name and id by adding or updating'
        arg_list = args.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        cls_name = arg_list[0]
        if cls_name not in ['BaseModel']:
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
        new_attr = arg_list[2]
        val = arg_list[3]
        obj = storage.all()
        key = f"{cls_name}.{id}"
        if key in obj:
            obj2 = obj[key]
            obj2.__dict__[new_attr] = val
            storage.save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
