**思路**
将整数K作为移动的部分，不断与A的最后一位叠加，从而更新数组
注意点：边界条件存在A>=K,和A<K的情况
**代码**
```
class Solution {
public:
    vector<int> addToArrayForm(vector<int>& num, int k) {
        int len = num.size()-1;
        while(len>=0)
        {
            k = k + num[len];
            num[len] = k % 10;
            k = k / 10;
            len--;
        }
        while(k>0)
        {
            num.insert(num.begin(),0);
            num[0] = k % 10;
            k = k /10;
        }
        return num;       
    }
};
```
**复杂度**
时间复杂度O（N+max（0，K-N））
while函数遍历N遍，若K超过N，还需要遍历K-N遍
空间复杂度O（N+max（0，K-N））