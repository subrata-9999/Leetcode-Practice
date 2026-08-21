class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        list1 = []
        list2 = []
        list3 = []
        list1.append(nums[0])
        list2.append(nums[1])
        
        for i in range(2, len(nums)):
            if list1[len(list1)-1] > list2[len(list2) - 1]:
                list1.append(nums[i])
            else:
                list2.append(nums[i])
        

        
        return list1 + list2


        