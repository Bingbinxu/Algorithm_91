**方法**
在求得小岛数量的基础上增加计算面积的功能
**代码**
```C++
实现语言: C++
class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int maxx = 0;
        for(int i = 0;i < grid.size();i++){
            for(int j = 0; j< grid[0].size();j++)
            {
                maxx = max(maxx, getIslandarea(i,j,grid));
            }
        }
        return maxx;

    }
private:
    int getIslandarea(int i, int j, vector<vector<int>>& grid)
    {
        if(i < 0 || i >= grid.size() || j >= grid[0].size() || grid[i][j] == 0)
        {
            return 0;
        }（）
        grid[i][j] = 0; //已经访问的元素置为0，代表已经visited，访问过
        return 1 + getIslandarea(i - 1, j, grid)+getIslandarea(i + 1, j, grid)+getIslandarea(i, j + 1, grid)+getIslandarea(i, j - 1, grid);
    }
};
```
**复杂度分析**
时间复杂度: O(m*n)
空间复杂度: O(m*n)
