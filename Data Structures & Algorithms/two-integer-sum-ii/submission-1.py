class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers)-1

        while l_ptr < r_ptr:
            sm = numbers[l_ptr] + numbers[r_ptr]
            if sm < target:
                l_ptr += 1
            elif sm > target:
                r_ptr -= 1
            else:
                return [l_ptr+1, r_ptr+1]
        return []