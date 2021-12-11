**方法**
将陆地加入队列，不断从上下左右四个方向扩展，并将满足条件的（距离大的）加入队列，持续直到队列为空
**代码**
```C++
实现语言: C++
class Solution {
    const int dx[4] = {0, 1, 0, -1};
    const int dy[4] = {1, 0, -1, 0};

public:
    int maxDistance(vector<vector<int>>& grid) {
        int N = grid.size();
        queue<pair<int,int>> q;
        vector<vector<int>> d(N, vector(N, 1000)); //二位数组初始化N×N,元素为1000的数组
        for(int i = 0;i < N;i++)
        {
            for(int j = 0;j < N;j++)
            {
                if(grid[i][j] == 1)
                {
                    q.push(make_pair(i,j));
                    d[i][j] = 0; //记录每个格子陆地距离海洋的距离                
                }
            }
        }
        while(!q.empty())
        {
            auto k = q.front();
            q.pop();
            for(int i = 0;i < 4;i++)
            {
                int newx = k.first + dx[i], newy = k.second + dy[i];
                if(newx < 0 || newx >= N || newy < 0 || newy >= N)
                {
                    continue;
                }
                if(d[newx][newy] > d[k.first][k.second] + 1)//新的都会加进去，旧的大的也会被小的值代替
                {
                    d[newx][newy] = d[k.first][k.second] + 1; //取出每个值的最小值
                    q.push(make_pair(newx, newy));
                }
            }
        }
        int res = -1;
        for(int i = 0;i < N;i++)
        {
            for(int j = 0;j < N;j++)
            {
                if(grid[i][j] == 0 && d[i][j] <= 200)
                {
                    res = max(res, d[i][j]);             
                }
            }
        }
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(n*n)
空间复杂度: O(n*n)
