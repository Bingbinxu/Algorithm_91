**思路**
遇到数字执行10进制的数字计算，前一个比后一个多10倍
遇到[进行压栈处理
遇到]进行出站处理
遇到普通字符，加上就行
**代码**
```
class Solution {
public:
    string decodeString(string s) {
        int num = 0;
        string str = "";
        string res = "";
        stack<int> numstack;
        stack<string> strstack;
        int len = s.size();
        for(int i = 0;i < len; i++)
        {
            if(s[i]>='0' && s[i]<='9')
            {
                num = 10*num + s[i] -'0';
            }
            else if(s[i]=='[')
            {
                numstack.push(num);
                strstack.push(str);
                num = 0;
                str = "";
            }
            else if(s[i]==']')
            {
                int j = numstack.top();
                numstack.pop();
                for(int k = 0;k < j;k++ )
                {
                    strstack.top() += str;
                }
                str = strstack.top();
                strstack.pop();
            }
            else
            {
                str +=s[i];
            }

        }
        return str;

    }
};
```
**复杂度**
时间复杂度遍历s，同时遍历里面重复[]的次数,复杂度为O（NUM的和）
空间复杂度O([]里的lenth*num)
