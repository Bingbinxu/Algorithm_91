**方法**
动态规划
**代码**
```C++
实现语言: C++
class Solution {
public:
    int rob(vector<int>& nums) {
        // define robe x to obtain max value as dp function. 
        // dp(x) =  max(num[x] + dp(x-2), dp(x-1))
        
        vector<int> dp(2, 0); 
        for(int i=0; i< nums.size(); i++)
        {
            
            int current = max(nums[i] + dp[0], dp[1]); 
            dp[0] = dp[1]; 
            dp[1] = current; 
        }
        
        return dp[1]; 
    
        
    }
};
```
**复杂度分析**
时间复杂度: O(N)
空间复杂度: O(1)
