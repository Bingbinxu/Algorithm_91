**方法**
dfs 参考一同学
**代码**
```C++
实现语言: C++
class Solution {
    int res = 0;
    unordered_set<int> colSet;  /* 竖线|中是否出现index 相等 */
    unordered_set<int> diffSet; /* \ 对角线(捺): 差相等 */
    unordered_set<int> sumSet;  /* / 对角线(撇): 和相等 */
public:
	int totalNQueens(int n) {
        // corner case
        if (n <= 0) return res;
        dfs(0, n);
        return res;
    }
    void dfs(int row, int n) /* n: N皇后的N, 对应几行几列的棋盘 */
    {
        if (row == n)
        {
            res++;
            return;
        }
        // row 不能相等
        for (int i = 0; i < n; i++)
        {
            if (!colSet.count(i) && !diffSet.count(row - i) && !sumSet.count(row + i))
            {
                colSet.insert(i);
                diffSet.insert(row - i);
                sumSet.insert(row + i);
                dfs(row + 1, n);

                // 开始回溯
                colSet.erase(i);
                diffSet.erase(row - i);
                sumSet.erase(row + i);
            }
        }
    }
};
```
复杂度分析:
时间复杂度: O(N!)
空间复杂度: O(N)

自己做的：
class Solution {
public:
    int totalNQueens(int n) {
        set<int> cols;
        set<int> piediagonal;
        set<int> nadiagonal;
        
        return backtrack(n, 0, cols, piediagonal, nadiagonal);
    }
    
private:
     int backtrack(int n, int row, set<int> cols, set<int> piediagonal, set<int> nadiagonal){
        if(row == n){
            return 1;
        }
        
        int count = 0;
        for(int i = 0; i < n; i++){ // iterate each column
            if(cols.count(i)){
                continue;
            }
            
            if(piediagonal.count(row - i)){ // 撇做差diagonal from left top to right bottom
                continue;
            }
            
            if(nadiagonal.count(row + i)){ // 捺做和 diagonal from right top to left bottom
                continue;
            }
            
            cols.insert(i);
            piediagonal.insert(row - i);
            nadiagonal.insert(row + i);
            count += backtrack(n, row + 1, cols, piediagonal, nadiagonal);
            //回溯算法，重新选定i后计算所有可能性
            cols.erase(i);
            piediagonal.erase(row - i);
            nadiagonal.erase(row + i);
        }
        return count;
    }
};