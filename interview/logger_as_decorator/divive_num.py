from logger_as_decorator import log1

@log1.main()
def divide(num1, num2):
    return num1 / num2


if __name__ == '__main__':
    result = divide(10, 0)
    print(result)