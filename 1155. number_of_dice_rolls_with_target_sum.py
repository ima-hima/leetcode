class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if target < d or target > d * f:
            return 0

        return self.numRollsToTarget(d-1, f, target-1) % 1000000007


dice, sides, target
1,2,1: 1 all 1s
1,2,2: 1 all 2s

2,2,2: 1 all 1s
2,2,3: 2 1,2; 2,1
2,2,4: 1 all 2s

3,2,3: 1 all 1s
3,2,4: 3 1,2,1; 1,1,2; 2,1,1
3,2,5: 3 1,2,2; 2,1,2; 2,2,1
3,2,6: 1 all 2s

1,3,1: 1 all 1s
1,3,2: 1 all 2s
1,3,3: 1 all 3s

2,3,3: 1 all 1s
2,3,4: 3 1,3; 3,1; 2,2
2,3,5: 2 2,3; 3,2;
2,3,6: 1 all 2s

3,3,3: 1 all 1s
3,3,4: 3 1,1,2; 1,2,1; 2,1,1
3,3,5: 6 1,1,3; 1,3,1; 3,1,1; 1,2,2; 2,1,2; 2,2,1
3,3,6: 1,1,
3,3,7:
3,3,8:
3,3,9: all 3s

