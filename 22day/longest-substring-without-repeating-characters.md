**思路**
官方思路：判断树s[r]是否存在,存在的话：
1.如果重复，左侧向右移动一位
2.如果不重复，扩展右侧
记录最长的长度
**代码**
```C++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char ,int> spl;
        int max_len = 0, l = 0, r = 0;
        while(r<s.size())
        {
            if(spl.count(s[r])>0) //判断树s[r]是否存在
            {
                int last = spl[s[r]];
                if (last >= l && last <= r)
                l = last +1; //如果重复，左侧向右移动一位
            }
            max_len = max(max_len, r -l +1); //记录最长的长度
            spl[s[r]] = r;
            r ++;
        }
        return max_len;
    }
};
```
**复杂度**
时间复杂度：排序算法O（N）
空间复杂度：存储所有的节点O（S）S为不重复字符串长度