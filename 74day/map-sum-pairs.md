**方法**
哈系表
**代码**
```C++
class MapSum {
    unordered_map<string, int> dict;
public:
    MapSum() {
    }
    
    void insert(string key, int val) {
        if (dict.count(key) == 0)
            dict[key] = val;
        else dict[key] = val;
    }
    
    int sum(string prefix) {
        int sum = 0;
        for (auto& kvp : dict)
        {
            if (kvp.first.find(prefix) != string::npos && kvp.first.find(prefix) == 0) 
        }
        return sum;
    }
};

```
**复杂度分析**
时间复杂度: insert: O(1), sum: O(N), 其中N是哈希表的size
空间复杂度: O(N)
