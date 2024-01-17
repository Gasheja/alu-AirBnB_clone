AirBnB clone - The console Project! 🏨
Welcome to our "AirBnB clone - The console Project" This is a comprehensive web application that combines various components such as database storage, a back-end API, and front-end interfacing, all designed to replicate some functionalities of AirBnB. This Project was done by (Mugisha Gasheja and Eric Nyuma Jr. )

Step 1 - The Console 🕹️
Description
Creating the data model
Manage (create, update, destroy, etc) objects via a console / command interpreter
Store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means from our console code (the command interpreter itself) and from the front-end and RestAPI that we will build later.

This abstraction will also allow us to change the type of storage easily without updating all of our codebase.

The console will be a tool to validate this storage engine

Files And Directories
models: directory will contain all classes used for the entire project. A class, called “model” in a OOP * project is the representation of an object/instance.
tests: directory will contain all unit tests.
console.py: file is the entry point of our command interpreter.
models/base_model.py: file is the base class of all our models. It contains common elements: .attributes: id, created_at and updated_at .methods: save() and to_json()
models/engine: directory will contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.
Using The Console
Run the console: ./console.py
Quit the console: (hbnb) quit
Display the help for a command: (hbnb) help
Show an object: (hbnb) show or (hbnb) .show()
Destroy an object: (hbnb) destroy or (hbnb) .destroy()
Show all objects, or all instances of a class: (hbnb) all or (hbnb) all
Update an attribute of an object: (hbnb) update "" or (hbnb) .update(, , "")
Examples
Interactive Mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
===================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
Non-Interactive Mode:
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
==================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
==================================
EOF  help  quit
(hbnb) 
$
Author
Mugisha Gasheja, Eric Nyuma Jr.
