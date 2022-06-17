class Solution {
public:
    bool ans = true;
    int check(TreeNode* root){
        if (!root) return 0;
        int left = check(root->left);
        int right = check(root->right);
        if (abs(left-right)>1){
            ans = false;
        }
        return 1+max(left,right);
    }
    bool isBalanced(TreeNode* root) {
        check(root);
        return ans;
    }

};