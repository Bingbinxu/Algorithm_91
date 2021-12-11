**思路**
回溯算法dfs+去重
**代码(C++)**
```C++
实现语言: C++
class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());  // 先排序, 防止后面重复处理
        vector<int> curGroup;
        dfs(candidates, target, 0, 0, curGroup);
        return res;
    }
    void dfs(const vector<int>& candidates, int target, int startPos, int sum, vector<int>& curGroup)
    {
        if (target == sum)
        {
            res.push_back(curGroup);
            return;
        }
        if (sum > target) return;        
        for (int i = startPos; i < candidates.size(); i++)
        {
            /* 去重, 对于for循环，比如1,1,2……，如果循环到第二个1,实际上肯定在第一个1的序列里 */
            if (i > startPos && candidates[i] == candidates[i-1]) continue;
            curGroup.push_back(candidates[i]);
            dfs(candidates, target, i+1, sum + candidates[i], curGroup);
            curGroup.pop_back();
        }
    }
};
```
**复杂度分析**
回溯深度 h = target / len(nums)
时间复杂度：O(n^h)
空间复杂度：O(h)
