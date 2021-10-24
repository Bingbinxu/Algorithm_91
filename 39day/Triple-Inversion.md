**思路**
 二分法
**代码**
```C++
int solve(vector<int>& nums) {
    map<int, int> dict;
    int res = 0;
    for (auto& num : nums)
    {
        auto it = dict.upper_bound(3*num); // 找到第1个满足要求的数key1, 那哈希表中排在key1后面的数(比key1更大)也全满足 > 3*num
        if (it != dict.end())
        {
            for (auto it1 = it; it1 != dict.end(); it1++)
                res += it1->second;
        }        

        if (dict.count(num) > 0)
            dict[num]++; 
        else dict[num] = 1;      
    }
    return res;
}
```
**复杂度**
时间复杂度：O(NlogN)
空间复杂度：O(N)
