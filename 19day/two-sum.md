**思路**
对每个值遍历，将sum-i的值存入map，如果后面有相应的值，则迅速找出
**代码**
```C++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> map;
        for(int i = 0;i < nums.size();i++)
        {
            if(map.count(nums[i]))
               return vector<int> {map[nums[i]], i};

            map[target - nums[i]] = i;
        }
        return vector<int>{};

    }
};
```
**复杂度**
时间复杂度：遍历O（N）
空间复杂度：最坏的情况存储所有的节点O（N）