**思路**
回溯算法dfs+剪枝
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        if (nums.empty()) return {{}};
        if (nums.size() == 1) return {nums};
        vector<vector<int>> result;
        dfs(nums, result, 0);      
        return result;
    }
private:

    void dfs(vector<int> nums, vector<vector<int>>& result, int startPos) {   
        if (startPos == nums.size() - 1) {  
            result.push_back(nums); 
            return;
        }
        unordered_set<int> usedDict;  /* 记录哪些数已经用过 */
        for (int i = startPos; i < nums.size(); ++i) { 
            swap(nums[i], nums[startPos]);  
            if (!usedDict.count(nums[startPos])) {
                usedDict.insert(nums[startPos]);
                dfs(nums, result, startPos + 1);  
            }
            swap(nums[i], nums[startPos]); 
        }
    }
};
```
**复杂度分析**
时间复杂度： O(N*N(N-1)...(N-k+1))
空间复杂度： O(N)