# Run command: 
#       python3 -m unittest test_calc.py 
# To run the program.
# 
# After run the program, enter 2 number as the inputs
#
# At the end of the result, you should see: FAILED (failures=4)
import unittest
import calc

print("Please input 2 number.")

inp1 = int(input("The first number: "))
inp2 = int(input("The second number: "))

class TestCase(unittest.TestCase):
    #should fail
    def test_addition1(self):
        result = calc.addition(inp1,inp2) + 1
        self.assertEqual(result,inp1+inp2)
    #should pass
    def test_addition2(self):
        result = calc.addition(inp1,inp2)
        self.assertEqual(result,inp1+inp2)
    #should fail
    def test_subtraction1(self):
        result = calc.subtraction(inp1,inp2) + 1
        self.assertEqual(result,inp1-inp2)
    #should pass
    def test_subtraction2(self):
        result = calc.subtraction(inp1,inp2)
        self.assertEqual(result,inp1-inp2)
    #should fail
    def test_multiplication1(self):
        result = calc.multiplication(inp1,inp2) + 1
        self.assertEqual(result,inp1*inp2)
    #should pass
    def test_multiplication2(self):
        result = calc.multiplication(inp1,inp2)
        self.assertEqual(result,inp1*inp2)
    #should fail
    def test_division1(self):
        result = calc.division(inp1,inp2) + 1
        self.assertEqual(result,inp1/inp2)
    #should pass
    def test_division2(self):
        result = calc.division(inp1,inp2)
        self.assertEqual(result,inp1/inp2)
    

if __name__ == '__main__':unittest.main()
