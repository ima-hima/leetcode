class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        sortedNums = sorted(nums) # this will allow output list to be checkable
        length     = len(sortedNums)
        idx1  = 0
        final   = []
        finished = False

        while idx1 < length - 3: # Once it's at target there's no way to sum less than target
            a    = sortedNums[idx1] 
            idx2 = idx1 + 1
            finished = False
            for b in sortedNums[idx2:-2]:
                idx3 = idx2 + 1
                finished = False
                for c in sortedNums[idx3:-1]:
                    idx4 = idx3 + 1
                    finished = False
                    for d in sortedNums[idx4:]:
                        if a + b + c + d > target:
                            # print('a + b + c + d', a + b + c + d)
                            break
                        if a + b + c + d == target:
                            try: # this to initialize list
                                if [a, b, c, d] > final[-1]:
                                    final.append([a, b, c, d])
                            except:
                                final.append([a, b, c, d])
                        idx4 += 1
                    idx3 += 1
                idx2 += 1
            idx1 += 1
        return final
