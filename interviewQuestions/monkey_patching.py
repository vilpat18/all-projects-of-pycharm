class Test:
    def exsiting_code(self):
        print('this is class method')


obj = Test()
# obj.exsiting_code()


def monkey_function():
    print('this is monkey function')


obj.exsiting_code = monkey_function
monkey_function()




