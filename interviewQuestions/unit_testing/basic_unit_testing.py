import unittest

class TestCaseSample(unittest.TestCase):
    def setUp(self):
        print('this is setup the environment')

    def test_method(self):
        print('this is test case')
        print(10/2)
        print(10 * 100)
        print(100/0)


    def tearDown(self):
        print('clear the test cases')


unittest.main()