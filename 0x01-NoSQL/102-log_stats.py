#!/usr/bin/env python3
'''102-log_stats.py
'''
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints statistics about Nginx request logs.'''
    print('{} logs'.format(nginx_collection.count_documents({})))

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, req_count))

    status_checks_count = nginx_collection.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_checks_count))


def print_top_ips(server_collection):
    '''Prints statistics about the top 10 HTTP IPs in a collection.'''
    print('Top IPs:')
    try:
        request_logs = server_collection.aggregate([
            {'$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}},
            {'$sort': {'totalRequests': -1}},
            {'$limit': 10},
        ])
        for request_log in request_logs:
            ip = request_log['_id']
            ip_requests_count = request_log['totalRequests']
            print('\t{}: {}'.format(ip, ip_requests_count))
    except Exception as e:
        print(f"Error while fetching top IPs: {e}")


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.'''
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')

        print_nginx_request_logs(client.logs.nginx)

        print_top_ips(client.logs.nginx)

    except Exception as e:
        print(f"Error during MongoDB connection or query execution: {e}")


if __name__ == '__main__':
    run()
