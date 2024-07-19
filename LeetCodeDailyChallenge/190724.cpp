class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> answer; 
        
        int n = matrix.size();
        int m = matrix[0].size();

        vector<int> minRows;
        for (int i = 0; i < n ; i++){
            int mini = INT_MAX;
            for (int j = 0; j < m; j++){
                if (matrix[i][j] < mini){
                    mini = matrix[i][j];
                }
            }
            minRows.push_back(mini);
        }

        vector<int> maxCols;
        for(int j = 0; j < m; j++){
            int maxi = INT_MIN;
            for(int i = 0; i < n; i++){
                if (matrix[i][j] > maxi){
                    maxi = matrix[i][j];
                }
            }
            maxCols.push_back(maxi);
        }

        for(int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (matrix[i][j] == minRows[i] && matrix[i][j] == maxCols[j]){
                    answer.push_back(matrix[i][j]);
                }
            }
        }
        return answer;
    }
};
