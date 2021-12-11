**方法**
不连续的动态规划
**代码**
```C++
实现语言: C++
class Solution {
    double f[25][25][101]; /* dp[i][j][k]: 跳k 步后到达格子(i,j), 此时继续按"日"字向前跳, 跳到大K步时留在棋盘上的概率之和(走法的总概率)。 */
public:
    double knightProbability(int N, int K, int r, int c) {
        memset(f, 0.0, sizeof(f));
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                f[i][j][K] = 1; /* 预处理边界 */
        int dx[] = {-2,-1,1,2,2,1,-1,-2}; /* 8组方向向量 */
        int dy[] = {1,2,2,1,-1,-2,-2,-1};
        for (int k = K - 1; k >= 0; k--)
            for (int i = 0; i < N; i++)
                for (int j = 0; j < N; j++)
                    for (int u = 0; u < 8; u++) /* 枚举8个方向, 累加其中合法方向的概率 */
                    {
                        int x = i + dx[u], y = j + dy[u];
                        if (x >= 0 && x < N && y >= 0 && y < N)
                            f[i][j][k] += f[x][y][k+1] / 8;                        
                    }        
        return f[r][c][0];
    }
};
```
**复杂度分析**
时间复杂度: O(K×N×N)
空间复杂度: O(N×N)
