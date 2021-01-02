

def makedecor1(f1):
    def inner():
        print("chandni chowk to china")
        f1()
    return inner

def makedecor2(f2):
    def inner1():
        print("khiladi 786")
        f2()
    return inner1

@makedecor2
@makedecor1
def akshaykumar():
    print("akshay kumar's flop movies list")

akshaykumar()