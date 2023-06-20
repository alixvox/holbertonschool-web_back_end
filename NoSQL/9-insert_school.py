#!/usr/bin/env python3
''' Inserts document in collection based on kwargs '''


def insert_school(mongo_collection, **kwargs):
    ''' Inserts document in collection based on kwargs '''
    return mongo_collection.insert_one(kwargs).inserted_id
