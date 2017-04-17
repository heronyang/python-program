#!/usr/bin/python

while True:
    try:
        s = raw_input('> ')
        print '>>' + s
    except(EOFError):
        print 'bye'
        break
