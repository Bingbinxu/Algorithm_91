**思路**
先构建一大顶堆，然后取出k小元素
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    int kthSmallest(vector<vector<int>>& M, int k) {
        priority_queue<int, vector<int>, greater<int>> q;
        int res;        
        const int rows = M.size();
        const int cols = M.front().size(); /* 题意: n == matrix.length == matrix[i].length >= 1 */
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                q.push(M[i][j]);
            }
        }
        while (!q.empty() && k - 1 > 0)  // 所求数的index 为k-1
        {
            q.pop();
            k--;
        }
        res = q.empty() ? -1 : q.top();
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
