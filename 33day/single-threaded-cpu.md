**思路**
参考yanglr同学的C++实现，采用排序和小顶堆
**代码**
```C++
实现语言: C++
class Solution {
public:
    typedef long long LL; 
    typedef pair<LL, LL> PLL;
    vector<int> getOrder(vector<vector<int>>& tasks) {
        for (int i=0; i<tasks.size(); i++) // 下标小的排前面
            tasks[i].push_back(i);       
        sort(tasks.begin(), tasks.end());
        priority_queue<PLL, vector<PLL>, greater<>>pq;  //小顶堆
        
        LL cur = 0;
        vector<int>rets;
        for (int i=0; i<tasks.size(); i++)
        {
            while (cur < tasks[i][0] && !pq.empty())
            {
                rets.push_back(pq.top().second);
                cur+=pq.top().first;
                pq.pop();
            }            
            
            pq.push({tasks[i][1], tasks[i][2]}); 
            cur = max(cur, (LL)tasks[i][0]);    
        }
        while (!pq.empty())
        {
            rets.push_back(pq.top().second);
            cur += pq.top().first;
            pq.pop();
        }
        return rets;        
    
    }
};
时间复杂度: O(N logN) , 其中N 为数组长度。
空间复杂度: O(N)