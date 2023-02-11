#!/usr/bin/python3
"""Method Command Interpreter"""

import shlex
import inspect
import cmd
import sys
import models
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.place import Place
from models.city import City
from models.state import State
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "
    class_dict = {"BaseModel": BaseModel, "User": User, "Place": Place,
                  "State": State, "City": City, "Amenity": Amenity,
                  "Review": Review}

    def do_create(self, args):
        """
        Creates a new instance of BaseModel, saves it, and prints the id
        Usage: create <class name>
        """
        if not args:
            print("** class name missing **")
        else:
            if args in HBNBCommand.class_dict.keys():
                new_creation = HBNBCommand.class_dict[args]()
                models.storage.save()
                print(new_creation.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of a specific instance
        Usage: show <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                print(models.storage.all()[key_value])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, args):
        """Deletes an instance
        Usage: destroy <class name> <id>
        """
        strings = args.split()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        else:
            key_value = strings[0] + '.' + strings[1]
            try:
                del models.storage.all()[key_value]
                models.storage.save()
            except KeyError:
                print("** no instance found **")

    def do_all(self, args):
        """Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: all <class name>
        """
        strings = args.split()
        new_list = []
        address_value = 0
        if len(strings) == 1:
            if strings[0] not in HBNBCommand.class_dict.keys():
                print("** class doesn't exist **")
            else:
                for key in models.storage.all().keys():
                    class_name = key.split('.')
                    if class_name[0] == strings[0]:
                        new_list.append(str(models.storage.all()[key]))
                    else:
                        continue
                print(new_list)
        else:
            for key, value in models.storage.all().items():
                new_list.append(str(models.storage.all()[key]))
            print(new_list)

    def do_update(self, args):
        """Update an instance.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        strings = shlex.split(args)
        models.storage.reload()
        new_dict = models.storage.all()
        if len(strings) == 0:
            print("** class name missing **")
        elif strings[0] not in HBNBCommand.class_dict.keys():
            print("** class doesn't exist **")
        elif len(strings) == 1:
            print("** instance id missing **")
        elif strings[0] + '.' + strings[1] not in new_dict.keys():
            print("** no instance found **")
        elif len(strings) == 2:
            print("** attribute name missing **")
        elif len(strings) == 3:
            print("** value missing **")
        else:
            key = strings[0] + '.' + strings[1]
            if hasattr(new_dict[key], strings[2]):
                caster = type(getattr(new_dict[key], strings[2]))
                setattr(new_dict[key], strings[2], caster(strings[3]))
                models.storage.save()
            else:
                setattr(new_dict[key], strings[2], strings[3])
                models.storage.save()

    def do_quit(self, args):
        """Quits the program
        """
        raise SystemExit

    def do_EOF(self, args):
        """Handles end of file condition
        """
        return True

    def do_help(self, args):
        """Get help on commands
        'help' or '?' with no arguments prints a list of commands for which
        help is available
        'help <command>' or '? <command>' gives help on <command>
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """Doesn't execute anything when user enter an empty line
        """
        pass

    def default(self, args):
        """Method that deals with all instances of a command being preceeded by
        a class name.
        ex. User.all()
        """
        counter = 0
        command_method = args.split('.')
        specific_method = command_method[1].split('(')
        if specific_method[0] == "count":
            for key in models.storage.all().keys():
                if key.split('.')[0] == command_method[0]:
                    counter += 1
            print(counter)
        if specific_method[0] == "all":
            self.do_all(command_method[0])
        if specific_method[0] == "show":
            current_id = specific_method[1].split(')')
            self.do_show(command_method[0] + ' ' + current_id[0])
        if specific_method[0] == "destroy":
            current_id = specific_method[1].split(')')
            self.do_destroy(command_method[0] + ' ' + current_id[0])
        if specific_method[0] == "update":
            all_entries = specific_method[1].split(')')
            all_attributes = all_entries[0].split(',')
            if '{' in all_attributes[1]:
                for sets in range(1, len(all_attributes)):
                    if sets == 1 and sets != len(all_attributes) - 1:
                        first_set = all_attributes[sets].split('{')
                        sending_set = first_set[1].split(':')
                    elif sets == 1 and sets == len(all_attributes) - 1:
                        first_set = all_attributes[sets].split('{')
                        first_set = first_set[1].split('}')
                        sending_set = first_set[0].split(':')
                    elif sets == len(all_attributes) - 1:
                        first_set = all_attributes[sets].split('}')
                        sending_set = first_set[0].split(':')
                    else:
                        sending_set = all_attributes[sets].split(':')
                    self.do_update(command_method[0] + ' ' +
                                   all_attributes[0] + ' ' +
                                   sending_set[0] + sending_set[1])
            else:
                self.do_update(command_method[0] + ' ' + all_attributes[0] +
                               all_attributes[1] + all_attributes[2])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
