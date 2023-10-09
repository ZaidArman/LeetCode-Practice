class Solution(object):
    def removeDuplicates(self, nums):
        # Check if the input list is empty
        if not nums:
            return 0  # If empty, return 0 as there are no duplicates to remove
        
        # Initialize a variable 'k' to keep track of the length of the modified array
        k = 1  # Start with 1 because the first element is always unique
        
        # Iterate through the 'nums' list starting from the second element (index 1)
        for i in range(1, len(nums)):
            # Compare the current element with the previous element
            if nums[i] != nums[i - 1]:
                # If the current element is unique, move it to position 'k'
                nums[k] = nums[i]  # Update the 'k'th position with the unique element
                k += 1  # Increment 'k' to keep track of the length of the modified array
        
        # 'k' now represents the length of the modified array
        return k
