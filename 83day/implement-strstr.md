**思路**
滑动窗口
**代码(C++)**
```C++
实现语言: C++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = haystack.length();
        int n = needle.length();
        if (m < n) return -1;
        if (n == 0) return 0;       
        int i = 0, j = 0, left = 0;      
        while (i < m && j < n) {
            if (haystack[i] == needle[j]) {
                ++i;
                ++j;
            } else {
                left++;
                i = left;
                j = 0;
            }
        }         
        if (j == n) return left;       
        return -1;
    }
};
```
**复杂度分析**
时间复杂度: O(N×M)
空间复杂度: O(1）
