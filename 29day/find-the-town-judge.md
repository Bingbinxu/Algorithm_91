**思路**
利用图的方式直接统计出入度
对每个点来说：信任别人出度为1,别人入度为1,由于有个人别人都信任他，所以他的入度为n-1
**代码**
```C++
class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if(trust.empty() && n ==1)
        {
            return 1;
        }
        unordered_map<int, int> count;
        for(auto& relation : trust)
        {
            count[relation[0]] += -1;
            count[relation[1]] += 1;
        }
        for(auto& k : count)
        {
            if(k.second == n-1)
            {
                return k.first;
            }
        }
        return -1;
    }
};
```
**复杂度**
时间复杂度：遍历O(N)
空间复杂度：利用MAP存储所有trust，故为O(N)