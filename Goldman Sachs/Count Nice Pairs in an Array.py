class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        ''' Time Complexity: O(n ^ 2)
        
        rev_nums_hashMap = {}
        for num in nums:
            num_string = str(num)
            rev_num_string = num_string[::-1]
            rev_num = int(rev_num_string)
            rev_nums_hashMap[num] = rev_num
        
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] + rev_nums_hashMap[nums[j]]) == (nums[j] + rev_nums_hashMap[nums[i]]):
                    count += 1
        
        return count
        '''

        hash_map = {}
        for num in nums:
            num_string = str(num)
            rev_num_string = num_string[::-1]
            rev_num = int(rev_num_string)
            
            if (num - rev_num) in hash_map:
                hash_map[num - rev_num] += 1
            else:
                hash_map[num - rev_num] = 1

        count = 0
        for x in hash_map:
            count += (hash_map[x] * (hash_map[x] - 1)) // 2

        return count