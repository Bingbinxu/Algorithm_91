**方法**
利用暴力搜索，将小时取为12小时内，分钟取为60分钟内，这样枚举所有的数值，判断其中正好二进制位数为为1的和为turnedOn的情况
**代码**
```C++
实现语言: C++
class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> res = {};
        for(int h = 0;h < 12;h++)
        {
            for(int m = 0;m < 60;m++)
            {
                if(count(h)+count(m) == turnedOn)
                {
                    string str = m < 10 ? "0" + to_string(m) : to_string(m);
                    res.push_back(to_string(h)+":"+ str); 
                }
            }
        }
        return res;
    }
    int count(int n)
    {
        int count = 0;
        while(n > 0)
        {
            n = n & (n -1);  //每次都会将最右边的1 变成 0，利用这个特性快速判断1的个数
            count++;
        }
        return count;
    }
};
```
复杂度分析:
时间复杂度: O(1)
空间复杂度: O(1）
