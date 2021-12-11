**思路**
动态规划

**代码(C++)**

```C++
class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        int sum = 0;
        for (int& num : nums) sum += num;
        int diff = sum - target;
        if (diff < 0 || diff % 2 != 0) return 0;
        int neg = diff / 2;
        vector<int> dp(neg + 1);
        dp[0] = 1;
        for (int& num : nums) {
            for (int j = neg; j >= num; j--) dp[j] += dp[j - num];
        }
        return dp[neg];
    }
};
```
**复杂度分析**
时间复杂度：O(N^2)
空间复杂度：O(N)