class MyLib:
    def __init__(self):
        print 'init is called'

    def __helper(self):
        print 'private helper'

    def f(self):
        print 'f'
        self.__helper()
