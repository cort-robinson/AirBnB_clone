#!/usr/bin/python3
"""
module that houses the base_model class
"""
import uuid
from datetime import datetime
import models

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """
    defines all common attributes/
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initializes the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at") and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """string represemtation of base model"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id,
                                         self.__dict__)

    def save(self):
        """updates public instance attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        if "created_at" in my_dict:
            my_dict["created_at"] = my_dict["created_at"].strftime(time)
        if "updated_at" in my_dict:
            my_dict["updated_at"] = my_dict["updated_at"].strftime(time)
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
