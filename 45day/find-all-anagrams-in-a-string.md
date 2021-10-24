**思路**
 滑动窗口+hash
**代码**
```C++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
    vector<int> dictP(26, 0);
    vector<int> dictSP(26, 0);
    for (auto c : p)
        dictP[c - 'a']++;   
    vector<int> res;
    int k = p.length();
    for (int i = 0; i < s.length(); ++i) {
        if (i - k >= 0) { 
            dictSP[s[i - k] - 'a']--;
        }
        dictSP[s[i] - 'a']++;
        if (dictSP == dictP)
            res.push_back(i - k + 1);
    }
    return res;
    }
};
```
**复杂度**
时间复杂度：遍历S：O(N)
空间复杂度：O(1)
