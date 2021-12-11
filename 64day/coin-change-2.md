**思路**
这个题属于背包问题的类似问题, 每种面值的硬币都有选或不选两种选择。
顺着题目的要求定义dp数组:dp[i] = Σ dp[i - coin[i]] (coin[i] ∈ coins)
**代码(C++)**
```C++
class Solution {
public:
    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount +1);
        dp[0] = 1;
        for(int& coin : coins)
        {
            for(int i = coin ; i <= amount; i++)
            {
                dp[i] = dp[i-coin] + dp[i];
            }
        }
        return dp[amount];
    }
};
```
**复杂度分析**
时间复杂度：O(n*m)
空间复杂度：O(m)