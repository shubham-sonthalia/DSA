class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        map<int, int> freq; 
        for(int i = 0; i < nums.size(); i++){
            if (freq.find(nums[i]) != freq.end()){
                return true;
            }
            freq[nums[i]] = 1; 
        }
        return false;
        
    }
};
