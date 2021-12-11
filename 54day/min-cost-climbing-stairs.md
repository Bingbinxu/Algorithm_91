**方法**
动态规划
边界条件dp[0],dp[1]
dp[i]的状态只和dp[i-1]和dp[i-2]有关
**代码**
```C++
实现语言: C++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        const int N = cost.size();
        vector<int> dp(N);
        dp[0] = cost[0];
        dp[1] = cost[1];
        for (int i = 2; i < N; i++)
            dp[i] = cost[i] + min(dp[i-2], dp[i-1]);
        return min(dp[N-2], dp[N-1]);
    }
};
```
**复杂度分析**
时间复杂度: O(N)
空间复杂度: O(N)
