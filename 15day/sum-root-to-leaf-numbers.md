**思路**
BFS:用队列保存每一层，遍历每一层，将×10的值存储在下一层节点里
DFS:深度搜索，每一条持续向下，直到不存在子节点，然后递归×10
**代码**
```C++
DFS：
class Solution {
public:
    int sum = 0;
    int sumNumbers(TreeNode* root) {
        dfs(root, 0);
        return sum;
    }
    void dfs(TreeNode* root, int num){
        if(!root) return;
        if(!root->left && !root->right)
        {
            sum += num * 10 + root->val;
            return;
        }
        dfs(root->left, num * 10 + root->val);
        dfs(root->right, num * 10 + root->val);
    }
};
BFS：
class Solution {
public:
    int sumNumbers(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> qt;
        qt.push(root);

        int sum = 0;

        while (!qt.empty()) {
            int size = qt.size();
            while (size--) {
                TreeNode* node = qt.front();
                qt.pop();

                if (node->left) {
                    node->left->val += 10 * node->val;
                    qt.push(node->left);
                }

                if (node->right) {
                    node->right->val += 10 * node->val;
                    qt.push(node->right);
                }

                if (!node->left && !node->right) { // leaf node
                    sum += node->val;
                }
            }
        }

        return sum;
    }
};
```
**复杂度**
DFS：
时间复杂度：遍历所有节点O（N）
空间复杂度：O（h），需要树的高度指针
BFS：
时间复杂度：遍历所有节点O（N）
空间复杂度：O（q），最坏的是满二叉树，与n同阶