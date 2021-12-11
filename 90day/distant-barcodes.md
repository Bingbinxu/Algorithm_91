**思路**
先对数字出现的频率排序，然后按照抽屉原理，没有任何数超过总数的一半
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    vector<int> rearrangeBarcodes(vector<int>& barcodes) {
        unordered_map<int, int> dict; // 映射:  key -> count
        for (auto& x : barcodes)
            dict[x] += 1;

        vector<pair<int, int>> pq; // pair: (count, key)
        for (auto& x : barcodes)
            pq.push_back({dict[x], x});
        sort(pq.begin(), pq.end(), greater<pair<int, int>>());

        int n = barcodes.size();
        vector<int> res(n);
        int i = 0;
        for (auto& x : pq)
        {
            res[i] = x.second;
            i += 2;
            if (i >= n)
                i = 1;
        }
        return res;
    }
};
```
**复杂度分析**
时间复杂度: O(NlogN)
空间复杂度: O(N）
