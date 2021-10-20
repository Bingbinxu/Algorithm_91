**思路**
 二分法：利用取得的绝对值之差的二分法
 在绝对值最大和最小间取值，通过判断这个绝对值是否满足有K个小于它进行调整left和right
 如果绝对值大于选定的绝对值的数量大于K个，调小，反之调大
**代码**
```C++
long possible(vector<int>& nums, int d) //此处返回值为long，否则不过
{
    const int N = nums.size();
    long count = 0; // count可能会超过2^31, 故用long存储比较稳妥
    long i = 0;
    for(int j = 1;j < N;j++)
    {
        //long i = 0;
        while (nums[j] - nums[i] > d) 
        {i++;}
        count += j - i;
        
    }
    return count;
};
int solve(vector<int>& nums, int k) {
    const int N = nums.size();
    sort(begin(nums), end(nums));
    k += 1;      //  0-indexed -> 1-indexed
    int left = 0, right = nums[N - 1] - nums[0];
    while (left <= right)
    {
        int guess = left + (right - left) / 2; 
        if (possible(nums, guess) >= k)
            right = guess -1;
        else
            left = guess + 1;
    }
    return left;
}
```
**复杂度**
时间复杂度：二分次数O(nlogN)，有个求绝对值的遍历
空间复杂度：O(m)，排序空间消耗
