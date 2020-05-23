import unittest
from AddBinary import Solution


class RemoveDuplicatesfromSortedArrayTest(unittest.TestCase):
    def test_basic_function(self):
        temp = Solution()
        self.input = "11"
        self.input2 = "1"
        self.assertEqual(temp.addBinary(self.input,self.input2), "100")

if __name__ == "__main__":
    unittest.main()
