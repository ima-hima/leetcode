import unittest
import random


def solution(A):
    if len(A) == 0:
        return 1
    if len(A) == 1:
        if A[0] <= 0:
            return 1
        if A[0] == 1:
            return 2
        return 1

    new_A = sorted(A)
    if new_A[0] <= 0:
        if new_A[-1] <= 0:
            # entire list < 0
            return 1
    
    i = 0
    while new_A[i] <= 0:
        i += 1
    current = 1
    for value in new_A[i:]:
        # print(current, value)
        if value > current + 1:
            return current + 1
        current = value
    return new_A[-1] + 1



class Test_missing_int(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(solution([]), 1)

    def test_not_in_list(self):
        self.assertEqual(solution([1, 1, 3, 2, 3, 2]), 4)

    def test_all_negative(self):
        self.assertEqual(solution([-1, -1, -3, -2, -3, -1]), 1)

    def test_single_less_than_zero(self):
        self.assertEqual(solution([-10000]), 1)

    def test_single_equal_zero(self):
        self.assertEqual(solution([0]), 1)

    def test_single_equal_one(self):
        self.assertEqual(solution([1]), 2)

    def test_single_greater_one(self):
        self.assertEqual(solution([2]), 1)

    def test_their_input_all_ones(self):
        self.assertEqual(solution([1, 1, 1, 1, 1]), 2)

    def test_their_input_all_twos(self):
        self.assertTrue(solution([2, 2, 2, 2, 2]), 1)



unittest.main()

