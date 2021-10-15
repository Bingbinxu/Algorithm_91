**思路**
利用双指针分别管理写和读
**代码**
```C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.empty()) return 0;
        int l = 0, r = 0;
        while(r < nums.size())
        {
            if(nums[l] != nums[r])
            {
                l += 1;
                nums[l] = nums[r];
            }
            r += 1;
        }
        return l + 1;
    }
};
```
**复杂度**
时间复杂度：遍历数组O(N)
空间复杂度：O(1)