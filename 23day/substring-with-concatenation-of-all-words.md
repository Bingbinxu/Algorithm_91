**思路**
官方思路：以word里面总字符串长度，对s里面的子字符串进行遍历
每取s中子字符串的长度，就用map来检查是否能恰好用word里面的构成，不能右打断，不能右数量的不一致，如果有就break
**代码**
```C++
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> res;
        map<string, int> mapp;
        int count = words.size();
        if(words.empty() || count == 0)
        {
            return res;
        }
        for(auto s : words)
        {
            mapp[s] += 1;
        }
        int slen = s.size(), wordlen = words[0].size();
        int match = 0;
        int sumlen = wordlen*count;
        for(int i = 0;i < slen - sumlen + 1;i++)
        {
            string cur = s.substr(i, sumlen);
            map<string, int> temp;
            int j = 0;
            for(;j < cur.size();j+=wordlen)
            {
                string word = cur.substr(j, wordlen);
                if(!mapp.count(word))
                {
                    break;
                }
                temp[word] += 1;
                if(temp[word] > mapp[word])
                {
                    break;
                }
            }
            if(j == cur.size())
            {
                res.push_back(i);
            }
        }
        return res;
    }
};
```
**复杂度**
时间复杂度：排序算法O(（N-m*k）*m)
空间复杂度：存储所有的节点O（m）,m为words个数