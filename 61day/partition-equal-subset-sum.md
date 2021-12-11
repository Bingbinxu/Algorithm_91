**思路**
动态规划
**代码(C++)**
```C++
class Solution {
public:
    bool canPartition(vector<int>& nums) {
        int sum0 = accumulate(nums.begin(), nums.end(), 0);
        if (sum0 % 2 != 0) return false; // 总和是偶数才有可能分成两组       
        int sum = sum0 / 2;
        bool dp[sum + 1]; // dp[i]: 数组nums是子序列的和是否能达到i, 能就记作true, 否则false。 每新来一个数nums[i], 都有选或不选两种状态
        fill(dp, dp + sum + 1, false);
        dp[0] = true;
        for (auto& num : nums)
        {
            for (int j = sum; j >= 0; j--)
            {
                if (j >= num)
                    dp[j] = dp[j] || dp[j - num]; //该问题可转化为 [0, y-1] 中找到target=x 的子集，或者 [ 0 y-1] 中找到 target = x - num[y]，其中一个能找到则表明可以找到。函数关系为dp(x, y) = dp(x, y-1) || dp(x - num[y] , y-1)
            }            
        }
        return dp[sum];
    }
};
```
**复杂度分析**
时间复杂度：O(n*m) m = total_sum / 2
空间复杂度：O(n)