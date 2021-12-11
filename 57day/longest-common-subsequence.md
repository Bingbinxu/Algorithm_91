**方法**
对每个text1计算text2中的数量，迭代text1.相当于不论从哪个位置找都可以
动态规划，建立在每个dp前的基础上，要么相等后加一，要么取最大值
**代码**
```C++
实现语言: C++
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1,vector<int>(text2.size() + 1, 0));
        for(int i = 1;i <= text1.size(); i++)
        {
            for(int j = 1; j <= text2.size(); j++)
            {
                if(text1[i - 1] == text2[j - 1])
                dp[i][j] = dp[i -1][j - 1] + 1;
                else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
        return dp[text1.size()][text2.size()];

    }
};
```
**复杂度分析**
时间复杂度: O(M×N)
空间复杂度: O(M*N)