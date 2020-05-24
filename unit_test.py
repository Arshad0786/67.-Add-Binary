import unittest
from AddBinary import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = "11"
        self.input2 = "1"
        self.assertEqual(temp.addBinary(self.input,self.input2), "100")

    def test_basic_function2(self):
        temp = Solution()
        self.input = "1010"
        self.input2 = "1011"
        self.assertEqual(temp.addBinary(self.input,self.input2), "10101")

    def test_basic_function3(self):
        temp = Solution()
        self.input = "111111"
        self.input2 = "111111"
        self.assertEqual(temp.addBinary(self.input,self.input2), "1111110")

    def test_long_carry(self):
        temp = Solution()
        self.input = "1111111111111111111"
        self.input2 = "1"
        self.assertEqual(temp.addBinary(self.input,self.input2), "10000000000000000000")



if __name__ == "__main__":
    unittest.main()
