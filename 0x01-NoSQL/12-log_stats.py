#!/usr/bin/env python3
from pymongo import MongoClient
''' script that provides stats about local nginx logs in mongo db '''

client = MongoClient('mongodb://127.0.0.1:27017')
db = client.logs
collection = db.nginx

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

method_counts = {method: collection.count_documents({ "method" : method})
			for method in methods}
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"    method {method}: {method_counts[method]}")
print(f"{status_check_count} status check")
