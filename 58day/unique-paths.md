**方法**
正反向一样的，都是进行迭代，先是每行，然后在每行里列循环，依据每个值跟左边和上边有关，可以通过合理的遍历，节约空间
**代码**
```C++
实现语言: C++
class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<int> dp(n+1,0);
        dp[n-1] = 1;
        for(int i = m -1; i >=0; --i){
            for(int j = n -1; j >= 0; j--)
                dp[j] += dp[j + 1];
        }
        return dp[0];

    }
};
```
**复杂度分析**
时间复杂度: O(M×N)
空间复杂度: O(N)
