#!/usr/bin/python3
"""Defines the class FileStorage"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
        Serializes instances to a JSON file and deserializes Json file to
        istances
        Attribute:
        __file_path(string): path to JSON file
        __objects(dictionary): store objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionnary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file __file_path"""
        dic = FileStorage.__objects
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump({obj: dic[obj].to_dict() for obj in dic.keys()}, f)

    def reload(self):
        """deserializess the JSON file to __ojects"""
        try:
            with open(FileStorage.__file_path, encoding="utf-8") as f:
                dict_format = json.load(f)
                for obj in dict_format.values():
                    cls_name = obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
