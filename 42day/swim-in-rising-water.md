**思路**
 二分法+DFS搜索，设置搜索边界条件
**代码**
```C++
class Solution {
public:
    bool dfs(int mid, int x, int y, set<pair<int, int>>& visited, vector<vector<int>>& grid) {
        if (x > grid.size() - 1 || x < 0 || y > grid[0].size() - 1 || y < 0) return false;
        if (grid[x][y] > mid) return false;
        if (x == grid.size() - 1 && y == grid[0].size() - 1) return true;
        if (visited.count({x, y})) return false;
        visited.insert({x, y});
        bool res = dfs(mid, x + 1, y, visited, grid) || dfs(mid, x - 1, y, visited, grid) || dfs(mid, x, y + 1, visited, grid) || dfs(mid, x, y - 1, visited, grid);
        return res;
    }
    
    int swimInWater(vector<vector<int>>& grid) {
        int l = 0;
        int r = INT_MIN;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[i].size(); j++) r = max(r, grid[i][j]);
        }
        set<pair<int, int>> visited;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (dfs(mid, 0, 0, visited, grid)) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
            visited.clear();
        }
        return l;
    }
};
```
**复杂度**
时间复杂度：二分次数O(NlogM)
空间复杂度：O(N)
