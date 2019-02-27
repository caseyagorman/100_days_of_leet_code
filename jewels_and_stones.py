class Solution:
    def numJewelsInStones(self, J, S):
        output = 0
        for char in S:
            if char in J:
                output += 1
        return output
