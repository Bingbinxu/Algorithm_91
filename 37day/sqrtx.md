**思路**
牛顿法
**代码**
```C++
class Solution {
public:
    int mySqrt(int x) {
        if(x == 0)
        return 0;
        double a = x;
        double num = x;
        while(abs(num - a / num) > 1e-10 * num)
        {
            num = (num + a / num) / 2;
        }
        return (int)num;

    }
};
```
**复杂度**
时间复杂度：遍历数组O(logN)
空间复杂度：O(1)
```C++
二分法
class Solution {
public:
    int mySqrt(int x) {
        if(x < 2)
        return x;
        int l =  1,r = x;
        while(l <= r)
        {
            int p = l + (r - l) / 2;
            long s = (long)p * p;
            if(s > x)
            {
                r = p - 1;
            }
            else if(s < x)
            {
                l = p + 1;
            }
            else
            {
                return p;
            }
        }
        return r;
    }
};
```