import unittest
from typing import List

class Solution:
    def countAndSay(self, n: int) -> str:
        # n is guaranteed to be > 0 and < 30
        if n < 2:
            return '1'
        input_str = '1'
        output_str = ''
        for loop_idx in range(n-1):
            output_str = ''
            # print(loop_idx, input_str)
            # print(loop_idx, output_str)
            count = 0
            cur_char = input_str[0]
            for input_idx in range(len(input_str)):
                # print(output_str)
                if input_str[input_idx] == cur_char:
                    count += 1
                # if input_idx == len(input_str) - 1:
                #     output_str += str(count) + cur_char

                else:
                    # print('cur_char', input_idx, input_str[input_idx], cur_char)
                    output_str += str(count) + cur_char

                    cur_char = input_str[input_idx]
                    count = 1 
                # print(output_str)
            output_str += str(count) + cur_char
                # print(output_str)
            input_str = output_str
            # print(output_str)
        return output_str
        


class TestSubstring(unittest.TestCase):

    def test_one(self):
       soln = Solution()
       self.assertEqual(soln.countAndSay(1), '1')

    def test_two(self):
       soln = Solution()
       self.assertEqual(soln.countAndSay(2), '11')

    def test_three(self):
       soln = Solution()    
       self.assertEqual(soln.countAndSay(3), '21')


unittest.main()
