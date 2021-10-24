**思路**
 二分法：利用false和true作为分界线，左加右减
**代码**
```C++
class Solution {
public:
    int firstBadVersion(int n) {
        int left = 1;
        int right = n;
        while(left <= right)
        {
            int middle = left + (right - left) / 2;
            if(isBadVersion(middle) == false)
            {
                left = middle + 1;
            }
            else if(isBadVersion(middle) == true)
            {
                right = middle - 1;
            }
        }
        return left;       
    }
};
```
**复杂度**
时间复杂度：二分次数O(logN)
空间复杂度：O(1)
