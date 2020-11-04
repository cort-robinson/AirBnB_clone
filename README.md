# 0x00. AirBnB clone - The console

## Resources:
Read or watch:
* [cmd module](https://intranet.hbtn.io/rltoken/Fx9HXIjmGzbmET4ylYg2Rw)
* [uuid module](https://intranet.hbtn.io/rltoken/eaQ6aELbdqb0WmPddhD00g)
* [datetime](https://intranet.hbtn.io/rltoken/_ySDcgtfrwLkTyQzYHTH0Q)
* [unittest module](https://intranet.hbtn.io/rltoken/QX7d4D__xhOJIGIWZBp39g)
* [args/kwargs](https://intranet.hbtn.io/rltoken/jQd3P_uSO0FeU6jlN-z5mg)
* [Python test cheatsheet](https://intranet.hbtn.io/rltoken/WPlydsqB0PG0uVcixemv9A)

---
## Learning Objectives:bulb:
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

### [0. README, AUTHORS](./README.md)
* Write a README.md:
    * You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference [Docker’s AUTHORS page](https://intranet.hbtn.io/rltoken/LhxU3SNypZwn428dmpz_qw)


### [1. Be PEP8 compliant!](./tests)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./tests)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:


### [4. Create BaseModel from dictionary](./models/base_model.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()). Now it’s time to re-create an instance with a dictionary representation.


### [5. Store first object](./models/engine/file_storage.py)
* Now we can recreate a BaseModel from another one by using a dictionary representation:


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./console.py)
* Update your command interpreter (console.py) to have these commands:

* create: Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel
* show: Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234.
* destroy: Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
* all: Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all.
* update: Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com".
    * Usage: update <class name> <id> <attribute name> "<attribute value>"
Let’s add some rules:

* You can assume arguments are always in the right order
* Each arguments are separated by a space
* A string argument with a space must be between double quote
* The error management starts from the first argument to the last one


### [8. First User](./models/user.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./models)
* Write all those classes that inherit from BaseModel:
    * [State](./models/state.py)
    * [City](./models/city.py)
    * [Amenity](./models/amenity.py)
    * [Place](./models/place.py)
    * [Review](./models/Review.py)


### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review

Update your command interpreter (console.py) to allow those actions: show, create, destroy, update and all with all classes created previously.

Enjoy your first console!

---

## Authors
* **Reese Hicks** - [dreeseh](https://github.com/dreeseh)
* **Cort Robinson** - [cort-robinson](https://github.com/cort-robinson)