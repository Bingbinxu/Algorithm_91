**思路**
利用数学推导，得到前缀和和整体和关于余树的关系，从而找到余树相等的下标
利用map存储余树
官方代码里有错误当res利用min取最小值，改变了循环的次数，应改掉
map[0] = -1是为了应对删除数是第一个的情况
**代码**
```C++
int solve(vector<int>& nums, int k) {
    int tar = 0;
    for (auto i : nums) {
        tar += i;
    }
    tar = tar % k;
    map<int, int> map;
    map[0] = -1;
    
    int prefix = 0, res_len = nums.size(), res = nums.size();
    for (int i = 0; i < res_len; i++) {
        prefix += nums[i];
        int mod = prefix % k;
        map[mod] = i;
        int x = prefix - tar;
        int y = ((x % k) + k) % k;
        if (map.count(y)) {
            res = min(res, i - map[y]);            
        }
    }
    return res == nums.size() ? -1 : res;
}
```
**复杂度**
时间复杂度：对每个前缀进行遍历O(N)
空间复杂度：O(min(N,k))