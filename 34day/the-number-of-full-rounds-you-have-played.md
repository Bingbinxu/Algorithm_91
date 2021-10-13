**思路**
先通过两个字符串获得小时和分钟的时间，然后分两种情况讨论，即finish>start和finish<start
对于finish>start在分为两种情况，即在15min内和15min外
**代码**
```C++
实现语言: C++
class Solution {
public:
    int numberOfRounds(string startTime, string finishTime) {
        int h1 = stoi(startTime.substr(0, 2));
        int m1 = stoi(startTime.substr(3, 2));
        int h2 = stoi(finishTime.substr(0, 2));
        int m2 = stoi(finishTime.substr(3, 2));
        if(h1 == h2 && m2 - m1 > 0 && m2 - m1 < 15){
            return 0;
        }
        int startIndex = h1 * 4 + (m1 + 14) / 15; //往后取整
        int endIndex = h2 * 4 + m2 / 15;
        if(endIndex < startIndex){
            return 96 - startIndex + endIndex;
        }
        return endIndex - startIndex;
    }
};
时间复杂度: O(1)
空间复杂度: O(1)