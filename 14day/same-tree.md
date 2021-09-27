**思路**
找到最小的迭代公式，给出递归推出的条件
判断根节点，然后依次左右节点进行迭代
**代码**
```C++
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p==nullptr && q==nullptr) return true;
        if(p==nullptr || q==nullptr) return false;
        if(p->val != q->val) return false;
        return isSameTree(p->right,q->right) && isSameTree(p->left,q->left);

    }
};
```
**复杂度**
时间复杂度：遍历所有节点O（N）
空间复杂度：O（h），需要树的高度指针