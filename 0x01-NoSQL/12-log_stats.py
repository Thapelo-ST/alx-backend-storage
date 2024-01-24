#!/usr/bin/env python3
from pymongo import MongoClient
''' script that provides stats about local nginx logs in mongo db '''

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

methodCount = {
    method: collection.count_documents({"method": method})
    for method in methods
}
status_check_count = collection.count_documents(
 {"method": "GET", "path": "/status"})

print("{} logs".format(total_logs))
print("Methods:")
for method in methods:
    print("\tmethod {}: {}".format(method, methodCount[method]))
print("{} status check".format(status_check_count))
