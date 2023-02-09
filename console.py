#!/usr/bin/python3
'''
Console program
'''
import cmd
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    '''
    Cmd application
    '''
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program

        '''
        return True

    def do_EOF(self, line):
        '''Quit command to exit the program

        '''
        return True

    def emptyline(self):
        '''
        Prevent execution of last command after new line

        '''
        pass

    def do_create(self, line):
        '''create a new instance of BaseModel'''
        if len(line) == 0:
            print("** class name missing **")
        elif len(line) > 0 and line != "BaseModel":
            print("** class doesn't exist **")
        elif line == "BaseModel":
            obj = BaseModel()
            print(obj.id)

    def do_show(self, line):
        '''show print a base models string rep'''
        line_list = []
        line_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] == "BaseModel":
            print("** instance id missing **")
        else:
            full_address = f"{line_list[0]}.{line_list[1]}"
            with open("file.json", "r") as f:
                models_dict = json.load(f)
            if full_address in models_dict:
                obj2 = BaseModel(**(models_dict[full_address]))
                print(obj2)
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
