**思路**
二分查找 + 判断。

**代码**
```C++
(C++)
bool ispossible(vector<int>& nums, int mid) {
    int start = nums[0];
    int end = start + mid;
    for (int i = 0; i < 3; i++) {
        int index = 0;
        while (nums[index] <= end) index++;
        if (index >= nums.size()) return true;
        start = nums[index];
        end = start + mid;
    }
    return false;
}

double solve(vector<int>& nums) {
    if (nums.size() <= 3) return 0;
    sort(nums.begin(), nums.end());
    int l = 0;
    int r = nums[nums.size() - 1] - nums[0];
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (ispossible(nums, mid)) {
            r = mid - 1;
        } else {
            l = mid + 1;
        }
    }
    return (double)l / 2;
}
```
**复杂度分析**
时间复杂度：O(NLogN + LogN * Log(M - N))，NLogN为排序，M为数组最大值，N为数组最小值。
空间复杂度：O(LogN)