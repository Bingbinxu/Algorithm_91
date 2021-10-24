**思路**
 滑动窗口+左侧丢掉判断+右侧增加判断
**代码**
```C++
class Solution {
public:
    int maxVowels(string s, int k) {
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        int count = 0;
        int res = 0;
        for(int i = 0; i <= s.size(); i++)
        {
            if(i >= k)
            {
                count -=  vowels.count(s[i - k]);
            }
            count += vowels.count(s[i]);
            res = max(res, count);
        }
        return res;

    }
};
```
**复杂度**
时间复杂度：遍历S：O(N)
空间复杂度：O(1)
