**思路**
dfs+染色
**代码**
```C++
class Solution {
    vector<vector<int>> G;
    vector<int> colors;
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        G = vector<vector<int>>(n);
        for(const auto & d :dislikes)
        {
            G[d[0] - 1].push_back(d[1] - 1);
            G[d[1] - 1].push_back(d[0] - 1);
        }
        colors = vector<int>(n,0);
        for(int i = 0;i < n;i++)
        {
            if(colors[i] == 0 && !dfs(i, 1))
                return false;
        }
        return true;

    }
    bool dfs(int cur, int color)
    {
        colors[cur] = color;
        for(int next : G[cur])
        {
            if(colors[next] == color)
                return false;
            if(colors[next] == 0 && !dfs(next,-color)) //把未分组的利用-1进行检查是否有重复
                return false;
        }
        return true;
    }
};
```
**复杂度**
时间复杂度：O(V+E）V，E代表图的点和边的数目
空间复杂度：类似邻接表O(V+E)