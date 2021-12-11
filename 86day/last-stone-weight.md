**思路**
topK的变形，利用topK维持一个从大到小的队列，然后比较选择粉碎或者加入
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        if(stones.size() == 1) return stones.front();
        priority_queue<int> topk;
        for(auto& i : stones)
        {
            topk.push(i);
        }
        while(topk.size()>=2)
        {
            int fs = topk.top();
            topk.pop();
            int ss = topk.top();
            topk.pop();
            if(fs != ss)
            {
                topk.push(fs - ss);
            }
        }
        return topk.empty() ? 0 : topk.top();
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
