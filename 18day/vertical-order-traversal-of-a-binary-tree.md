**思路**
官方思路：先将所有的按先（x,y,v）存储，然后先对x排序，再对y排序，最后对值排序
**代码**
```C++
class Solution {
public:
    struct node{
            int val;
            int x;
            int y;
            node(int v, int X, int Y):val(v),x(X),y(Y){};
        };
    static bool cmp(node a, node b)
    {
        if(a.x^b.x)
        {
            return a.x < b.x;
        }
        if(a.y^b.y)
        {
            return a.y<b.y;
        }
        return a.val<b.val;
    }
    vector<node> a;
    int min=1000, max=-1000;
    vector<vector<int>> verticalTraversal(TreeNode* root) {
    
    dfs(root,0,0);
    sort(a.begin(),a.end(),cmp);
        vector<vector<int>>ans(max-min+1);
        for(auto xx:a)
        {
            ans[xx.x-min].push_back(xx.val);
        }
        return ans;
    }
    void dfs(TreeNode* root,int x,int y)
    {
        if(root==nullptr)
            return;
        if(x<min)
            min=x;
        if(x>max)
            max=x;
        a.push_back(node(root->val,x,y));
        dfs(root->left,x-1,y+1);
        dfs(root->right,x+1,y+1);
    }
};
```
**复杂度**
时间复杂度：排序算法O（NlogN）
空间复杂度：存储所有的节点O（N）