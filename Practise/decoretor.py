def makedecor(f1):
    def inner():
        print("he maintains proper diet")
        f1()

    return inner


def makedecor1(f2):
    def inside():
        print("he drinks 2ltrs of cow milk daily")
        f2()

    return inside


def makedecor2(f3):
    def inner1():
        print("recently he joined abko english academy")
        f3()

    return inner1


def makedecor3(f4):
    def inner2():
        print("now days he speaks better english")
        f4()

    return inner2


def makedecor4(f5):
    def inner3():
        print("i am sure he must have cracked the inerview")
        f5()

    return inner3


def makedecor5(f6):
    def inner4():
        print("he used to play videogames in childhood")
        f6()

    return inner4


@makedecor5
@makedecor4
@makedecor3
@makedecor2
@makedecor1
@makedecor
def harshal():
    print("harsh is body builder")


harshal()

