<img src="https://www.holbertonschool.com/assets/holberton-logo-1cc451260ca3cd297def53f2250a9794810667c7ca7b5fa5879a569a457bf16f.png" alt="Holberton logo">

# 0x00. AirBnB clone - The console
---

## Description

This is the first step towards building our first full web application: the AirBnB clone.

A command interpreter to manage our Airbnb clone objects:

 * Create a new object (ex: a new User or a new Place)
 * Retrieve an object from a file, a database etc…
 * Do operations on objects (count, compute stats, etc…)
 * Update attributes of an object
 * Destroy an object

##### Example 1 | help command in interactive mode

```
vagrant:AirBnB_clone$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help all
Prints a string representation of all instances, can include class
        name to specify only instances of that class
        Usage: all <class name>

(hbnb)

```

##### Example 2 | help command non-interactive mode

```

vagrant:AirBnB_clone$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) vagrant:AirBnB_cat test_helpsole.py
help
vagrant:AirBnB_clone$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update


```

### List of allowed functions and system calls


## Requirements for Python Scripts

 * Allowed editors: vi, vim, emacs
 * All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
 * All your files should end with a new line
 * The first line of all your files should be exactly #!/usr/bin/python3
 * A README.md file, at the root of the folder of the project, is mandatory
 * Your code should use the PEP 8 style (version 1.7 or more)
 * All your files must be executable
 * The length of your files will be tested using wc
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## Requirements for Python unit tests

 * Allowed editors: vi, vim, emacs
 * All your files should end with a new line
 * All your test files should be inside a folder tests
 * You have to use the unittest module
 * All your test files should be python files (extension: .py)
 * All your test files and folders should start by test_
 * Your file organization in the tests folder should be the same as your project:
for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
for models/user.py, unit tests must be in: tests/test_models/test_user.py
 * All your tests should be executed by using this command: python3 -m unittest discover tests
 * You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
 * All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
 * All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
 * All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

---
File|Task
---|---
AUTHORS | the authors page
README.md | read me file
tests | unit tests
base_model.py | a parent class that takes care of the initialization, serialization and deserialization of your future instances
file_storage.py | an abstract storage engine
console.py | a program that handles a command interpreter
user.py | a class User that inherits from BaseModel
state.py | a class State that inherits from BaseModel
city.py | a class City that inherits from BaseMode
amenity.py | a class Amenity that inherits from BaseMode
place.py | a class Place that inherits from BaseMode
review.py | a class Review that inherits from BaseMode

### Authors

[Besthor Igbe](https://github.com/besthor)
