# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

import unittest

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            # need to reinsert
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            for first_key in self.cache.keys():
                del self.cache[first_key]
                break


class TestLRUCache(unittest.TestCase):

    # this is actually already covered in their example.
    def test_does_get_update_cache(self):
        soln = LRUCache(2)

        args = [ [1,1],
                 [2,2],
                 [1],   # I accessed 1, so now 2 is oldest value
                 [3,3], # Should bump 2.
                 [2],   # should return -1
                 [1]    # should return 1
               ]

        functions = [ "put",
                      "put",
                      "get",
                      "put",
                      "get",
                      "get"
                    ]
        outputs = [None,None,1,None,-1,1]
        inputs = [getattr(soln, functions[i])(*args[i]) for i in range(len(functions))]
        self.assertEqual(inputs, outputs)

# this is actually already covered in their example.
    def test_does_put_update_cache(self):
        soln = LRUCache(2)

        args = [ [1,1],
                 [2,2],
                 [1],   # I accessed 1, so now 2 is oldest value
                 [2,1], # Now 1 is oldest.
                 [3,3], # bump 1
                 [2],   # should return 1
                 [1]    # should return -1
               ]

        functions = [ "put",
                      "put",
                      "get",
                      "put",
                      "put",
                      "get",
                      "get"
                    ]
        outputs = [None,None,1,None,None,1,-1]
        inputs = [getattr(soln, functions[i])(*args[i]) for i in range(len(functions))]
        self.assertEqual(inputs, outputs)


    def test_their_test(self):
        soln = LRUCache(2)

        args = [ [1,1],
                 [2,2],
                 [1],   # I accessed 1, so now 2 is oldest value
                 [3,3], # bump 2
                 [2],   # -1
                 [4,4],
                 [1],
                 [3],
                 [4],
               ]

        functions = [ "put",
                      "put",
                      "get",
                      "put",
                      "get",
                      "put",
                      "get",
                      "get",
                      "get",
                    ]
        outputs = [None,None,1,None,-1,None,-1,3,4]
        inputs = [getattr(soln, functions[i])(*args[i]) for i in range(len(functions))]
        self.assertEqual(inputs, outputs)


unittest.main()
