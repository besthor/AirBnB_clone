#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
from models.engine.file_storage import FileStorage

"""A variable storage, an instance of FileStorage"""
storage = FileStorage()
storage.reload()
