**思路**
利用双端队列维持窗口的滑动
利用单调递增栈将max维持在队列最前端
**代码**
```C++
class Solution {
    vector<int> res;  
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        for(int i = 0; i < nums.size();i++)
        {
            if(!q.empty() && i - k + 1 > q.front()) // 此处维持k长度的队列，维持弹出最大值
            {
                q.pop_front();
            }
            while(!q.empty() && nums[i] >= nums[q.back()]) //此处维持递减的队列，把左侧比nums[i]大的值全部弹出，最前面的就是最大值
            {
                q.pop_back();
            }
            q.push_back(i);
            if(i >= k - 1)
            {
                res.push_back(nums[q.front()]);
            }
        }
        return res;
    }
};
```
**复杂度**
时间复杂度：遍历O(N)
空间复杂度：利用队列存储，最差情况是窗口长度O(k)