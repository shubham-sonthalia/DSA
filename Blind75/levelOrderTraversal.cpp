

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> answer;
        queue<TreeNode*> queue; 
        if (!root){
            return answer;
        }
        queue.push(root);
        while (!queue.empty()){  
            vector<int> temp;
            int s = queue.size();
            for (int i = 0; i < s; i++){
                TreeNode* cur = queue.front();
                 if (cur->left != NULL){
                    queue.push(cur->left);
                }
                if (cur->right != NULL){
                    queue.push(cur->right);
                }
                temp.push_back(cur->val);
                queue.pop();
            }
            answer.push_back(temp);  
        }
        return answer;
    }
};
