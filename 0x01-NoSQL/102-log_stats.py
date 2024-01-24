#!/usr/bin/env python3
"""Script to provide stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient

def get_top_ips(collection, top_n=10):
    """Get the top N most present IPs in the collection."""
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": top_n}
    ]
    return list(collection.aggregate(pipeline))

''' main function '''


def main():
	''' main function core of the script '''
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {
	    method: collection.count_documents({"method": method})
	    for method in methods
	}

    status_check_count = collection.count_documents(
       {"method": "GET", "path": "/status"}
    )

    print("{} logs".format(total_logs))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method, method_counts[method]))
    print("{} status check".format(status_check_count))

    top_ips = get_top_ips(collection)
    print("\nIPs:")
    for index, ip_info in enumerate(top_ips, start=1):
        print("\t{}: {}".format(index, ip_info['_id'], ip_info['count']))


if __name__ == "__main__":
    main()

