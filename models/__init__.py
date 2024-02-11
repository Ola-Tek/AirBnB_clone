#!/usr/bin/python3
""" a script showing the magic methods for models directory """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
