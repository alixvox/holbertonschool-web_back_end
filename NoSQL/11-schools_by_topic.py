#!/usr/bin/env python3
''' Lists docs of "school" that have specific topic '''


def schools_by_topic(mongo_collection, topic):
    ''' Lists docs of "school" that have specific topic '''
    return mongo_collection.find(
        {
            "topics": topic
        }
    )
