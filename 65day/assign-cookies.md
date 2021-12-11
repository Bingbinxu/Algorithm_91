**思路**
贪心+双指针;通过对饼干和胃口排序，用双指针遍历
**代码(C++)**
```C++
class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(),g.end());
        sort(s.begin(),s.end());
        int gl = g.size();
        int sl = s.size();
        int gi=0 ,si = 0,res = 0;
        while(gi < gl && si < sl)
        {
            if(s[si] >= g[gi])
            {
                si++;
                gi++;
                res++;
            }
            else
            {
                si++;
            }
        }
        return res;
    }
};
```
**复杂度分析**
时间复杂度：O(N^logn)
空间复杂度：O(1)