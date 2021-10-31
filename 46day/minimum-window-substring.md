**方法**
利用数组构造的hash，记录字母的词频表，然后不断向右扩张，直到含有t全部的字母，此时左侧收缩，直到含有字母数<t,然后利用count记录最小长度
**代码**
```C++
实现语言: C++
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> trecord(265, 0);
        vector<int> srecord(265, 0);
        for(int i = 0;i < t.size();i++)
        {
            trecord[t[i]]++; //构造频次表
        }
        int left = 0;
        int right = 0;
        int count = 0; //记录最小数量
        string ret;
        int retindex = INT_MAX;
        while(right < s.size())
        {
            int index = s[right];
            srecord[index]++;
            if(trecord[index] > 0 && srecord[index] <= trecord[index])
            {
                count++;
            }
            while(count == t.size())
            {
                if((right - left +1) < retindex)
                {
                    retindex = right -left + 1;
                    ret = s.substr(left, retindex); //从left截取right-left+1的长度
                }
                int leftindex = s[left];
                srecord[leftindex]--;
                if(srecord[leftindex] < trecord[leftindex])
                {
                    count--;
                }
                left++;
            }
            right++;
        }
        return ret;
    }
};
```
复杂度分析:
时间复杂度: O(N+K) N为S串长度，K为T串长度
空间复杂度: O(C)，C为T串个数
