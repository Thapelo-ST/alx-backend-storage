#!/usr/bin/env python3
''' listing schcools by topic '''


def schools_by_topic(mongo_collection, topic):
	'''
		all the schools will be listed for having a
		specific topic
	'''
	finder = mongo_collection.find({ 'topics' : topic })
	schools = list(finder)
	return schools
