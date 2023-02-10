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
    classes = {"BaseModel": BaseModel}
    classes_list = ["BaseModel"]

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

    def validate(string):
        '''validate the input line'''
        if len(string) == 0:
            print("** class name missing **")
            return False
        elif len(string) > 0 and string not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False
        elif string in HBNBCommand.classes_list:
            return True

    def validate_strlist(string):
        '''validate the string list'''
        pass

    def do_create(self, line):
        '''create a new instance of BaseModel'''
        check = HBNBCommand.validate(line)
        if check == True:
            obj = HBNBCommand.classes[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        '''show print a base models string rep'''
        line_list = []
        line_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] in HBNBCommand.classes_list:
            print("** instance id missing **")
        else:
            full_address = f"{line_list[0]}.{line_list[1]}"
            try:
                with open("file.json", "r") as f:
                    models_dict = json.load(f)
                    if full_address in models_dict:
                        obj2 = HBNBCommand.classes[line_list[0]](**(models_dict[full_address]))
                        print(obj2)
                    else:
                        print("** no instance found **")
            except FileNotFoundError as e:
                print("** no instances saved **")
                print(e)

    def do_destroy(self, line):
        '''Destroy an instance'''
        line_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] in HBNBCommand.classes_list:
            print("** instance id missing **")
        else:
            full_address = f"{line_list[0]}.{line_list[1]}"
            try:
                with open("file.json", "r") as f:
                    models_dict = json.load(f)
                    if full_address in models_dict:
                        del models_dict[full_address]
                        with open("file.json", "w") as f:
                            json.dump(models_dict, f, indent=2)
                    else:
                        print("** no instance found **")
            except FileNotFoundError as e:
                print("** no instances saved **")
                print(e)

    def do_all(self, line):
        '''Print all instances based on the class'''
        try:
            with open("file.json", "r") as f:
                models_dict = json.load(f)
                print("[", end="")
                if models_dict:
                    for item in models_dict:
                        if line and line in HBNBCommand.classes_list:
                            obj3 = HBNBCommand.classes[line](**(models_dict[item]))
                            print(f"\"{obj3}\"", end="")
                        elif len(line) == 0:
                            for classes in HBNBCommand.classes_list:
                                obj4 = HBNBCommand.classes[classes](**(models_dict[item]))
                            print(f"\"{obj4}\"", end="")

                print("]")
        except FileNotFoundError as e:
            print("** no instances saved **")
            print(e)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
