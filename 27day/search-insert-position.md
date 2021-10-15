**思路**
利用二分法查找
**代码**
```C++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size()-1; //此处要注意
        while(l <= r) //等号可以退出，l=mid+1后就不满足条件了
        {
            const int mid = (l + r) >> 1;
            const int midval = nums[mid];
            if(midval == target)
            {
                return mid;
            }
            else if(midval < target)
            {
                l = mid + 1;
            }
            else{
                r = mid - 1;
            }

        }
        return l;
    }
};
```
**复杂度**
时间复杂度：二分法O(logN)
空间复杂度：O(1)