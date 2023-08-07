#!/usr/bin/python3
"""This module defines the class BaseModel"""
import uuid
import datetime


class BaseModel:
    """This class defines all common attributes/methods for other classes:
       Attributes:
          id: string
          created_at: datetime
          updated_at: datetime
    """
    def __init__(self, *args, **kwargs):
        """initializes attrinutes of the class
            Attributes:
                args: arguments
                kwargs: arguments for the constructor of a BaseModel
        """
        print('kwargs -------------------------------------')
        if kwargs is not None and len(kwargs) != 0:
            print("not empty")
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        date = datetime.datetime.fromisoformat(value)
                        self.__dict__[key] = date
                    else:
                        self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id,
                                     self.__dict__)

    def save(self):
        """Updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        string = self.__dict__.copy()
        string['__class__'] = self.__class__.__name__
        string['created_at'] = self.created_at.isoformat()
        string['updated_at'] = self.updated_at.isoformat()
        return string
