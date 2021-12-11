**思路**
动态规划
**代码(C++)**
```C++
class Solution {
public:
    bool canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (1 + maxChoosableInteger) * maxChoosableInteger / 2;
        if(sum < desiredTotal) return false;
        unordered_map<int,int> d;
        return dfs(maxChoosableInteger, 0, desiredTotal, 0, d);
    }

    bool dfs(int n,int s,int t,int S,unordered_map<int,int>& d){
        if(d[S]) return d[S];
        int& ans = d[S];
        if(s >= t) return ans = true;
        if(S == (((1 << n) - 1) << 1)) return ans = false;
        for(int m = 1;m <= n;++m){
            if(S & (1 << m)) continue;
            int nextS = S | (1 << m);
            if(s + m >= t) return ans = true;
            bool r1 = dfs(n, s + m, t, nextS, d);
            if(!r1) return ans = true;
        }
        return ans = false;
    }
};
```
**复杂度分析**
时间复杂度：O(2^n)
空间复杂度：O(2^n)