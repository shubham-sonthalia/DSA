// https://leetcode.com/problems/same-tree/

class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if ((!p && q) || (p && !q)){
            return false;
        }
        if (!p && !q){
            return true;
        }
        if (p->val == q-> val){
            return isSameTree(p->left, q-> left) && isSameTree(p->right, q ->right);
        }
        return false;
    }
};
