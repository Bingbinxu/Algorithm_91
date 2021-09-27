**思路**
找到最小的迭代公式，给出递归推出的条件
**代码**
```C++
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if(!root) return 0;
        int left = maxDepth(root->left);
        int right = maxDepth(root->right);
        return max(left,right)+1;
    }
};
```
**复杂度**
时间复杂度：遍历所有节点O（N）
空间复杂度：O（1）