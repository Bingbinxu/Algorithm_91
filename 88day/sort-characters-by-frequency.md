**思路**
先构建一格哈系表，进行收集频率，然后对频率数进行排序
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> dict;
        for (auto& ch : s)
        {
            if (dict.find(ch) == dict.end())
                dict[ch] = 1;
            else dict[ch]++;
        }
        string res;
        vector<pair<char, int>> kvVect;
        for (auto& kvp : dict)
            kvVect.push_back(kvp);        
        auto cmp = [](const pair<char, int>& p1, const pair<char, int>& p2)
        {
            return p1.second > p2.second;
        };
        sort(kvVect.begin(), kvVect.end(), cmp);
        for (auto& kvp : kvVect)
        {
            while (kvp.second--)
                res.push_back(kvp.first);
        } 
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
