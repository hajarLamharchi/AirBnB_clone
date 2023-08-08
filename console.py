#!/usr/bin/python3
"""
    define a program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
