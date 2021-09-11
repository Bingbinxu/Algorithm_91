 **思路**
 先找出数组s中含有c的字符下标
 循环找出每个字符对应的c的下标距离，求出最短距离
 **代码**
 ```
 class Solution {
public:
    vector<int> shortestToChar(string s, char c) {
        vector<int> cp;        
        int len = s.size();
        vector<int> sp; 
        for(int i = 0; i < len; i++)
        {
            if (s[i]== c)
            {
                cp.push_back(i);
            }          
        }
       for(int i = 0; i < len; i++)
        {
            sp.push_back(abs(i -cp[0]));
            for (int j =1; j < cp.size(); j ++)
            {
                int a = abs(i -cp[j]);
                if(sp[i] > a)
                {
                    sp[i] = a;
                }
            }
        }      
       return sp;
    }
};
```
 **复杂度分析**
 时间复杂度 循环遍历找出c，为O（N）；循环算距离O（N*K），K为s中含有c的个数
 空间复杂度 O（N）