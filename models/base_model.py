#!/usr/bin/python3
"""Shebang script that defines a class model called BaseModel"""
import models
from uuid import uuid4()
from datetime import datetime


class BaseModel:
    """a general class called the basemodel which contains all attribute and models that needs to be inherited. It defines the base model of the airbnb project"""

    def __init__(self, *args, **kwargs):
        """initializes a new base model

            Args:
            *args: they provide space for unused arguments
            **kwargs: the key values of the dictionary attributes
            """
            time_format = Y-%m-%dT%H:%M:%S.%f
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            if len(kwargs) != 0:
                for a, b in kwargs.items():
                    if a == "created_at" or a == "updated_at":
                        self.__dict__[a] = datetime.strptime(b, time_format)
                    else:

                        self.__dict__[a] = b
                else:

                    models.storage.new(self)

    def save(self):
        """update and save updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns dictionary containing all keys/values of _dict_of tge instance and also class name of tge obj
        """
        dict_return = self.__dict__.copy()
        dict_return["created_at"] = self.created_at.isoformat()
        dict_return["updated_at"] = self.updated_at.isoformat()
        dict_return["__class__"] = self.__class__.__name__
            return dict_return

    def __str__(self):
        """a class that represent the string representation of the class name, id and dict keys and values"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
