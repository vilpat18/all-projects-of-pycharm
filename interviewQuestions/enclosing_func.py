def enclosing_func(msg):
    def printer():
        print(msg)
    printer()


enclosing_func('hello')

""" closure is function object that remembers 
    the values in enclosing scope even when
      its not present in the memory """


