class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        ptr = 0
        n = len(arr)
        # Check if 1 is present in array or not
        for i in range(n):
            if arr[i] == 1:
                ptr = 1
                break
    
        # If 1 is not present
        if ptr == 0:
            return 1
    
        # Changing values to 1
        for i in range(n):
            if arr[i] <= 0 or arr[i] > n:
                arr[i] = 1
    
        # Updating indices according to values
        for i in range(n):
            arr[(arr[i] - 1) % n] += n
    
        # Finding which index has value less than n
        for i in range(n):
            if arr[i] <= n:
                return i + 1
    
        # If array has values from 1 to n
        return n + 1
