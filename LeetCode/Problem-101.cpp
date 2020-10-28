// Problem 101 - Symmetric Trees

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isMirrorImage(TreeNode *node1, TreeNode *node2) {
        if (node1 == nullptr && node2 == nullptr) return true;
        else if ((node1 == nullptr) || (node2 == nullptr)) return false;
        else {
            return node1->val == node2->val && isMirrorImage(node1->left, node2->right) && isMirrorImage(node1->right, node2->left);
        }
    }
    
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        return isMirrorImage(root->left, root->right);
    }
};
