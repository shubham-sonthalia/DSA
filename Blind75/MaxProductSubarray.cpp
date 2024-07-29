class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size(); 
        int maxi = nums[0]; 
        int prod = 1; 
        for(int i = 0; i < n; i++){
            prod *= nums[i];
            if (prod > maxi){
                maxi = prod;
            }
            if (prod == 0){
                prod = 1;
            }
        }
        prod = 1; 
        for(int i = n - 1; i >= 0; i--){
            prod *= nums[i];
            if (prod > maxi){
                maxi = prod;
            }
            if (prod == 0){
                prod = 1;
            }
        }
        return maxi;
    }
};


class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size(); 
        int maxi = 1; 
        int mini = 1; 
        int ans = nums[0]; 
        for(int i = 0; i < n; i++){
            if (nums[i] == 0){
                mini = 1; 
                maxi = 1; 
                ans = max(ans, 0);
                continue;
            }
            int temp = mini; 
            mini = min(min(nums[i]*mini, nums[i]*maxi), nums[i]);
            maxi = max(max(nums[i]*maxi, nums[i]*temp), nums[i]);
            ans = max(maxi, ans);
        }
        return ans;     
    }
};
