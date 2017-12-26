#!/usr/bin/env python

users = [
    { 'admin': True, 'active': True, 'name': 'Kevin' },
    { 'admin': True, 'active': False, 'name': 'Elisabeth' },
    { 'admin': False, 'active': True, 'name': 'Josh' },
    { 'admin': False, 'active': False, 'name': 'Kim' },
]

line = 0
for user in users:
    line += 1
    if user["active"] and user["admin"]:
        print("%s ACTIVE - (ADMIN) %s" % (line, user["name"]))
    elif user["active"]:
        print("%s ACTIVE - %s" % (line, user["name"]))
    elif user["admin"]:
        print("%s (ADMIN) %s" % (line, user["name"]))
    else:
        print("%s %s" % (line, user["name"]))

