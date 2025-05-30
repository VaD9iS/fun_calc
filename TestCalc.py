import unittest
import calc

class CalcTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("SetUpClass")
        print("==============")


    @classmethod
    def tearDownClass(cls):
        print("TearDownClass")
        print("==================")

# на курсах сказали что на версии 3.13 Python не срабатывает, пришлось закомментировать 
    # def setUp(self):
    #     print("Set up for [" + self.shortDescription() + "]")
    #
    # def setDown(self):
    #     print("Set down dor [" + self.shortDescription() + "]")

    def test_abb(self):
        print("id: " + self.id())
        self.assertEqual(calc.add(1,2), 3)

    def test_sub(self):
        print("id: " + self.id())
        self.assertEqual(calc.sub(4, 2), 2)

    def test_mul(self):
        print("id: " + self.id())
        self.assertEqual(calc.mul(2, 5), 10)

    def test_dev(self):
        print("id: " + self.id())
        self.assertEqual(calc.div(10, 2), 5)


if __name__ == '__main__':
    unittest.main