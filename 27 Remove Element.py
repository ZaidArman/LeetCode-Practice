class Solution(object):
    def removeElement(self, nums, val):
        # Initialize a variable to keep track of valid elements
        k = 0
        # Iterate through the indices of the 'nums' list
        for i in range(len(nums)):
            # Check if the current element is not equal to 'val'
            if nums[i] != val:
                # If the element is not 'val', copy it to position 'k'
                nums[k] = nums[i]
                # Increment the 'k' variable to track the number of valid elements
        
        # Return the new length of the list with 'val' removed
        return k
