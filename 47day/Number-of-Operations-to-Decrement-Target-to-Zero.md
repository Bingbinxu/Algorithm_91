**方法**
利用滑动窗口，计算newT=sums(nums)-target的最长字串，往右滑动判定条件>newT,往左移动判定条件也是<newT
**代码**
```C++
实现语言: C++
int solve(vector<int>& nums, int target) {
    int N = nums.size();
    int newT = accumulate(nums.begin(), nums.end(), 0) - target;
    if(newT == 0)
    {
        return N;
    }
    int sum = 0;
    int maxlen = 0;
    int left = 0;
    for(int i = 0;i < N;i++)
    {
        sum += nums[i];
        while(sum >= newT && i >= left)
        {
            if(sum == newT)
            {
                maxlen = max(maxlen, i - left +1);
            }
            sum -= nums[left];
            left++;
        }
    }
    return maxlen ==0 ? -1 : N - maxlen; 
}
```
**复杂度分析**
时间复杂度: O(N),N为S串长度
空间复杂度: O(1)
