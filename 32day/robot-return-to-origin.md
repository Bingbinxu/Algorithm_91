**思路**
模拟法
定义一个初始坐标(x, y), 每次从moves数组读入一个字符, 根据具体反向进行一次x或y的增减。
看循环结束时, 是否能使 x == 0 且 y ==0 。

**代码**
```C++
实现语言: C++
class Solution {
public:
    bool judgeCircle(string moves) {
        int x = 0;
        int y = 0;
        for (const auto& move : moves)
        {
            switch (move)
            {
                case 'U':
                    y--;
                    break;
                case 'D':
                    y++;
                    break;
                case 'R':
                    x++;
                    break;
                case 'L':
                    x--;
                    break;
                }
        }
        return x == 0 && y == 0;
    }
};
```
**复杂度分析**
时间复杂度：O(n), n是字符串moves的长度
空间复杂度：O(1)