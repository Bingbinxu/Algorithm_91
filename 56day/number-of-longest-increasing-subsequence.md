**方法**
动态规划
转移方程，需要考察dp(j)，0 <= j <= i-1
如果 nums[i] > nums[j]，
如果长度增加,dp[j].first + 1 > dp[i].first更新dp(i)和计数 
如果长度相等,dp[i].first == dp[j].first + 1，累加计数
如果 nums[i] ≤ nums[j]，不能组成上升子序列，跳过

**代码**
```C++
实现语言: C++
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int N = nums.size();
        int res = 0;
        int maxLen = 0;
        vector<pair<int, int>> dp(N, {1, 1}); /* dp[i]: pair of { length, 以 nums[i] 结尾的LIS(最长上升子序列)的个数 } */
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[i] > nums[j])
                {
                    if (dp[i].first == dp[j].first + 1)
                        dp[i].second += dp[j].second;
                    if (dp[j].first + 1 > dp[i].first)
                        dp[i] = {dp[j].first + 1, dp[j].second};
                }
            }
            if (maxLen == dp[i].first) res += dp[i].second;
            if (maxLen < dp[i].first)
            {
                maxLen = dp[i].first;
                res = dp[i].second;
            }
        }
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(N*N)
空间复杂度: O(N)
