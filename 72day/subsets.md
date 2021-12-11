**思路**
用二进制的位作为选取的值
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        const int n = nums.size();
        vector<vector<int>> res;
        for (int s = 0; s < (1 << n); s++)
        { /* s表示一个状态state, 相当于取位 */
            vector<int> curSet;
            for (int i = 0; i < n; i++)
                if ((s & (1 << i)) > 0)
                    curSet.push_back(nums[i]);
            res.push_back(curSet);
        }
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(N * 2^N)
空间复杂度: (N * 2^N)