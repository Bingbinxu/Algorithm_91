**思路**
建立一个size为k的小顶堆
每次比较，保持小顶堆性质
**代码**
```C++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> counts;
        for(int i : nums) counts[i]++;
        //priority_queue<pair<int,int>> q;
        priority_queue<pair<int,int>, vector<pair<int, int>>, greater<pair<int, int>>> q;
        for(auto it : counts)
        {
            if(q.size()!=k)
            {
                q.push(make_pair(it.second, it.first));
            }
            else{
                if(it.second > q.top().first){
                    q.pop();
                    q.push(make_pair(it.second, it.first));
                }
            }
        }
        vector<int> res;
        while(q.size())
        {
            res.push_back(q.top().second);
            q.pop();
        }
        return vector<int>(res.rbegin(), res.rend());
    }
};
```
**复杂度**
时间复杂度：遍历O（N×logK）
空间复杂度：最坏的情况存储所有的节点O（N）