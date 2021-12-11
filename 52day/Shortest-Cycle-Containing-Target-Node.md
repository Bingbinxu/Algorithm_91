**方法**
理解输入的核心：数组下标访问的元素对应下一个数组下标
**代码**
```C++
实现语言: C++
int solve(vector<vector<int>>& graph, int target) {
    queue<int> q;
    q.push(target);
    unordered_set<int> visited;
    int step = 0;
    while (!q.empty()) {
        int len = q.size();
        for (int i = 0; i < len; i++) {
            auto cur = q.front();
            q.pop();
            visited.insert(cur);
            for (auto& it : graph[cur]) {
                //return it;
                if (!visited.count(it)) {
                    q.push(it);
                } else if (it == target) {
                    return step + 1; //满足情况状态弹出加一
                }
            }
        }
        step += 1;//结束了一格q列表，加一
    }
    return -1;   
}
```
**复杂度分析**
时间复杂度: O(v+e)，v节点数，e边数
空间复杂度: O(v)
class Solution {
public:
    int rob(vector<int>& nums) {
        // define robe x to obtain max value as dp function. 
        // dp(x) =  max(num[x] + dp(x-2), dp(x-1))
        
        vector<int> dp(2, 0); 
        for(int i=0; i< nums.size(); i++)
        {
            
            int current = max(nums[i] + dp[0], dp[1]); 
            dp[0] = dp[1]; 
            dp[1] = current; 
        }
        
        return dp[1]; 
    
        
    }
};
时间复杂度为O(N)，空间复杂度为 O(1)。