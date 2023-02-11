#!/usr/bin/python3
'''
Console program
'''
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    '''
    Cmd application
    '''
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}
    class_list = ["BaseModel"]

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
        elif len(string) > 0 and string not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return False
        elif string in HBNBCommand.classes:
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
        line_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] in HBNBCommand.classes:
            print("** instance id missing **")
        else:
            full_address = f"{line_list[0]}.{line_list[1]}"
            models = storage.all()
            if full_address in models:
                print(models[full_address])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        '''Destroy an instance'''
        line_list = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] in HBNBCommand.classes:
            print("** instance id missing **")
        else:
            full_address = f"{line_list[0]}.{line_list[1]}"
            models = storage.all()
            if full_address in models:
                del models[full_address]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        '''Print all instances based on the class'''
        if not line or line and line in HBNBCommand.classes:
            models = storage.all()
            obj_list = []
            for obj in models.values():
                obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, line):
        '''Updates the class with the attributes in line'''
        line_list = line.split()
        if len(line) == 0:
            print("** class name missing **")
        elif line_list[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(line_list) == 1 and line_list[0] in HBNBCommand.classes:
            print("** instance id missing **")
        elif len(line_list) == 2:
            print("** attribute name missing **")
        elif len(line_list) == 3:
            print("** value missing **")
        else:
            key = f"{line_list[0]}.{line_list[1]}"
            my_dict = storage.all()
            if key in my_dict:
                val = line_list[3]
                print(type(val))
                setattr(my_dict[key], line_list[2], val)
                storage.save()
            else:
                print("** no instance found **")

    def complete_create(self, text, line, begidx, endidx):
        if text:
            return [cls for cls in self.class_list if cls.startswith(text)]
        else:
            return self.class_list


if __name__ == "__main__":
    HBNBCommand().cmdloop()
