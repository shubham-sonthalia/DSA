class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        
        int* prefixProduct = new int[n];
        prefixProduct[0] = nums[0];
        for(int i = 1; i < n; i++){
            prefixProduct[i] = prefixProduct[i - 1]*nums[i];
        }
        
        int* suffixProduct = new int[n];
        suffixProduct[n - 1] = nums[n - 1];
        for(int i = n - 2; i > -1; i--){
            suffixProduct[i] = suffixProduct[i + 1]*nums[i];
        }
        // 1 2 6 24
        // 24  24  12  4 

        // answer[0] = suffixProduct[i + 1]
        // answer[1] = suffixProduct[2]* prefixProduct[0]
        // answer[2] = suffixProduct[3]*prefixProduct[1]
        // answer[3] = prefixProduct[2]
        vector<int> answer;
        for(int i = 0; i < n; i++){
            if (i == 0){
                answer.push_back(suffixProduct[1]);
            }
            else if (i == n - 1){
                answer.push_back(prefixProduct[n - 2]);
            }
            else{
                answer.push_back(suffixProduct[i + 1]*prefixProduct[i - 1]);
            }
        }
        return answer;
    }
};
