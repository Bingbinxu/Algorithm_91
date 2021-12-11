**思路**
 核心：利用仿射变换可以将任意漂亮数组转换成全偶或者全奇数组
      一个全偶数漂亮数组和一个全奇数漂亮数组可以组成一个漂亮数组
      迭代
**代码(C++)**
```C++
实现语言: C++
C++ Code:

class Solution {
public:
    vector<int> beautifulArray(int n) {
        if(n == 1) return {1};
        auto l = beautifulArray((n + 1) / 2);
        auto r = beautifulArray(n / 2);
        vector<int> ans;
        for(auto x : l) ans.push_back(2 * x - 1);
        for(auto x : r) ans.push_back(2 * x);
        return ans;
    }
};
```
**复杂度分析**
时间复杂度: O(N logN)
空间复杂度: O(N)
