**思路**
这个题属于背包问题的类似问题, 每种面值的硬币都有选或不选两种选择。
顺着题目的要求定义dp数组:dp[i] = Σ dp[i - coin[i]] (coin[i] ∈ coins)
**代码(C++)**
```C++
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount +1,amount+1); //最大值设为所有面值为1的相加再加一
        dp[0] = 0;
        for(int& coin : coins)
        {
            for(int i = coin ; i <= amount; i++)
            {
                dp[i] = min(dp[i-coin] + 1,dp[i]);
            }
        }
        return dp[amount] == amount+1? -1:dp[amount];
    }
};
```
**复杂度分析**
时间复杂度：O(n*m)
空间复杂度：O(m)