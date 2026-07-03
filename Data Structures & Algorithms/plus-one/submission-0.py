class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        else:
            carryover = 0
            i = len(digits) - 1

            while i >= 0:
                if carryover == 1:
                    digits[i] += 1
                    carryover = 0
                if digits[i] >= 10:
                    digits[i] -= 10
                    carryover = 1
                i -= 1
            
            if carryover == 1:
                digits.insert(0,1)
                
        return digits