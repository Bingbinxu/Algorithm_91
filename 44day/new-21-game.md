**思路**
 滑动窗口+动态规划，动规不熟
**代码**
```C++
class Solution {
public:
    double new21Game(int n, int k, int maxPts) {
        if (k == 0) {
            return 1.0;
        }
        vector<double> dp(k + maxPts);
        for (int i = k; i <= n && i < k + maxPts; i++) {
            dp[i] = 1.0;
        }
        dp[k - 1] = 1.0 * min(n - k + 1, maxPts) / maxPts;
        for (int i = k - 2; i >= 0; i--) {
            dp[i] = dp[i + 1] - (dp[i + maxPts + 1] - dp[i + 1]) / maxPts;
        }
        return dp[0];
    }
};
```
**复杂度**
时间复杂度：O(min(n, k+w))
空间复杂度：O(k+w)
