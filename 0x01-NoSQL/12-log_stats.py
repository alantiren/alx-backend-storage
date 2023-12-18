#!/usr/bin/env python3
'''Task 12's module.
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs.

    Args:
        nginx_collection (pymongo.collection.Collection): The MongoDB collection
            containing Nginx request logs.

    Returns:
        None
    '''
    print('{} logs'.format(nginx_collection.count_documents({})))

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, req_count))

    status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')

        print_nginx_request_logs(client.logs.nginx)

    except Exception as e:
        print(f"Error during MongoDB connection or query execution: {e}")


if __name__ == '__main__':
    run()
