/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

//Solution 1 Recursion, checking left and right
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (p==NULL && q==NULL) return true;
        if (p==NULL || q==NULL) return false;
        if(p->val != q->val) return false;
        return (isSameTree(p->left,q->left) && isSameTree(p->right,q->right));
        }
};

// Soluton 2 Iteration, use queue to check
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<TreeNode*> queue;
        if(!p or !q) return p==q;
        queue.push(p);queue.push(q);
        while(!queue.empty()){
            TreeNode* left = queue.front();queue.pop();
            TreeNode* right = queue.front();queue.pop();
            if(left==NULL && right==NULL) continue;
            if(left==NULL || right==NULL) return false;
            if(left->val!=right->val) return false;
            queue.push(left->left); // p left
            queue.push(right->left);// q left
            queue.push(left->right);
            queue.push(right->right);
        }
        return true;
        }
};