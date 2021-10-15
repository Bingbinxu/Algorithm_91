**思路**
利用数组桶排序
**代码**
```C++
实现语言: C++
class Solution {
public:
    vector<int> sortArray(vector<int>& nums) {
        vector<int> count(50000 * 2 + 1);
        vector<int> res;
        for(auto i : nums)
        {
            count[50000 + i] += 1;
        }
        for(int j = 0; j < count.size(); j++)
        {
            while(count[j]--)
            {
                res.push_back(j - 50000);
            }
        }
        return res;
    }
};
时间复杂度: O(n)
空间复杂度: O(m)