**思路**
先统计词频，并将字符保存成数组形式
然后根据数组26个下标，分别以每个元素作为分界线，求得三种情况下最小值，避免了排序
**代码**
```C++
实现语言: C++
class Solution {
public:
    int minCharacters(string a, string b) {
        vector<int> fA(26); // 统计词频数组
        vector<int> fB(26);
        for (auto ch : a)
            fA[ch - 'a'] += 1;
        for (auto ch : b)
            fB[ch - 'a'] += 1;
       // return equal(fA,fB,a,b);
        return min(min(greater(fA,fB), greater(fB,fA)), equal(fA,fB,a,b));
    }
    int greater(vector<int> ca, vector<int> cb){
        int res = INT_MAX;
        for (int key = 0; key < 26; key++) // key: 每个字母在词频数组中对应的index
        {
            if(key>0) //a不能作为分界线
            {
                int changes = 0;
                for (int i = key; i < 26; i++)
                    changes += ca[i];  // 把字符串a中 > key对应的字母的字母改小              
                for (int i = 0; i < key; i++)
                    changes += cb[i];
                res = min(res, changes);
            }         
        }
        return res; 
    }
    int equal(vector<int> ca, vector<int> cb, string a, string b){
        int res = INT_MAX;
        for (int key = 0; key < 26; key++) // key: 每个字母在词频数组中对应的index
        {
            int real = (a.size()+b.size()-ca[key]-cb[key]);
            res = min(res, real);
        }
        return res;
    }
};
时间复杂度: O(m+n)
空间复杂度: O(26)