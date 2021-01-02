class A:
  def __init__(self):
      print("in it A")
  def _feature1(self):
      print("1 is working")

  def feature2(self):
      self._feature1()
      print("2 is working")

class B(A):
    def __init__(self):

        print("in it b")


    def feature1(self):
        super().feature2()
        super()._feature1()
        print("3 is working")
b1 = B()
b1.feature1()
