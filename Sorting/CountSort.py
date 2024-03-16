class Solution:
    #Function to arrange all letters of a string in lexicographical 
    #order using Counting Sort.

    # input = 'adcze' 
    # output = 'acdez'
    def countSort(self,arr):
        # code here
        n = len(arr);
        inputArray = list(arr);

        # create a count array
        countArray = [0 for i in range(26)]
        
        #iterate over the inputArray and fill the countArray 
        for c in inputArray:
            countArray[ord(c) - ord('a')] += 1
        
        #prefix of the countArray 
        for i in range(1, len(countArray)):
            countArray[i] = countArray[i] + countArray[i - 1]
            
        # next step is to iterate from the end over the input array 
        outputArray = ['a' for i in range(n)]
        for i in range(len(inputArray) - 1, -1, -1):
            outputArray[countArray[ord(inputArray[i]) - ord('a')] - 1] = inputArray[i]
            countArray[ord(inputArray[i]) - ord('a')] -= 1 
        
        return ''.join(outputArray);
