#!/usr/bin/python

def a(callback):
    callback('hello')

def b(msg):
    print(msg)

a(callback=b)
