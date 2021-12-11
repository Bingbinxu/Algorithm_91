**思路**
回溯算法dfs
**代码(C++)**
```C++
实现语言: C++
class Solution {
    vector<vector<int>> res;

public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> curGroup;
        dfs(candidates, target, curGroup, 0, 0);
        return res;
    }
    void dfs(vector<int>& candidates, int target, vector<int>& curGroup, int sum, int index)
    {
        if (sum > target)
            return;
        if (sum == target)
            res.push_back(curGroup);
        else
        {
            for (int i = index; i < candidates.size(); i++)
            {
                curGroup.push_back(candidates[i]);
                dfs(candidates, target, curGroup, sum + candidates[i], i);
                curGroup.pop_back(); //清空方便下次从头计算
            }
        }
    }
};
```
**复杂度分析**
时间复杂度：O(n^(target/min))，n为candidates数组的长度，min为数组中最小元素，target/min为递归栈的最大深度
空间复杂度：O(target/min)，记录路径信息的list的长度不超过target/min
