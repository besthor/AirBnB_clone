#!/usr/bin/python3
""" module models """


from models.engine.file_storage import FileStorage

classes = {'BaseModel': 'BaseModel', 'Amenity': 'Amenity', 'State': 'State',
           'Place': 'Place', 'Review': 'Review', 'User': 'User'}
storage = FileStorage()
storage.reload()
