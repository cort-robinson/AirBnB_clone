#!/usr/bin/python3
"""
module that houses the base_model class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    defines all common attributes/
    methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """initializes the base model"""
        t = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if hasattr(self, "created_at")\
               and type(self.created_at) is str:
                self.created_at = \
                    datetime.strptime(kwargs.get("created_at"), t)
            if hasattr(self, "updated_at")\
               and type(self.updated_at) is str:
                self.updated_at = \
                    datetime.strptime(kwargs.get("updated_at"), t)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """string represemtation of base model"""
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates public instance attribute updated_at
        with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing keys/values of __dict__"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = str(self.created_at.isoformat())
        if "updated_at" in my_dict:
            my_dict["updated_at"] = str(self.updated_at.isoformat())
        return my_dict
