class A:
    def feature1(self):
        print("1 is working")
    def feature2(self):
        print("2 is working")

class B(A):
    def feature3(self):
        print("3 is working")

    def feature4(self):
        print("4 is working")
class C(B):
    def feature5(self):
        print("1 is working")

    def feature6(self):
        print("2 is working")

a1 = A()
b1 = B()
b1.feature3()
a1.feature1()
a1.feature2()
c1 = C()
c1.feature1()
