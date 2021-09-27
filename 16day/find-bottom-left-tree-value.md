**思路**
BFS广度优先遍历
遍历每一层，将每一层依次入队，然后遍历弹出，直到队列为空
**代码**
```C++
class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        queue<TreeNode*> q;
        TreeNode* s = nullptr;
        q.push(root);
        while(!q.empty())
        {
            s = q.front();
            int size = q.size();
            while(size--){
                TreeNode* cur =q.front();
                q.pop();
                if(cur->left)
                q.push(cur->left);
                if(cur->right)
                q.push(cur->right);
            }
        }
        return s->val;
    }
};
```
**复杂度**
时间复杂度：遍历所有节点O（N）
空间复杂度：最差情况O（N），最好情况树的高度O（h）