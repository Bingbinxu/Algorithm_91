**思路**
大顶堆，取出K-1，剩下就是K大
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int res;
        priority_queue<int> q;
        for (auto& num : nums)
            q.push(num);
        
        while (!q.empty() && k > 1)
        {
            auto top = q.top();            
            q.pop();
            k--;
        }
        res = q.top();
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
