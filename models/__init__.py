#!/usr/bin/python3
"""This package provides various modules for creating the console
   for the Airbnb clone project
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
