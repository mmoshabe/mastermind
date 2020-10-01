import unittest
import mastermind
from unittest.mock import patch
from io import StringIO

from mastermind import check_correctness
# from unittest.mock import patch
# from io import StringIO
# import mastermind

class MyTestCase(unittest.TestCase):
    def test_create_code(self):
        '''test a Function that creates the 4 digit code, using random digits from 1 to 8'''
        for i in range(100):
            my_code = mastermind.create_code()
            for x in range(4):
                self.assertGreater(my_code[x],0)
                self.assertLess(my_code[x], 9)
            

    def test_check_correctness(self):
        """tests whether check_correctness checks correctness of answer 
        and show output to user"""
        self.assertEqual(check_correctness(8,1), False)
        self.assertEqual(check_correctness(0,4), True)
    
    
    @patch("sys.stdin", StringIO("012\n14h8\n5678"))
    def test_get_answer_input(self):
        """tests whether the user inputs the right input"""
        answer = mastermind.get_user_input()
        self.assertEqual(len(answer), 4)    
        # self.assertIsInstance(mastermind.get_user_input(),)
        self.assertTrue(answer.isnumeric())
    

    @patch("sys.stdin", StringIO("012\n14h8\n5678"))
    def test_take_turn(self):
        """tests whether the function take_turn return a right tuple""" 
        code = [1,2,3,4]
        self.assertIsInstance(mastermind.take_turn(code),tuple)


    # @patch("sys.stdin", StringIO("1234\n5678\n"))
    # def test_compare(self):
    #     self.assertEqual(get_answer_input(), 1234)
    #     self.assertEqual(get_answer_input(), 5678)
    #     self.assertIn()


if __name__ == '__main__':
   unittest.main()